#!/usr/bin/env python3
"""Gen nhạc nền (không lời) qua API — dùng khi KHÔNG có connector ElevenLabs trên Claude, hoặc user chọn MUSIC_TOOL=api.

  python3 _tools/gen-music.py --prompt "bright minimal pop, soft plucks, 100 bpm, no vocals" --seconds 20 \
          --out outputs/audio/X_music_v1.mp3 [--provider elevenlabs_music]
  python3 _tools/gen-music.py --list-providers

Nhà cung cấp: --provider > MUSIC_PROVIDER trong ~/.config/ai-studio/prefs.env > elevenlabs_music.
Danh sách + cách lấy key: _tools/providers.json mục "music". Nhạc gần như không có nhà miễn phí thật:
elevenlabs_music cần gói trả phí · replicate_music trả theo lượt (rẻ, thường có credit dùng thử).
Luôn ép không lời (force_instrumental). Sau khi gen: kiểm không vocal bằng faster-whisper như audio-plan dặn.
Mỗi bản nhạc (cùng tên, bỏ _vN) tối đa 2 lượt (1 gen + 1 sửa). Exit giống gen-image.py.
"""
import argparse, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _api as A

MAX_TURNS = 2


def compose(provider, k, a):
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
    p.add_argument("--no-fallback", action="store_true"); p.add_argument("--list-providers", action="store_true")
    a = p.parse_args()
    P = A.providers("music")
    if a.list_providers:
        for n, v in P.items(): print(f"{n:18s} {v['label']} · key: {' + '.join(k['env'] for k in v['keys'])}")
        return
    a.prompt = a.prompt or (open(a.prompt_file, encoding="utf-8").read().strip() if a.prompt_file else "")
    if not (a.prompt and a.out and a.seconds): p.error("cần --prompt (hoặc --prompt-file), --seconds và --out")
    A.guard_out(a.out)
    turns = A.turns_used(a.out, "audio")
    if turns >= MAX_TURNS: A.die(3, f"HẾT LƯỢT: {A.asset_base(a.out)} đã gen {turns} lần (1 gen + 1 sửa) → user tự chọn nhạc")
    provider = a.provider or A.default_provider("music", "elevenlabs_music")
    if provider not in P: provider = "elevenlabs_music"
    provider, data, tried = A.run("music", provider, lambda pv, k: compose(pv, k, a), a.no_fallback)
    out = A.save_media(data, a.out)
    dur = A.duration(out)
    A.write_log(out, "audio", {"turn": turns + 1, "provider": provider, "tried": tried, "prompt": a.prompt, "seconds": dur})
    print(f"{out} ({provider}, {dur if dur is not None else '?'}s, lượt {turns + 1}/{MAX_TURNS}) → kiểm không vocal bằng faster-whisper")


if __name__ == "__main__":
    main()
