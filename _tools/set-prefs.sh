#!/bin/sh
# Lưu lựa chọn công cụ của máy này (không phải key, không bí mật) → ~/.config/ai-studio/prefs.env
# Dùng: sh _tools/set-prefs.sh IMAGE_TOOL=claude UGC_TOOL=topview TOPVIEW_CONN=mcp ...
# Không đối số → in lựa chọn hiện tại. Key/secret KHÔNG lưu ở đây — dùng set-key.sh (popup ẩn).
PREFS="$HOME/.config/ai-studio/prefs.env"
mkdir -p "$(dirname "$PREFS")"; touch "$PREFS"

[ $# -eq 0 ] && { cat "$PREFS"; exit 0; }

for kv in "$@"; do
  case "$kv" in
    IMAGE_TOOL=*|IMAGE_PROVIDER=*|VIDEO_TOOL=*|UGC_TOOL=*|VO_TOOL=*|MUSIC_TOOL=*|TOPVIEW_CONN=*|HIGGSFIELD_CONN=*) ;;
    *) echo "Bỏ qua (tên không hợp lệ): $kv"; continue ;;
  esac
  name="${kv%%=*}"
  grep -v "^$name=" "$PREFS" > "$PREFS.tmp"; printf '%s\n' "$kv" >> "$PREFS.tmp"; mv "$PREFS.tmp" "$PREFS"
done
cat "$PREFS"
