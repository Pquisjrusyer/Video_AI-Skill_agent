#!/usr/bin/env python3
"""Thu nhỏ ảnh để QC (thay cho `sips -Z`, chạy được cả Mac lẫn Windows).

  python3 _tools/thumb.py in.png out.jpg [cạnh-dài-px, mặc định 768]
"""
import os, sys
from PIL import Image

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")

if len(sys.argv) < 3:
    sys.exit(__doc__)
src, dst = sys.argv[1], sys.argv[2]
size = int(sys.argv[3]) if len(sys.argv) > 3 else 768
im = Image.open(src)
im.thumbnail((size, size))
os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
im.convert("RGB").save(dst, quality=88)
print(f"{dst} {im.width}x{im.height}")
