#!/usr/bin/env python3
"""Gen clip video từ ảnh khung đầu (đã pass QC cổng 2a) qua API — VIDEO_TOOL=api.

  python3 _tools/gen-video.py --prompt-file prompts-used/S01.txt --image outputs/images/X_B-01_S01-mo-ta_v1.png \
          --out outputs/videos/X_S01_mo-ta_v1.mp4 --ratio 9:16 --seconds 5 [--audio] [--provider fal_video] [--model ...]
          [--param cfg_scale=0.6]   (thêm / ghi đè tham số riêng của model)
  python3 _tools/gen-video.py --list-providers

Nhà cung cấp: --provider > VIDEO_PROVIDER trong ~/.config/ai-studio/prefs.env > fal_video.
Danh sách + cách lấy key: _tools/providers.json mục "video". Video KHÔNG có nhà miễn phí lâu dài: fal.ai / Replicate
thường tặng credit dùng thử khi đăng ký; Gemini Veo cần bật thanh toán.
--seconds = thời lượng RENDER (render_s trong storyboard), tool làm tròn về mức model hỗ trợ.
--audio = để model tạo tiếng trong clip (UGC / tiếng môi trường). Video voiceover → bỏ (VO + nhạc thêm ở cổng 2b).
Mỗi clip (cùng tên, bỏ _vN) tối đa 2 lượt: 1 gen + 1 sửa. Quá → exit 3. Báo danh sách clip cho user TRƯỚC khi gen.
Exit giống gen-image.py.
"""
import argparse, base64, io, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _api as A

MAX_TURNS = 2
DEFAULT_MODEL = {"fal_video": "fal-ai/kling-video/v3/pro/image-to-video", "replicate_video": "kwaivgi/kling-v3-video",
                 "gemini_veo": "veo-3.1-generate-preview"}
# fal: tên trường ảnh + cách đặt thời lượng theo model (model khác → --image-field / --param)
FAL_MODELS = {"fal-ai/kling-video/v3/pro/image-to-video": {"image": "start_image_url", "dur": (3, 15), "audio": "generate_audio"},
              "fal-ai/kling-video/v3/standard/image-to-video": {"image": "start_image_url", "dur": (3, 15), "audio": "generate_audio"}}
IMG_FIELDS = ("start_image", "first_frame_image", "image", "input_image", "image_url", "start_image_url", "first_frame")
GEM = "https://generativelanguage.googleapis.com/v1beta"


def frame_uri(path, maxside=1536):
    """Ảnh khung đầu → data URI JPEG gọn (< ~1MB) để gửi kèm request."""
    from PIL import Image
    im = Image.open(path).convert("RGB"); im.thumbnail((maxside, maxside)); buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90); return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def params(pairs):
    out = {}
    for kv in pairs:
        k, v = kv.split("=", 1)
        out[k] = True if v.lower() == "true" else False if v.lower() == "false" else int(v) if v.isdigit() else v
    return out


def wait(fn, label, limit=1800, every=8):
    t0 = time.time()
    while True:
        r = fn()
        if r is not None: return r
        if time.time() - t0 > limit: raise A.Fail("timeout", f"{label} chạy quá {limit // 60} phút")
        time.sleep(every)


def gen_fal(k, a, prompt):
    H = {"Authorization": f"Key {k['FAL_KEY']}"}
    model = a.model or DEFAULT_MODEL["fal_video"]
    spec = FAL_MODELS.get(model, {"image": "image_url", "dur": (5, 10), "audio": None})
    lo, hi = spec["dur"]
    body = {"prompt": prompt, a.image_field or spec["image"]: frame_uri(a.image),
            "duration": str(max(lo, min(hi, round(a.seconds))))}
    if spec.get("audio"): body[spec["audio"]] = a.audio
    body.update(params(a.param))
    sub = A.http(f"https://queue.fal.run/{model}", body, H)
    print(f"… fal đang render (request {sub.get('request_id', '?')})", flush=True)

    def done():
        s = A.http(sub["status_url"], headers=H)
        if s.get("status") == "COMPLETED": return True
        if s.get("status") in ("FAILED", "ERROR"): raise A.Fail("other", f"fal lỗi: {str(s)[:300]}")
    wait(done, "fal")
    r = A.http(sub["response_url"], headers=H)
    url = (r.get("video") or {}).get("url")
    if not url: raise A.Fail("other", f"fal không trả video: {str(r)[:300]}")
    return url, {}, model


def gen_replicate(k, a, prompt):
    H = {"Authorization": f"Bearer {k['REPLICATE_API_TOKEN']}"}
    model = a.model or DEFAULT_MODEL["replicate_video"]
    info = A.http(f"https://api.replicate.com/v1/models/{model}", headers=H)
    props = (((info.get("latest_version") or {}).get("openapi_schema") or {}).get("components", {})
             .get("schemas", {}).get("Input", {}).get("properties", {}))
    field = a.image_field or next((f for f in IMG_FIELDS if f in props), "image")
    inp = {"prompt": prompt, field: frame_uri(a.image)}
    if "duration" in props:
        d = props["duration"]; s = round(a.seconds)
        if "minimum" in d: s = max(d["minimum"], s)
        if "maximum" in d: s = min(d["maximum"], s)
        inp["duration"] = s
    if "aspect_ratio" in props: inp["aspect_ratio"] = a.ratio
    for f in ("generate_audio", "audio"):
        if f in props and props[f].get("type") == "boolean": inp[f] = a.audio
    inp.update(params(a.param))
    r = A.http(f"https://api.replicate.com/v1/models/{model}/predictions", {"input": inp}, H)
    print(f"… Replicate đang render (id {r.get('id', '?')})", flush=True)

    def done():
        nonlocal r
        if r.get("status") in ("succeeded", "failed", "canceled"): return r
        r = A.http(r["urls"]["get"], headers=H)
    r = wait(done, "Replicate")
    if r["status"] != "succeeded":
        err = str(r.get("error") or r["status"])
        raise A.Fail("safety" if "nsfw" in err.lower() or "sensitive" in err.lower() else "other", f"Replicate: {err[:300]}")
    out = r["output"]
    return (out[0] if isinstance(out, list) else out), {}, model


def gen_veo(k, a, prompt):
    H = {"x-goog-api-key": k["GEMINI_API_KEY"]}
    model = a.model or DEFAULT_MODEL["gemini_veo"]
    secs = min((4, 6, 8), key=lambda s: abs(s - a.seconds))      # Veo 3.1: 4 / 6 / 8 giây
    b64 = frame_uri(a.image).split(",", 1)[1]
    body = {"instances": [{"prompt": prompt, "image": {"inlineData": {"mimeType": "image/jpeg", "data": b64}}}],
            "parameters": {"aspectRatio": "9:16" if a.ratio in ("9:16", "4:5", "3:4") else "16:9",
                           "resolution": "720p", "durationSeconds": str(secs)}}
    body["parameters"].update(params(a.param))
    op = A.http(f"{GEM}/models/{model}:predictLongRunning", body, H)
    print(f"… Veo đang render ({op.get('name', '?')})", flush=True)

    def done():
        s = A.http(f"{GEM}/{op['name']}", headers=H)
        if s.get("error"): raise A.Fail("other", f"Veo lỗi: {str(s['error'])[:300]}")
        return s if s.get("done") else None
    s = wait(done, "Veo", every=10)
    resp = s.get("response", {}).get("generateVideoResponse", {})
    samples = resp.get("generatedSamples") or []
    if not samples:
        why = str(resp.get("raiMediaFilteredReasons") or resp)[:300]
        raise A.Fail("safety" if "filter" in why.lower() or resp.get("raiMediaFilteredCount") else "other", f"Veo không trả video: {why}")
    return samples[0]["video"]["uri"], H, model


GEN = {"fal_video": gen_fal, "replicate_video": gen_replicate, "gemini_veo": gen_veo}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt-file"); p.add_argument("--prompt"); p.add_argument("--image", help="ảnh khung đầu đã pass")
    p.add_argument("--out"); p.add_argument("--ratio", default="9:16"); p.add_argument("--seconds", type=float, default=5)
    p.add_argument("--audio", action="store_true", help="model tạo tiếng trong clip")
    p.add_argument("--provider"); p.add_argument("--model"); p.add_argument("--image-field")
    p.add_argument("--param", action="append", default=[], help="key=value thêm cho model")
    p.add_argument("--no-fallback", action="store_true"); p.add_argument("--list-providers", action="store_true")
    a = p.parse_args()
    P = A.providers("video")
    if a.list_providers:
        for n, v in P.items(): print(f"{n:16s} {v['label']} · key: {' + '.join(k['env'] for k in v['keys'])} · model mặc định {DEFAULT_MODEL[n]}")
        return
    prompt = a.prompt or (open(a.prompt_file, encoding="utf-8").read().strip() if a.prompt_file else "")
    if not (prompt and a.image and a.out): p.error("cần --prompt-file (hoặc --prompt), --image và --out")
    if not os.path.exists(a.image): A.die(1, f"KHÔNG THẤY ẢNH KHUNG ĐẦU: {a.image}")
    A.guard_out(a.out)
    turns = A.turns_used(a.out, "clip")
    if turns >= MAX_TURNS: A.die(3, f"HẾT LƯỢT: {A.asset_base(a.out)} đã gen {turns} lần (1 gen + 1 sửa) → ghi note để user tự xử lý")
    provider = a.provider or A.default_provider("video", "fal_video")
    if provider not in P: provider = "fal_video"
    first = provider

    def gen(pv, k):
        if pv != first: a.model = a.image_field = None; a.param = []   # đổi nhà → model / tham số riêng không còn đúng
        return GEN[pv](k, a, prompt)
    provider, (url, dl_headers, model), tried = A.run("video", provider, gen, a.no_fallback)
    out = A.download(url, a.out, dl_headers)
    dur = A.duration(out)
    A.write_log(out, "clip", {"turn": turns + 1, "provider": provider, "model": model, "tried": tried, "prompt": prompt,
                              "image": a.image, "ratio": a.ratio, "seconds_asked": a.seconds, "seconds": dur, "audio": a.audio})
    print(f"{out} ({provider} · {model}, {dur if dur is not None else '?'}s, lượt {turns + 1}/{MAX_TURNS})")


if __name__ == "__main__":
    main()
