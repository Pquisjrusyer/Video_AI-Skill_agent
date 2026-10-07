# Ghi chú format — Static + Video Combo (3 static + 1 video)

> Quy trình chạy bằng 6 lệnh chính (+ `/brief` tuỳ chọn) (`/start` → `/edit`, xem `production-steps.md`). File này chỉ ghi phần **riêng của combo** — 1 ad set đủ format để Meta tự tìm format thắng.

## `/storyboard` — danh sách asset cố định
| Asset | Mục đích | Ratio | Tham khảo nội dung (thẻ 4A theo `_prompts/nano-banana/image-prompt-card.md`) |
|---|---|---|---|
| Static 1 — Clean hero | Static chính, carousel, catalog | 1:1 | `_prompts/nano-banana/product-photography.md` → Base Template (nền studio / đá marble / tối giản) |
| Static 2 — Lifestyle | Feed single image, bối cảnh | 4:5 | Variation 1 (bối cảnh hợp brand) |
| Static 3 — In-use / tay | In-use, **làm first frame cho video** | = ratio video (4:5) | Variation 2 (chỉ tay, không mặt) |
| Video — từ Static 3 | Product reveal, không lời thoại | = ratio Static 3 (4:5). Cần 9:16 → thêm 1 frame 9:16 riêng ở 4A | thẻ 4C `_prompts/veo3/video-prompt-card.md` theo `_skills/video/` (image-to-video) |

## `/assets`
- 3 static: thẻ 4A theo `image-prompt-card.md` (prompt + ref sản phẩm thật), Claude gen ở cổng 2 (`_skills/image/SKILL.md` → Gen GPT Image); 4B QC. QC: màu đúng reference · label đọc được · không méo sản phẩm · đúng aesthetic brand.
- Video: thẻ 4C theo `video-prompt-card.md`, viết sau khi Static 3 duyệt ở 4B, first frame = Static 3. **Veo tối đa 8s/clip** — muốn 15s thì 2 scene storyboard, mặc định mỗi scene keyframe riêng (4A/4B). Ngoại lệ ghi rõ: clip 2 dùng frame cuối clip 1 → thẻ 4C clip 2 viết sau khi clip 1 qua `/check`. Prompt khoá sản phẩm: *"Maintain exact product appearance from the first frame. Do not alter product color, label, or packaging shape."* · Audio: *"No dialogue, no music, no sound effects; quiet natural ambience only."*
- Headline trên static: **mặc định để text trong Ads Manager** (Primary Text + Headline) — A/B test text không phải gen lại ảnh. Chỉ bake text vào ảnh khi có lý do.

## `/edit`
Naming:
```
[campaign-code]_static_hero_[product]_1x1_v1.jpg
[campaign-code]_static_lifestyle_[product]_4x5_v1.jpg
[campaign-code]_static_inuse_[product]_4x5_v1.jpg
[campaign-code]_video_lifestyle_[product]_4x5_v1.mp4
```

## Dựng ad set trong Ads Manager
```
Ad Set: [Campaign] — Static+Video Combo Test
├── Ad 1: Static Hero — 1:1 — clean shot + offer headline
├── Ad 2: Static Lifestyle — 4:5 — in-context + benefit headline
├── Ad 3: Static In-use — 4:5 — hands close-up + CTA
└── Ad 4: Video — 4:5 / 9:16 — product reveal, no dialogue
```
AI disclosure bật trên **cả 4 ad** · preview mobile trước khi publish.

## Sau 3–5 ngày → `performance-notes.md`
| Ad | Format | CTR | CPC | Hook rate (video) | Notes |
|---|---|---|---|---|---|
Ghi: format thắng + hướng iteration tiếp.
