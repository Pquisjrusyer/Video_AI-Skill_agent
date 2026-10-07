#!/usr/bin/env python3
"""Tải b-roll miễn phí từ Pexels + Pixabay vào _assets/broll-library/generic/stock/.

    set -a; . ~/.config/ai-studio/.env; set +a
    python3 _tools/fetch-stock-broll.py "serum drop macro" "cream texture" --limit 5

Bỏ qua nguồn nào không có API key. Chỉ lấy clip dọc (h > w) để hợp 9:16.
Xem _assets/broll-library/free-sources.md về license + cảnh báo model release.
"""
import json, os, re, sys, urllib.parse, urllib.request

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "_assets", "broll-library", "generic", "stock")

# Pexels trả 403 cho UA mặc định "Python-urllib". Áp UA thường cho cả get() lẫn urlretrieve.
_opener = urllib.request.build_opener()
_opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)")]
urllib.request.install_opener(_opener)


def get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def pexels(query, limit):
    key = os.environ.get("PEXELS_API_KEY")
    if not key:
        return []
    q = urllib.parse.urlencode({"query": query, "per_page": limit, "orientation": "portrait"})
    out = []
    for v in get(f"https://api.pexels.com/videos/search?{q}", {"Authorization": key})["videos"]:
        # file lớn nhất vẫn <= 1920 chiều rộng, tránh tải bản 4K nặng vô ích
        files = [f for f in v["video_files"] if f["height"] > f["width"] and f["width"] <= 1920]
        if files:
            best = max(files, key=lambda f: f["width"])
            out.append(("pexels", best["link"], v["url"], v.get("user", {}).get("name", "")))
    return out


def pixabay(query, limit):
    key = os.environ.get("PIXABAY_API_KEY")
    if not key:
        return []
    q = urllib.parse.urlencode({"key": key, "q": query, "per_page": max(3, limit)})
    out = []
    for h in get(f"https://pixabay.com/api/videos/?{q}")["hits"][:limit]:
        v = h["videos"].get("large") or h["videos"]["medium"]
        if v["height"] > v["width"]:
            out.append(("pixabay", v["url"], h["pageURL"], h.get("user", "")))
    return out


def main(queries, limit):
    os.makedirs(OUT, exist_ok=True)
    if not (os.environ.get("PEXELS_API_KEY") or os.environ.get("PIXABAY_API_KEY")):
        sys.exit("Cần PEXELS_API_KEY và/hoặc PIXABAY_API_KEY trong env (~/.config/ai-studio/.env, nạp bằng: set -a; . ~/.config/ai-studio/.env; set +a).")

    # Log tải thô tách riêng — CREDITS.md chỉ chứa clip đã lọc + đổi tên để dùng.
    credits = os.path.join(OUT, "_download-log.md")
    new = not os.path.exists(credits)
    with open(credits, "a") as log:
        if new:
            log.write("# Stock b-roll — log tải thô (không phải danh sách dùng)\n\n"
                      "Ghi tự động bởi _tools/fetch-stock-broll.py. Clip giữ lại → đổi tên + ghi vào CREDITS.md.\n\n"
                      "| File | Nguồn | Query | Link gốc | Tác giả |\n|---|---|---|---|---|\n")
        for query in queries:
            slug = re.sub(r"[^a-z0-9]+", "-", query.lower()).strip("-")
            for i, (src, url, page, author) in enumerate(pexels(query, limit) + pixabay(query, limit), 1):
                name = f"stock-{src}-{slug}-{i}.mp4"
                path = os.path.join(OUT, name)
                if os.path.exists(path):
                    print(f"skip  {name}")
                    continue
                urllib.request.urlretrieve(url, path)
                log.write(f"| `{name}` | {src} | {query} | {page} | {author} |\n")
                print(f"saved {name}")

    print(f"\n→ {os.path.normpath(OUT)}")
    print("Nhớ: clip có mặt người nhận diện được thì KHÔNG dùng trong ad. Xoá trước khi import vào index.md.")
    print("Clip giữ lại: rename file theo mô tả (stock-[nguồn]-[mô-tả-ngắn].mp4), "
          "thêm vào CREDITS.md bảng giữ lại + index.md + keywords.json.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lim = next((int(a.split("=")[1]) for a in sys.argv[1:] if a.startswith("--limit=")), None)
    if "--limit" in sys.argv:
        lim = int(sys.argv[sys.argv.index("--limit") + 1])
        args.remove(str(lim))
    if not args:
        sys.exit(__doc__)
    main(args, lim or 3)
