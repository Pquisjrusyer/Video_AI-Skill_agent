#!/usr/bin/env python3
"""Bảng review video ĐÃ DỰNG (cổng 3): khung hình tiêu biểu từng cảnh + transcript đúng đoạn đó so với script.

  python3 _tools/review-board.py campaigns/<campaign> [outputs/review/<video>.mp4]

- Không chỉ video → lấy file .mp4 mới nhất trong outputs/review/ (rồi tới outputs/final/).
- Mốc cảnh + lời script lấy từ prompts-used/clips.json (không có thì scripts/storyboard.json): trường `time` dạng "0.0–3.5s".
- Mỗi cảnh: 2 khung hình (đầu + giữa cảnh) · lời nghe được trong khoảng thời gian cảnh (faster-whisper, CPU) so với
  `line_en` (chữ thiếu gạch đỏ, thừa tô vàng, % khớp) + dịch VI · kiểm: lời bị cắt ngang ranh giới cảnh, lặng quá lâu, nói quá nhanh.
- Ra outputs/review/review-board.html → gửi user bằng file card display=render. User góp ý theo mã cảnh.
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _board
from _media import probe, frame_at, transcribe, norm, diff_html, MAX_WPS, MIN_MATCH

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
if len(sys.argv) < 2:
    sys.exit(__doc__)
CAMP = sys.argv[1]

def J(*p): return os.path.join(CAMP, *p)
video = sys.argv[2] if len(sys.argv) > 2 else ""
if video and not os.path.isabs(video) and not os.path.exists(video): video = J(video)
if not video:
    cands = sorted(glob.glob(J("outputs", "review", "*.mp4")), key=os.path.getmtime) or \
            sorted(glob.glob(J("outputs", "final", "*.mp4")), key=os.path.getmtime)
    if not cands: sys.exit("Không có video trong outputs/review/ hoặc outputs/final/")
    video = cands[-1]

src = J("prompts-used", "clips.json") if os.path.exists(J("prompts-used", "clips.json")) else J("scripts", "storyboard.json")
data = json.load(open(src, encoding="utf-8"))
scenes = data.get("clips") or data.get("scenes") or []
campaign = data.get("campaign", "")

def rng(t):
    nums = re.findall(r"\d+(?:\.\d+)?", str(t or ""))
    return (float(nums[0]), float(nums[1])) if len(nums) >= 2 else None

m = probe(video); dur = m["dur"]
words = transcribe(video, data.get("lang") or "en")
max_wps = data.get("max_wps") or MAX_WPS   # tiếng Việt đếm theo tiếng (âm tiết) → nhanh hơn tiếng Anh
rows, summary, used = [], [], set()
for s in scenes:
    r = rng(s.get("time"))
    if not r: continue
    a, b = r; b = min(b, dur) if dur else b
    checks, line = [], s.get("line_en") or s.get("vo", "")
    ws = [w for w in words if a <= (w.start + w.end) / 2 < b]   # xếp theo điểm giữa từ — mốc whisper lệch ±0.2s
    used.update(id(w) for w in ws)
    heard = " ".join(w.word.strip() for w in ws)
    heard_html = ""
    if line:
        heard_html, score = diff_html(line, heard)
        checks.append((score >= MIN_MATCH, f"Lời khớp script {score*100:.0f}%"))
        if ws:
            cut = [w for w in ws if w.end > b + 0.25]
            checks.append((not cut, "Lời trọn trong cảnh" if not cut else f"Lời tràn sang cảnh sau: “{cut[-1].word.strip()}” kết thúc {cut[-1].end:.1f}s"))
            gaps = [ws[i + 1].start - ws[i].end for i in range(len(ws) - 1)]
            g = max(gaps) if gaps else 0
            checks.append((g <= 1.5, f"Khoảng lặng dài nhất {g:.1f}s" + ("" if g <= 1.5 else " — hơi hụt nhịp")))
            wps = len(norm(heard)) / max(ws[-1].end - ws[0].start, 0.1)
            checks.append((wps <= max_wps, f"Tốc độ {wps:.1f} từ/giây" + ("" if wps <= max_wps else " — nhanh, dễ rít")))
        else:
            checks.append((False, "Không nghe thấy lời trong cảnh này"))
    elif heard:
        checks.append((False, f"Script không có lời nhưng nghe thấy: “{heard[:60]}”"))
    ts = [a + min(0.3, (b - a) / 4), (a + b) / 2]
    imgs = [(t, frame_at(video, t)) for t in ts]
    imgs = [(t, im) for t, im in imgs if im]
    frames = "".join(f'<figure><img src="{_board.img_uri(im, 240)}"><figcaption>{t:.1f}s</figcaption></figure>' for t, im in imgs)
    rows.append({"id": s.get("id", ""), "time": s.get("time", ""), "purpose": s.get("purpose", ""), "tool": "Bản dựng",
                 "image": _board.img_uri(imgs[-1][1]) if imgs else "", "image_caption": f"giữa cảnh · {imgs[-1][0]:.1f}s" if imgs else "",
                 "line_en": line, "line_vi": s.get("line_vi") or s.get("vo_vi", ""), "onscreen": s.get("onscreen", ""),
                 "heard_html": heard_html, "frames_html": frames, "checks": checks, "out": os.path.relpath(video, CAMP).replace("\\", "/"), "out_abs": os.path.abspath(video),
                 "wps": data.get("wps")})
    bad = [t for ok, t in checks if not ok]
    summary.append(f"{s.get('id')}: " + ("LỖI: " + "; ".join(bad) if bad else "OK"))

stray = [w for w in words if id(w) not in used]
extra = f"<p class='muted'>Lời ngoài mọi cảnh: “{' '.join(w.word.strip() for w in stray)}”</p>" if stray else ""
total = scenes and rng(scenes[-1].get("time"))
head = f"Video: {os.path.basename(video)} · {m['w']}×{m['h']} · {dur:.2f}s" + (f" (script {total[1]:g}s)" if total else "")
page = _board.page("Review bản dựng", campaign, rows, howto=head, extra_html=extra,
                   safe=_board.safe_zone(data.get("platform")), ratio=data.get("ratio") or "9:16", duration=dur, camp_abs=os.path.abspath(CAMP))
dst = J("outputs", "review", "review-board.html"); os.makedirs(os.path.dirname(dst), exist_ok=True)
open(dst, "w", encoding="utf-8").write(page)
print(dst); print(head); print("\n".join(summary))
