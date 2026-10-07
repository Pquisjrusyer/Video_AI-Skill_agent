---
name: setup
description: Cài và kiểm tra cấu hình máy cho project AI Video trên Mac hoặc Windows — hỏi user chọn công cụ (UGC / video: TopView, Higgsfield, Google Flow để test; ảnh; giọng đọc; nhạc) và cách kết nối (MCP hoặc API key qua popup), rồi cài đúng thứ cần (Python, Node.js, ffmpeg, faster-whisper, key OpenAI/TopView/Higgsfield, connector). Dùng khi user nói "set up dự án", "setup máy", "cài đặt project", "kiểm tra setup", "đổi công cụ", "đổi key", "cập nhật key OpenAI", "nhập key TopView/Higgsfield", hoặc hook setup-check báo thiếu.
---

# Set up dự án

User không rành kỹ thuật. **Claude tự chạy lệnh**, chỉ nhờ user bấm khi máy bắt buộc (hộp thoại cài, mật khẩu máy, đăng nhập). Tiếng Việt, mỗi lần nói 1 việc, ngắn (không giải thích kỹ thuật trừ khi user hỏi).
Không tự nhập mật khẩu, không dùng `sudo`. **Không bao giờ** xin key / mật khẩu qua chat — mọi key chỉ nhập qua popup ẩn của `set-key.sh` (bước 7). Hỏi trước khi tải / cài bất kỳ thứ gì.

## 0. Kiểm tra + nhận hệ điều hành

```bash
sh "$CLAUDE_PROJECT_DIR/_tools/setup-check.sh"; uname -s; sh "$CLAUDE_PROJECT_DIR/_tools/set-prefs.sh"
```
`uname -s`: `Darwin` = Mac · `MINGW*` / `MSYS*` = Windows. Đã chọn công cụ + không báo thiếu → "✅ Máy đã sẵn sàng" và dừng (trừ khi user muốn đổi công cụ → bước 1).

## 1. Hỏi user chọn công cụ (bắt buộc lần đầu, hoặc khi user muốn đổi)

Dùng AskUserQuestion. Lượt 1 (4 câu):

| Câu hỏi | Lựa chọn → giá trị lưu |
|---|---|
| Video UGC (người nói trước camera) làm bằng gì? | TopView — Claude gọi qua MCP/API → `UGC_TOOL=topview` · Higgsfield — Claude gọi qua MCP/API → `UGC_TOOL=higgsfield` · Google Flow — **chỉ để test**, bạn tự render → `UGC_TOOL=flow` |
| Video cảnh (b-roll, demo sản phẩm) làm bằng gì? | Higgsfield → `VIDEO_TOOL=higgsfield` · TopView → `VIDEO_TOOL=topview` · Google Flow — **chỉ để test**, bạn tự render → `VIDEO_TOOL=flow` |
| Ảnh: ai gen? | Claude gen qua API (Recommended) → `IMAGE_TOOL=claude` · Tôi tự gen → `IMAGE_TOOL=self` |
| Giọng đọc (VO) ai gen? | Claude qua connector ElevenLabs → `VO_TOOL=elevenlabs` · Claude bằng OpenAI TTS (dùng chung key OpenAI) → `VO_TOOL=openai` · Tôi tự gen → `VO_TOOL=self` |

Lượt 2:
- (khi `IMAGE_TOOL=claude`) Nhà cung cấp ảnh mặc định: OpenAI GPT Image — trả phí, chất lượng cao nhất (Recommended) → `IMAGE_PROVIDER=openai` · Cloudflare — **miễn phí** ~200 ảnh/ngày, có ảnh tham chiếu → `cloudflare` · Gemini / fal.ai / Replicate (trả phí) → `gemini` / `fal` / `replicate`. Pollinations, Hugging Face (miễn phí, không ảnh tham chiếu) chỉ hợp ảnh minh hoạ. Lỗi lúc gen → popup tự hỏi đổi nhà.
- Nhạc nền: Claude qua connector ElevenLabs → `MUSIC_TOOL=elevenlabs` · Tôi tự chọn → `MUSIC_TOOL=self`
- Với **mỗi** công cụ đã chọn trong TopView / Higgsfield, hỏi cách kết nối:
  - "Kết nối [TopView/Higgsfield] bằng gì?" → **MCP — đăng nhập tài khoản, không cần key (Recommended)** → `TOPVIEW_CONN=mcp` / `HIGGSFIELD_CONN=mcp` · **API key** — dán key vào popup → `TOPVIEW_CONN=api` / `HIGGSFIELD_CONN=api`

Lưu (không phải bí mật, nằm ngoài project):
```bash
sh "$CLAUDE_PROJECT_DIR/_tools/set-prefs.sh" UGC_TOOL=topview VIDEO_TOOL=higgsfield TOPVIEW_CONN=mcp HIGGSFIELD_CONN=api IMAGE_TOOL=claude VO_TOOL=openai MUSIC_TOOL=self
```
Sau đó chỉ làm các bước dưới mà lựa chọn cần. Bước không cần → bỏ qua, không nhắc.

## 2. Python 3 (cần cho gen ảnh, faster-whisper)

Kiểm: `python3 --version || python --version || py -3 --version`

**Mac** — lỗi hoặc hiện hộp thoại → `xcode-select --install`. Nói user: "Máy sẽ hiện hộp thoại cài **Command Line Developer Tools** → bấm **Install**, chờ xong rồi nhắn mình."

**Windows**
- Chưa có Python → hỏi rồi chạy `winget install -e --id Python.Python.3.13`. Nói user: "Bấm **Yes** nếu Windows hỏi quyền. Xong thì thoát hẳn Claude rồi mở lại, nhắn 'setup tiếp'."
- Có `python` nhưng không có `python3` (lỗi hay gặp nhất) → tạo alias để mọi lệnh `python3` trong dự án chạy được:
  ```bash
  D=$(dirname "$(command -v python)"); case "$D" in *AppData*) cp "$D/python.exe" "$D/python3.exe" && python3 --version ;; *) echo "Python không nằm trong AppData: $D" ;; esac
  ```
  Python cài ngoài AppData (cần quyền admin) → báo user, không tự sửa.

## 3. Node.js (cần để dựng video Remotion — cổng 3)

Kiểm: `node -v`.

**Mac** — lấy bản LTS mới nhất:
```bash
V=$(curl -s https://nodejs.org/dist/index.json | python3 -c "import json,sys;print(next(r['version'] for r in json.load(sys.stdin) if r['lts']))"); echo "node-$V.pkg"
```
Hỏi: "Mình tải bộ cài Node.js `node-$V.pkg` (~80MB) từ nodejs.org nhé?" → đồng ý:
```bash
curl -L -o ~/Downloads/node-$V.pkg https://nodejs.org/dist/$V/node-$V.pkg && open ~/Downloads/node-$V.pkg
```
Nói user: "Bộ cài đã mở → bấm **Continue** đến hết, nhập mật khẩu máy khi được hỏi. Xong thì thoát hẳn Claude (Cmd+Q) rồi mở lại, nhắn 'setup tiếp'."

**Windows** — hỏi rồi chạy `winget install -e --id OpenJS.NodeJS.LTS`. Xong → thoát hẳn Claude, mở lại.

## 4. ffmpeg (xem / cắt khung clip — cổng 2–3)

Kiểm: `ffmpeg -version`. Thiếu → hỏi rồi cài:
- **Windows:** `winget install -e --id Gyan.FFmpeg` → mở lại Claude.
- **Mac:** có Homebrew (`brew -v`) → `brew install ffmpeg`. Không có Homebrew → bỏ qua, ở cổng 3 dùng `npx remotion ffmpeg` bên trong dự án Remotion đã `npm install`.

Không chạy `npx remotion ffmpeg` ở thư mục gốc (báo lỗi `could not determine executable to run`).

## 5. faster-whisper (transcript — cổng 3)

```bash
python3 -m pip install --user faster-whisper && python3 -c "import faster_whisper; print('ok')"
```
Lỗi pip cũ → `python3 -m pip install --user --upgrade pip` rồi thử lại. Lỗi khác → báo nguyên văn dòng lỗi cuối, không thử cách lạ.
Máy không có GPU NVIDIA (đa số laptop) → mọi chỗ gọi faster-whisper dùng `device="cpu", compute_type="int8"`; lỗi `cublas64_12.dll` nghĩa là đang chạy GPU.

## 6. Connector ElevenLabs (chỉ khi `VO_TOOL` hoặc `MUSIC_TOOL` = `elevenlabs`)

Kiểm: ToolSearch `creative_generate_speech`. Có tool → ✅.
Không có → nói user: "Vào **claude.ai → Settings → Connectors** → bật **ElevenLabs** → đăng nhập tài khoản ElevenLabs của team → mở lại session." Chưa bật được → hỏi user có muốn đổi sang OpenAI TTS (`set-prefs.sh VO_TOOL=openai`) không.

## 7. Nhập key — luôn qua popup ẩn

Quy tắc chung cho **mọi** key: **mở popup trước**, rồi mới nói user lấy key ở đâu. Key không bao giờ đi qua chat. User lỡ dán key vào chat → không dùng, khuyên thu hồi ngay, nhập lại qua popup.
```bash
sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" TÊN_KEY "goi y lay key o dau (viet khong dau)"
```

### 7a. Key ảnh (khi `IMAGE_TOOL=claude`) + OpenAI (khi `VO_TOOL=openai`)

Nhà ảnh khác OpenAI → dùng popup chọn nhà + key: `sh "$CLAUDE_PROJECT_DIR/_tools/pick-provider.sh" image "chon nha cung cap anh"` (Cloudflare cần thêm Account ID — popup có ô riêng). Kiểm: `python3 _tools/gen-image.py --check`.

OpenAI:
```bash
sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" OPENAI_API_KEY "platform.openai.com/api-keys > Create new secret key (sk-...)" && python3 "$CLAUDE_PROJECT_DIR/_tools/gen-image.py" --check
```
Nói user: "Popup đã mở. Lấy key ở **platform.openai.com/api-keys** → **Create new secret key** (bắt đầu bằng `sk-`). Tài khoản cần nạp credit và xác minh tổ chức (Settings → Organization → Verify)."
`OK` → ✅, nhắc 1 lần: "Nên đặt giới hạn chi tiêu: **Settings → Limits**." `LỖI API 401` → key sai/đã thu hồi. `403`/`verify` → chưa xác minh tổ chức. `429`/`quota` → hết credit.

### 7b. TopView (khi `UGC_TOOL` hoặc `VIDEO_TOOL` = `topview`)

- `TOPVIEW_CONN=mcp`: nói user "Vào **claude.ai → Settings → Connectors → Add custom connector**, dán URL `https://mcp.topview.ai/mcp`, đăng nhập tài khoản TopView, rồi mở lại session." Kiểm: ToolSearch `topview` có tool → ✅.
- `TOPVIEW_CONN=api`: cần **2 popup** (API key + UID):
```bash
sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" TOPVIEW_API_KEY "TopView > avatar goc phai > API Settings > tab API > Key (chua co: Add Key)" && sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" TOPVIEW_UID "TopView > API Settings > tab API > Topview Uid"
```
  Nói user: "2 popup lần lượt hiện ra. Lấy ở **TopView → ảnh đại diện góc phải → API Settings → tab API**: dán **Key** vào popup 1, **Topview Uid** vào popup 2." Tài khoản cần gói có API + credit.

### 7c. Higgsfield (khi `UGC_TOOL` hoặc `VIDEO_TOOL` = `higgsfield`)

- `HIGGSFIELD_CONN=mcp`: nói user "Vào **claude.ai → Settings → Connectors → Add custom connector**, dán URL `https://mcp.higgsfield.ai/mcp`, đăng nhập tài khoản Higgsfield, rồi mở lại session." Kiểm: ToolSearch `higgsfield` có tool → ✅.
- `HIGGSFIELD_CONN=api`: cần **2 popup** (Key ID + Key Secret):
```bash
sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" HIGGSFIELD_API_KEY "Higgsfield Console > API keys > Key ID" && sh "$CLAUDE_PROJECT_DIR/_tools/set-key.sh" HIGGSFIELD_API_SECRET "Higgsfield Console > API keys > Key Secret (chi hien 1 lan)"
```
  Nói user: "2 popup lần lượt hiện ra. Tạo key ở **Higgsfield Console → API keys**: dán **Key ID** vào popup 1, **Key Secret** vào popup 2 (secret chỉ hiện 1 lần lúc tạo, nhớ copy ngay)."

Key chưa kiểm được bằng lệnh → kiểm ở lần gen đầu tiên; lỗi 401/403 → nhập lại qua popup.

## 8. Google Flow (khi `UGC_TOOL` hoặc `VIDEO_TOOL` = `flow` — chỉ để test)

Cần tài khoản Google truy cập được **Google Flow** (labs.google/flow) với Veo 3.1. Claude chỉ viết thẻ, user tự render. Không cài gì.

## 9. Kết thúc

Chạy lại bước 0. Báo đúng 3 dòng:
```
✅ Máy đã sẵn sàng (Mac/Windows).
🧰 Công cụ: UGC [..] · video [..] · ảnh [..] · giọng [..] · nhạc [..] (kết nối: MCP/API)
▶️ Bắt đầu video: gửi **brief** (dán / kéo file vào chat) hoặc **link sản phẩm** để Claude gợi ý brief
```
Còn thiếu mục tuỳ chọn → thêm 1 dòng: thiếu gì, dùng khi nào. Lỗi lạ → bảng "Lỗi hay gặp" trong `_workflows/setup-guide.md`.

Rồi **hỏi luôn brief** (AskUserQuestion) và đi thẳng vào Bước 0 của `_workflows/brief-intake.md`: "Bắt đầu video đầu tiên? Bạn đã có brief chưa?" — Có, gửi brief · Chưa, gửi link sản phẩm để gợi ý · Để sau. Chọn "Để sau" → dừng.
