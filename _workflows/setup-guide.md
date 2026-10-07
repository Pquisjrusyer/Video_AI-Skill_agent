# Setup máy mới

## Phần 1 — Cho người mới (làm 1 lần, ~15 phút)

> Máy Mac. Không cần biết code. Ảnh GPT Image do Claude gen qua API (cần 1 key OpenAI, bước 3). Video gen trên web.

### Bước 1 — Mở được folder project
1. Cài **Google Drive for desktop** (drive.google.com/download), đăng nhập email công ty.
2. Nhờ owner (Tịnh) share Shared drive **VIDEO AI (V2)**.
3. Trong Finder → Google Drive → Shared drives → chuột phải **VIDEO AI (V2)** → **Available offline** (để Claude đọc/ghi file nhanh, không lỗi khi mất mạng).

### Bước 2 — Cài Claude
1. Cài **Claude desktop** (claude.ai/download), đăng nhập.
2. Mở tab **Code** → chọn folder `VIDEO AI (V2)` vừa ở bước 1.
3. Lần đầu mở, Claude tự kiểm tra máy và báo còn thiếu gì.

### Bước 3 — Nói với Claude: **"set up dự án"**
Claude tự kiểm tra và cài Python, Node.js, faster-whisper, xin key OpenAI, rồi hướng dẫn bật connector ElevenLabs. Bạn chỉ cần:
- Bấm **Install / Continue** khi máy hiện hộp thoại cài, nhập mật khẩu máy khi được hỏi.
- Thoát hẳn Claude (Cmd+Q) rồi mở lại khi Claude dặn.
- Tạo key OpenAI tại **platform.openai.com/api-keys** (tài khoản đã nạp credit + xác minh tổ chức). Khi Claude mở hộp thoại **"AI Video — nhập key"** → dán key → OK. Đổi key sau này: nói **"đổi key OpenAI"**. Nên đặt giới hạn chi tiêu: platform.openai.com → **Settings → Limits** (budget tháng + email cảnh báo), **Billing** nạp trả trước, tắt auto-recharge.
- Bật connector ElevenLabs trong claude.ai → Settings → Connectors, đăng nhập tài khoản team (⚠️ **không dán key/mật khẩu vào chat**).

### Bước 4 — Tài khoản web để gen ảnh/video (không cần cài)
| Việc | Web |
|---|---|
| Ảnh Nano Banana | gemini.google.com |
| Ảnh GPT Image | Claude tự gen (key bước 3). Không có key → chatgpt.com |
| Video Veo 3.1 | labs.google/flow |
| Video UGC avatar | topview.ai |
| Nhạc / SFX | Thư viện nhạc bạn quen dùng (ghi nguồn khi thả file vào) |

### Bước 5 — Kiểm tra
Mở session mới trong Claude. Claude không báo gì về setup = đủ. Hoặc nói lại **"set up dự án"** để kiểm tra.
Bắt đầu làm: đọc `HUONG-DAN-SU-DUNG.md`, rồi nói với Claude kiểu *"làm video 15s cho sản phẩm X, link …"*.

---

## Phần 2 — Cho Claude

> Hook `SessionStart` (`.claude/settings.json` → `_tools/setup-check.sh`) chạy mỗi khi mở session: đủ thì im lặng, thiếu thì báo. Nhắc user 1 lần: nói "set up dự án" → chạy skill `.claude/skills/setup/`. Rồi làm tiếp task — chỉ chặn ở bước thật sự cần thứ bị thiếu.
> **Không bao giờ** yêu cầu user dán key vào chat, không `cat` file key. Kiểm tra lại: `sh _tools/setup-check.sh` (chỉ in tên key).

| Thiếu | Cần cho | Claude làm |
|---|---|---|
| Node.js / npx | Cổng 3 — dựng Remotion | Skill setup bước 3. Remotion không cài trước — tự `npm install` trong thư mục tạm (`remotion-setup.md`). ffmpeg đi kèm: `npx remotion ffmpeg`. |
| faster-whisper | Cổng 3 — transcript word-level | Skill setup bước 4 |
| `OPENAI_API_KEY` | Cổng 2 — gen ảnh GPT Image (`_tools/gen-image.py`) | Skill setup bước 6 (`set-key.sh` → hộp thoại ẩn). Thiếu → thẻ tự gen. |
| Connector ElevenLabs | Cổng 2 — gen VO | Skill setup bước 5. Không có → thẻ tự gen VO. |
| `PEXELS_API_KEY` / `PIXABAY_API_KEY` | Tuỳ chọn — `_tools/fetch-stock-broll.py` | Key miễn phí pexels.com/api, pixabay.com/api → `sh _tools/set-key.sh PEXELS_API_KEY`. Hook không kiểm. |
| File `.env` trong folder project | — | Nguy hiểm (share qua Drive): chuyển key sang `~/.config/ai-studio/.env`, xoá file trong project. |

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| ElevenLabs hết credit / connector lỗi | Hết ký tự trong gói / chưa đăng nhập | Nạp thêm, đăng nhập lại connector, hoặc thẻ tự gen VO |
| Không tải được file VO từ `storage.googleapis.com` | Mạng chặn egress (một số môi trường cloud) hoặc link hết hạn (2 giờ) | Lấy link mới qua `creative_get_flow_run_status`; vẫn lỗi → user tải tay, thả vào `outputs/audio/` |
| Gen ảnh `LỖI API 401` / `403` / `429` | Key sai hoặc bị thu hồi / chưa xác minh tổ chức / hết credit | 401 → "đổi key OpenAI". 403 → platform.openai.com → Settings → Organization → Verify. 429 → nạp Billing |
| `npx: command not found` | Chưa cài Node / chưa mở lại app | Nói "set up dự án", Cmd+Q rồi mở lại |
| File trong Drive mở chậm / lỗi đọc | Folder chưa bật offline | Bước 1.3 |
| `Operation not permitted` khi xoá `node_modules` | `npm install` chạy trong folder Drive | Chỉ build Remotion trong `/tmp/…` (`remotion-setup.md`) |
