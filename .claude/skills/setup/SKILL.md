---
name: setup
description: Cài và kiểm tra cấu hình máy cho project AI Video (Python, Node.js, faster-whisper, key ChatGPT/OpenAI gen ảnh, connector ElevenLabs). Dùng khi user nói "set up dự án", "setup máy", "cài đặt project", "kiểm tra setup", "đổi key", "cập nhật key OpenAI", hoặc hook setup-check báo thiếu.
---

# Set up dự án

User không rành kỹ thuật. **Claude tự chạy lệnh**, chỉ nhờ user bấm khi máy bắt buộc (hộp thoại cài, mật khẩu máy, đăng nhập connector). Mỗi lần nói 1 việc, tiếng Việt, ngắn.

## 1. Kiểm tra

```bash
sh "$CLAUDE_PROJECT_DIR/_tools/setup-check.sh"; python3 --version; node -v
```
Im lặng + có version = đủ → báo "Máy đã sẵn sàng" và dừng. Thiếu gì → làm đúng bước đó, theo thứ tự dưới.

## 2. Python 3 (cần cho faster-whisper)

`python3 --version` lỗi hoặc hiện hộp thoại → chạy `xcode-select --install`.
Nói user: "Máy sẽ hiện hộp thoại cài **Command Line Developer Tools** → bấm **Install**, chờ xong (5–15 phút) rồi nhắn mình." Xong → chạy lại bước 1.

## 3. Node.js (cần để dựng video Remotion)

Lấy bản LTS mới nhất (không hardcode version):
```bash
V=$(curl -s https://nodejs.org/dist/index.json | python3 -c "import json,sys;print(next(r['version'] for r in json.load(sys.stdin) if r['lts']))")
echo "node-$V.pkg"
```
**Hỏi user trước khi tải**: "Mình tải bộ cài Node.js `node-$V.pkg` (~80MB) từ nodejs.org nhé?" → đồng ý mới chạy:
```bash
curl -L -o ~/Downloads/node-$V.pkg https://nodejs.org/dist/$V/node-$V.pkg && open ~/Downloads/node-$V.pkg
```
Nói user: "Bộ cài đã mở → bấm **Continue** đến hết, nhập mật khẩu máy khi được hỏi. Xong thì **thoát hẳn Claude (Cmd+Q) rồi mở lại**, nhắn mình 'setup tiếp'."
Không tự nhập mật khẩu, không dùng `sudo`.

## 4. faster-whisper

```bash
python3 -m pip install --user faster-whisper && python3 -c "import faster_whisper; print('ok')"
```
Lỗi pip cũ → `python3 -m pip install --user --upgrade pip` rồi thử lại. Lỗi khác → báo nguyên văn dòng lỗi cuối cho user, không thử cách lạ.

## 5. Connector ElevenLabs (để Claude gen giọng đọc — không cần API key)

Kiểm tra: ToolSearch `creative_generate_speech`. Có tool → ✅.
Không có / báo cần xác thực → nói user: "Vào **claude.ai → Settings → Connectors** → bật **ElevenLabs** → đăng nhập tài khoản ElevenLabs của team → mở lại session." Không có connector vẫn làm được: VO xuất thẻ để tự gen trên elevenlabs.io.
**Không bao giờ** xin key/mật khẩu qua chat — key chỉ nhập qua hộp thoại của `set-key.sh`.

## 6. Key ChatGPT / OpenAI (để Claude tự gen ảnh GPT Image)

Hook báo `OPENAI_API_KEY: THIẾU`, hoặc user muốn đổi key mới → nói user:
"Bạn cần 1 API key OpenAI: vào **platform.openai.com/api-keys** → **Create new secret key** → copy (bắt đầu bằng `sk-`). Tài khoản cần nạp credit (Billing) và đã xác minh tổ chức (Settings → Organization → Verify) để dùng model ảnh. Copy xong nhắn mình."
User nhắn xong → chạy (hộp thoại ẩn hiện trên máy, user tự dán key, bấm OK):
```bash
sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" OPENAI_API_KEY && python3 "$CLAUDE_PROJECT_DIR/_tools/gen-image.py" --check
```
`OK` → ✅. Rồi nhắc user (1 lần): "Nên đặt giới hạn chi tiêu: **platform.openai.com → Settings → Limits** → đặt budget tháng + email cảnh báo; **Billing** → nạp trả trước, tắt auto-recharge." `LỖI API 401` → key sai/đã thu hồi, làm lại. `403`/`verify` → chưa xác minh tổ chức. `429`/`quota` → hết credit.
Không có key vẫn làm được: thẻ ảnh để user tự gen trên chatgpt.com.

## 7. Kết thúc

Chạy lại bước 1. Đủ hết → báo 1 dòng: "✅ Máy đã sẵn sàng. Bắt đầu: nói 'làm video [thời lượng] cho sản phẩm [tên/link]'." Còn thiếu mục tuỳ chọn → nói rõ mục đó dùng khi nào.

Lỗi lạ → tra bảng "Lỗi hay gặp" trong `_workflows/setup-guide.md`.
