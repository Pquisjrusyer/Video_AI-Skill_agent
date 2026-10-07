#!/usr/bin/env python3
"""Dựng video Remotion bằng BỘ DÙNG CHUNG CẢ MÁY — cài 1 lần, mọi campaign dùng lại (không npm install mỗi lần).

  python3 _tools/remotion.py ensure                       # cài / cập nhật bộ dùng chung (tự chạy khi cần)
  python3 _tools/remotion.py check   campaigns/<c>        # kiểm timeline.json + đủ file, không render
  python3 _tools/remotion.py stills  campaigns/<c>        # 1 khung giữa mỗi cảnh + ảnh ghép xem nhanh (1 lần đóng gói)
  python3 _tools/remotion.py review  campaigns/<c>        # video review → outputs/review/<code>_review_vN.mp4
  python3 _tools/remotion.py final   campaigns/<c> --name <tên chuẩn>.mp4 [--extra 4:5]   # + chuẩn hoá -14 LUFS
  python3 _tools/remotion.py status | clean

Dữ liệu dựng: campaigns/<c>/remotion-project/timeline.json (schema: _skills/motion-graphic/references/remotion-setup.md).
Media đọc thẳng từ campaigns/<c>/outputs/ (src trong timeline: "videos/x.mp4", "audio/vo-S01.mp3", "images/logo.png").
Cần code riêng cho 1 campaign → đặt file .tsx vào remotion-project/src/ (ghi đè khung chung), không sửa bộ dùng chung.
Bộ dùng chung: ~/.config/ai-studio/remotion-base (ngoài dự án / Drive / git). Phiên bản khoá ở _tools/remotion-base/package.json.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
REPO_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "remotion-base")
BASE = os.path.expanduser("~/.config/ai-studio/remotion-base")
MARK = os.path.join(BASE, ".installed")
SIZES = {"9:16": (1080, 1920), "4:5": (1080, 1350), "1:1": (1080, 1080), "16:9": (1920, 1080)}
NPM_NET = ["--no-audit", "--no-fund", "--fetch-timeout=600000", "--fetch-retries=5",
           "--fetch-retry-mintimeout=20000", "--fetch-retry-maxtimeout=120000"]


def run(cmd, cwd=None):
    exe = shutil.which(cmd[0]) or cmd[0]                     # Windows: npm → npm.cmd
    r = subprocess.run([exe] + cmd[1:], cwd=cwd)
    if r.returncode: sys.exit(f"LỖI khi chạy: {' '.join(cmd)} (mã {r.returncode})")


def digest():
    h = hashlib.sha256()
    for f in ("package.json", "package-lock.json"):
        p = os.path.join(REPO_BASE, f)
        if os.path.exists(p): h.update(open(p, "rb").read())
    return h.hexdigest()[:16]


def ensure(quiet=False):
    if not shutil.which("node"): sys.exit("THIẾU Node.js → nói 'set up dự án' (skill setup bước 3).")
    os.makedirs(BASE, exist_ok=True)
    for f in ("render.mjs",):                                  # script + khung luôn lấy bản mới nhất từ repo (nhẹ)
        shutil.copy2(os.path.join(REPO_BASE, f), BASE)
    ok = os.path.exists(MARK) and open(MARK).read().strip() == digest() and os.path.isdir(os.path.join(BASE, "node_modules", "remotion"))
    if ok:
        if not quiet: print(f"✓ Bộ Remotion dùng chung đã cài ({BASE}) — dùng lại, không cài nữa.")
        return
    print(f"Cài bộ Remotion dùng chung lần đầu / cập nhật phiên bản → {BASE} (vài phút, chỉ 1 lần trên máy này)…", flush=True)
    shutil.copy2(os.path.join(REPO_BASE, "package.json"), BASE)
    lock = os.path.join(REPO_BASE, "package-lock.json")
    if os.path.exists(lock):
        shutil.copy2(lock, BASE); run(["npm", "ci"] + NPM_NET, cwd=BASE)
    else:
        run(["npm", "install"] + NPM_NET, cwd=BASE)
        shutil.copy2(os.path.join(BASE, "package-lock.json"), lock)   # khoá cây gói cho máy sau (npm ci)
        print("→ đã tạo _tools/remotion-base/package-lock.json (nhớ commit để máy khác cài giống hệt).")
    print("Tải trình duyệt render của Remotion (1 lần)…", flush=True)
    run(["node", "-e", "import('@remotion/renderer').then(m=>m.ensureBrowser()).then(()=>console.log('✓ trình duyệt render sẵn sàng'))"], cwd=BASE)
    open(MARK, "w").write(digest())
    print("✓ Xong. Lần dựng sau ở mọi dự án trên máy này dùng lại, không cài nữa.")


def load(camp):
    tl_path = os.path.join(camp, "remotion-project", "timeline.json")
    if not os.path.exists(tl_path): sys.exit(f"THIẾU {tl_path} — Claude viết timeline.json trước (schema trong remotion-setup.md).")
    tl = json.load(open(tl_path, encoding="utf-8"))
    pub = os.path.abspath(os.path.join(camp, "outputs"))
    srcs = [s.get("src") for s in tl.get("scenes", [])] + [s.get("logo") for s in tl.get("scenes", [])]
    a = tl.get("audio") or {}
    srcs += [v.get("src") for v in a.get("vo", [])] + [x.get("src") for x in a.get("sfx", [])] + [(a.get("music") or {}).get("src")]
    missing = [s for s in srcs if s and not os.path.exists(os.path.join(pub, s))]
    total = sum(s.get("duration", 0) for s in tl.get("scenes", []))
    print(f"timeline: {len(tl.get('scenes', []))} cảnh · tổng {total:g}s · {tl.get('width', 1080)}×{tl.get('height', 1920)}")
    if missing: sys.exit("THIẾU FILE trong outputs/:\n  " + "\n  ".join(missing))
    return tl_path, tl, pub


def workdir(camp):
    slug = re.sub(r"[^A-Za-z0-9_-]+", "-", os.path.basename(os.path.abspath(camp)))
    w = os.path.join(BASE, "work", slug)
    if os.path.exists(os.path.join(w, "src")): shutil.rmtree(os.path.join(w, "src"))
    shutil.copytree(os.path.join(REPO_BASE, "src"), os.path.join(w, "src"))
    own = os.path.join(camp, "remotion-project", "src")
    if os.path.isdir(own): shutil.copytree(own, os.path.join(w, "src"), dirs_exist_ok=True)   # code riêng campaign ghi đè
    return os.path.join(w, "src", "index.ts")


def render(camp, mode, out, size=None):
    ensure(quiet=True)
    tl_path, tl, pub = load(camp)
    cmd = ["node", "render.mjs", "--entry", workdir(camp), "--public", pub, "--props", os.path.abspath(tl_path), "--mode", mode, "--out", out]
    if size: cmd += ["--size", size]
    run(cmd, cwd=BASE)
    return tl


def code_of(camp, tl):
    return tl.get("campaign") or os.path.basename(os.path.abspath(camp))


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    cmd = a[0]
    if cmd == "ensure": return ensure()
    if cmd == "status":
        print(f"Bộ dùng chung: {BASE}"); print("Đã cài, đúng phiên bản." if os.path.exists(MARK) and open(MARK).read().strip() == digest() else "Chưa cài / khác phiên bản → tự cài ở lần dựng đầu (hoặc chạy ensure)."); return
    if cmd == "clean":
        shutil.rmtree(os.path.join(BASE, "work"), ignore_errors=True); print("Đã dọn thư mục làm việc."); return
    if len(a) < 2: sys.exit(__doc__)
    camp = a[1]
    if cmd == "check": load(camp); print("✓ Đủ file, sẵn sàng render."); return
    rev = os.path.join(camp, "outputs", "review"); os.makedirs(rev, exist_ok=True)
    if cmd == "stills":
        d = os.path.join(rev, "_stills"); shutil.rmtree(d, ignore_errors=True)
        tl = render(camp, "stills", os.path.abspath(d))
        from PIL import Image                                   # ghép khung xem nhanh
        ims = [Image.open(os.path.join(d, f"{s['id']}.png")) for s in tl["scenes"]]
        th = [im.copy() for im in ims]; [t.thumbnail((360, 640)) for t in th]
        sheet = Image.new("RGB", (sum(t.width for t in th) + 12 * (len(th) + 1), max(t.height for t in th) + 24), "white")
        x = 12
        for t in th: sheet.paste(t, (x, 12)); x += t.width + 12
        p = os.path.join(rev, f"{code_of(camp, tl)}_stills.jpg"); sheet.save(p, quality=88); print(f"✓ Ảnh ghép xem nhanh: {p}")
    elif cmd == "review":
        tl0 = json.load(open(os.path.join(camp, "remotion-project", "timeline.json"), encoding="utf-8"))
        code = code_of(camp, tl0)
        n = 1 + max([int(m.group(1)) for f in glob.glob(os.path.join(rev, f"{code}_review_v*.mp4")) if (m := re.search(r"_v(\d+)\.mp4$", f))] or [0])
        out = os.path.abspath(os.path.join(rev, f"{code}_review_v{n}.mp4")); render(camp, "video", out); print(f"✓ Bản review: {out}")
    elif cmd == "final":
        name = a[a.index("--name") + 1] if "--name" in a else None
        if not name: sys.exit("Cần --name <tên chuẩn theo CLAUDE.md>.mp4")
        fin = os.path.join(camp, "outputs", "final"); os.makedirs(fin, exist_ok=True)
        jobs = [(name, None)]
        if "--extra" in a:
            r = a[a.index("--extra") + 1]; w, h = SIZES[r]
            jobs.append((re.sub(r"_\d+x\d+_", f"_{r.replace(':', 'x')}_", name) if re.search(r"_\d+x\d+_", name) else name.replace(".mp4", f"_{r.replace(':', 'x')}.mp4"), f"{w}x{h}"))
        for nm, size in jobs:
            raw = os.path.abspath(os.path.join(rev, "_raw_" + nm)); render(camp, "video", raw, size)
            dst = os.path.abspath(os.path.join(fin, nm))
            if shutil.which("ffmpeg"):
                run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1:LRA=11", "-c:a", "aac", "-b:a", "192k", dst])
                os.remove(raw); print(f"✓ Final (-14 LUFS): {dst}")
            else:
                shutil.move(raw, dst); print(f"✓ Final (chưa chuẩn hoá âm lượng — máy thiếu ffmpeg): {dst}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
