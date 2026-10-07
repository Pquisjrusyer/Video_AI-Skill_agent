#!/bin/sh
# Popup "gọi hồn provider" — từng bước: chọn nhà → đã có key chưa? → (hướng dẫn lấy key + nút mở trang) → nhập key.
# gen-image.py tự gọi khi API lỗi; skill goi-hon gọi khi user đọc thần chú.
# Dùng: sh _tools/pick-provider.sh image "câu thần chú / lý do" ["openai,gemini" = nhà loại khỏi danh sách]
#   → lưu key vào ~/.config/ai-studio/.env (ngoài project, không in ra); nhà tự thêm → providers-custom.json;
#     tuỳ chọn đặt làm mặc định (prefs.env). In tên nhà đã chọn ở dòng cuối. Huỷ / không mở được popup → exit 1.
# Dữ liệu nhà cung cấp + hướng dẫn lấy key: _tools/providers.json.
TASK="${1:-image}"; REASON="${2:-🔮 Gọi hồn provider}"; EXCLUDE="${3:-}"
DIR="$(cd "$(dirname "$0")" && pwd)"
ENV_FILE="$HOME/.config/ai-studio/.env"
PY=python3; command -v python3 >/dev/null 2>&1 || PY=python
NL='
'

if command -v osascript >/dev/null 2>&1; then
  # ---- Mac: chuỗi hộp thoại AppleScript ----
  osa() { osascript -e "$1" 2>/dev/null; }
  esc() { printf %s "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'; }
  LIST=$($PY "$DIR/providers_cli.py" list "$TASK" "$EXCLUDE")
  STEP=pick
  while :; do
    case $STEP in
    pick)
      ITEMS=$(printf %s "$LIST" | cut -f2 | sed 's/"/\\"/g; s/^/"/; s/$/"/' | paste -sd, -)
      PICK=$(osa "choose from list {$ITEMS} with prompt \"$(esc "$REASON") — Bước 1/3: chọn nhà cung cấp\" with title \"🔮 AI Video — gọi hồn provider\"")
      [ -z "$PICK" ] || [ "$PICK" = false ] && { echo "Đã huỷ" >&2; exit 1; }
      P=$(printf %s "$LIST" | awk -F'\t' -v l="$PICK" '$2==l{print $1; exit}'); STEP=have ;;
    have)
      B=$(osa "button returned of (display dialog \"Bước 2/3 — Bạn đã có key của $P chưa?\" buttons {\"‹ Quay lại\", \"Chưa / chưa biết lấy ở đâu\", \"Có rồi › nhập key\"} default button 3 with title \"🔮 gọi hồn provider\")")
      case "$B" in "Có rồi"*) STEP=input ;; "Chưa"*) STEP=guide ;; "‹"*) STEP=pick ;; *) echo "Đã huỷ" >&2; exit 1 ;; esac ;;
    guide)
      G=$($PY "$DIR/providers_cli.py" get "$TASK" "$P" guide); U=$($PY "$DIR/providers_cli.py" get "$TASK" "$P" url)
      BTN='"‹ Quay lại", "Hoàn tất › nhập key"'; [ -n "$U" ] && BTN='"‹ Quay lại", "🌐 Mở trang lấy key", "Hoàn tất › nhập key"'
      B=$(osa "button returned of (display dialog \"$(esc "$G")\" buttons {$BTN} default button \"Hoàn tất › nhập key\" with title \"📖 Hướng dẫn lấy key — $P\")")
      case "$B" in "🌐"*) open "$U" ;; "Hoàn tất"*) STEP=input ;; "‹"*) STEP=have ;; *) echo "Đã huỷ" >&2; exit 1 ;; esac ;;
    input)
      OUT=""
      if [ "$P" = custom ]; then
        N=$(osa 'text returned of (display dialog "Tên nhà cung cấp (không dấu, VD together)" default answer "")') || exit 1
        BU=$(osa 'text returned of (display dialog "Base URL (VD https://api.together.xyz/v1)" default answer "")') || exit 1
        M=$(osa 'text returned of (display dialog "Model ảnh (VD black-forest-labs/FLUX.1-schnell)" default answer "")') || exit 1
        K=$(osa 'text returned of (display dialog "API key" default answer "" with hidden answer)') || exit 1
        RF=$(osa 'button returned of (display dialog "Nhà này có ảnh tham chiếu (/images/edits)?" buttons {"Không", "Có"} default button 1)')
        SLUG=$(printf %s "$N" | tr 'A-Z' 'a-z' | tr -cd 'a-z0-9'); EN="CUSTOM_$(printf %s "$SLUG" | tr 'a-z' 'A-Z')_API_KEY"
        [ -n "$SLUG" ] && [ -n "$BU" ] && [ -n "$M" ] || { osa 'display dialog "Cần đủ Tên, Base URL và Model." buttons {"OK"}'; continue; }
        [ "$RF" = "Có" ] && RJ=true || RJ=false
        OUT="PROVIDER=custom:$SLUG${NL}ENV:$EN=$K${NL}CUSTOM={\"name\":\"$SLUG\",\"base_url\":\"${BU%/}\",\"model\":\"$M\",\"refs\":$RJ,\"key_env\":\"$EN\"}"
      else
        OUT="PROVIDER=$P"
        KEYS=$($PY "$DIR/providers_cli.py" get "$TASK" "$P" keys)
        OLDIFS=$IFS; IFS="$NL"
        for line in $KEYS; do
          EN=$(printf %s "$line" | cut -f1); LB=$(printf %s "$line" | cut -f2); HD=$(printf %s "$line" | cut -f3)
          [ "$HD" = 1 ] && H=" with hidden answer" || H=""
          V=$(osa "text returned of (display dialog \"Bước 3/3 — $(esc "$LB") của $P (để trống = giữ key đã lưu)\" default answer \"\"$H with title \"🔮 gọi hồn provider\")") || { IFS=$OLDIFS; echo "Đã huỷ" >&2; exit 1; }
          OUT="$OUT${NL}ENV:$EN=$V"
        done
        IFS=$OLDIFS
      fi
      D=$(osa 'button returned of (display dialog "Dùng nhà cung cấp này làm mặc định từ giờ?" buttons {"Chỉ lần này", "Làm mặc định"} default button 1)')
      [ "$D" = "Làm mặc định" ] && OUT="$OUT${NL}DEFAULT=1" || OUT="$OUT${NL}DEFAULT=0"
      break ;;
    esac
  done
else
  # ---- Windows: popup PowerShell (provider-dialog.ps1) ----
  PS1=$(cygpath -w "$DIR/provider-dialog.ps1" 2>/dev/null || echo "$DIR/provider-dialog.ps1")
  OUT=$(powershell.exe -NoProfile -STA -ExecutionPolicy Bypass -File "$PS1" -Task "$TASK" -Reason "$REASON" -Exclude "$EXCLUDE" 2>/dev/null) || { echo "Đã huỷ" >&2; exit 1; }
  OUT=$(printf %s "$OUT" | tr -d '\r')
fi

# ---- Lưu kết quả (không in key) ----
save() {  # $1 tên, $2 giá trị — rỗng thì giữ key cũ
  V=$(printf %s "$2" | tr -d '[:space:]'); [ -n "$V" ] || return 0
  mkdir -p "$(dirname "$ENV_FILE")"; touch "$ENV_FILE" && chmod 600 "$ENV_FILE"
  grep -v "^$1=" "$ENV_FILE" > "$ENV_FILE.tmp"; printf '%s=%s\n' "$1" "$V" >> "$ENV_FILE.tmp"
  mv "$ENV_FILE.tmp" "$ENV_FILE" && chmod 600 "$ENV_FILE"
}
P=""; DEF=0
OLDIFS=$IFS; IFS="$NL"
for line in $OUT; do
  case "$line" in
    PROVIDER=*) P=${line#PROVIDER=} ;;
    ENV:*) kv=${line#ENV:}; save "${kv%%=*}" "${kv#*=}" ;;
    CUSTOM=*) $PY "$DIR/providers_cli.py" add-custom "${line#CUSTOM=}" ;;
    DEFAULT=1) DEF=1 ;;
  esac
done
IFS=$OLDIFS
[ -n "$P" ] || { echo "Đã huỷ" >&2; exit 1; }
[ "$DEF" = 1 ] && sh "$DIR/set-prefs.sh" "IMAGE_PROVIDER=$P" >/dev/null
echo "$P"
