#!/usr/bin/env python3
"""Gen ảnh qua API, nhiều nhà cung cấp. Key ở ~/.config/ai-studio/.env (không bao giờ in ra).
Quy trình đầy đủ: _skills/image/SKILL.md mục "Gen GPT Image".

  python3 _tools/gen-image.py --prompt-file p.txt --out outputs/images/X_B-01_S01-mo-ta_v1.png --ratio 9:16 [--quality medium] [--ref a.png --ref b.png] [--provider openai]
  python3 _tools/gen-image.py --check [--provider cloudflare]     # kiểm key nhà cung cấp đang dùng
  python3 _tools/gen-image.py --list-providers

Nhà cung cấp: --provider > IMAGE_PROVIDER trong ~/.config/ai-studio/prefs.env > openai.
Lỗi key / hết credit / timeout → popup chọn nhà cung cấp khác + dán key (`_tools/pick-provider.sh`) → chạy lại
đúng ảnh đó. Huỷ popup (hoặc --no-fallback) → exit 4 như cũ. Lần lỗi không tính lượt.
--ref theo ĐÚNG thứ tự Image 1, Image 2… trong prompt. Nhà không nhận ảnh tham chiếu → bỏ ref, cảnh báo.
Mỗi ảnh (cùng tên, bỏ _vN) tối đa 2 lượt: 1 gen + 1 sửa. Quá → exit 3, user tự sửa tay.
Mỗi lượt thành công ghi 1 dòng vào <thư mục out>/_gen-log.jsonl (kèm prompt, nhà cung cấp).
Exit: 0 ok · 1 lỗi khác · 2 bị bộ lọc an toàn chặn · 3 hết lượt · 4 key/credit/timeout và không đổi được nhà cung cấp.
"""
import argparse, base64, datetime, io, json, mimetypes, os, re, subprocess, sys, tempfile, time
import urllib.error, urllib.parse, urllib.request, uuid
for _s in (sys.stdout, sys.stderr):  # Windows console mặc định cp1252 → in tiếng Việt bị lỗi
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spells import spell  # câu thần chú khi API có vấn đề

CFG = os.path.expanduser("~/.config/ai-studio")
ENV_FILE, PREFS = os.path.join(CFG, ".env"), os.path.join(CFG, "prefs.env")
TOOLS = os.path.dirname(os.path.abspath(__file__))
MAX_TURNS = 2  # 1 gen + 1 sửa
# Cạnh chia hết cho 16, đúng tỷ lệ, trong giới hạn gpt-image-2.
RATIOS = {"9:16": "1152x2048", "16:9": "2048x1152", "4:5": "1536x1920", "1:1": "1024x1024",
          "2:3": "1024x1536", "3:2": "1536x1024"}
OK_EXT = {".png", ".jpg", ".jpeg", ".webp"}

from providers_cli import load as _load_providers  # providers.json + ~/.config/ai-studio/providers-custom.json


def providers():
    """id → (key cần, nhận ảnh tham chiếu?, miễn phí?, mô tả, cấu hình nhà tự thêm)"""
    return {p["id"]: ([k["env"] for k in p["keys"]], bool(p["refs"]), bool(p.get("free")), p["label"], p.get("custom"))
            for p in _load_providers("image") if p["id"] != "custom"}


PROVIDERS = providers()


class Fail(Exception):
    """kind: key | credit | timeout | safety | other"""
    def __init__(self, kind, msg): super().__init__(msg); self.kind = kind


def die(code, msg):
    print(msg, file=sys.stderr); sys.exit(code)


def read_kv(path):
    d = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1); d[k.strip()] = v.strip().strip('"')
    return d


def keys_for(provider):
    env = read_kv(ENV_FILE); out = {}
    for k in PROVIDERS[provider][0]:
        out[k] = os.environ.get(k) or env.get(k, "")
    missing = [k for k, v in out.items() if not v]
    if missing:
        raise Fail("key", f"THIẾU {', '.join(missing)} cho {provider}")
    return out


# ---------- HTTP ----------
def http(url, body=None, headers=None, method=None, raw=False, timeout=300):
    """Thử lại lỗi tạm thời 3 lần. Trả dict (JSON) hoặc bytes (raw)."""
    last = ""
    for attempt in range(3):
        req = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                return data if raw else json.loads(data or b"{}")
        except urllib.error.HTTPError as e:
            txt = (e.read() or b"").decode("utf-8", "replace")[:600]
            low = txt.lower()
            if e.code in (401,) or "invalid api key" in low or "api_key_invalid" in low or "unauthorized" in low:
                raise Fail("key", f"LỖI KEY {e.code}: {txt[:200]}")
            if (e.code == 402 or "insufficient_quota" in low or "billing" in low or "balance" in low
                    or "credit" in low or "quota" in low or "resource_exhausted" in low or "allocation" in low):
                raise Fail("credit", f"HẾT CREDIT / HẠN MỨC {e.code}: {txt[:200]}")
            if e.code == 403:
                raise Fail("key", f"KEY KHÔNG CÓ QUYỀN {e.code}: {txt[:200]}")
            if "moderation" in low or "safety" in low or "nsfw" in low:
                raise Fail("safety", f"BỊ BỘ LỌC AN TOÀN CHẶN: {txt[:200]}")
            if e.code != 429 and e.code < 500:
                raise Fail("other", f"LỖI API {e.code}: {txt[:200]}")
            last = f"LỖI API {e.code}: {txt[:200]}"
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = f"LỖI MẠNG / TIMEOUT: {e}"
        time.sleep(8 * (attempt + 1))
    raise Fail("timeout", last + " (đã thử 3 lần)")


def multipart(fields, files):
    b = uuid.uuid4().hex; out = b""
    for k, v in fields.items():
        out += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    for k, name, data, ctype in files:
        out += (f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{name}"\r\n'
                f"Content-Type: {ctype}\r\n\r\n").encode() + data + b"\r\n"
    return out + f"--{b}--\r\n".encode(), f"multipart/form-data; boundary={b}"


def file_part(k, path):
    return (k, os.path.basename(path), open(path, "rb").read(), mimetypes.guess_type(path)[0] or "image/png")


def small_png(path, maxside):
    from PIL import Image
    im = Image.open(path).convert("RGB"); im.thumbnail((maxside, maxside)); buf = io.BytesIO()
    im.save(buf, "PNG"); return buf.getvalue()


def data_uri(path):
    return f"data:{mimetypes.guess_type(path)[0] or 'image/png'};base64," + base64.b64encode(open(path, "rb").read()).decode()


def fit16(w, h, maxside):
    s = min(1.0, maxside / max(w, h)); return int(w * s) // 16 * 16, int(h * s) // 16 * 16


# ---------- nhà cung cấp: trả bytes ảnh ----------
def gen_openai(k, a, prompt, size, refs):
    H = {"Authorization": f"Bearer {k['OPENAI_API_KEY']}"}
    params = {"model": a.model, "prompt": prompt, "size": size, "quality": a.quality}
    if refs:
        body, ct = multipart(params, [file_part("image[]", f) for f in refs])
        res = http("https://api.openai.com/v1/images/edits", body, {**H, "Content-Type": ct}, timeout=600)
    else:
        res = http("https://api.openai.com/v1/images/generations", json.dumps(params).encode(),
                   {**H, "Content-Type": "application/json"}, timeout=600)
    return base64.b64decode(res["data"][0]["b64_json"])


def gen_gemini(k, a, prompt, size, refs):
    model = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")
    parts = [{"text": prompt}] + [{"inline_data": {"mime_type": mimetypes.guess_type(f)[0] or "image/png",
                                                  "data": base64.b64encode(open(f, "rb").read()).decode()}} for f in refs]
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": a.ratio or "9:16"}}}
    res = http(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
               json.dumps(body).encode(), {"x-goog-api-key": k["GEMINI_API_KEY"], "Content-Type": "application/json"})
    for p in res.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        d = p.get("inlineData") or p.get("inline_data")
        if d: return base64.b64decode(d["data"])
    raise Fail("safety" if "SAFETY" in json.dumps(res) else "other", f"Gemini không trả ảnh: {json.dumps(res)[:200]}")


def gen_fal(k, a, prompt, size, refs):
    model = os.environ.get("FAL_IMAGE_MODEL", "fal-ai/nano-banana")
    body = {"prompt": prompt, "num_images": 1, "aspect_ratio": a.ratio or "9:16", "output_format": "png"}
    if refs: model += "/edit"; body["image_urls"] = [data_uri(f) for f in refs]
    res = http(f"https://fal.run/{model}", json.dumps(body).encode(),
               {"Authorization": f"Key {k['FAL_KEY']}", "Content-Type": "application/json"}, timeout=600)
    return http(res["images"][0]["url"], raw=True)


def gen_replicate(k, a, prompt, size, refs):
    model = os.environ.get("REPLICATE_IMAGE_MODEL", "google/nano-banana")
    inp = {"prompt": prompt, "aspect_ratio": a.ratio or "9:16", "output_format": "png"}
    if refs: inp["image_input"] = [data_uri(f) for f in refs]
    res = http(f"https://api.replicate.com/v1/models/{model}/predictions", json.dumps({"input": inp}).encode(),
               {"Authorization": f"Bearer {k['REPLICATE_API_TOKEN']}", "Content-Type": "application/json", "Prefer": "wait"}, timeout=600)
    out = res.get("output")
    url = out[0] if isinstance(out, list) else out
    if not url: raise Fail("other", f"Replicate chưa trả ảnh (status {res.get('status')})")
    return http(url, raw=True)


def gen_cloudflare(k, a, prompt, size, refs):
    model = os.environ.get("CLOUDFLARE_IMAGE_MODEL", "@cf/black-forest-labs/flux-2-klein-9b")
    w, h = fit16(*map(int, size.split("x")), 1920)                       # giới hạn 256–1920
    files = [(f"input_image_{i}", f"ref{i}.png", small_png(f, 511), "image/png") for i, f in enumerate(refs[:4])]  # ref < 512px, tối đa 4
    body, ct = multipart({"prompt": prompt[:2048], "width": w, "height": h}, files)
    res = http(f"https://api.cloudflare.com/client/v4/accounts/{k['CLOUDFLARE_ACCOUNT_ID']}/ai/run/{model}", body,
               {"Authorization": f"Bearer {k['CLOUDFLARE_API_TOKEN']}", "Content-Type": ct})
    img = (res.get("result") or {}).get("image")
    if not img: raise Fail("other", f"Cloudflare không trả ảnh: {json.dumps(res)[:200]}")
    return base64.b64decode(img)


def gen_pollinations(k, a, prompt, size, refs):
    w, h = fit16(*map(int, size.split("x")), 1536)
    q = {"width": w, "height": h, "nologo": "true"}
    if os.environ.get("POLLINATIONS_IMAGE_MODEL"): q["model"] = os.environ["POLLINATIONS_IMAGE_MODEL"]
    H = {"Authorization": f"Bearer {k['POLLINATIONS_KEY']}"}
    url = "https://gen.pollinations.ai/image/" + urllib.parse.quote(prompt[:1800]) + "?" + urllib.parse.urlencode(q)
    return http(url, headers=H, raw=True)


def gen_huggingface(k, a, prompt, size, refs):
    model = os.environ.get("HF_IMAGE_MODEL", "black-forest-labs/FLUX.1-schnell")
    w, h = fit16(*map(int, size.split("x")), 1344)
    return http(f"https://router.huggingface.co/hf-inference/models/{model}",
                json.dumps({"inputs": prompt, "parameters": {"width": w, "height": h}}).encode(),
                {"Authorization": f"Bearer {k['HF_TOKEN']}", "Content-Type": "application/json"}, raw=True)


def gen_custom(k, a, prompt, size, refs, cfg):
    base, H = cfg["base_url"].rstrip("/"), {"Authorization": f"Bearer {k[cfg['key_env']]}"}
    params = {"model": cfg["model"], "prompt": prompt, "size": size, "n": 1, "response_format": "b64_json"}
    if refs:
        body, ct = multipart(params, [file_part("image", f) for f in refs])
        res = http(base + "/images/edits", body, {**H, "Content-Type": ct}, timeout=600)
    else:
        res = http(base + "/images/generations", json.dumps(params).encode(), {**H, "Content-Type": "application/json"}, timeout=600)
    d = res["data"][0]
    return base64.b64decode(d["b64_json"]) if d.get("b64_json") else http(d["url"], raw=True)


GEN = {"openai": gen_openai, "gemini": gen_gemini, "fal": gen_fal, "replicate": gen_replicate,
       "cloudflare": gen_cloudflare, "pollinations": gen_pollinations, "huggingface": gen_huggingface}


def to_target(data, size, out):
    """Lưu PNG. Nhà trả sai tỷ lệ → cắt giữa về đúng tỷ lệ yêu cầu (không phóng to)."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert("RGB"); tw, th = map(int, size.split("x"))
    r, ir = tw / th, im.width / im.height
    if abs(ir - r) > 0.02:
        if ir > r: nw = int(im.height * r); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
        else: nh = int(im.width / r); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    im.save(out, "PNG"); return im.size


def prep_ref(path, tmp):
    if not os.path.exists(path):
        die(1, f"KHÔNG THẤY FILE REF: {path} (file Drive chưa tải offline?)")
    if os.path.splitext(path)[1].lower() in OK_EXT:
        return path
    out = os.path.join(tmp, os.path.splitext(os.path.basename(path))[0] + ".png")
    try:  # Pillow chạy cả Mac lẫn Windows; sips (chỉ Mac) để đỡ định dạng Pillow không đọc được (VD HEIC)
        from PIL import Image
        Image.open(path).save(out, "PNG")
    except Exception:
        subprocess.run(["sips", "-s", "format", "png", path, "--out", out], check=True, capture_output=True)
    return out


def pick_other(reason, tried):
    """Popup chọn nhà cung cấp khác + dán key. Trả tên nhà, hoặc None nếu huỷ / không mở được popup."""
    try:
        r = subprocess.run(["sh", os.path.join(TOOLS, "pick-provider.sh"), "image", reason, ",".join(tried)],
                           capture_output=True, text=True, encoding="utf-8", timeout=900)
    except Exception:
        return None
    name = (r.stdout or "").strip().splitlines()[-1:] or [""]
    global PROVIDERS
    PROVIDERS = providers()  # có thể vừa thêm nhà tự thêm trong popup
    return name[0] if r.returncode == 0 and name[0] in PROVIDERS else None


def check(provider):
    k = keys_for(provider)
    if provider == "openai":
        http("https://api.openai.com/v1/models", headers={"Authorization": f"Bearer {k['OPENAI_API_KEY']}"})
    elif provider == "gemini":
        http("https://generativelanguage.googleapis.com/v1beta/models", headers={"x-goog-api-key": k["GEMINI_API_KEY"]})
    elif provider == "cloudflare":
        http("https://api.cloudflare.com/client/v4/user/tokens/verify", headers={"Authorization": f"Bearer {k['CLOUDFLARE_API_TOKEN']}"})
    print(f"{provider}: OK" + ("" if provider in ("openai", "gemini", "cloudflare") else " (đã có key — kiểm thật ở lần gen đầu)"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt-file"); p.add_argument("--out")
    p.add_argument("--ref", action="append", default=[])
    p.add_argument("--model", default="gpt-image-2", help="model của OpenAI")
    p.add_argument("--ratio", choices=RATIOS)
    p.add_argument("--size", help="WxH tuỳ chỉnh, thay cho --ratio")
    p.add_argument("--quality", default="medium", choices=["low", "medium", "high"])
    p.add_argument("--provider", help="id nhà cung cấp — xem --list-providers")
    p.add_argument("--no-fallback", action="store_true", help="không mở popup đổi nhà cung cấp khi lỗi")
    p.add_argument("--require-ref", action="store_true",
                   help="ảnh có nhân vật / label sản phẩm: chỉ dùng nhà nhận ảnh tham chiếu, không bao giờ bỏ ref")
    p.add_argument("--check", action="store_true"); p.add_argument("--list-providers", action="store_true")
    a = p.parse_args()
    provider = a.provider or read_kv(PREFS).get("IMAGE_PROVIDER") or "openai"
    if provider not in PROVIDERS: provider = "openai"
    if a.list_providers:
        for n, (ks, ref, free, desc, cfg) in PROVIDERS.items(): print(f"{n:16s} {desc} · key: {' + '.join(ks)}")
        return
    if a.check:
        try: check(provider)
        except Fail as f: die(4, f"{provider}: {f}")
        return
    if not (a.prompt_file and a.out and (a.ratio or a.size)):
        p.error("cần --prompt-file, --out và --ratio (hoặc --size)")
    if os.path.exists(a.out):
        die(1, f"FILE ĐÃ CÓ, không ghi đè: {a.out} → tăng _vN")

    log = os.path.join(os.path.dirname(os.path.abspath(a.out)), "_gen-log.jsonl")
    base = re.sub(r"_v\d+(\.\w+)$", "", os.path.basename(a.out))
    turns = 0
    if os.path.exists(log):
        turns = sum(1 for l in open(log, encoding="utf-8") if l.strip() and json.loads(l).get("image") == base)
    if turns >= MAX_TURNS:
        die(3, f"HẾT LƯỢT: {base} đã gen {turns} lần (1 gen + 1 sửa) → ghi note để user tự sửa tay")

    prompt = open(a.prompt_file, encoding="utf-8").read().strip()
    size = a.size or RATIOS[a.ratio]
    tried, notes = [], []
    with tempfile.TemporaryDirectory() as tmp:
        refs = [prep_ref(f, tmp) for f in a.ref]
        while True:
            tried.append(provider)
            use_refs = refs if PROVIDERS[provider][1] else []
            try:
                if refs and not use_refs:
                    if a.require_ref:   # ảnh nhân vật / label sản phẩm: không được bỏ ảnh tham chiếu
                        raise Fail("noref", f"{provider} không nhận ảnh tham chiếu, ảnh này bắt buộc có ref")
                    notes.append(f"{provider} không nhận ảnh tham chiếu → bỏ {len(refs)} ref, kiểm kỹ sản phẩm/nhân vật")
                cfg = PROVIDERS[provider][4]
                data = (gen_custom(keys_for(provider), a, prompt, size, use_refs, cfg) if cfg
                        else GEN[provider](keys_for(provider), a, prompt, size, use_refs))
                break
            except Fail as f:
                if f.kind == "safety": die(2, f"{provider}: {f}")
                if f.kind == "other": die(1, f"{provider}: {f}")
                reason = {"key": "key sai / thiếu", "credit": "hết credit / hạn mức", "timeout": "timeout / mất mạng",
                          "noref": "không nhận ảnh tham chiếu"}[f.kind]
                magic = spell(provider, f.kind)
                print(f"🔮 {magic}", flush=True)                     # Claude chép nguyên câu này cho user
                print(f"{provider}: {f}", file=sys.stderr)
                skip = tried + ([n for n, v in PROVIDERS.items() if not v[1]] if a.require_ref and refs else [])
                nxt = None if a.no_fallback else pick_other(f"{magic}\n({provider}: {reason})", skip)
                if not nxt: die(4, f"{provider}: {f} → không đổi được nhà cung cấp, xuất thẻ tự gen")
                print(f"→ chuyển sang {nxt}", file=sys.stderr)
                provider = nxt

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    w, h = to_target(data, size, a.out)
    entry = {"time": datetime.datetime.now().isoformat(timespec="seconds"), "image": base, "file": os.path.basename(a.out),
             "turn": turns + 1, "provider": provider, "tried": tried, "model": a.model if provider == "openai" else "",
             "prompt": prompt, "size": f"{w}x{h}", "quality": a.quality, "refs": a.ref, "notes": notes}
    with open(log, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    for n in notes: print("⚠️ " + n)
    print(f"{a.out} ({provider}, {w}x{h}, lượt {turns + 1}/{MAX_TURNS})")


if __name__ == "__main__":
    main()
