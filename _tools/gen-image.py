#!/usr/bin/env python3
"""Gen ảnh GPT Image qua OpenAI API. Key: OPENAI_API_KEY trong ~/.config/ai-studio/.env (không bao giờ in ra).
Quy trình đầy đủ: _skills/image/SKILL.md mục "Gen GPT Image".

  python3 _tools/gen-image.py --prompt-file p.txt --out outputs/images/X_B-01_S01-mo-ta_v1.png --ratio 9:16 [--quality medium] [--ref a.png --ref b.png]
  python3 _tools/gen-image.py --check      # chỉ kiểm key còn dùng được

--ref theo ĐÚNG thứ tự Image 1, Image 2… trong prompt. Có --ref → endpoint edits, không có → generations.
Mỗi ảnh (cùng tên, bỏ _vN) tối đa 2 lượt: 1 gen + 1 sửa. Quá → exit 3, user tự sửa tay.
Mỗi lượt thành công ghi 1 dòng vào <thư mục out>/_gen-log.jsonl (kèm prompt).
Exit: 0 ok · 1 lỗi khác · 2 bị bộ lọc an toàn chặn · 3 hết lượt · 4 key/credit (fallback thẻ tự gen).
"""
import argparse, base64, datetime, json, mimetypes, os, re, subprocess, sys, tempfile, time
import urllib.error, urllib.request, uuid
# Windows console mặc định cp1252 → in tiếng Việt bị lỗi
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")

ENV_FILE = os.path.expanduser("~/.config/ai-studio/.env")
API = "https://api.openai.com/v1/"
MAX_TURNS = 2  # 1 gen + 1 sửa
# Cạnh chia hết cho 16, đúng tỷ lệ, trong giới hạn gpt-image-2.
RATIOS = {"9:16": "1152x2048", "16:9": "2048x1152", "4:5": "1536x1920", "1:1": "1024x1024",
          "2:3": "1024x1536", "3:2": "1536x1024"}
OK_EXT = {".png", ".jpg", ".jpeg", ".webp"}


def die(code, msg):
    print(msg, file=sys.stderr)
    sys.exit(code)


def load_key():
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key and os.path.exists(ENV_FILE):
        for line in open(ENV_FILE):
            if line.startswith("OPENAI_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"')
    if not key:
        die(4, "THIẾU OPENAI_API_KEY → chạy: sh _tools/set-key.sh OPENAI_API_KEY")
    return key


def multipart(fields, files):
    b = uuid.uuid4().hex
    out = b""
    for k, v in fields.items():
        out += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    for k, path in files:
        ctype = mimetypes.guess_type(path)[0] or "image/png"
        out += (f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{os.path.basename(path)}"\r\n'
                f"Content-Type: {ctype}\r\n\r\n").encode() + open(path, "rb").read() + b"\r\n"
    return out + f"--{b}--\r\n".encode(), f"multipart/form-data; boundary={b}"


def call(key, path, body=None, ctype=None):
    for attempt in range(3):  # chỉ thử lại lỗi tạm thời; lỗi không trả ảnh thì không tính lượt
        req = urllib.request.Request(API + path, data=body, headers={"Authorization": f"Bearer {key}"})
        if ctype:
            req.add_header("Content-Type", ctype)
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            err = json.loads(e.read() or b"{}").get("error", {})
            msg, code = err.get("message", ""), err.get("code") or ""
            if e.code in (401, 403) or code == "insufficient_quota" or "billing" in msg.lower():
                die(4, f"LỖI KEY/CREDIT {e.code}: {msg}")
            if code == "moderation_blocked" or "safety" in msg.lower():
                die(2, f"BỊ BỘ LỌC AN TOÀN CHẶN: {msg}")
            if e.code != 429 and e.code < 500:
                die(1, f"LỖI API {e.code}: {msg}")
            last = f"LỖI API {e.code}: {msg}"
        except (urllib.error.URLError, TimeoutError) as e:
            last = f"LỖI MẠNG: {e}"
        time.sleep(10 * (attempt + 1))
    die(1, last + " (đã thử 3 lần)")


def prep_ref(path, tmp):
    if not os.path.exists(path):
        die(1, f"KHÔNG THẤY FILE REF: {path} (file Drive chưa tải offline?)")
    if os.path.splitext(path)[1].lower() in OK_EXT:
        return path
    out = os.path.join(tmp, os.path.splitext(os.path.basename(path))[0] + ".png")
    subprocess.run(["sips", "-s", "format", "png", path, "--out", out], check=True, capture_output=True)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt-file")
    p.add_argument("--out")
    p.add_argument("--ref", action="append", default=[])
    p.add_argument("--model", default="gpt-image-2")
    p.add_argument("--ratio", choices=RATIOS)
    p.add_argument("--size", help="WxH tuỳ chỉnh, thay cho --ratio")
    p.add_argument("--quality", default="medium", choices=["low", "medium", "high"])
    p.add_argument("--check", action="store_true")
    a = p.parse_args()
    key = load_key()
    if a.check:
        call(key, "models")
        return print("OPENAI_API_KEY: OK")
    if not (a.prompt_file and a.out and (a.ratio or a.size)):
        p.error("cần --prompt-file, --out và --ratio (hoặc --size)")
    if os.path.exists(a.out):
        die(1, f"FILE ĐÃ CÓ, không ghi đè: {a.out} → tăng _vN")

    log = os.path.join(os.path.dirname(os.path.abspath(a.out)), "_gen-log.jsonl")
    base = re.sub(r"_v\d+(\.\w+)$", "", os.path.basename(a.out))
    turns = 0
    if os.path.exists(log):
        turns = sum(1 for l in open(log) if l.strip() and json.loads(l).get("image") == base)
    if turns >= MAX_TURNS:
        die(3, f"HẾT LƯỢT: {base} đã gen {turns} lần (1 gen + 1 sửa) → ghi note để user tự sửa tay")

    prompt = open(a.prompt_file).read().strip()
    params = {"model": a.model, "prompt": prompt, "size": a.size or RATIOS[a.ratio], "quality": a.quality}
    with tempfile.TemporaryDirectory() as tmp:
        refs = [prep_ref(f, tmp) for f in a.ref]
        if refs:
            body, ctype = multipart(params, [("image[]", f) for f in refs])
            res = call(key, "images/edits", body, ctype)
        else:
            res = call(key, "images/generations", json.dumps(params).encode(), "application/json")

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "wb").write(base64.b64decode(res["data"][0]["b64_json"]))
    entry = {"time": datetime.datetime.now().isoformat(timespec="seconds"), "image": base,
             "file": os.path.basename(a.out), "turn": turns + 1, **params, "refs": a.ref}
    with open(log, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"{a.out} (lượt {turns + 1}/{MAX_TURNS})")


if __name__ == "__main__":
    main()
