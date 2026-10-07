# 🎬 Video AI Skill Agent

Hệ thống Agent AI tự động hóa quy trình sáng tạo Video Ads & Content (Meta Ads DTC, TikTok, Reels) với quy trình 3 cổng chuẩn hóa:
- **Kế hoạch**: Brief, Script, Storyboard, Prompt Packs.
- **Tài nguyên**: Gen ảnh (GPT Image / Nano Banana), Gen giọng đọc (ElevenLabs), Video + UGC qua TopView / Higgsfield (MCP hoặc API; Google Flow để test). Công cụ từng việc chọn ở bước "set up dự án".
- **Dựng hoàn thiện**: Remotion pipeline, b-roll sync theo timeline thoại và QC chuẩn Meta Ads.

---

## 🚀 Hướng dẫn cài đặt nhanh (Quick Start)

Xem chi tiết từng bước cài đặt tại: 📖 **[SETUP.md](./SETUP.md)**

```bash
# 1. Clone repository
git clone https://github.com/Pquisjrusyer/Video_AI-Skill_agent.git
cd Video_AI-Skill_agent

# 2. Cài đặt thư viện Python
pip install -r requirements.txt

# 3. Tạo file cấu hình API Key
cp .env.example .env    # Hoặc copy .env.example .env trên Windows
```

---

## 📚 Tài liệu dự án (Documentation)

- 🛠️ **[SETUP.md](./SETUP.md)**: Hướng dẫn cài đặt môi trường, packages (Python, Node.js, Remotion, FFmpeg).
- 📖 **[HUONG-DAN-SU-DUNG.md](./HUONG-DAN-SU-DUNG.md)**: Hướng dẫn quy trình làm video 3 cổng dành cho người dùng.
- ⚙️ **[CLAUDE.md](./CLAUDE.md)**: Quy chuẩn kỹ thuật, định tuyến kỹ năng (skills), format video và quy tắc bảo mật.
- 📂 **`_workflows/`**: Chi tiết quy trình UGC, Voiceover, Motion Graphic, Product Demo.
- 📂 **`_skills/`**: Kỹ năng agent cho hình ảnh, video, audio và motion graphic.

---

## 📁 Cấu trúc thư mục

```text
├── _brand/             # Brand kits, visual guidelines & briefs
├── _products/          # Thông tin SKU, claim APPROVED, visual identity
├── _characters/        # Profile nhân vật & reference images
├── _assets/            # B-roll library, stock keywords & footage
├── _skills/            # AI Agent skills (image, video, audio, scene-routing)
├── _workflows/         # Các quy trình sản xuất video chi tiết
├── _tools/             # Scripts tự động (gen-image.py, fetch-stock, post-edit)
├── campaigns/          # Các chiến dịch video theo tháng / SKU
├── SETUP.md            # Hướng dẫn setup máy mới & cài pack
├── requirements.txt    # Danh sách thư viện Python
└── CLAUDE.md           # Master prompt & system configuration
```
