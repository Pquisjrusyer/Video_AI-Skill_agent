#!/bin/sh
# Mở File Explorer (Windows) / Finder (Mac) tới 1 file hoặc thư mục — CHỈ mở / chọn, không bao giờ chạy file.
# Dùng: sh _tools/open-path.sh "campaigns/<campaign>/outputs/videos/X_S01_v1.mp4"
#   File có → mở thư mục chứa nó, chọn sẵn file · file chưa có → mở thư mục cha (tạo nếu chưa có) · thư mục → mở thư mục.
P="${1:?Thiếu đường dẫn}"
if [ -d "$P" ]; then DIR="$P"; FILE=""
elif [ -f "$P" ]; then DIR=$(dirname "$P"); FILE="$P"
else DIR=$(dirname "$P"); FILE=""; mkdir -p "$DIR"; fi

if command -v osascript >/dev/null 2>&1; then
  if [ -n "$FILE" ]; then open -R "$FILE"; else open "$DIR"; fi
else
  W() { cygpath -w "$1" 2>/dev/null || printf %s "$1"; }
  if [ -n "$FILE" ]; then explorer.exe "/select,$(W "$FILE")"; else explorer.exe "$(W "$DIR")"; fi
fi
exit 0   # explorer.exe trả mã 1 dù mở thành công
