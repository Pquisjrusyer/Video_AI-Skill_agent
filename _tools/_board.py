"""Khung HTML dùng chung cho storyboard.py (cổng 1), clip-board.py (cổng 2), review-board.py (cổng 3): 1 thẻ / cảnh.

row = {
  id, time, purpose, tool, render_s, use_s, status ("" | "chờ render" | "đã có clip"),
  image (data-uri), image_caption, image_name (có → nút 📋 Copy ảnh / ⬇️ Tải ảnh), visual_vi,
  prompts: [(nhãn, prompt_en, prompt_vi), ...],    # mỗi prompt có nút Copy
  line_en, line_vi, onscreen, notes_vi, wps,
  heard_html, frames_html,                          # clip-board / review-board
  out, checks: [(ok, text), ...],
}
Giao diện: thẻ theo cảnh, responsive (3 cột máy tính · 2 cột tablet · 1 cột điện thoại), tự đổi sáng/tối.
"""
import base64, html, io, json, os, re

e = html.escape


def safe_zone(platform):
    """platform = {"ids": ["meta_reels", "tiktok"], ...} → lề an toàn gộp (lấy lớn nhất mỗi phía) + nhãn. Không có → None."""
    ids = (platform or {}).get("ids") or []
    if not ids: return None
    data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "platforms.json"), encoding="utf-8"))["platforms"]
    ps = [p for p in data if p["id"] in ids]
    if not ps: return None
    z = {k: max(p["safe"][k] for p in ps) for k in ("top", "bottom", "left", "right")}
    z["label"] = " + ".join(p["label"] for p in ps)
    z["notes"] = [f'{p["label"]}: {p["note"]}' for p in ps]
    z["platforms"] = ps
    return z


def _secs(d):
    m = re.search(r"\d+(?:\.\d+)?", str(d or ""))
    return float(m.group()) if m else None


def spec_panel(safe, duration=None):
    """Thẻ gợi ý thông số cho từng nền tảng đã chọn — hiện cùng khung vùng an toàn. duration: '20s' hoặc số giây."""
    if not safe: return ""
    d = _secs(duration); cards = []
    for p in safe["platforms"]:
        w, h = map(int, p["size"].split("x")); s = p["safe"]
        px = f'trên {round(h * s["top"] / 100)}px · dưới {round(h * s["bottom"] / 100)}px · trái {round(w * s["left"] / 100)}px · phải {round(w * s["right"] / 100)}px'
        lo, hi = p["len_ok"]; bl, bh = p["len_best"]
        ok_max = f"{hi // 60} phút" if hi >= 600 else f"{hi}s"
        if d is None: dur = ""
        elif d < lo or d > hi: dur = f'<span class="pill bad">Video {d:g}s ngoài giới hạn {lo}–{ok_max}</span>'
        elif bl <= d <= bh: dur = f'<span class="pill ok">Video {d:g}s ✓ đúng mức nên làm</span>'
        else: dur = f'<span class="pill warn">Video {d:g}s · nên {bl}–{bh}s</span>'
        tips = "".join(f"<li>{e(t)}</li>" for t in p.get("tips", []))
        cards.append(
            f'<div class="spec"><div class="spec-h"><b>{e(p["label"])}</b>{_chip(p["ratio"] + " · " + p["size"], "accent")}</div>'
            f'<dl><dt>Độ dài</dt><dd>Cho phép {lo}–{ok_max} · <b>nên {bl}–{bh}s</b> {dur}</dd>'
            f'<dt>Vùng an toàn</dt><dd>{px}</dd><dt>File</dt><dd>{e(p["file"])}</dd>'
            f'<dt>Chữ quảng cáo</dt><dd>{e(p["text"])}</dd><dt>Lưu ý</dt><dd>{e(p["note"])}</dd></dl>'
            + (f'<ul class="tips">{tips}</ul>' if tips else "") + "</div>")
    return f'<section class="specs">{"".join(cards)}</section>'


def _pic(src, alt):
    """Ảnh + lớp phủ vùng an toàn (hiện khi trang có nền tảng)."""
    return f'<div class="pic"><img src="{src}" alt="{e(alt)}" loading="lazy"><div class="safe"><i class="t"></i><i class="b"></i><i class="l"></i><i class="r"></i><b></b></div></div>'


def img_uri(im, size=360, quality=80):
    im = im.copy(); im.thumbnail((size, size)); buf = io.BytesIO()
    im.convert("RGB").save(buf, "JPEG", quality=quality)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


FULL = 2048   # ảnh dùng được (khung đầu, nhân vật): nhúng đủ nét để copy / tải dùng ngay ở nền tảng khác


def full_uri(im):
    return img_uri(im, FULL, 92)


def jpg_name(path):
    return os.path.splitext(os.path.basename(path))[0] + ".jpg"


def img_tools(name):
    """Nút dưới ảnh: copy ảnh vào clipboard (dán thẳng vào web khác) + tải ảnh."""
    return (f'<div class="imgbtn"><button class="btn" onclick="cpImg(this)" title="Copy ảnh để dán vào web khác">📋 Copy</button>'
            f'<button class="btn" onclick="dlImg(this,\'{e(name)}\')" title="Tải ảnh về máy">⬇ Tải</button></div>') if name else ""


WPS = 2.4   # tốc độ đọc ước tính (VO ElevenLabs ~2.4 từ/giây; UGC Flow test: 20 từ / 7.4s ≈ 2.7)


def line_estimate(text, use_s, wps=WPS):
    """'5 từ ≈ 2.1s · cảnh dùng 3.5s ✅' — kiểm độ dài lời ngay từ kịch bản, chưa cần file âm thanh."""
    n = len(re.findall(r"[A-Za-z0-9']+", text or ""))
    if not n: return ""
    est = n / wps
    try: use = float(use_s)
    except (TypeError, ValueError): return f"{n} từ ≈ {est:.1f}s"
    ok = est <= use
    return f"{n} từ ≈ {est:.1f}s · cảnh dùng {use:g}s " + ("✅" if ok else f"⚠️ dài hơn cảnh {est - use:.1f}s — rút lời hoặc kéo dài cảnh")


def _chip(text, cls=""):
    return f'<span class="chip {cls}">{e(text)}</span>' if text else ""


def _row(r, campaign):
    prompts = "".join(
        f'<div class="pcard"><div class="phead"><span>{e(lbl)}</span><button class="btn sm" onclick="cpText(this)">Copy</button></div>'
        f'<pre>{e(en)}</pre><p class="vi"><span class="tag">VI</span>{e(vi)}</p></div>'
        for lbl, en, vi in r.get("prompts", []) if en)
    est = line_estimate(r.get("line_en"), r.get("use_s"), r.get("wps") or WPS)
    line = (f'<div class="quote"><div class="qlabel">Lời thoại / VO</div><p class="en">“{e(r["line_en"])}”</p>'
            f'<p class="vi"><span class="tag">VI</span>{e(r.get("line_vi", ""))}</p>'
            + (f'<span class="pill {"warn" if "⚠" in est else "ok"}">{e(est)}</span>' if est else "") + "</div>"
            if r.get("line_en") else '<p class="muted small">Không có lời thoại</p>')
    status = r.get("status", "")
    checks = "".join(f'<li class="{"ok" if ok else "bad"}"><span>{"✓" if ok else "!"}</span>{e(t)}</li>' for ok, t in r.get("checks", []))
    nbad = sum(1 for ok, _ in r.get("checks", []) if not ok)
    pic = _pic(r["image"], r["id"]) if r.get("image") else '<div class="noimg">chưa có ảnh</div>'
    out = r.get("out", "")
    folder, name = (out.rsplit("/", 1) if "/" in out else ("", out))
    rs = f'Render {r["render_s"]}s · dùng {r.get("use_s", "")}s' if r.get("render_s") else ""
    st_cls = "have" if status == "đã có clip" else ("bad" if nbad else "")
    return f"""<article class="scene" id="{e(r['id'])}">
<header class="shead">
  <span class="sid">{e(r['id'])}</span><span class="stime">{e(r.get('time', ''))}</span>{_chip(r.get('purpose'), 'accent')}
  <span class="grow"></span>{_chip(r.get('tool'))}{_chip(rs)}{_chip(status, st_cls)}{_chip(f'{nbad} cảnh báo', 'bad') if nbad else ''}
</header>
<div class="sbody">
  <div class="media"><figure>{pic}{img_tools(r.get('image_name')) if r.get('image') else ''}</figure>
    {f'<div class="cap">{e(r["image_caption"])}</div>' if r.get('image_caption') else ''}
    {f'<p class="visual">{e(r["visual_vi"])}</p>' if r.get('visual_vi') else ''}</div>
  <div class="content">{prompts}{line}
    {f'<div class="onscreen"><span class="qlabel">Chữ trên màn hình</span>{e(r["onscreen"])}</div>' if r.get('onscreen') else ''}
    {f'<div class="heard"><div class="qlabel">Nghe được trong clip <span class="legend"><del>thiếu</del> <ins>thừa / khác</ins></span></div>{r["heard_html"]}</div>' if r.get('heard_html') else ''}
    {f'<div class="frames">{r["frames_html"]}</div>' if r.get('frames_html') else ''}
    {f'<p class="note"><b>Ghi chú:</b> {e(r["notes_vi"])}</p>' if r.get('notes_vi') else ''}</div>
  <aside class="side">
    <div class="qlabel">Lưu về</div>
    {f'<div class="path"><code>{e(name)}</code><button class="btn sm" onclick="cpPath(this)" data-p="{e(out)}">Copy</button></div><div class="muted small">{e(folder)}/</div>' if out else '<div class="muted small">—</div>'}
    {f'<div class="qlabel">Kiểm tra</div><ul class="checks">{checks}</ul>' if checks else ''}
    <label class="done"><input type="checkbox" data-k="{e(campaign)}:{e(r['id'])}"><span>Xong / đã duyệt</span></label>
  </aside>
</div>
</article>"""


def character_html(ch, img_uris):
    """Thẻ nhân vật đầu trang: ảnh (face-ref / nửa người / trong bối cảnh) + IDENTITY LOCK EN + mô tả VI + giọng."""
    if not ch: return ""
    pics = "".join(f'<figure><img src="{x[0]}" loading="lazy"><figcaption>{e(x[1])}</figcaption>{img_tools(x[2] if len(x) > 2 else "")}</figure>'
                   for x in img_uris)
    return (f'<section class="char"><header class="shead"><span class="sid">👤</span><b>Nhân vật: {e(ch.get("name", ""))}</b>'
            f'{_chip(ch.get("source"), "accent")}</header><div class="cbody"><div class="cpics">{pics}</div><div class="content">'
            f'<div class="pcard"><div class="phead"><span>IDENTITY LOCK — chép nguyên văn vào mọi prompt có nhân vật</span>'
            f'<button class="btn sm" onclick="cpText(this)">Copy</button></div><pre>{e(ch.get("identity_lock_en", ""))}</pre>'
            f'<p class="vi"><span class="tag">VI</span>{e(ch.get("identity_vi", ""))}</p></div>'
            + (f'<div class="onscreen"><span class="qlabel">Giọng</span>{e(ch["voice_en"])}</div>' if ch.get("voice_en") else "")
            + "</div></div></section>")


CSS = """
:root{--bg:#f4f2ee;--card:#fff;--ink:#1c1b19;--muted:#75726c;--line:#e7e3dc;--soft:#f7f5f1;--code:#f3f0ea;
--accent:#9e1b2c;--accent-soft:#f6e6e8;--ok:#1f7a45;--ok-soft:#e3f3e9;--bad:#b42318;--bad-soft:#fdecea;--warn:#a15c07;--warn-soft:#fdf1dc;
--r:14px;--shadow:0 1px 2px rgba(0,0,0,.04),0 4px 16px rgba(0,0,0,.05)}
@media (prefers-color-scheme:dark){:root{--bg:#121211;--card:#1c1b1a;--ink:#ecebe7;--muted:#a3a09a;--line:#2e2c29;--soft:#232220;--code:#262523;
--accent:#ff7a8a;--accent-soft:#3a1d22;--ok:#5fd08e;--ok-soft:#173022;--bad:#ff8a80;--bad-soft:#3a1c1a;--warn:#f5b04d;--warn-soft:#3a2a12;--shadow:none}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:14.5px/1.6 "Be Vietnam Pro",system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .in{max-width:1240px;margin:0 auto;padding:14px 20px 10px}
h1{font-size:20px;margin:0;letter-spacing:-.01em}h1 small{font-weight:500;color:var(--muted);font-size:14px;margin-left:6px}
.meta{color:var(--muted);font-size:13px;margin:2px 0 8px}
.bar{display:flex;align-items:center;gap:10px;font-size:12.5px;color:var(--muted)}
.track{flex:1;max-width:260px;height:6px;border-radius:9px;background:var(--line);overflow:hidden}.track i{display:block;height:100%;width:0;background:var(--ok);transition:width .3s}
.nav{display:flex;gap:6px;overflow-x:auto;padding:8px 0 2px;scrollbar-width:none}.nav::-webkit-scrollbar{display:none}
.nav a{flex:none;text-decoration:none;color:var(--ink);font-size:12.5px;font-weight:600;padding:4px 10px;border:1px solid var(--line);border-radius:99px;background:var(--card)}
.nav a.done{background:var(--ok-soft);border-color:transparent;color:var(--ok)}.nav a.warn{background:var(--bad-soft);border-color:transparent;color:var(--bad)}
main{max-width:1240px;margin:0 auto;padding:18px 20px 60px;display:flex;flex-direction:column;gap:16px}
.look{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:12px 16px;box-shadow:var(--shadow)}
.scene,.char{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);overflow:hidden;scroll-margin-top:130px}
.scene.is-done{border-color:color-mix(in srgb,var(--ok) 45%,var(--line))}
.shead{display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid var(--line);background:var(--soft)}
.sid{font-weight:700;font-size:13px;background:var(--ink);color:var(--card);border-radius:8px;padding:2px 9px}
.stime{font-weight:600;font-variant-numeric:tabular-nums}.grow{flex:1}
.chip{font-size:12px;padding:2px 9px;border-radius:99px;background:var(--card);border:1px solid var(--line);color:var(--muted);white-space:nowrap}
.chip.accent{background:var(--accent-soft);color:var(--accent);border-color:transparent;font-weight:600}
.chip.have{background:var(--ok-soft);color:var(--ok);border-color:transparent}.chip.bad{background:var(--bad-soft);color:var(--bad);border-color:transparent}
.sbody{display:grid;grid-template-columns:220px minmax(0,1fr) 250px;gap:18px;padding:16px}
.cbody{display:grid;grid-template-columns:auto minmax(0,1fr);gap:18px;padding:16px}.cpics{display:flex;gap:10px;flex-wrap:wrap}.cpics figure{width:150px}
figure{margin:0}figure img{width:100%;display:block;border-radius:10px;background:var(--soft);border:1px solid var(--line)}
.media figure img{aspect-ratio:var(--ar,9/16);object-fit:cover}
.pic{position:relative}.safe{display:none;position:absolute;inset:0;pointer-events:none;border-radius:10px;overflow:hidden}
body.show-safe .safe{display:block}.safe i{position:absolute;background:rgba(220,38,38,.30)}
.safe .t{left:0;right:0;top:0;height:var(--st)}.safe .b{left:0;right:0;bottom:0;height:var(--sb)}
.safe .l{left:0;top:var(--st);bottom:var(--sb);width:var(--sl)}.safe .r{right:0;top:var(--st);bottom:var(--sb);width:var(--sr)}
.safe b{position:absolute;top:var(--st);bottom:var(--sb);left:var(--sl);right:var(--sr);border:1.5px dashed rgba(255,255,255,.95);box-shadow:0 0 0 1px rgba(0,0,0,.25)}
.safebtn.on{background:var(--bad-soft);color:var(--bad);border-color:transparent}.safeinfo{font-size:12px;color:var(--muted);margin-top:4px;display:none}
body.show-safe .safeinfo{display:block}.specs{display:none;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}body.show-safe .specs{display:grid}
.spec{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);padding:12px 14px;font-size:13px}
.spec-h{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:8px}.spec dl{margin:0;display:grid;grid-template-columns:88px 1fr;gap:4px 10px}
.spec dt{color:var(--muted);font-size:12px;font-weight:600}.spec dd{margin:0}.spec .pill{margin-left:4px}.pill.bad{background:var(--bad-soft);color:var(--bad)}
.tips{margin:8px 0 0;padding-left:18px;color:var(--muted);font-size:12.5px}figcaption,.cap{font-size:11.5px;color:var(--muted);margin-top:4px;word-break:break-all}
.noimg{aspect-ratio:9/16;border-radius:10px;display:grid;place-items:center;color:var(--muted);background:repeating-linear-gradient(45deg,var(--soft),var(--soft) 8px,var(--line) 8px,var(--line) 9px)}
.visual{font-size:13px;margin:8px 0 0}
.imgbtn{display:flex;gap:6px;margin-top:6px}.imgbtn .btn{flex:1;white-space:nowrap;padding:5px 4px;font-size:12px}
.btn{font:inherit;font-size:12.5px;font-weight:600;padding:6px 10px;border-radius:9px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer;transition:background .15s,border-color .15s}
.btn:hover{border-color:var(--accent);color:var(--accent)}.btn.sm{padding:3px 10px;font-size:12px}
.content{display:flex;flex-direction:column;gap:10px;min-width:0}
.pcard{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.phead{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:7px 10px;font-size:12px;font-weight:600;color:var(--muted);background:var(--soft);border-bottom:1px solid var(--line)}
pre{margin:0;padding:10px 12px;white-space:pre-wrap;word-break:break-word;font:12.5px/1.55 ui-monospace,"Cascadia Code",Menlo,Consolas,monospace;background:var(--code);max-height:260px;overflow:auto}
.vi{margin:0;padding:8px 12px;font-size:13.5px}.tag{display:inline-block;font-size:10px;font-weight:700;letter-spacing:.04em;color:var(--accent);background:var(--accent-soft);border-radius:5px;padding:0 5px;margin-right:6px;vertical-align:1px}
.quote{border-left:3px solid var(--accent);background:var(--soft);border-radius:0 12px 12px 0;padding:10px 12px}.quote .en{margin:2px 0 0;font-weight:600;font-size:15px}.quote .vi{padding:4px 0 6px}
.qlabel{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:2px}
.pill{display:inline-block;font-size:12px;font-weight:600;border-radius:99px;padding:2px 10px}.pill.ok{background:var(--ok-soft);color:var(--ok)}.pill.warn{background:var(--warn-soft);color:var(--warn)}
.onscreen{font-size:13.5px}.onscreen .qlabel{display:block}
.heard{border:1px dashed var(--line);border-radius:12px;padding:10px 12px;font-size:13.5px}.legend{float:right;text-transform:none;letter-spacing:0;font-weight:500}
del{color:var(--bad);text-decoration-thickness:2px}ins{background:var(--warn-soft);color:var(--warn);text-decoration:none;border-radius:4px;padding:0 3px}
.frames{display:flex;gap:10px;flex-wrap:wrap}.frames figure{width:110px}.frames figure img{aspect-ratio:9/16;object-fit:cover}
.note{margin:0;font-size:13px;color:var(--muted)}
.side{display:flex;flex-direction:column;gap:6px;border-left:1px solid var(--line);padding-left:16px}
.path{display:flex;align-items:center;gap:6px}.path code{flex:1;font-size:12px;background:var(--code);padding:4px 8px;border-radius:7px;word-break:break-all}
.checks{list-style:none;margin:0 0 6px;padding:0;display:flex;flex-direction:column;gap:4px;font-size:12.5px}
.checks li{display:flex;gap:6px;align-items:flex-start;padding:4px 8px;border-radius:8px}.checks li span{font-weight:800;width:14px;flex:none;text-align:center}
.checks li.ok{background:var(--ok-soft);color:var(--ok)}.checks li.bad{background:var(--bad-soft);color:var(--bad)}
.done{margin-top:auto;display:flex;align-items:center;gap:8px;padding:8px 10px;border:1px solid var(--line);border-radius:10px;cursor:pointer;font-weight:600;font-size:13px;user-select:none}
.done input{width:18px;height:18px;accent-color:var(--ok)}.done:has(input:checked){background:var(--ok-soft);color:var(--ok);border-color:transparent}
.muted{color:var(--muted)}.small{font-size:12px}.extra{color:var(--muted);font-size:13px}
.toast{position:fixed;left:50%;bottom:22px;transform:translateX(-50%) translateY(20px);opacity:0;background:var(--ink);color:var(--card);padding:8px 16px;border-radius:99px;font-size:13px;font-weight:600;transition:.2s;pointer-events:none;z-index:9}
.toast.on{opacity:1;transform:translateX(-50%)}
@media (max-width:1020px){.sbody{grid-template-columns:200px minmax(0,1fr)}.side{grid-column:1/-1;border-left:0;padding-left:0;border-top:1px solid var(--line);padding-top:12px}}
@media (max-width:640px){.top .in,main{padding-left:14px;padding-right:14px}h1{font-size:17px}.sbody,.cbody{grid-template-columns:1fr;padding:12px}
.media{max-width:280px;width:100%;margin:0 auto}.cpics figure{width:calc(50% - 5px)}.shead{padding:10px 12px}.scene,.char{scroll-margin-top:150px}}
"""

JS = """
const toast=(t)=>{const x=document.getElementById('toast');x.textContent=t;x.classList.add('on');clearTimeout(x._t);x._t=setTimeout(()=>x.classList.remove('on'),1600)};
function copyText(t,b){(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>toast('Đã copy ✓')).catch(()=>{const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');toast('Đã copy ✓')}catch(e){toast('Không copy được')}a.remove()})}
function cpText(b){copyText(b.closest('.pcard').querySelector('pre').innerText,b)}
function cpPath(b){copyText(b.dataset.p,b)}
function imgOf(b){return b.closest('figure').querySelector('img')}
function cpImg(b){const im=imgOf(b),c=document.createElement('canvas');c.width=im.naturalWidth;c.height=im.naturalHeight;c.getContext('2d').drawImage(im,0,0);
const blocked=()=>{toast('Trình duyệt chặn copy ảnh');alert('Trình duyệt chặn copy ảnh.\\nCách khác: chuột phải vào ảnh → Sao chép hình ảnh (Copy image), hoặc bấm ⬇️ Tải ảnh.')};
if(!navigator.clipboard||!window.ClipboardItem){blocked();return}
/* truyền Promise vào ClipboardItem ngay trong cú bấm — giữ quyền copy (Chrome, Edge, Safari) */
navigator.clipboard.write([new ClipboardItem({'image/png':new Promise(res=>c.toBlob(res,'image/png'))})]).then(()=>toast('Đã copy ảnh ✓')).catch(blocked)}
function dlImg(b,n){const a=document.createElement('a');a.href=imgOf(b).src;a.download=n;document.body.appendChild(a);a.click();a.remove();toast('Đã tải '+n)}
function progress(){const all=[...document.querySelectorAll('input[data-k]')],n=all.filter(x=>x.checked).length;
document.getElementById('pct').style.width=(all.length?100*n/all.length:0)+'%';document.getElementById('cnt').textContent=n+'/'+all.length;
all.forEach(x=>{const s=x.closest('.scene');s&&s.classList.toggle('is-done',x.checked);const a=document.querySelector('.nav a[href="#'+(s&&s.id)+'"]');a&&a.classList.toggle('done',x.checked)})}
document.querySelectorAll('input[data-k]').forEach(x=>{try{x.checked=localStorage.getItem(x.dataset.k)==='1'}catch(e){}
x.addEventListener('change',()=>{try{localStorage.setItem(x.dataset.k,x.checked?'1':'0')}catch(e){}progress()})});
progress();
"""


def page(title, campaign, rows, howto="", look="", extra_html="", top_html="", safe=None, ratio="9:16", duration=None):
    nav = "".join(f'<a href="#{e(r["id"])}" class="{"warn" if any(not ok for ok, _ in r.get("checks", [])) else ""}">{e(r["id"])}</a>' for r in rows)
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} · {e(campaign)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body class="{'show-safe' if safe else ''}" style="--ar:{ratio.replace(':', '/')};{f"--st:{safe['top']}%;--sb:{safe['bottom']}%;--sl:{safe['left']}%;--sr:{safe['right']}%" if safe else ''}">
<div class="top"><div class="in">
  <h1>{e(title)}<small>{e(campaign)}</small></h1>
  {f'<div class="meta">{e(howto)}</div>' if howto else ''}
  <div class="bar">Đã duyệt <b id="cnt">0/0</b><div class="track"><i id="pct"></i></div>
  {f'<button class="btn sm safebtn on" onclick="document.body.classList.toggle(\'show-safe\');this.classList.toggle(\'on\')" title="{e(chr(10).join(safe["notes"]))}">▣ Khung + thông số: {e(safe["label"])}</button>' if safe else ''}</div>
  {f'<div class="safeinfo">Dải đỏ = bị giao diện app che (chữ, logo, CTA, mặt nhân vật phải nằm trong khung nét đứt) · trên {safe["top"]}% · dưới {safe["bottom"]}% · trái {safe["left"]}% · phải {safe["right"]}%</div>' if safe else ''}
  <nav class="nav">{nav}</nav>
</div></div>
<main>
{spec_panel(safe, duration)}{f'<div class="look"><span class="qlabel">Look chung</span><br>{e(look)}</div>' if look else ''}{top_html}
{''.join(_row(r, campaign) for r in rows)}
{f'<div class="extra">{extra_html}</div>' if extra_html else ''}
</main>
<div class="toast" id="toast"></div>
<script>{JS}</script></body></html>"""
