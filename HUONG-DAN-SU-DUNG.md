# Hướng dẫn sử dụng — AI Video Project

> Dành cho người dùng (không cần biết code). Không có lệnh phải nhớ, cứ **nói bằng lời thường** với Claude.
> Claude lo phần viết: script, storyboard, prompt, **gen ảnh**, QC, dựng video. **Bạn** lo render video trên web và duyệt.

---

## 0. Lần đầu dùng trên máy mới (1 lần, ~15 phút)

1. Cài **Google Drive for desktop**, xin quyền Shared drive **VIDEO AI (V2)**, chuột phải folder → **Available offline**.
2. Cài **Claude desktop** → tab **Code** → chọn folder `VIDEO AI (V2)`.
3. Nói: **"set up dự án"** → Claude tự cài Python, Node.js, faster-whisper và mở hộp thoại để bạn dán **key OpenAI** (gen ảnh). Bạn chỉ bấm Install/Continue, nhập mật khẩu máy khi được hỏi.
4. Bật connector **ElevenLabs** (claude.ai → Settings → Connectors) để Claude gen giọng đọc.

Chi tiết + lỗi hay gặp: `_workflows/setup-guide.md`.

---

## 1. Quy trình làm 1 video — 3 cổng

```
Bạn: "làm video 15s cho sản phẩm X, link …"
  │
  ▼
CỔNG 1 — KẾ HOẠCH ─────────────────────────────────────────
  Claude: hỏi chốt format (1 câu) → brief → script → storyboard → thẻ prompt ảnh
  Bạn:    đọc, góp ý → "ok cổng 1"   (chưa gen ảnh, sửa kế hoạch không tốn tiền)
  │
  ▼
CỔNG 2 — ẢNH ──────────────────────────────────────────────
  Claude: báo danh sách ảnh → bạn OK → gen ảnh + QC (mỗi ảnh 1 gen + 1 sửa;
          vẫn lỗi → note để bạn sửa tay) → thẻ video → bảng âm thanh → gen giọng đọc → bộ bàn giao
  Bạn:    tải file giọng đọc về outputs/audio/ → "ok cổng 2"
          render video theo bộ bàn giao → outputs/videos/
          chọn nhạc + SFX → outputs/audio/ → "clip xong rồi"
  │
  ▼
CỔNG 3 — FINAL ────────────────────────────────────────────
  Claude: kiểm file → dựng video (Remotion) → bản review
  Bạn:    xem, góp ý → Claude sửa → "ok cổng 3"
          upload từ outputs/final/ lên Meta
```

**Trong mỗi cổng Claude làm liền một mạch**, chỉ dừng ở cuối để bạn duyệt.
Muốn xem giữa chừng → dặn trước: *"dừng cho mình xem script trước"*.

---

## 2. Ai làm gì

| Việc | Ai |
|---|---|
| Brief, script, storyboard, prompt ảnh/video, bảng âm thanh | Claude |
| Gen ảnh (GPT Image) | **Claude**, ở cổng 2 (cần key OpenAI — nói "set up dự án"; đổi key: "đổi key OpenAI") |
| Sửa tay ảnh Claude đã note | **Bạn** (chatgpt.com / Photoshop / Canva) → thả lại `outputs/images/` đúng tên |
| Gen ảnh Nano Banana (Gemini) · render video (Flow/Veo, TopView) · chọn nhạc, SFX | **Bạn**, theo thẻ Claude viết |
| Gen giọng đọc (VO) | Claude qua connector ElevenLabs → **bạn tải file về** |
| QC ảnh/clip, dựng video, xuất final | Claude |
| Duyệt cuối mỗi cổng | Người phụ trách (Account / Creative lead) |

---

## 3. Câu nói hay dùng

| Muốn | Nói |
|---|---|
| Bắt đầu video mới | "làm video 15s cho sản phẩm X, link …" / "đây là script, làm video giúp mình" |
| Xem đang tới đâu | "campaign X đang ở bước nào?" |
| Duyệt | "ok cổng 1" · "ok cổng 2" · "ok cổng 3" |
| Sửa | "sửa hook ngắn lại" · "ảnh B-02 lỗi tay, viết lại prompt" |
| Báo đã gen xong | "ảnh xong rồi" · "clip xong rồi" |
| Dừng giữa chừng | "dừng cho mình xem storyboard" |
| Kiểm tra máy | "set up dự án" |

---

## 4. File nằm ở đâu

```
campaigns/[YYYY-MM]_[tên]/
├── status.md          ← MỞ FILE NÀY để biết đang ở cổng nào, ai làm tiếp
├── brief.md · scripts/script.md · scripts/storyboard.md
├── prompts-used/      ← thẻ prompt ảnh/video, bảng âm thanh, bộ bàn giao (handoff.md)
└── outputs/
    ├── images/  ← bạn thả ảnh vào đây
    ├── videos/  ← bạn thả clip vào đây
    ├── audio/   ← giọng đọc, nhạc, SFX
    ├── review/  ← bản dựng để xem
    └── final/   ← CHỈ upload Meta từ đây
```

**Đặt tên file đúng như trong thẻ prompt** (Claude ghi sẵn), VD `KOLOR-2026-10-BLOOM_B-01_S01-dot_v1.png`. Sai tên → Claude không nhận ra file.
Gen lại → tăng số: `_v2`, `_v3`.

---

## 5. Mẹo tiết kiệm token

- **Xong 1 cổng → mở session mới.** Claude đọc `status.md` là biết làm tiếp, không cần chat cũ. Chat càng dài càng tốn.
- **Góp ý gom 1 lần**, không nhắn từng ý lẻ.
- **1 session = 1 campaign.** Không làm 2 video trong cùng 1 chat.
- Nhờ việc nhỏ ngoài lề (hỏi đáp, tra cứu) → mở session riêng.

---

## 6. Quy tắc cần nhớ

- **1 script = 1 campaign** (1 folder riêng). Dùng lại nhân vật / ảnh seed giữa các campaign thoải mái.
- Brand nào thì chỉ dùng context brand đó (`_brand/`). Claim chỉ lấy từ danh sách APPROVED trong `_products/[sp]/product-brief.md`.
- **Không dán API key / mật khẩu vào chat.**
- Trước khi upload Meta: bật **AI disclosure**, kiểm lip sync (xem 1.5x), logo/màu/chữ trên bao bì đúng, file lấy từ `outputs/final/`.
