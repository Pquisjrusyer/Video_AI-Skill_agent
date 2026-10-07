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

2. Kiểm tra máy đã có FFmpeg chưa (dùng để xem/cắt khung clip khi kiểm video):
   ```bash
   ffmpeg -version
   ```
   *Nếu báo không tìm thấy lệnh, cài rồi mở lại terminal:*
   - Windows: `winget install Gyan.FFmpeg`
   - Mac: `brew install ffmpeg`

   > Không chạy `npx remotion ffmpeg` ở thư mục gốc — lệnh này chỉ chạy được **bên trong** một dự án Remotion đã `npm install` (bước 3), ở ngoài sẽ báo lỗi `could not determine executable to run`.

3. Khi làm việc với một campaign cụ thể (ví dụ chạy thử render Remotion):
   ```bash
   cd campaigns/2026-10_glass-skin-duo-ugc-60s/remotion-project
   npm install
   ```

---

### Bước 4: Chọn công cụ + nhập API key (Claude làm giúp)

Mở dự án trong Claude, nói: **"set up dự án"**. Claude sẽ:
1. Hỏi bạn chọn công cụ cho từng việc (bấm chọn, có gợi ý sẵn): video UGC, video cảnh (TopView / Higgsfield / Google Flow để test), ảnh, giọng đọc, nhạc.
2. Với TopView / Higgsfield: hỏi kết nối bằng **MCP** (chỉ đăng nhập tài khoản, không cần key) hay **API key**.
3. Cần key nào thì **mở popup** để bạn dán key vào. Popup có ghi sẵn chỗ lấy key. Key được lưu ở:
   - Windows: `C:\Users\<tên máy>\.config\ai-studio\.env`
   - Mac: `~/.config/ai-studio/.env`

   **Nằm ngoài thư mục dự án** nên không bị lộ khi share qua Drive / git.

Đổi hoặc thêm key sau này: nói **"đổi key OpenAI"**, **"nhập key TopView"**… hoặc tự chạy:
```bash
sh _tools/set-key.sh OPENAI_API_KEY
```

> ⚠️ **Không tạo file `.env` trong thư mục dự án và không dán key vào chat.** Các tool của dự án không đọc file `.env` trong thư mục dự án, nên key để ở đó sẽ không được dùng, lại dễ bị lộ. `.env.example` chỉ để tham khảo tên các key.

---

### Bước 5: Connector (nếu đã chọn ở Bước 4)
Claude sẽ nhắc đúng connector cần bật. Cách bật chung: **claude.ai → Settings → Connectors**:
- **ElevenLabs** (giọng đọc / nhạc): bật connector, đăng nhập tài khoản team.
- **TopView** / **Higgsfield** qua MCP: **Add custom connector** → dán URL `https://mcp.topview.ai/mcp` hoặc `https://mcp.higgsfield.ai/mcp` → đăng nhập.

Bật xong thì mở lại session.

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
