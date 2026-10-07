#!/usr/bin/env python3
"""Storyboard có hình (cổng 1): scripts/storyboard.json → scripts/storyboard.md + scripts/storyboard.html

  python3 _tools/storyboard.py campaigns/<campaign>

- .html: cùng khung với bảng clip (`clip-board.py`) — mỗi cảnh: mã · thời gian · mục đích · công cụ · render/dùng ·
  ảnh minh hoạ · prompt ảnh + prompt video (nháp) có nút Copy kèm dịch VI · lời thoại/VO EN + VI · chữ trên màn hình ·
  file lưu về. Copy prompt sang nền tảng nào cũng đủ thông tin. Gửi user bằng file card display=render.
- .md : bảng gọn cho các bước sau đọc.
Đường dẫn trong JSON tính từ thư mục campaign. Cấu trúc JSON: `_prompts/templates/storyboard-template.md`.
"""
import json, os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _board

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
if len(sys.argv) < 2:
    sys.exit(__doc__)
camp = sys.argv[1]
sb = json.load(open(os.path.join(camp, "scripts", "storyboard.json"), encoding="utf-8"))
scenes = sb.get("scenes", [])

def cell(s): return str(s or "").replace("|", "\\|").replace("\n", "<br>")
def line_en(s): return s.get("line_en") or s.get("vo", "")
def line_vi(s): return s.get("line_vi") or s.get("vo_vi", "")
def prompts(s):
    return [("Prompt ảnh (khung đầu)", s.get("prompt_en", ""), s.get("prompt_vi", "")),
            ("Prompt video (nháp — chốt lại ở cổng 2 theo ảnh thật)", s.get("video_prompt_en", ""), s.get("video_prompt_vi", ""))]

# ---------- Markdown ----------
md = [f"# Storyboard — {sb.get('campaign', '')}", "",
      "> Sinh từ `scripts/storyboard.json` bằng `_tools/storyboard.py` — sửa JSON rồi chạy lại, không sửa tay file này.",
      f"> {sb.get('duration', '')} · {sb.get('ratio', '')} · {sb.get('format', '')}", ""]
if sb.get("look"): md += [f"**Look chung:** {sb['look']}", ""]
md += ["| Cảnh | Thời gian | Mục đích | Ảnh | Hình (mô tả) | Lời thoại / VO | Dịch | Ước tính lời | Chữ trên màn hình | Công cụ · render/dùng | Lưu về |",
       "|---|---|---|---|---|---|---|---|---|---|---|"]
for s in scenes:
    im = f"![{s['id']}](../{s['image']})".replace(" ", "%20") if s.get("image") else "—"
    rd = f"{cell(s.get('tool'))} · {s.get('render_s', '')}s/{s.get('use_s', '')}s" if s.get("render_s") else cell(s.get("tool"))
    md.append(f"| {s['id']} | {cell(s.get('time'))} | {cell(s.get('purpose'))} | {im} | {cell(s.get('visual_vi'))} | "
              f"{cell(line_en(s))} | {cell(line_vi(s))} | {cell(_board.line_estimate(line_en(s), s.get('use_s'), sb.get('wps') or _board.WPS))} | "
              f"{cell(s.get('onscreen'))} | {rd} | {cell(s.get('out'))} |")
md += ["", "## Prompt từng cảnh (EN → dịch VI)", ""]
for s in scenes:
    md += [f"### {s['id']}", ""]
    for lbl, en, vi in prompts(s):
        if en: md += [f"**{lbl}:**", "", "```", en, "```", "", f"**Dịch:** {vi}", ""]
    if s.get("notes_vi"): md += [f"**Ghi chú:** {s['notes_vi']}", ""]
for key, title in (("images", "Danh sách ảnh"), ("assets", "Danh sách asset")):
    rows = sb.get(key) or []
    if rows:
        cols = list(rows[0].keys())
        md += [f"## {title}", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        md += ["| " + " | ".join(cell(r.get(c)) for c in cols) + " |" for r in rows] + [""]
open(os.path.join(camp, "scripts", "storyboard.md"), "w", encoding="utf-8").write("\n".join(md))

# ---------- HTML ----------
rows = []
for s in scenes:
    p = os.path.join(camp, s["image"]) if s.get("image") else ""
    rows.append({
        "id": s["id"], "time": s.get("time", ""), "purpose": s.get("purpose", ""),
        "tool": " · ".join(x for x in (s.get("tool", ""), s.get("route", "")) if x),
        "render_s": s.get("render_s", ""), "use_s": s.get("use_s", ""),
        "image": _board.full_uri(Image.open(p)) if p and os.path.exists(p) else "",
        "image_name": _board.jpg_name(p) if p and os.path.exists(p) else "",
        "image_abs": os.path.abspath(p) if p and os.path.exists(p) else "",
        "out_abs": os.path.abspath(os.path.join(camp, s["out"])) if s.get("out") else "",
        "image_caption": os.path.basename(s.get("image", "")) + (" (ảnh minh hoạ)" if "_P-" in s.get("image", "") else ""),
        "visual_vi": s.get("visual_vi", ""), "prompts": prompts(s),
        "line_en": line_en(s), "line_vi": line_vi(s), "onscreen": s.get("onscreen", ""),
        "notes_vi": s.get("notes_vi", ""), "out": s.get("out", ""), "wps": sb.get("wps"),
    })
plat = sb.get("platform") or {}

# ---------- Kiểm lố thời lượng: cảnh + lời đọc ước tính so với thời lượng brief ----------
def _end(t):
    import re as _re
    n = _re.findall(r"\d+(?:\.\d+)?", str(t or "")); return float(n[1]) if len(n) >= 2 else None
target = _board._secs(sb.get("duration"))
wps = sb.get("wps") or _board.WPS
scene_end = max([x for x in (_end(s.get("time")) for s in scenes) if x is not None], default=None)
words = sum(len(__import__("re").findall(r"[A-Za-z0-9']+", line_en(s) or "")) for s in scenes)
problems = []
if target is None:
    problems.append("Chưa có thời lượng video trong storyboard.json → HỎI USER bao nhiêu giây trước khi làm tiếp")
else:
    if scene_end is not None and scene_end > target + 0.2:
        problems.append(f"Các cảnh kéo dài tới {scene_end:g}s, LỐ {scene_end - target:.1f}s so với {target:g}s")
    if scene_end is not None and scene_end < target - 0.5:
        problems.append(f"Các cảnh chỉ tới {scene_end:g}s, THIẾU {target - scene_end:.1f}s so với {target:g}s")
    if words and words / wps > target + 0.2:
        problems.append(f"Lời đọc {words} từ ≈ {words / wps:.1f}s, LỐ {words / wps - target:.1f}s so với {target:g}s → rút lời")
warn_html = ("<div class='look' style='border-color:var(--bad);background:var(--bad-soft);color:var(--bad)'><b>⚠️ Kiểm thời lượng:</b><br>"
             + "<br>".join(_board.e(p) for p in problems) + "</div>") if problems else ""
meta = " · ".join(x for x in (sb.get("duration", ""), sb.get("ratio", ""), sb.get("format", ""),
                              ("Bản phụ: " + ", ".join(plat["extra_ratios"])) if plat.get("extra_ratios") else "",
                              ("Template: " + plat["template"]) if plat.get("template") else "") if x)
ch = sb.get("character") or {}
ch_imgs = [(_board.full_uri(Image.open(os.path.join(camp, im))), os.path.basename(im), _board.jpg_name(im))
           for im in ch.get("images", []) if os.path.exists(os.path.join(camp, im))]
html_out = _board.page("Storyboard", sb.get("campaign", ""), rows, howto=meta, look=sb.get("look", ""),
                       top_html=warn_html + _board.character_html(ch, ch_imgs), safe=_board.safe_zone(plat), ratio=sb.get("ratio") or "9:16", duration=sb.get("duration"), camp_abs=os.path.abspath(camp))
dst = os.path.join(camp, "scripts", "storyboard.html")
open(dst, "w", encoding="utf-8").write(html_out)
print(dst); print(os.path.join(camp, "scripts", "storyboard.md"))
for p in problems: print("⚠️ " + p)
if target is not None and not problems: print(f"✓ Thời lượng: các cảnh tới {scene_end:g}s · lời ≈ {words / wps:.1f}s · đúng {target:g}s")
