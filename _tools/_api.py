"""Phần dùng chung cho gen-voice.py / gen-music.py / gen-video.py (gen-image.py có bản riêng, cùng cách làm).

- Key ở ~/.config/ai-studio/.env (ngoài project, dùng chung cả máy) — không bao giờ in giá trị.
- Lỗi key / hết credit / timeout → in câu thần chú 🔮 + popup `pick-provider.sh <task>` đổi nhà cung cấp + dán key → chạy lại.
- Mỗi lượt thành công ghi 1 dòng vào <thư mục out>/_gen-log.jsonl.
Exit chung: 0 ok · 1 lỗi khác · 2 bị bộ lọc an toàn chặn · 3 hết lượt · 4 key/credit/timeout và không đổi được nhà cung cấp.
"""
import base64, datetime, json, mimetypes, os, re, shutil, subprocess, sys, time
import urllib.error, urllib.request

for _s in (sys.stdout, sys.stderr):  # Windows console mặc định cp1252 → in tiếng Việt bị lỗi
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
from spells import spell  # noqa: E402

CFG = os.path.expanduser("~/.config/ai-studio")
ENV_FILE, PREFS = os.path.join(CFG, ".env"), os.path.join(CFG, "prefs.env")
PREF_KEY = {"voice": "VO_PROVIDER", "music": "MUSIC_PROVIDER", "video": "VIDEO_PROVIDER"}
REASON = {"key": "key sai / thiếu", "credit": "hết credit / hạn mức", "timeout": "timeout / mất mạng"}


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


def providers(task):
    """id → mục trong providers.json (nhóm voice / music / video)"""
    return {p["id"]: p for p in json.load(open(os.path.join(TOOLS, "providers.json"), encoding="utf-8"))[task]}


def default_provider(task, fallback):
    return read_kv(PREFS).get(PREF_KEY[task]) or fallback


def keys_for(task, pid):
    env = read_kv(ENV_FILE); out = {}
    for k in providers(task)[pid]["keys"]:
        out[k["env"]] = os.environ.get(k["env"]) or env.get(k["env"], "")
    missing = [k for k, v in out.items() if not v]
    if missing:
        raise Fail("key", f"THIẾU {', '.join(missing)} cho {pid}")
    return out


def http(url, body=None, headers=None, method=None, raw=False, timeout=300, tries=3):
    """Thử lại lỗi tạm thời. body dict → gửi JSON. Trả dict (JSON) hoặc bytes (raw)."""
    headers = dict(headers or {})
    if isinstance(body, (dict, list)):
        body = json.dumps(body).encode(); headers.setdefault("Content-Type", "application/json")
    last = ""
    for attempt in range(tries):
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                return data if raw else json.loads(data or b"{}")
        except urllib.error.HTTPError as e:
            txt = (e.read() or b"").decode("utf-8", "replace")[:600]
            low = txt.lower()
            if e.code == 401 or "invalid api key" in low or "api_key_invalid" in low or "unauthorized" in low:
                raise Fail("key", f"LỖI KEY {e.code}: {txt[:200]}")
            if (e.code == 402 or "insufficient" in low or "billing" in low or "balance" in low or "credit" in low
                    or "quota" in low or "resource_exhausted" in low or "allocation" in low or "exhausted" in low):
                raise Fail("credit", f"HẾT CREDIT / HẠN MỨC {e.code}: {txt[:200]}")
            if e.code == 403:
                raise Fail("key", f"KEY KHÔNG CÓ QUYỀN {e.code}: {txt[:200]}")
            if "moderation" in low or "safety" in low or "nsfw" in low or "content policy" in low:
                raise Fail("safety", f"BỊ BỘ LỌC AN TOÀN CHẶN: {txt[:200]}")
            if e.code != 429 and e.code < 500:
                raise Fail("other", f"LỖI API {e.code}: {txt[:300]}")
            last = f"LỖI API {e.code}: {txt[:200]}"
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = f"LỖI MẠNG / TIMEOUT: {e}"
        time.sleep(8 * (attempt + 1))
    raise Fail("timeout", last + f" (đã thử {tries} lần)")


def data_uri(path):
    return f"data:{mimetypes.guess_type(path)[0] or 'image/png'};base64," + base64.b64encode(open(path, "rb").read()).decode()


def pick_other(task, reason, tried):
    """Popup chọn nhà cung cấp khác + dán key. Trả id nhà, hoặc None nếu huỷ / không mở được popup."""
    try:
        r = subprocess.run(["sh", os.path.join(TOOLS, "pick-provider.sh"), task, reason, ",".join(tried)],
                           capture_output=True, text=True, encoding="utf-8", timeout=900)
    except Exception:
        return None
    name = (r.stdout or "").strip().splitlines()[-1:] or [""]
    return name[0] if r.returncode == 0 and name[0] in providers(task) else None


def run(task, provider, gen, no_fallback=False, skip=()):
    """Gọi gen(provider, keys) — lỗi key/credit/timeout thì đọc thần chú + popup đổi nhà. Trả (provider, kết quả, tried)."""
    tried = []
    while True:
        tried.append(provider)
        try:
            return provider, gen(provider, keys_for(task, provider)), tried
        except Fail as f:
            if f.kind == "safety": die(2, f"{provider}: {f}")
            if f.kind == "other": die(1, f"{provider}: {f}")
            magic = spell(provider.split("_")[0], f.kind)
            print(f"🔮 {magic}", flush=True)                       # Claude chép nguyên câu này cho user
            print(f"{provider}: {f}", file=sys.stderr)
            nxt = None if no_fallback else pick_other(task, f"{magic}\n({provider}: {REASON[f.kind]})", list(tried) + list(skip))
            if not nxt: die(4, f"{provider}: {f} → không đổi được nhà cung cấp, xuất thẻ cho user tự gen")
            print(f"→ chuyển sang {nxt}", file=sys.stderr)
            provider = nxt


# ---------- log + giới hạn lượt ----------
def log_path(out):
    return os.path.join(os.path.dirname(os.path.abspath(out)), "_gen-log.jsonl")


def asset_base(out):
    return re.sub(r"_v\d+(\.\w+)$", "", os.path.basename(out))


def turns_used(out, field):
    log, base = log_path(out), asset_base(out)
    if not os.path.exists(log): return 0
    return sum(1 for l in open(log, encoding="utf-8") if l.strip() and json.loads(l).get(field) == base)


def write_log(out, field, entry):
    entry = {"time": datetime.datetime.now().isoformat(timespec="seconds"), field: asset_base(out),
             "file": os.path.basename(out), **entry}
    with open(log_path(out), "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def guard_out(out):
    if os.path.exists(out): die(1, f"FILE ĐÃ CÓ, không ghi đè: {out} → tăng _vN")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)


# ---------- media ----------
def ffmpeg():
    return shutil.which("ffmpeg")


def duration(path):
    exe = shutil.which("ffprobe")
    if not exe: return None
    r = subprocess.run([exe, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    try: return round(float(r.stdout.strip()), 2)
    except ValueError: return None


def sniff(data):
    """Đoán đuôi file âm thanh / video từ vài byte đầu."""
    if data[:4] == b"RIFF": return ".wav"
    if data[:3] == b"ID3" or data[:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2"): return ".mp3"
    if data[:4] == b"OggS": return ".ogg"
    if data[:4] == b"fLaC": return ".flac"
    if data[4:8] == b"ftyp": return ".mp4"
    return ""


def save_media(data, out):
    """Ghi bytes ra `out`. Định dạng khác đuôi out (VD wav → mp3) → đổi bằng ffmpeg; không có ffmpeg → giữ đuôi gốc."""
    want, got = os.path.splitext(out)[1].lower(), sniff(data)
    if not got or got == want or (want == ".m4a" and got == ".mp4"):
        open(out, "wb").write(data); return out
    tmp = os.path.splitext(out)[0] + ".src" + got
    open(tmp, "wb").write(data)
    if not ffmpeg():
        real = os.path.splitext(out)[0] + got; os.replace(tmp, real)
        print(f"⚠️ không có ffmpeg → giữ định dạng gốc: {real}"); return real
    subprocess.run([ffmpeg(), "-v", "error", "-y", "-i", tmp, out], check=True)
    os.remove(tmp); return out


def download(url, out, headers=None):
    return save_media(http(url, headers=headers, raw=True, timeout=600), out)
