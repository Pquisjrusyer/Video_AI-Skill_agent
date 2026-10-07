# Hướng dẫn sử dụng — AI Video Project

> Dành cho người dùng (không cần biết code). Không có lệnh phải nhớ, cứ **nói bằng lời thường** với Claude.
> Claude lo phần viết: script, storyboard, prompt, **gen ảnh**, QC, dựng video. **Bạn** lo render video trên web và duyệt.

---

## 0. Lần đầu dùng trên máy mới (1 lần, ~15 phút)

1. Cài **Google Drive for desktop**, xin quyền Shared drive **VIDEO AI (V2)**, chuột phải folder → **Available offline**.
2. Cài **Claude desktop** → tab **Code** → chọn folder `VIDEO AI (V2)`.
3. Nói: **"set up dự án"** → Claude **hỏi bạn chọn công cụ** cho từng việc (ảnh, video, UGC, giọng đọc, nhạc — có gợi ý sẵn), rồi tự cài đúng thứ cần trên Mac hoặc Windows và mở hộp thoại để bạn dán key (nếu cần). Bạn chỉ bấm Install/Yes, nhập mật khẩu máy khi được hỏi.
4. Nếu chọn ElevenLabs: bật connector **ElevenLabs** (claude.ai → Settings → Connectors). Đổi công cụ sau này: nói **"đổi công cụ"**.

Chi tiết + lỗi hay gặp: `_workflows/setup-guide.md`.

---

## 1. Quy trình làm 1 video — 3 cổng

```
Bạn: "làm video 15s cho sản phẩm X, link …"
  │
  ▼
CỔNG 1 — KẾ HOẠCH ─────────────────────────────────────────
  Claude: hỏi bạn có brief chưa (có → gửi để Claude bám theo · chưa → Claude gợi ý 2–3 brief từ link sản phẩm)
          → chốt format → brief → script → storyboard CÓ ẢNH minh hoạ từng cảnh
          (prompt kèm dịch tiếng Việt) → thẻ prompt ảnh
  Bạn:    xem storyboard (hiện thẳng trong chat), góp ý theo cảnh → "ok cổng 1"
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
| Gen ảnh (GPT Image) | **Claude** (nếu chọn ở setup): ảnh minh hoạ storyboard ở cổng 1, ảnh thật ở cổng 2. Đổi key: "đổi key OpenAI" |
| Sửa tay ảnh Claude đã note | **Bạn** (chatgpt.com / Photoshop / Canva) → thả lại `outputs/images/` đúng tên |
| Gen ảnh Nano Banana (Gemini) · render video trên Google Flow khi test (TopView / Higgsfield thì Claude gen qua MCP/API) · chọn nhạc, SFX | **Bạn**, theo thẻ Claude viết |
| Gen giọng đọc (VO) | **Claude**, theo công cụ đã chọn: connector ElevenLabs hoặc OpenAI TTS |
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
| Đổi công cụ (ảnh / video / UGC / giọng / nhạc) | "đổi công cụ" |

---

## 4. File nằm ở đâu

```
campaigns/[YYYY-MM]_[tên]/
├── status.md          ← MỞ FILE NÀY để biết đang ở cổng nào, ai làm tiếp
├── brief.md · scripts/script.md · scripts/storyboard.html (storyboard có ảnh) + .md
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
- Brand nào thì chỉ dùng context brand đó (`_brand/`). Claim chỉ lấy từ danh sách APPROVED trong `_products/<brand>/<sku>/product-brief.md`.
- **Không dán API key / mật khẩu vào chat.**
- Trước khi upload Meta: bật **AI disclosure**, kiểm lip sync (xem 1.5x), logo/màu/chữ trên bao bì đúng, file lấy từ `outputs/final/`.
