#!/usr/bin/env python3
"""Kiểm key ĐÃ CÓ trên máy (dùng chung mọi dự án) + còn dùng được không — chạy TRƯỚC khi hỏi user nhập key.

  python3 _tools/key-status.py            # kiểm các key mà lựa chọn công cụ (prefs.env) cần
  python3 _tools/key-status.py --all      # kiểm mọi key đang lưu
  python3 _tools/key-status.py --offline  # chỉ xem có / thiếu, không gọi API

Key lưu ở ~/.config/ai-studio/.env (Windows: C:\\Users\\<tên>\\.config\\ai-studio\\.env) — ngoài mọi dự án, nên dự án
nào trên cùng máy cũng dùng lại được. Không bao giờ in giá trị key.
Kiểm "khả dụng" = gọi 1 API đọc thông tin miễn phí (không tốn credit). Hết credit thì chỉ biết lúc gen thật
(gen-image.py tự đọc thần chú + mở popup đổi nhà cung cấp).
Exit: 0 đủ + dùng được · 1 thiếu hoặc lỗi (in danh sách để popup đúng key đó).
"""
import json, os, sys, urllib.error, urllib.request

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
CFG = os.path.expanduser("~/.config/ai-studio")
ENV, PREFS = os.path.join(CFG, ".env"), os.path.join(CFG, "prefs.env")


def kv(path):
    d = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1); d[k.strip()] = v.strip().strip('"')
    return d


def get(url, headers):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return None, str(e).encode()


# key → hàm kiểm (trả (ok, ghi chú)). None = không có API kiểm miễn phí.
def chk_openai(env):
    c, _ = get("https://api.openai.com/v1/models", {"Authorization": f"Bearer {env['OPENAI_API_KEY']}"})
    return (c == 200, "OK (credit chỉ biết khi gen)" if c == 200 else f"LỖI {c} — key sai / đã thu hồi" if c in (401, 403) else f"không kiểm được ({c})")
def chk_gemini(env):
    c, _ = get("https://generativelanguage.googleapis.com/v1beta/models", {"x-goog-api-key": env["GEMINI_API_KEY"]})
    return (c == 200, "OK" if c == 200 else f"LỖI {c}")
def chk_cloudflare(env):
    if not env.get("CLOUDFLARE_ACCOUNT_ID"): return (False, "thiếu Account ID")
    c, b = get("https://api.cloudflare.com/client/v4/user/tokens/verify", {"Authorization": f"Bearer {env['CLOUDFLARE_API_TOKEN']}"})
    ok = c == 200 and b'"active"' in b
    return (ok, "OK (token active)" if ok else f"LỖI {c} — token sai / hết hạn")
def chk_hf(env):
    c, _ = get("https://huggingface.co/api/whoami-v2", {"Authorization": f"Bearer {env['HF_TOKEN']}"})
    return (c == 200, "OK" if c == 200 else f"LỖI {c}")
def chk_elevenlabs(env):
    c, b = get("https://api.elevenlabs.io/v1/user", {"xi-api-key": env["ELEVENLABS_API_KEY"]})
    if c == 401 and b"permission" in b.lower(): return (True, "OK (key giới hạn quyền, không đọc được thông tin tài khoản)")
    return (c == 200, "OK" if c == 200 else f"LỖI {c} — key sai / đã thu hồi" if c in (401, 403) else f"không kiểm được ({c})")
def chk_fal(env):
    c, _ = get("https://api.fal.ai/v1/models?limit=1", {"Authorization": f"Key {env['FAL_KEY']}"})
    return (c == 200, "OK (credit chỉ biết khi gen)" if c == 200 else f"LỖI {c} — key sai" if c in (401, 403) else f"không kiểm được ({c})")
def chk_replicate(env):
    c, _ = get("https://api.replicate.com/v1/account", {"Authorization": f"Bearer {env['REPLICATE_API_TOKEN']}"})
    return (c == 200, "OK" if c == 200 else f"LỖI {c}")

CHECKS = {"OPENAI_API_KEY": chk_openai, "GEMINI_API_KEY": chk_gemini, "CLOUDFLARE_API_TOKEN": chk_cloudflare,
          "HF_TOKEN": chk_hf, "REPLICATE_API_TOKEN": chk_replicate, "ELEVENLABS_API_KEY": chk_elevenlabs, "FAL_KEY": chk_fal}


def task_keys(task, pid):
    """Key nhà cung cấp `pid` của nhóm voice / music / video cần — đọc từ providers.json."""
    items = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "providers.json"), encoding="utf-8"))[task]
    return next(([k["env"] for k in p["keys"]] for p in items if p["id"] == pid), [])
IMAGE_KEYS = {"openai": ["OPENAI_API_KEY"], "gemini": ["GEMINI_API_KEY"], "fal": ["FAL_KEY"], "replicate": ["REPLICATE_API_TOKEN"],
              "cloudflare": ["CLOUDFLARE_API_TOKEN", "CLOUDFLARE_ACCOUNT_ID"], "pollinations": ["POLLINATIONS_KEY"], "huggingface": ["HF_TOKEN"]}


def needed(prefs):
    need = []
    if prefs.get("IMAGE_TOOL", "claude") == "claude":
        need += IMAGE_KEYS.get(prefs.get("IMAGE_PROVIDER", "openai"), [])
    if prefs.get("VO_TOOL") == "openai": need.append("OPENAI_API_KEY")
    # Gen qua API (giọng / nhạc / video): key của nhà cung cấp đang chọn
    for tool, task, pref, dflt in (("VO_TOOL", "voice", "VO_PROVIDER", "elevenlabs"), ("MUSIC_TOOL", "music", "MUSIC_PROVIDER", "elevenlabs_music"),
                                   ("VIDEO_TOOL", "video", "VIDEO_PROVIDER", "fal_video")):
        if prefs.get(tool) == "api": need += task_keys(task, prefs.get(pref, dflt))
    for svc, keys in (("topview", ["TOPVIEW_API_KEY", "TOPVIEW_UID"]), ("higgsfield", ["HIGGSFIELD_API_KEY", "HIGGSFIELD_API_SECRET"])):
        if svc in (prefs.get("UGC_TOOL"), prefs.get("VIDEO_TOOL")) and prefs.get(f"{svc.upper()}_CONN") == "api": need += keys
    return list(dict.fromkeys(need))


def main():
    env, prefs = kv(ENV), kv(PREFS)
    keys = [k for k, v in env.items() if v and k.isupper()] if "--all" in sys.argv else needed(prefs)
    if not keys:
        print("Lựa chọn công cụ hiện tại không cần key nào." if prefs else "Chưa chọn công cụ (prefs.env trống) → skill setup bước 1."); return 0
    print(f"Key lưu chung cả máy: {ENV}")
    bad = []
    for k in keys:
        if not env.get(k):
            print(f"  ✗ {k}: THIẾU"); bad.append(k); continue
        if k == "CLOUDFLARE_ACCOUNT_ID" and "--offline" not in sys.argv:
            print(f"  ✓ {k}: đã có (kiểm cùng CLOUDFLARE_API_TOKEN)"); continue
        if "--offline" in sys.argv or k not in CHECKS:
            print(f"  ✓ {k}: đã có" + ("" if "--offline" in sys.argv else " (nhà này không có API kiểm miễn phí — kiểm ở lần gen đầu)")); continue
        ok, note = CHECKS[k](env)
        print(f"  {'✓' if ok else '✗'} {k}: đã có · {note}")
        if not ok and not note.startswith("không kiểm được"): bad.append(k)
    if bad: print("CẦN NHẬP / ĐỔI: " + " ".join(bad))
    else: print("✅ Đủ key, dùng được — KHÔNG cần hỏi user nhập lại.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
