#!/bin/sh
# SessionStart hook: kiểm tra máy + nhắc công cụ user đã chọn. Chạy được trên Mac và Windows (Git Bash).
# Đủ hết + đã chọn công cụ → in 1 dòng "Công cụ đã chọn". Thiếu → in danh sách để Claude nhắc user "set up dự án".
# stdout của hook SessionStart được đưa vào context — không cần Python để in.
# Không bao giờ in giá trị key — chỉ in tên key thiếu/có.
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" || exit 0

# Key + lựa chọn công cụ để NGOÀI folder project (folder này được share/đưa lên Drive).
ENV_FILE="$HOME/.config/ai-studio/.env"
PREFS="$HOME/.config/ai-studio/prefs.env"
val() { [ -f "$ENV_FILE" ] && sed -n "s/^$1=//p" "$ENV_FILE" | tail -1; }

# Windows: lệnh Python thường là `python` hoặc `py -3`, không có `python3`.
PY=""
for c in python3 python "py -3"; do
  $c -c 'import sys; sys.exit(sys.version_info[0] != 3)' >/dev/null 2>&1 && { PY="$c"; break; }
done

missing=""
[ -f .env ] && missing="$missing
- File .env trong folder project: CÓ — NGUY HIỂM, chuyển key sang $ENV_FILE (sh _tools/set-key.sh TÊN_KEY) rồi xoá"
if [ -z "$PY" ]; then
  missing="$missing
- Python 3: THIẾU (cần cho gen ảnh, transcript)"
else
  [ "$PY" = "python3" ] || missing="$missing
- Lệnh python3: THIẾU (máy có '$PY' nhưng các lệnh dự án gọi python3 — skill setup bước 2 tạo alias)"
  $PY -c 'import faster_whisper' >/dev/null 2>&1 || missing="$missing
- faster-whisper: THIẾU (cần cho cổng 3 — transcript). Máy không GPU → chạy device=\"cpu\""
fi
command -v npx >/dev/null 2>&1 || missing="$missing
- Node.js/npx: THIẾU (cần cho cổng 3 — dựng Remotion)"
command -v ffmpeg >/dev/null 2>&1 || missing="$missing
- ffmpeg: THIẾU (cần cho cổng 2–3 — xem/cắt khung clip)"
[ -s "$PREFS" ] || missing="$missing
- Chưa chọn công cụ (ảnh / video / UGC / giọng đọc / nhạc) — skill setup bước 1"

prefs=""
[ -s "$PREFS" ] && prefs=$(tr '\n' ' ' < "$PREFS")
if grep -q '^IMAGE_TOOL=claude' "$PREFS" 2>/dev/null; then
  ip=$(sed -n 's/^IMAGE_PROVIDER=//p' "$PREFS" | tail -1); ip=${ip:-openai}
  case "$ip" in
    openai) need=OPENAI_API_KEY ;; gemini) need=GEMINI_API_KEY ;; fal) need=FAL_KEY ;; replicate) need=REPLICATE_API_TOKEN ;;
    cloudflare) need="CLOUDFLARE_ACCOUNT_ID CLOUDFLARE_API_TOKEN" ;; pollinations) need=POLLINATIONS_KEY ;; huggingface) need=HF_TOKEN ;;
  esac
  for k in $need; do [ -n "$(val "$k")" ] || missing="$missing
- $k: THIẾU (nhà cung cấp ảnh đang chọn: $ip — popup: sh _tools/pick-provider.sh image)"; done
fi
grep -q '^VO_TOOL=openai' "$PREFS" 2>/dev/null && [ -z "$(val OPENAI_API_KEY)" ] && missing="$missing
- OPENAI_API_KEY: THIẾU (đã chọn giọng đọc OpenAI TTS)"
# TopView / Higgsfield: kết nối API → cần key (nhập qua popup set-key.sh); MCP → đăng nhập connector, không kiểm được ở đây.
for svc in TOPVIEW HIGGSFIELD; do
  lower=$(echo "$svc" | tr 'A-Z' 'a-z')
  grep -Eq "^(UGC|VIDEO)_TOOL=$lower" "$PREFS" 2>/dev/null || continue
  conn=$(sed -n "s/^${svc}_CONN=//p" "$PREFS" | tail -1)
  case "$conn" in
    api) [ "$svc" = TOPVIEW ] && need="TOPVIEW_API_KEY TOPVIEW_UID" || need="HIGGSFIELD_API_KEY HIGGSFIELD_API_SECRET"
         for k in $need; do [ -n "$(val "$k")" ] || missing="$missing
- $k: THIẾU (đã chọn $lower qua API — skill setup bước 7, popup)"; done ;;
    mcp) ;;
    *) missing="$missing
- Chưa chọn cách kết nối $lower (MCP hay API key) — skill setup bước 1" ;;
  esac
done

[ -n "$prefs" ] && echo "Công cụ đã chọn trên máy này (~/.config/ai-studio/prefs.env): $prefs— làm theo bảng 'Ai làm gì' trong CLAUDE.md."
[ -z "$missing" ] && exit 0

echo "SETUP CÒN THIẾU trên máy này:$missing

Nhắc user 1 câu: nói 'set up dự án' để Claude cài giúp (skill .claude/skills/setup/). Rồi làm tiếp task — chỉ chặn ở bước thật sự cần thứ bị thiếu. Không bao giờ yêu cầu user dán API key vào chat — Claude chạy: sh _tools/set-key.sh TÊN_KEY → hộp thoại ẩn hiện trên máy user."
