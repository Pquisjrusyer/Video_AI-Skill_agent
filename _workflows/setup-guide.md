# Setup máy mới

## Phần 1 — Cho người mới (làm 1 lần, ~15 phút)

> Máy Mac hoặc Windows. Không cần biết code. Ở bước 3, Claude hỏi bạn chọn công cụ cho từng việc (ảnh, video, UGC, giọng đọc, nhạc) rồi chỉ cài đúng thứ cần.

### Bước 1 — Mở được folder project
1. Cài **Google Drive for desktop** (drive.google.com/download), đăng nhập email công ty.
2. Nhờ owner (Tịnh) share Shared drive **VIDEO AI (V2)**.
3. Trong Finder (Mac) / File Explorer (Windows) → Google Drive → Shared drives → chuột phải **VIDEO AI (V2)** → **Available offline** (để Claude đọc/ghi file nhanh, không lỗi khi mất mạng).

### Bước 2 — Cài Claude
1. Cài **Claude desktop** (claude.ai/download), đăng nhập.
2. Mở tab **Code** → chọn folder `VIDEO AI (V2)` vừa ở bước 1.
3. Lần đầu mở, Claude tự kiểm tra máy và báo còn thiếu gì.

### Bước 3 — Nói với Claude: **"set up dự án"**
Claude hỏi bạn chọn công cụ (bấm chọn, có gợi ý sẵn), rồi tự kiểm tra và cài những gì cần: Python, Node.js, ffmpeg, faster-whisper, key OpenAI, connector ElevenLabs. Bạn chỉ cần:
- Bấm **Install / Continue / Yes** khi máy hiện hộp thoại cài, nhập mật khẩu máy khi được hỏi.
- Thoát hẳn Claude (Mac: Cmd+Q · Windows: thoát ở khay hệ thống) rồi mở lại khi Claude dặn.
- Đổi công cụ sau này: nói **"đổi công cụ"**.
- (Nếu chọn Claude gen ảnh hoặc giọng OpenAI) Tạo key OpenAI tại **platform.openai.com/api-keys** (tài khoản đã nạp credit + xác minh tổ chức). Khi Claude mở hộp thoại **"AI Video — nhập key"** → dán key → OK. Đổi key sau này: nói **"đổi key OpenAI"**. Nên đặt giới hạn chi tiêu: platform.openai.com → **Settings → Limits** (budget tháng + email cảnh báo), **Billing** nạp trả trước, tắt auto-recharge.
- (Nếu chọn ElevenLabs) Bật connector ElevenLabs trong claude.ai → Settings → Connectors, đăng nhập tài khoản team (⚠️ **không dán key/mật khẩu vào chat**).

### Bước 4 — Tài khoản web để gen ảnh/video (không cần cài)
| Việc | Web |
|---|---|
| Ảnh Nano Banana | gemini.google.com |
| Ảnh GPT Image | Claude tự gen (key bước 3). Không có key → chatgpt.com |
| Video b-roll / demo, UGC | **TopView** (topview.ai) / **Higgsfield** (higgsfield.ai) — Claude gọi qua MCP hoặc API key (popup ở bước 3) |
| Video khi test | **Google Flow** — labs.google/flow (bạn tự render) |
| Nhạc / SFX | Thư viện nhạc bạn quen dùng (ghi nguồn khi thả file vào) |

### Bước 5 — Kiểm tra
Mở session mới trong Claude. Claude không báo gì về setup = đủ. Hoặc nói lại **"set up dự án"** để kiểm tra.
Bắt đầu làm: đọc `HUONG-DAN-SU-DUNG.md`, rồi nói với Claude kiểu *"làm video 15s cho sản phẩm X, link …"*.

---

## Phần 2 — Cho Claude

> Hook `SessionStart` (`.claude/settings.json` → `_tools/setup-check.sh`) chạy mỗi khi mở session: báo công cụ user đã chọn (`~/.config/ai-studio/prefs.env`), thiếu gì thì liệt kê. Nhắc user 1 lần: nói "set up dự án" → chạy skill `.claude/skills/setup/`. Rồi làm tiếp task — chỉ chặn ở bước thật sự cần thứ bị thiếu.
> **Không bao giờ** yêu cầu user dán key vào chat, không `cat` file key. Kiểm tra lại: `sh _tools/setup-check.sh` (chỉ in tên key).

| Thiếu | Cần cho | Claude làm |
|---|---|---|
| Chưa chọn công cụ | Mọi cổng — biết ai làm việc gì | Skill setup bước 1 (`_tools/set-prefs.sh`) |
| Python 3 / lệnh `python3` | Gen ảnh, transcript | Skill setup bước 2. Windows thường chỉ có `python` → tạo alias `python3.exe` |
| Node.js / npx | Cổng 3 — dựng Remotion | Skill setup bước 3. Remotion không cài trước — tự `npm install` trong thư mục tạm (`remotion-setup.md`). |
| ffmpeg | Cổng 2–3 — xem/cắt khung clip, đo duration | Windows `winget install Gyan.FFmpeg` · Mac `brew install ffmpeg`, rồi mở lại terminal. Kiểm: `ffmpeg -version`. |
| faster-whisper | Cổng 3 — transcript word-level | Skill setup bước 5. Máy không GPU → `device="cpu", compute_type="int8"` |
| `TOPVIEW_API_KEY` + `TOPVIEW_UID` / `HIGGSFIELD_API_KEY` + `HIGGSFIELD_API_SECRET` | Cổng 2 — Claude gen video/UGC qua API (nếu chọn API thay vì MCP) | Skill setup bước 7b / 7c (popup). Chọn MCP thì không cần key |
| Key nhà cung cấp ảnh khác (`CLOUDFLARE_*`, `POLLINATIONS_KEY`, `HF_TOKEN`, `GEMINI_API_KEY`, `FAL_KEY`, `REPLICATE_API_TOKEN`) | Cổng 1–2 — gen ảnh khi chọn nhà đó / khi OpenAI lỗi | Popup `sh _tools/pick-provider.sh image` (cũng tự hiện khi gen lỗi). Miễn phí: Cloudflare (dash.cloudflare.com → API token quyền Workers AI + Account ID), Pollinations (enter.pollinations.ai/keys), Hugging Face (huggingface.co/settings/tokens) |
| `OPENAI_API_KEY` | Cổng 1–2 — gen ảnh GPT Image (`_tools/gen-image.py`), OpenAI TTS | Skill setup bước 7 (`set-key.sh` → hộp thoại ẩn). Thiếu → thẻ tự gen. |
| Connector ElevenLabs | Cổng 2 — gen VO / nhạc (nếu chọn) | Skill setup bước 6. Không có → hỏi đổi sang OpenAI TTS, hoặc thẻ tự gen. |
| `PEXELS_API_KEY` / `PIXABAY_API_KEY` | Tuỳ chọn — `_tools/fetch-stock-broll.py` | Key miễn phí pexels.com/api, pixabay.com/api → `sh _tools/set-key.sh PEXELS_API_KEY`. Hook không kiểm. |
| File `.env` trong folder project | — | Nguy hiểm (share qua Drive): chuyển key sang `~/.config/ai-studio/.env`, xoá file trong project. |

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| ElevenLabs hết credit / connector lỗi | Hết ký tự trong gói / chưa đăng nhập | Nạp thêm, đăng nhập lại connector, hoặc thẻ tự gen VO |
| Không tải được file VO từ `storage.googleapis.com` | Mạng chặn egress (một số môi trường cloud) hoặc link hết hạn (2 giờ) | Lấy link mới qua `creative_get_flow_run_status`; vẫn lỗi → user tải tay, thả vào `outputs/audio/` |
| Gen ảnh báo LỖI KEY / HẾT CREDIT / TIMEOUT | Key sai, hết credit, mạng chập chờn | Popup đổi nhà cung cấp tự hiện → chọn nhà khác (có nhà miễn phí) + dán key. Hoặc sửa gốc: OpenAI 401 → "đổi key OpenAI", 403 → Verify tổ chức, 429 `insufficient_quota` → nạp Billing. Lưu ý `--check` chỉ kiểm key, không kiểm còn credit |
| `npx: command not found` | Chưa cài Node / chưa mở lại app | Nói "set up dự án", thoát hẳn Claude rồi mở lại |
| `python3: command not found` (Windows) | Windows đặt tên lệnh là `python` | Skill setup bước 2 tạo `python3.exe` cạnh `python.exe` |
| Chữ tiếng Việt lỗi / `UnicodeEncodeError: 'charmap'` (Windows) | Console Windows mặc định cp1252 | Script trong `_tools/` đã tự đặt UTF-8. Script mới: thêm `sys.stdout.reconfigure(encoding="utf-8")` |
| faster-whisper lỗi `cublas64_12.dll` | Máy không có GPU NVIDIA | Gọi `WhisperModel(..., device="cpu", compute_type="int8")` |
| `winget` không có (Windows) | Windows cũ thiếu App Installer | Cài **App Installer** từ Microsoft Store, hoặc tải bộ cài từ python.org / nodejs.org |
| `npx remotion ffmpeg` → `could not determine executable to run` | Chạy ngoài dự án Remotion (chưa có `@remotion/cli`) | Không cần lệnh này: dùng `ffmpeg` cài sẵn (dòng ffmpeg ở bảng trên). Muốn dùng bản của Remotion → `cd` vào `remotion-project/`, `npm install` trước |
| File trong Drive mở chậm / lỗi đọc | Folder chưa bật offline | Bước 1.3 |
| `Operation not permitted` khi xoá `node_modules` | `npm install` chạy trong folder Drive | Chỉ build Remotion trong `/tmp/…` (`remotion-setup.md`) |
