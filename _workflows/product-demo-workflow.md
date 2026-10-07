# Ghi chú format — Product Demo / Lifestyle (không có người nói)

> Quy trình chạy bằng 6 lệnh chính (+ `/brief` tuỳ chọn) (`/start` → `/edit`, xem `production-steps.md`). File này chỉ ghi phần **riêng của format demo** — các lệnh `/storyboard`, `/assets`, `/edit` đọc khi campaign là demo.

## Khi nào chọn format này
| Chọn Product Demo khi | Chọn UGC (`ugc-workflow.md`) khi |
|---|---|
| Show sản phẩm trong cảnh đẹp, không cần người nói | Cần social proof từ "người dùng thật" |
| Brand awareness, cold traffic rộng | Problem-aware audience, cần thuyết phục |
| Sản phẩm có visual mạnh (texture, packaging) | Sản phẩm cần giải thích / kết quả cần chứng minh |

## `/storyboard` — ảnh hero cho Veo
Mỗi clip Veo cần 1 ảnh first frame. Lên 2 phương án để chọn:
- **A:** sản phẩm trên bề mặt hợp bối cảnh sẽ animate
- **B:** sản phẩm có tay / đang dùng

Ảnh hero phải: sản phẩm sắc nét, đúng màu · bố cục có "chỗ để chuyển động" (không full-frame sản phẩm ngay từ đầu) · ánh sáng thật — Veo sẽ giữ theo ánh sáng này.

## `/assets` — prompt
- Ảnh hero (4A): thẻ theo `_prompts/nano-banana/image-prompt-card.md` theo `_skills/image/` — `product-photography.md` (Base Template / Variation 1) chỉ là thư viện tham khảo nội dung.
- Video (4C): thẻ theo `_prompts/veo3/video-prompt-card.md` (image-to-video, viết theo ảnh đã duyệt 4B) theo `_skills/video/` — `_prompts/veo3/product-demo.md` chỉ là thư viện ý tưởng chuyển động.
- **Veo gen tối đa 8s/clip.** Video 15s = 2 scene trong storyboard (0–8s, 8–15s), mặc định mỗi scene có keyframe riêng (4A/4B) + thẻ video riêng. Ngoại lệ phải ghi rõ: clip 2 dùng frame cuối clip 1 làm first frame → thẻ 4C của clip 2 chỉ viết sau khi clip 1 qua `/check`.

Motion sequence hay dùng (chia theo clip ≤ 8s):
```
Product reveal — clip 1 (8s): slow push-in wide → medium, rồi close-up chi tiết (texture/label)
               — clip 2 (7s): pull back ra toàn cảnh lifestyle, hold sản phẩm sắc nét, nền bokeh
In-use         — clip 1 (7s): sản phẩm tĩnh trên bề mặt → tay vào khung, cầm lên
               — clip 2 (8s): thao tác dùng (bóp/rót/mở) → đặt lại, tay ra khỏi khung
```

## `/check` — QC riêng
- [ ] Sản phẩm đồng nhất, đúng màu giữa các clip
- [ ] Label không bị méo / bịa chữ
- [ ] Chuyển động tự nhiên, không giật ở điểm nối 2 clip

## `/edit`
- Không có VO → ambient của Veo thường đủ cho Feed. Cần nhạc → nhạc royalty-free (Epidemic Sound, Artlist), duck theo `_skills/motion-graphic/references/audio-and-voice.md`.
- Naming: file thô theo `[campaign-code]_[asset-id]_[mô-tả-ngắn]_v[n].[ext]` (VD clip `2026-06-LAUNCH_S01_reveal_v1.mp4`); bản final trong `outputs/final/` theo convention `CLAUDE.md`, VD `[campaign-code]_videodemo_[angle]_[product]_[ratio]_v[version].mp4`
