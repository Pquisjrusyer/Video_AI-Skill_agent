# Handoff — KOLOR-2026-10-STUDIO

> Cổng 2. Người render chỉ cần file này. Thẻ ảnh: `prompt-pack.md`. Chữ: `scripts/script.md`. Âm thanh chi tiết: `audio-plan.md`.

## A. Bảng render

### S01 · `KOLOR-2026-10-STUDIO_S01_dot-bloom_v1.mp4` → `outputs/videos/`
Tool: **Veo 3.1 · image-to-video · 9:16 · 1080p** (chọn 1080p nếu có — campaign trước ra 720p)
First frame: `outputs/images/KOLOR-2026-10-STUDIO_B-01_S01-dot_v1.png` ✅
Render: **4s** · Dùng: 0.0–3.0s
Âm: không tạo cùng clip — mute khi dựng. Thêm sau: music · sfx-01

PROMPT (copy nguyên văn)
```
Maintain the subject from the first frame. Locked-off static macro shot on a 100mm macro lens; the camera does not move, tilt or rotate. From 0.0 to 0.5 seconds the fine black brush lifts straight up and exits the top-right of the frame, pulling a thin pink thread that snaps back into the nail. From 0.5 to 3.0 seconds the hot pink dot sinks into the wet clear gel and blooms outward in real time into five soft rounded petals with feathered watercolor edges, the pink staying deepest at the center while the long glossy highlight on the gel shifts slightly. From 3.0 to 4.0 seconds the bloom settles and holds still. The finger stays perfectly still with its natural skin creases unchanged. The background stays the same seamless light grey with soft neutral light from frame-left the whole time, no color change. Ends on a finished soft pink five-petal flower centered on the milky white nail, nothing else in frame.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
Kiểm khung đầu: ☐ khớp B-01 (móng, chấm hồng, cọ góc trên-phải)
Kiểm: ☐ máy KHÔNG xoay ☐ nền giữ xám (campaign trước nền ngả xanh ngọc) ☐ màu loang mềm, không nhảy cóc ☐ khung cuối: hoa 5 cánh, không còn cọ

### S02 · `KOLOR-2026-10-STUDIO_S02_nia-bottle_v1.mp4` → `outputs/videos/`
Tool: **Veo 3.1 · image-to-video · 9:16 · 1080p**
First frame: `outputs/images/KOLOR-2026-10-STUDIO_B-02_S02-nia-bottle_v1.png` ✅
Render: **4s** · Dùng: 0.3–3.8s (3.5s)
Âm: mute khi dựng. Thêm sau: music · sfx-02

PROMPT
```
Maintain the subject and the bottle from the first frame. Very slow push-in on an 85mm portrait lens, nothing else moves in the camera. From 0.0 to 1.5 seconds she holds still, eyes on her pink flower nails, one slow breath gently lifting her shoulders. From 1.5 to 3.0 seconds she raises her eyes to the camera and her closed lips ease into a small, calm smile, while her fingers tilt the bottle a few degrees toward the lens; a soft highlight slides down the glossy black glass. From 3.0 to 4.0 seconds she holds eye contact, still. Soft diffused light from frame-left, seamless light grey backdrop, unchanged. Do not alter the product color, label text or packaging shape; keep her face, hair and hand anatomy exactly the same; only one hand in frame. Ends on her looking into the camera with a calm smile, bottle upright beside her cheek, label sharp and readable.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
Kiểm khung đầu: ☐ khớp B-02
Kiểm: ☐ mặt không trôi ☐ chữ label không nhoè/biến ☐ 5 ngón suốt clip ☐ khung cuối: nhìn camera, chai thẳng

### S03 · S04 — MOTION-GRAPHIC
Dựng bằng Remotion ở cổng 3, không render tool ngoài.
- S03: `outputs/images/KOLOR-2026-10-STUDIO_B-03_S03-hand-patterns_v1.png` ⚠️ **chưa có — cần gen** (thẻ B-03 trong `prompt-pack.md`)
- S04: `_products/kolor-blooming-gel/reference-images/blooming-gel_official-01_2048.jpg` ✅

## B. Âm thanh (người dùng chọn → `outputs/audio/`)
| File | Nội dung | Mốc |
|---|---|---|
| `KOLOR-2026-10-STUDIO_music_v1.mp3` | Nhạc 12s — prompt trong `audio-plan.md` §B | 0–10s |
| `…_sfx-01_bloom_v1.mp3` | Soft airy swell | 1.2s |
| `…_sfx-02_click_v1.mp3` | Glass bottle tap | ~5.0s (theo clip thật) |
| `…_sfx-03_tick_v1.mp3` | Tick nhẹ ×4 (1 file) | 6.5 / 7.0 / 7.5 / 8.0s |
| `…_sfx-04_pop_v1.mp3` | Soft pop | 8.5s |

## C. Hướng dẫn dựng (Claude — cổng 3)
| # | Cảnh | Timeline | Nối | Chữ | Âm |
|---|---|---|---|---|---|
| 1 | S01 | 0.0–3.0 | — | "One dot." 0.0–1.2 → "Watch it bloom." 1.2–3.0 · giữa, 1/3 trên | beat in · sfx-01 |
| 2 | S02 | 3.0–6.5 | hard cut on beat | "Colors disperse into organic patterns in seconds." · 1/3 dưới | sfx-02 |
| 3 | S03 | 6.5–8.5 | hard cut | 4 từ hiện lần lượt mỗi 0.5s · 1/3 trên · zoom 100→106% | sfx-03 |
| 4 | S04 | 8.5–10.0 | hard cut | "Kolor Blooming Gel" · "Even Blooming · Long Lasting" · nút "Shop now" | sfx-04 · nhạc kết |

- Clip Veo: **watermark ✦ góc dưới phải** (campaign trước) → crop/scale nhẹ; chữ tránh góc dưới phải. 720p → scale lên 1080×1920.
- Cân màu: xám trung tính `#E9E9EB`, khớp S01↔S02; không đẩy saturation da.
- Font: sans-serif đậm, trắng có bóng mềm hoặc đen trên nền xám — chưa có font brand.
- Xuất: 1080×1920 · 30fps · H.264 · -14 LUFS · `KOLOR-2026-10-STUDIO_productdemo_nia_blooming-gel_9x16_v1.mp4`

## D. Tiêu chí duyệt
Theo `_prompts/handoff-template.md` §D + Meta compliance trong `CLAUDE.md`. Riêng video này: chữ đọc kịp khi tắt tiếng · label chai đúng ở S02 · Nia giống nhau S02 ↔ seed.
