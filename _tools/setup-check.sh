#!/bin/sh
# SessionStart hook: kiểm tra công cụ máy cần (Remotion, transcript). VO dùng connector ElevenLabs (MCP) — không kiểm ở đây. Đủ hết → im lặng.
# Thiếu → bơm context để Claude nhắc user theo _workflows/setup-guide.md. Không chặn task.
# Ảnh GPT Image: Claude gen qua _tools/gen-image.py → cần OPENAI_API_KEY. Video vẫn do người dùng tự gen.
# Không bao giờ in giá trị key — chỉ in tên key thiếu/có.
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" || exit 0

# Key để NGOÀI folder project (folder này được share/đưa lên Drive).
ENV_FILE="$HOME/.config/ai-studio/.env"

val() { [ -f "$ENV_FILE" ] && sed -n "s/^$1=//p" "$ENV_FILE" | tail -1; }

missing=""
[ -f .env ] && missing="$missing
- File .env trong folder project: CÓ — NGUY HIỂM, chuyển sang $ENV_FILE rồi xoá"
command -v npx >/dev/null 2>&1 || missing="$missing
- Node.js/npx: THIẾU (cần cho cổng 3 — dựng Remotion)"
python3 -c 'import faster_whisper' >/dev/null 2>&1 || missing="$missing
- faster-whisper: THIẾU (cần cho cổng 3 — transcript canh giờ b-roll/text)"
[ -n "$(val OPENAI_API_KEY)" ] || missing="$missing
- OPENAI_API_KEY: THIẾU (cần cho cổng 2 — Claude gen ảnh GPT Image; thiếu thì user tự gen theo thẻ)"

[ -z "$missing" ] && exit 0

msg="SETUP CÒN THIẾU trên máy này:$missing

Nhắc user 1 câu: nói 'set up dự án' để Claude cài giúp (skill .claude/skills/setup/). Rồi làm tiếp task của user — chỉ chặn ở chặng thật sự cần thứ bị thiếu. Không bao giờ yêu cầu user dán API key vào chat — Claude chạy: sh _tools/set-key.sh TÊN_KEY → hộp thoại ẩn hiện trên máy user để user tự dán."

python3 -c 'import json,sys; print(json.dumps({"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":sys.argv[1]}}))' "$msg"
