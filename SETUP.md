# 🚀 Hướng Dẫn Setup Dự Án (Project Setup Guide)

Tài liệu này hướng dẫn chi tiết cách cài đặt môi trường và các gói phụ thuộc (packages) sau khi clone source code dự án **Video AI Skill Agent** về máy mới.

---

## 📋 1. Yêu cầu hệ thống (Prerequisites)

| Công cụ | Phiên bản tối thiểu | Mục đích |
|---|---|---|
| **Python** | 3.10+ | Chạy các script tự động (`_tools/`), transcript audio |
| **Node.js & npm** | 18+ LTS | Dựng và render video Remotion |
| **Git** | 2.x+ | Quản lý mã nguồn |
| **Trợ lý AI** | Claude / Antigravity | Tự động hóa quy trình sản xuất video |

---

## 🛠️ 2. Các bước cài đặt sau khi Clone (Step-by-Step)

### Bước 1: Clone Repository
```bash
git clone https://github.com/Pquisjrusyer/Video_AI-Skill_agent.git
cd Video_AI-Skill_agent
```

---

### Bước 2: Cài đặt thư viện Python
Dự án cần thư viện `faster-whisper` để phục vụ bóc băng transcript, căn chỉnh khớp âm thanh (voiceover) và b-roll:

#### Trên Windows (PowerShell / Command Prompt):
```powershell
pip install -r requirements.txt
```
*(Hoặc: `pip install faster-whisper`)*

#### Trên macOS / Linux:
```bash
python3 -m pip install -r requirements.txt
```

---

### Bước 3: Cài đặt Node.js & Remotion
1. Kiểm tra máy đã cài đặt Node.js và npm chưa:
   ```bash
   node -v
   npm -v
   ```
   *Nếu chưa có, tải và cài đặt bản LTS tại: [https://nodejs.org](https://nodejs.org)*

2. Cài đặt FFmpeg tích hợp của Remotion (chạy 1 lần):
   ```bash
   npx remotion ffmpeg
   ```

3. Khi làm việc với một campaign cụ thể (ví dụ chạy thử render Remotion):
   ```bash
   cd campaigns/2026-10_glass-skin-duo-ugc-60s/remotion-project
   npm install
   ```

---

### Bước 4: Thiết lập file môi trường `.env` (API Keys)
Dự án đã có sẵn template mẫu [.env.example](file:///.env.example). Tạo một file `.env` ở thư mục gốc của dự án:

```bash
# Trên Windows PowerShell
Copy-Item .env.example .env

# Trên macOS / Linux
cp .env.example .env
```

Mở file `.env` và điền các API key cần thiết:
```env
# Dùng để Claude / Antigravity tự động gen ảnh (GPT Image) qua _tools/gen-image.py
OPENAI_API_KEY=sk-...

# Key tải stock B-roll miễn phí (tùy chọn)
PEXELS_API_KEY=
PIXABAY_API_KEY=
```

> ⚠️ **Lưu ý bảo mật**: File `.env` đã được cấu hình trong `.gitignore`, tuyệt đối không commit file chứa API key lên GitHub.

---

### Bước 5: Cấu hình Connector ElevenLabs (Tạo giọng đọc AI)
Nếu dùng Claude Desktop / Antigravity IDE:
1. Vào **Settings → Connectors** (hoặc tích hợp tool MCP).
2. Bật connector **ElevenLabs** và đăng nhập tài khoản của team.
3. Nếu không dùng connector, bạn vẫn có thể gen giọng đọc thủ công trực tiếp trên web [elevenlabs.io](https://elevenlabs.io) theo kịch bản trong `prompts-used/audio-plan.md`.

---

## 🧪 3. Kiểm tra môi trường (Verification)

Chạy lệnh kiểm tra nhanh để xác nhận máy đã sẵn sàng:

### Trên Windows:
```powershell
python -c "import faster_whisper; print('✅ Python & faster-whisper: OK')"
node -v
npm -v
```

### Trên macOS / Linux:
```bash
python3 -c "import faster_whisper; print('✅ Python & faster-whisper: OK')"
node -v
npm -v
```

---

## 🤖 4. Làm việc với AI Agent (Antigravity / Claude)

Sau khi mở folder dự án trong Antigravity hoặc Claude:
- Chỉ cần gõ: **`"set up dự án"`** hoặc **`"kiểm tra setup"`**, trợ lý AI sẽ tự động kích hoạt skill setup để kiểm tra toàn bộ môi trường.
- Bắt đầu tạo video mới bằng cách gửi yêu cầu: *"Làm video 15s cho sản phẩm [Tên sản phẩm], link: ..."*
- Chi tiết quy trình 3 cổng xem tại: [HUONG-DAN-SU-DUNG.md](file:///HUONG-DAN-SU-DUNG.md) và [CLAUDE.md](file:///CLAUDE.md).
