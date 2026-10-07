#!/bin/sh
# Mở 1 trang HTML (storyboard / bảng clip / bảng review) bằng trình duyệt mặc định của máy
# — nút 📋 Copy ảnh và 📂 Mở thư mục chỉ chạy đầy đủ ở trình duyệt thật, không chạy trong khung xem trước của Claude.
# Dùng: sh _tools/open-browser.sh "campaigns/<campaign>/outputs/review/clip-board.html"
F="${1:?Thiếu đường dẫn file HTML}"
[ -f "$F" ] || { echo "Không thấy file: $F" >&2; exit 1; }
if command -v osascript >/dev/null 2>&1; then
  open "$F"
else
  cmd.exe //c start "" "$(cygpath -w "$(cd "$(dirname "$F")" && pwd)/$(basename "$F")")"
fi
echo "Đã mở bằng trình duyệt: $F"
