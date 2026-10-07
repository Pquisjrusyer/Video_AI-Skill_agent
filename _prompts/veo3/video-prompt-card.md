# Video Prompt Card — chuẩn thẻ prompt video (lượt 4C)

> Dùng ở `/assets` lượt 4C, **chỉ sau khi ảnh đầu vào đã duyệt ở 4B** — prompt viết theo ảnh THẬT, không theo ảnh dự kiến.
> Syntax Veo: `_skills/video/references/veo.md` (§7 image-to-video). Rule chung: `universal-rules.md` (U1–U12). Thẻ này là khung nội dung bắt buộc; PROMPT gom lại thành văn xuôi tiếng Anh 50–200 từ.

```
### [SCENE ID] · [tên file clip]
Tool + cấu hình:   Veo 3.1 · image-to-video · 9:16 · 1080p
Render:            [4 / 6 / 8]s          Dùng trong bản dựng: [VD: 0.5–4.0s = 3.5s]
Lưu về:            outputs/videos/[campaign-code]_[scene-id]_[mô-tả-ngắn]_v[n].mp4   (VD: 2026-06-LAUNCH_S01_mirror_v1.mp4)

INPUT IMAGE ROLES
- First frame = [file ảnh đã duyệt]
- Last frame  = [file — chỉ khi tool hỗ trợ VÀ thật sự cần; KHÔNG dùng ảnh trạng thái trung gian làm khung cuối]
- Reference   = [chỉ khi tool hỗ trợ reference ingredients]

STARTING FRAME
Trạng thái ban đầu khớp ảnh đầu vào (ai ở đâu, tay ở đâu, sản phẩm ở đâu).
Ảnh đã ở giữa hành động → TIẾP TỤC từ đó, không lặp hành động từ đầu.

ACTION AND TIMING
0.0–1.5s: ...
1.5–4.0s: ...
(1 hành động chính. Hành động phức tạp → tách cảnh ở storyboard, không nhồi.)

CAMERA
Một chuyển động chính HOẶC static. Lens bằng lời (50mm / 100mm macro).

CONTINUITY
Identity · hình dáng + label sản phẩm ("Do not alter product color, label, or packaging shape.") · hướng + nhiệt màu ánh sáng khớp cảnh liền kề · vật lý: tiếp xúc tay–da, trọng lực, chất lỏng, phản chiếu gương.
Hiệu ứng (dải sáng lướt, lens flare…): vị trí · hướng · thời điểm · cường độ — VD "a soft warm light band sweeps left-to-right across her cheek from 2.0s to 3.0s, subtle intensity".

ENDING FRAME
Trạng thái cuối chính xác: còn gì / không còn gì trong khung; giữ yên [x]s để nối cảnh.

AUDIO CUES
Theo bảng âm thanh đã chốt. Ghi rõ: âm TẠO CÙNG CLIP vs âm THÊM KHI DỰNG.
Mặc định project: VO + nhạc + SFX đều thêm khi dựng → clip ghi "No dialogue, no music, no sound effects; quiet natural ambience only" (hoặc mute khi dựng). Không tự thêm lời/nhạc ngoài nội dung đã chốt.

AVOID
Lỗi hình + chuyển động cụ thể cho cảnh này (mặt trôi, tay nhân đôi trong gương, label nhoè, chất lỏng bay ngược...).

PROMPT  (copy nguyên văn)
...

QC: ☐ khớp first frame ☐ hành động đúng timing ☐ ending frame đúng ☐ sản phẩm không biến dạng ☐ audio đúng quy ước
Lỗi hay gặp → sửa: ...
```

## Quy tắc
- **Mặc định mỗi cảnh render riêng.** Chỉ gộp nhiều cảnh vào 1 clip khi user yêu cầu và phương án khả thi.
- Phân biệt **thời lượng render** (4/6/8s của Veo) với **thời lượng dùng** (cắt theo VO thật ở `/edit`).
- Không render tại đây — chỉ bàn giao thẻ.
