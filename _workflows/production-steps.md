# Quy trình sản xuất — 3 cổng

> Trạng thái campaign: `campaigns/[campaign]/status.md` (dòng **Tiếp theo** = việc kế + ai làm).
> Không có slash command — nói bằng lời thường ("làm video cho sp X", "ảnh xong rồi", "clip đã thả vào"). Claude tự biết đang ở bước nào nhờ `status.md`.
> Chi tiết theo format: `voiceover-video-workflow.md`, `ugc-workflow.md`, `product-demo-workflow.md`, `static-video-combo-workflow.md`, `motion-graphic-workflow.md`.

---

## 3 cổng

| Cổng | Claude làm (chạy liền, không dừng giữa chừng) | Người dùng duyệt / làm | File |
|---|---|---|---|
| **1. Kế hoạch** | Hỏi chốt format (1 câu, kèm recommend) → brief → script (đếm từ, đối chiếu claim APPROVED) → storyboard + route scene + danh sách asset → **thẻ prompt ảnh** | Duyệt cả gói 1 lần. Sửa chỗ nào nói chỗ đó. Chưa gen ảnh | `brief.md` · `scripts/script.md` · `scripts/storyboard.md` · `prompts-used/prompt-pack.md` |
| **2. Ảnh** | Báo danh sách ảnh → gen GPT Image theo đợt phụ thuộc → QC (lỗi → sửa 1 lần, vẫn lỗi → note user tự sửa tay) → khi ảnh pass: thẻ video theo ảnh thật → bảng âm thanh → gen VO → bộ bàn giao | OK danh sách ảnh. Sửa tay ảnh bị note (nếu có). Duyệt ảnh + bộ bàn giao. Render video, chọn nhạc/SFX → thả vào `outputs/` | `prompt-pack.md` · `audio-plan.md` · `handoff.md` |
| **3. Final** | Kiểm file (tên, duration, khung đầu/cuối) → dựng Remotion → bản review → sửa theo góp ý → final + compliance | Xem review, góp ý, duyệt final | `outputs/review/` · `outputs/final/` |

**Duyệt:** "ok cổng 1/2/3" → Claude ghi ✅ + tên người duyệt vào `status.md`.
**Muốn dừng giữa chừng:** nói trước, VD "dừng cho mình xem script" → Claude dừng đúng chỗ đó. Không nói → chạy liền.
**Cổng trước chưa ✅ → không làm việc của cổng sau.** Ngoại lệ duy nhất: user yêu cầu rõ.

### Không đổi
- Ảnh: Claude gen GPT Image ở đầu cổng 2 (`_skills/image/SKILL.md` → Gen GPT Image), tối đa 1 gen + 1 sửa/ảnh. Video, SFX, ảnh Nano Banana: **người dùng tự gen/chọn** theo thẻ. VO + nhạc nền: Claude gen qua connector ElevenLabs (MCP); user tải file về.
- Không viết prompt video trước khi có ảnh thật đã pass. Mỗi scene = 1 clip render riêng.
- Lỗi thuộc chặng trước (VD script dài lúc dựng) → sửa ở file của chặng đó, ghi 1 dòng vào `status.md` mục Vấn đề.
- 1 campaign = 1 script. Không báo giá.

---

## Quy đổi tên cổng cũ

Các file trong `_workflows/`, `_skills/`, `_prompts/` còn ghi tên cổng cũ. Đọc theo bảng này — **tên cũ chỉ là tên bước bên trong, không phải điểm dừng**:

| Tên cũ | Thuộc cổng mới | Dừng chờ duyệt? |
|---|---|---|
| A (brief) · B (script) · C (storyboard) · 4A (thẻ ảnh — chỉ viết, chưa gen) | 1 | Chỉ dừng ở cuối, sau thẻ ảnh |
| gen ảnh · 4B (QC ảnh) · 4C (thẻ video) · 4D (âm thanh + gen VO) · 4E (bàn giao) | 2 | Chỉ dừng ở cuối, sau bộ bàn giao |
| D (kiểm asset) · E (final) | 3 | Dừng ở bản review + final |
| `/start` `/brief` `/script` `/storyboard` | việc của cổng 1 | — |
| `/assets` | cuối cổng 1 + cổng 2 | — |
| `/check` `/edit` | cổng 3 | — |

---

## Tiết kiệm token — Claude làm theo

1. **1 cổng ≈ 1 session.** Xong cổng → user mở session mới. `status.md` giữ trạng thái, không cần chat cũ. Session dài là nguồn tốn token lớn nhất.
2. **Đọc đúng file cần, không đọc cả chuỗi.** Xem bảng "Đọc gì khi nào" trong `CLAUDE.md`. Đã đọc trong session → không đọc lại.
3. **File lớn → grep, không đọc hết.** `ugc-workflow.md`, `_assets/broll-library/index.md` (dò `keywords.json` trước), product-brief cũ.
4. **Xem ảnh bản thu nhỏ:** `sips -Z 768 in.png --out outputs/review/_qc/in.jpg` rồi mới Read. Chỉ xem bản gốc khi cần soi chữ label.
5. **Xem clip bằng 3 khung** (đầu/giữa/cuối, rộng 480px) qua `npx remotion ffmpeg`, không trích nhiều khung.
6. **Không chép lại nội dung** của file trước sang file sau — dẫn chiếu (`xem script.md §S02`).
7. **Gửi file vào chat 1 lần ở cuối cổng**, không gửi mỗi lần sửa nhỏ.
8. **Việc máy móc → lệnh bash** (đối tên file, đo duration), không suy luận từng file.
9. `status.md`: sửa đúng dòng thay đổi; mục Vấn đề mỗi ý 1 dòng.
