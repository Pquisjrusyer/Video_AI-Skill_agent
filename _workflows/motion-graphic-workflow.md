# Ghi chú format — Motion Graphic (ảnh tĩnh + graphic động, Remotion)

> Quy trình chạy bằng 6 lệnh chính (+ `/brief` tuỳ chọn) (`/start` → `/edit`, xem `production-steps.md`). File này chỉ ghi phần **riêng của motion graphic** — kỹ thuật Remotion nằm ở `_skills/motion-graphic/`.

## Khi nào chọn
Video không cần chuyển động thật: headline/offer động, quote card, số liệu, before/after dạng slide, end card CTA. Nhanh, kiểm soát từng frame. Có scene cần chuyển động thật → video **mixed**: scene đó tag `AI-VIDEO` (thẻ Veo tự gen), còn lại Remotion — `_skills/scene-routing/` quyết định từng scene.

## `/storyboard`
- Ưu tiên ảnh thật sản phẩm (`_products/.../reference-images/`) cho packshot/callout/end card — đúng packaging 100%.
- Ảnh nền cần gen: ghi vào danh sách asset; thẻ 4A ở `/assets` theo `_prompts/nano-banana/image-prompt-card.md` (`product-photography.md` / `lifestyle-still.md` chỉ là tham khảo nội dung), đúng ratio storyboard. Scene AI-VIDEO: thẻ 4C theo `_prompts/veo3/video-prompt-card.md`.

## `/edit`
- Template scene có sẵn: `_prompts/remotion/scene-templates.md` (Hero Reveal / Quote Card / Before-After / CTA End Card) — dùng trước khi tự viết.
- Mỗi scene render riêng để review trước khi ráp (Mode A), rồi ráp (Mode B) theo `_skills/motion-graphic/SKILL.md`.
- Text overlay: đối chiếu claim APPROVED trong `product-brief.md`.
- Naming: `[campaign-code]_motiongraphic_[description]_[ratio]_v[version].mp4`
- AI disclosure: bật nếu có ảnh nền AI-gen hoặc scene AI-VIDEO.

## Sau khi chạy ads
Có test song song bản motion graphic và bản AI-video → so Hook rate / CTR trong `performance-notes.md` để biết route nào hợp concept này.
