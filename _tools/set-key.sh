#!/bin/sh
# Nhập/đổi 1 API key qua hộp thoại macOS (ô ẩn) → ghi vào ~/.config/ai-studio/.env (ngoài folder project).
# Key không đi qua chat, không in ra màn hình. Dùng: sh _tools/set-key.sh OPENAI_API_KEY ["gợi ý lấy key ở đâu"]
# Gợi ý (tuỳ chọn) hiện trong popup — viết không dấu (hộp thoại Windows không hiển thị tiếng Việt có dấu).
NAME="${1:?Thiếu tên key, VD: OPENAI_API_KEY}"
HINT="${2:-}"
ENV_FILE="$HOME/.config/ai-studio/.env"

if command -v osascript >/dev/null 2>&1; then
  VAL=$(osascript -e "text returned of (display dialog \"Dán $NAME vào ô dưới rồi bấm OK. $HINT\" default answer \"\" with hidden answer with title \"AI Video — nhập key\")" 2>/dev/null) || { echo "Đã huỷ"; exit 1; }
else
  # Windows (Git Bash): hộp thoại ô ẩn qua PowerShell
  PS1=$(cygpath -w "$(dirname "$0")/key-dialog.ps1" 2>/dev/null || echo "$(dirname "$0")/key-dialog.ps1")
  VAL=$(powershell.exe -NoProfile -STA -ExecutionPolicy Bypass -File "$PS1" -Name "$NAME" -Hint "$HINT" 2>/dev/null) || { echo "Đã huỷ"; exit 1; }
fi
VAL=$(printf %s "$VAL" | tr -d '[:space:]')
[ -n "$VAL" ] || { echo "Key trống"; exit 1; }

mkdir -p "$(dirname "$ENV_FILE")"
touch "$ENV_FILE" && chmod 600 "$ENV_FILE"
grep -v "^$NAME=" "$ENV_FILE" > "$ENV_FILE.tmp"
printf '%s=%s\n' "$NAME" "$VAL" >> "$ENV_FILE.tmp"
mv "$ENV_FILE.tmp" "$ENV_FILE" && chmod 600 "$ENV_FILE"
echo "$NAME: đã lưu"
