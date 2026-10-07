# Status — Glass Skin Duo — "Sixty Seconds" 10s

> Quy trình 3 cổng: `_workflows/production-steps.md`. Duyệt: "ok cổng 1/2/3".
> Brand: **Kreizi Beauty** · Code: `KREIZI-2026-10-GLASSDUO` · Format: **Product demo** (chốt 2026-10-02) · Ratio: 9:16 · Duration: 10s · Nhân vật: **Maren** (mới)

| Cổng | Gồm | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 1. Kế hoạch | `brief.md` · `scripts/script.md` · `scripts/storyboard.md` · thẻ ảnh trong `prompts-used/prompt-pack.md` | ✅ | user (jason.do) | 2026-10-02 |
| 2. Ảnh | QC ảnh · thẻ video · `audio-plan.md` · VO · `handoff.md` | ☑ | | |
| 3. Final | kiểm file · review · `outputs/final/` | ☐ | | |

☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** User duyệt cổng 2 → render 3 clip Veo (S01–S03), gen VO + nhạc theo `audio-plan.md` (hoặc bật connector ElevenLabs để Claude gen) → thả vào `outputs/videos/` + `outputs/audio/` → Claude kiểm file + dựng Remotion (cổng 3).

## Asset
| Tên file | Loại | Ai gen | Xong | QC |
|---|---|---|---|---|
| `KREIZI-2026-10-GLASSDUO_A-01_seed-maren_v1.png` | seed nhân vật | Claude (GPT Image 2) | ✅ | ✅ worked v1 |
| `KREIZI-2026-10-GLASSDUO_B-01_S01-cheek-press_v1.png` | keyframe S01 | Claude | ✅ | ✅ worked v1 |
| `KREIZI-2026-10-GLASSDUO_B-02_S02-serum-pump_v1.png` | keyframe S02 | Claude | ✅ | ✅ worked v1, label đúng |
| `KREIZI-2026-10-GLASSDUO_B-03_S03-booster-dip_v1.png` | keyframe S03 | Claude | ✅ | ✅ worked v1 |
| S01–S03 `.mp4` | clip Veo | User | ☐ | |
| `vo-S01..S04`, `music` `.mp3` | VO + nhạc | User (connector chưa bật) | ☐ | |

## Vấn đề (mỗi ý 1 dòng)
- 2026-10-02 — Product page đang "Sold Out" → video không có giá/offer; xác nhận có hàng trước khi chạy Sales.
- 2026-10-02 — `brand-assets/` Kreizi trống → end card không logo, font serif trung tính.
- 2026-10-02 — Connector ElevenLabs chưa bật trên máy này → cần bật trước bước VO + nhạc ở cổng 2, nếu không sẽ xuất thẻ để user tự gen.
- 2026-10-02 — Tạo nhân vật mới `_characters/maren/` (Kreizi). Copy seed vào `reference-images/maren-face-ref-01.png` sau khi A-01 pass.
- 2026-10-02 — B-04 huỷ: end card dùng ảnh sản phẩm thật ghép Remotion (label đúng 100%), theo `_skills/image/SKILL.md` mục 6.
- 2026-10-02 — `_products/` đã bị chuyển sang `_products/Kreizi/…` và `_products/Kolor/…` (trong session). File campaign đã sửa đường dẫn; `CLAUDE.md` + `_brand/README.md` vẫn ghi đường dẫn cũ `_products/<sku>/`.
- 2026-10-02 — VO S04 ước tính ~1.9s > slot 1.5s → cổng 3 rút S03 còn ~2.3s, S04 ~1.7s (không sửa lời).
