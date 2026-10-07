#!/usr/bin/env python3
"""Bảng bàn giao + duyệt clip: prompts-used/clips.json → outputs/review/clip-board.html

  python3 _tools/clip-board.py campaigns/<campaign>

- Trước khi render: bảng bàn giao (ảnh khung đầu, cài đặt công cụ, prompt EN có nút Copy + dịch VI,
  lời thoại EN + VI, file lưu về, ô "Xong").
- Sau khi clip đã có ở đường dẫn `out`: chạy lại → mỗi cảnh thêm 3 khung hình cắt từ clip thật,
  lời nói thật (faster-whisper, CPU) so với lời thoại script (chữ thiếu / thừa tô màu, % khớp),
  và danh sách kiểm tra (tỷ lệ, độ dài, lời bị cắt, tốc độ nói).
Cần: ffmpeg + ffprobe trên PATH, Pillow, faster-whisper (chỉ khi có lời). Cấu trúc JSON: `_prompts/handoff-template.md`.
"""
import difflib, html, io, json, os, re, subprocess, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _board

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
if len(sys.argv) < 2:
    sys.exit(__doc__)

CAMP = sys.argv[1]
data = json.load(open(os.path.join(CAMP, "prompts-used", "clips.json"), encoding="utf-8"))

def P(rel): return os.path.join(CAMP, rel) if rel else ""
b64_img = _board.img_uri
from _media import probe, frame_at, transcribe, norm, diff_html, MAX_WPS, MIN_MATCH

rows, summary = [], []
for c in data.get("clips", []):
    out_path, checks, frames_html, heard_html = P(c.get("out")), [], "", ""
    ff = P(c.get("first_frame"))
    first = _board.full_uri(Image.open(ff)) if ff and os.path.exists(ff) else ""
    use_s = float(c.get("use_s") or 0); render_s = c.get("render_s", "")
    status = "chờ render"
    if out_path and os.path.exists(out_path):
        status = "đã có clip"
        m = probe(out_path); dur = m["dur"] or 0.0
        ratio_ok = m["h"] and abs(m["w"] / m["h"] - 9 / 16) < 0.02
        checks.append((ratio_ok, f'Khung {m["w"]}×{m["h"]} · {m["fps"]}fps' + ("" if ratio_ok else " — không phải 9:16")))
        checks.append((not use_s or dur + 0.05 >= use_s, f"Dài {dur:.2f}s (cần dùng {use_s:g}s)"))
        ts = [0.1, (use_s or dur) / 2, max(0.1, (use_s or dur) - 0.15)]
        imgs = [(t, frame_at(out_path, t)) for t in ts]
        frames_html = "".join(f'<figure><img src="{b64_img(im, 240)}"><figcaption>{t:.1f}s</figcaption></figure>' for t, im in imgs if im)
        audio_src = out_path if c.get("audio", "in-clip") == "in-clip" else P(c["audio"][3:]) if str(c.get("audio", "")).startswith("vo:") else ""
        if c.get("line_en") and audio_src and os.path.exists(audio_src):
            words = transcribe(audio_src)
            heard = " ".join(w.word.strip() for w in words)
            heard_html, score = diff_html(c["line_en"], heard)
            checks.append((score >= MIN_MATCH, f"Lời khớp script {score*100:.0f}%"))
            if words:
                start, end = words[0].start, words[-1].end; n = len(norm(heard))
                wps = n / max(end - start, 0.1)
                checks.append((not use_s or end <= use_s, f"Lời {start:.1f}s → {end:.1f}s" + ("" if not use_s or end <= use_s else f" — vượt {use_s:g}s, sẽ bị cắt")))
                checks.append((wps <= MAX_WPS, f"Tốc độ {wps:.1f} từ/giây" + ("" if wps <= MAX_WPS else " — nhanh, dễ rít")))
            else:
                checks.append((False, "Không nghe thấy lời nào"))
        elif c.get("line_en"):
            checks.append((False, "Chưa có file âm thanh để kiểm lời"))
    bad = [t for ok, t in checks if not ok]
    summary.append(f"{c['id']}: {status}" + (f" · LỖI: {'; '.join(bad)}" if bad else (" · OK" if checks else "")))
    rows.append({
        "id": c["id"], "time": c.get("time", ""), "purpose": c.get("purpose", ""), "tool": c.get("tool", ""),
        "render_s": c.get("render_s", ""), "use_s": f"{use_s:g}" if use_s else "", "status": status,
        "image": first, "image_caption": os.path.basename(c.get("first_frame", "")),
        "image_name": _board.jpg_name(ff) if first else "",
        "prompts": [("Prompt", c.get("prompt_en", ""), c.get("prompt_vi", ""))],
        "line_en": c.get("line_en", ""), "line_vi": c.get("line_vi", ""), "onscreen": c.get("onscreen", ""), "notes_vi": c.get("notes_vi", ""),
        "heard_html": heard_html, "frames_html": frames_html, "out": c.get("out", ""), "checks": checks, "wps": data.get("wps"),
    })

ch = data.get("character") or {}
ch_imgs = [(_board.full_uri(Image.open(P(im))), os.path.basename(im), _board.jpg_name(im)) for im in ch.get("images", []) if os.path.exists(P(im))]
page = _board.page("Bàn giao + duyệt clip", data.get("campaign", ""), rows, top_html=_board.character_html(ch, ch_imgs),
    safe=_board.safe_zone(data.get("platform")), ratio=data.get("ratio") or "9:16", duration=data.get("duration"), howto=" · ".join(
    x for x in (data.get("title", ""), data.get("howto", "")) if x))
dst = os.path.join(CAMP, "outputs", "review", "clip-board.html")
os.makedirs(os.path.dirname(dst), exist_ok=True)
open(dst, "w", encoding="utf-8").write(page)
print(dst); print("\n".join(summary))
