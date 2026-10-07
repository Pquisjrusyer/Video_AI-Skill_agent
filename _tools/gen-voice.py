#!/usr/bin/env python3
"""Gen giọng đọc (VO) qua API — dùng khi KHÔNG có connector ElevenLabs trên Claude, hoặc user chọn VO_TOOL=api.

  python3 _tools/gen-voice.py --text "Glossy in one coat." --out outputs/audio/X_vo-S01_v1.mp3 [--provider elevenlabs]
          [--voice <id/tên giọng>] [--style "warm, confident, unhurried"] [--lang en] [--speed 1.0]
  python3 _tools/gen-voice.py --text-file scripts/vo-S01.txt --out ...
  python3 _tools/gen-voice.py --list-providers

Nhà cung cấp: --provider > VO_PROVIDER trong ~/.config/ai-studio/prefs.env > elevenlabs. Danh sách + cách lấy key:
_tools/providers.json mục "voice". Miễn phí: cloudflare_melo / cloudflare_aura (chung hạn mức 10.000 neuron/ngày với ảnh),
gemini_tts (gói free), elevenlabs (free 10.000 ký tự/tháng, KHÔNG dùng thương mại).
Giọng: --voice > ELEVENLABS_VOICE_ID trong .env (chỉ elevenlabs) > mặc định từng nhà (DEFAULT_VOICE).
--style = cách đọc (OpenAI instructions / Gemini style). Bỏ qua với nhà không hỗ trợ.
Ra file đúng đuôi --out (đổi định dạng bằng ffmpeg). In thời lượng để so với thời lượng cảnh.
Lỗi key / hết credit / timeout → câu thần chú 🔮 + popup đổi nhà (`pick-provider.sh voice`). Exit giống gen-image.py.
"""
import argparse, base64, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _api as A

DEFAULT_VOICE = {"elevenlabs": "JBFqnCBsd6RMkjVDRZzb", "openai_tts": "coral", "gemini_tts": "Kore",
                 "cloudflare_aura": "luna", "cloudflare_melo": ""}
CF = "https://api.cloudflare.com/client/v4/accounts/{}/ai/run/"


def tts(provider, k, a, text):
    voice = a.voice or (A.read_kv(A.ENV_FILE).get("ELEVENLABS_VOICE_ID") if provider == "elevenlabs" else "") \
        or DEFAULT_VOICE.get(provider, "")
    if provider == "elevenlabs":
        body = {"text": text, "model_id": a.model or "eleven_multilingual_v2",
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "speed": a.speed}}
        return A.http(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128", body,
                      {"xi-api-key": k["ELEVENLABS_API_KEY"]}, raw=True), voice
    if provider == "openai_tts":
        body = {"model": a.model or "gpt-4o-mini-tts", "voice": voice, "input": text, "response_format": "mp3", "speed": a.speed}
        if a.style: body["instructions"] = a.style
        return A.http("https://api.openai.com/v1/audio/speech", body,
                      {"Authorization": f"Bearer {k['OPENAI_API_KEY']}"}, raw=True), voice
    if provider == "gemini_tts":
        part = {"type": "text", "text": text}
        if a.style: part["annotations"] = [{"type": "speech_metadata", "style": a.style}]
        body = {"model": a.model or "gemini-3.8-flash-tts", "input": [{"type": "user_input", "content": [part]}],
                "response_format": {"type": "audio"}, "generation_config": {"speech_config": [{"voice": voice}]}}
        r = A.http("https://generativelanguage.googleapis.com/v1beta/interactions", body, {"x-goog-api-key": k["GEMINI_API_KEY"]})
        audio = [c for s in r.get("steps", []) if s.get("type") == "model_output"
                 for c in s.get("content", []) if c.get("type") == "audio"]
        if not audio: raise A.Fail("other", f"Gemini không trả audio: {str(r)[:300]}")
        return base64.b64decode(audio[-1]["data"]), voice
    if provider in ("cloudflare_melo", "cloudflare_aura"):
        H = {"Authorization": f"Bearer {k['CLOUDFLARE_API_TOKEN']}"}
        base = CF.format(k["CLOUDFLARE_ACCOUNT_ID"])
        if provider == "cloudflare_aura":
            return A.http(base + "@cf/deepgram/aura-2-en", {"text": text, "speaker": voice, "encoding": "mp3"}, H, raw=True), voice
        r = A.http(base + "@cf/myshell-ai/melotts", {"prompt": text, "lang": a.lang}, H)
        audio = (r.get("result") or {}).get("audio")
        if not audio: raise A.Fail("other", f"MeloTTS không trả audio: {str(r)[:300]}")
        return base64.b64decode(audio), a.lang
    raise A.Fail("other", f"nhà cung cấp lạ: {provider}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text"); p.add_argument("--text-file"); p.add_argument("--out")
    p.add_argument("--provider"); p.add_argument("--voice"); p.add_argument("--model")
    p.add_argument("--style", default="", help="cách đọc, VD 'warm, confident, unhurried'")
    p.add_argument("--lang", default="en", help="MeloTTS: en / es / fr / zh / ja / ko")
    p.add_argument("--speed", type=float, default=1.0)
    p.add_argument("--no-fallback", action="store_true"); p.add_argument("--list-providers", action="store_true")
    a = p.parse_args()
    P = A.providers("voice")
    if a.list_providers:
        for n, v in P.items(): print(f"{n:16s} {v['label']} · key: {' + '.join(k['env'] for k in v['keys'])}")
        return
    text = a.text or (open(a.text_file, encoding="utf-8").read().strip() if a.text_file else "")
    if not (text and a.out): p.error("cần --text (hoặc --text-file) và --out")
    A.guard_out(a.out)
    provider = a.provider or A.default_provider("voice", "elevenlabs")
    if provider not in P: provider = "elevenlabs"

    def gen(pv, k):
        return tts(pv, k, a, text)
    provider, (data, voice), tried = A.run("voice", provider, gen, a.no_fallback)
    out = A.save_media(data, a.out)
    dur = A.duration(out)
    A.write_log(out, "audio", {"turn": A.turns_used(out, "audio") + 1, "provider": provider, "tried": tried,
                               "voice": voice, "style": a.style, "text": text, "seconds": dur})
    print(f"{out} ({provider}, giọng {voice or 'mặc định'}, {dur if dur is not None else '?'}s)")


if __name__ == "__main__":
    main()
