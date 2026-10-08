#!/usr/bin/env python3
"""Gen nhạc nền (không lời) qua API — dùng khi KHÔNG có connector ElevenLabs trên Claude, hoặc user chọn MUSIC_TOOL=api.

  python3 _tools/gen-music.py --prompt "bright minimal pop, soft plucks, 100 bpm, no vocals" --seconds 20 \
          --out outputs/audio/X_music_v1.mp3 [--provider elevenlabs_music]
  python3 _tools/gen-music.py --provider freesound_cc0 --query "upbeat pop loop" --seconds 20 --out ... [--pick 2]
  python3 _tools/gen-music.py --list-providers

Nhà cung cấp: --provider > MUSIC_PROVIDER trong ~/.config/ai-studio/prefs.env > freesound_cc0.
Danh sách + cách lấy key: _tools/providers.json mục "music":
  freesound_cc0 — MIỄN PHÍ: tìm nhạc CÓ SẴN giấy phép CC0 (dùng ads được, không cần ghi nguồn) trên Freesound,
                  --query = 2–4 từ khoá tiếng Anh (mood + thể loại, VD "chill lofi loop"); in 5 bài ứng viên,
                  --pick N chọn bài khác. Không phải AI gen → nghe thử trước khi dùng.
  gemini_lyria  — Google Lyria 3 (AI gen, trả phí, key Gemini) · elevenlabs_music (gói trả phí) · replicate_music (trả theo lượt).
Bản dài hơn --seconds → tự cắt + fade out 1.5s (ffmpeg).
Luôn ép không lời (force_instrumental). Sau khi gen: kiểm không vocal bằng faster-whisper như audio-plan dặn.
Mỗi bản nhạc (cùng tên, bỏ _vN) tối đa 2 lượt (1 gen + 1 sửa). Exit giống gen-image.py.
"""
import argparse, base64, os, subprocess, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _api as A

MAX_TURNS = 2


def compose(provider, k, a):
    if provider == "freesound_cc0":
        return freesound(k, a)
    if provider == "gemini_lyria":
        model = a.model or ("lyria-3-clip-preview" if a.seconds <= 30 else "lyria-3.5")
        text = a.prompt + f". About {int(round(a.seconds))} seconds. Instrumental only, no vocals."
        r = A.http("https://generativelanguage.googleapis.com/v1beta/interactions", {"model": model, "input": text},
                   {"x-goog-api-key": k["GEMINI_API_KEY"]}, timeout=600)
        audio = [c for st in r.get("steps", []) if st.get("type") == "model_output"
                 for c in st.get("content", []) if c.get("type") == "audio"]
        if not audio: raise A.Fail("other", f"Lyria không trả audio: {str(r)[:300]}")
        return base64.b64decode(audio[-1]["data"])
    if provider == "elevenlabs_music":
        body = {"prompt": a.prompt, "music_length_ms": int(a.seconds * 1000), "model_id": a.model or "music_v1",
                "force_instrumental": True}
        return A.http("https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128", body,
                      {"xi-api-key": k["ELEVENLABS_API_KEY"]}, raw=True, timeout=600)
    if provider == "replicate_music":
        H = {"Authorization": f"Bearer {k['REPLICATE_API_TOKEN']}"}
        model = a.model or "meta/musicgen"
        ver = A.http(f"https://api.replicate.com/v1/models/{model}", headers=H)["latest_version"]["id"]
        r = A.http("https://api.replicate.com/v1/predictions",
                   {"version": ver, "input": {"prompt": a.prompt + ", instrumental, no vocals",
                                              "duration": int(round(a.seconds)), "output_format": "mp3"}}, H)
        return poll_replicate(r, H)
    raise A.Fail("other", f"nhà cung cấp lạ: {provider}")


def freesound(k, a):
    """Tìm bài CC0 đủ dài, không lời; in 5 ứng viên; tải bản preview chất lượng cao (không cần OAuth)."""
    q = (a.query or "background music loop") + " -vocal -vocals -voice -singing -speech"
    flt = f'license:"Creative Commons 0" duration:[{max(3, a.seconds)} TO {a.seconds * 6 + 30}]'
    url = "https://freesound.org/apiv2/search/?" + urllib.parse.urlencode(
        {"query": q, "filter": flt, "sort": "rating_desc", "page_size": 15,
         "fields": "id,name,username,duration,license,previews,url,avg_rating,num_downloads"})
    res = A.http(url, headers={"Authorization": f"Token {k['FREESOUND_API_KEY']}"}).get("results", [])
    if not res: raise A.Fail("other", f"Freesound không có bài CC0 nào khớp \"{a.query}\" → đổi --query (VD \"upbeat pop\", \"chill lofi\")")
    for i, t in enumerate(res[:5], 1):
        print(f"  {'▶' if i == a.pick else ' '} {i}. {t['name']} — {t['username']} · {t['duration']:.0f}s · ★{t.get('avg_rating', 0):.1f} · {t['url']}")
    t = res[min(a.pick, len(res)) - 1]
    a.source = {"title": t["name"], "author": t["username"], "url": t["url"], "license": t["license"]}
    return A.http(t["previews"]["preview-hq-mp3"], raw=True, timeout=300)


def fit_length(out, seconds):
    """Dài hơn cần → cắt đúng độ dài + fade out 1.5s."""
    dur = A.duration(out)
    if not (dur and A.ffmpeg() and dur > seconds + 0.5): return
    tmp = out + ".tmp" + os.path.splitext(out)[1]
    fo = max(0.0, seconds - 1.5)
    subprocess.run([A.ffmpeg(), "-v", "error", "-y", "-i", out, "-t", str(seconds), "-af", f"afade=t=out:st={fo}:d=1.5", tmp], check=True)
    os.replace(tmp, out)


def poll_replicate(r, H, limit=900):
    t0 = time.time()
    while r.get("status") not in ("succeeded", "failed", "canceled"):
        if time.time() - t0 > limit: raise A.Fail("timeout", f"Replicate chạy quá {limit}s")
        time.sleep(5); r = A.http(r["urls"]["get"], headers=H)
    if r["status"] != "succeeded":
        err = str(r.get("error") or r["status"])
        raise A.Fail("safety" if "nsfw" in err.lower() or "safety" in err.lower() else "other", f"Replicate: {err[:300]}")
    out = r["output"]; url = out[0] if isinstance(out, list) else out
    return A.http(url, raw=True, timeout=600)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt"); p.add_argument("--prompt-file"); p.add_argument("--out")
    p.add_argument("--seconds", type=float, help="độ dài = tổng thời lượng video (+1–2s để fade)")
    p.add_argument("--provider"); p.add_argument("--model")
    p.add_argument("--query", help="freesound: 2–4 từ khoá tiếng Anh, VD 'upbeat pop loop'")
    p.add_argument("--pick", type=int, default=1, help="freesound: chọn bài thứ N trong danh sách ứng viên")
    p.add_argument("--no-fallback", action="store_true"); p.add_argument("--list-providers", action="store_true")
    a = p.parse_args()
    P = A.providers("music")
    if a.list_providers:
        for n, v in P.items(): print(f"{n:18s} {v['label']} · key: {' + '.join(k['env'] for k in v['keys'])}")
        return
    a.prompt = a.prompt or (open(a.prompt_file, encoding="utf-8").read().strip() if a.prompt_file else "")
    a.source = None
    if not ((a.prompt or a.query) and a.out and a.seconds): p.error("cần --prompt (hoặc --prompt-file / --query), --seconds và --out")
    A.guard_out(a.out)
    turns = A.turns_used(a.out, "audio")
    if turns >= MAX_TURNS: A.die(3, f"HẾT LƯỢT: {A.asset_base(a.out)} đã gen {turns} lần (1 gen + 1 sửa) → user tự chọn nhạc")
    provider = a.provider or A.default_provider("music", "freesound_cc0")
    if provider not in P: provider = "freesound_cc0"
    if provider != "freesound_cc0" and not a.prompt: a.prompt = a.query
    provider, data, tried = A.run("music", provider, lambda pv, k: compose(pv, k, a), a.no_fallback)
    out = A.save_media(data, a.out)
    fit_length(out, a.seconds)
    dur = A.duration(out)
    A.write_log(out, "audio", {"turn": turns + 1, "provider": provider, "tried": tried, "prompt": a.prompt or a.query,
                               "seconds": dur, "source": a.source})
    if a.source: print(f"📜 Nguồn: {a.source['title']} — {a.source['author']} · {a.source['license']} · {a.source['url']} (ghi vào Danh sách asset)")
    print(f"{out} ({provider}, {dur if dur is not None else '?'}s, lượt {turns + 1}/{MAX_TURNS}) → kiểm không vocal bằng faster-whisper")


if __name__ == "__main__":
    main()
