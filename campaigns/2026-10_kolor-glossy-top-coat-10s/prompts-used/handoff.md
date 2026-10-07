# Handoff — KOLOR-2026-10-TOPCOAT

> Tổng hợp nội dung đã viết ở cổng 2 (chờ duyệt cùng cổng 2). Người render copy được ngay.

## A. Bảng render

> ⚠️ **Đã thay bằng bản v2** (quy trình thật, render Dreamina/Seedance): xem `prompt-pack.md` → "Thẻ video v2". Ảnh khung đầu: B-03 (S01), B-04 (S02). Khối Veo bên dưới chỉ giữ để tham khảo.

### S01 · `KOLOR-2026-10-TOPCOAT_S01_one-coat_v1.mp4` → `outputs/videos/`
Tool / model:            Veo 3.1 · image-to-video · 9:16 · 1080p
Ảnh đầu vào:             First frame = `outputs/images/KOLOR-2026-10-TOPCOAT_B-01_S01-brush_v1.png` · KHÔNG dùng last frame
Render:                  4s        Dùng khi dựng: ~0.2–3.7s = 3.5s
Âm tạo cùng clip:        không, mute khi dựng
Âm thêm sau:             vo-S01 · sfx-01 · music
PROMPT (copy nguyên văn):
```
Maintain the hand, nails and background from the first frame exactly; the hand stays completely still. Static 100mm macro shot, no camera movement. The flat black gel brush loaded with clear gel lowers and touches the base of the middle fingernail near the cuticle. In one slow, even stroke it glides from the base to the tip of the nail, laying down a smooth layer of perfectly clear gel. Wherever the brush has passed, the satin cherry red surface turns into a glass-like mirror gloss with a crisp reflection of the soft window light, while the color itself stays the same red. The brush then lifts and exits toward the upper-right corner of the frame. Final image: the middle nail is mirror-glossy, the other two nails remain satin, no brush in frame. Soft diffused window light from frame-left throughout. No hand holding the brush is ever visible.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
Kiểm khung đầu: ☐ khớp B-01 · Kiểm khung cuối: ☐ không còn cọ, chỉ móng giữa bóng ☐ yên ~1s

### S02 · `KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v1.mp4` → `outputs/videos/`
Tool / model:            Veo 3.1 · image-to-video · 9:16 · 1080p
Ảnh đầu vào:             First frame = `outputs/images/KOLOR-2026-10-TOPCOAT_B-02_S02-glossy_v1.png`
Render:                  4s        Dùng khi dựng: ~0.3–3.3s = 3.0s
Âm tạo cùng clip:        không, mute khi dựng
Âm thêm sau:             vo-S02 · sfx-02 · music
PROMPT (copy nguyên văn):
```
Maintain the hand, nails and background from the first frame exactly. Static 100mm macro shot, no camera movement. The hand stays relaxed on the tabletop; from 0.5 seconds the wrist tilts very slightly to the right, about ten degrees, fingers keeping their exact positions. As it tilts, the crisp reflection of the soft window slides smoothly across each mirror-glossy cherry red nail from its left edge to its right edge, index then middle then ring nail, like light gliding over glass. The red color, nail shapes and skin stay unchanged. By 3 seconds the movement stops and the hand holds still. Soft diffused window light from frame-left throughout.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
Kiểm khung đầu: ☐ khớp B-02 · Kiểm khung cuối: ☐ vệt sáng ở phía phải các móng ☐ tay yên ~1s

### S03 · MOTION-GRAPHIC
Dựng bằng Remotion ở cổng 3, không render ở tool ngoài. Nguồn: `_products/Kolor/kolor-glossy-top-coat/reference-images/top-coat_official-06.jpg` + `_brand/kolor-acrylic/Logo/logo_black.png`.

> Mỗi clip render 2 bản nếu được, chọn bản đạt rồi đặt đúng tên `_v1`. Clip lỗi → báo theo mẫu phản hồi trong `_prompts/handoff-template.md`, không render lại cảnh đã đạt.

## B. Bộ âm thanh — chi tiết + prompt: `prompts-used/audio-plan.md`

| Asset | Ai làm | File |
|---|---|---|
| VO ×3 | ✅ **Claude đã gen** (OpenAI TTS, voice nova) | `KOLOR-2026-10-TOPCOAT_vo-S01/S02/S03_v1.mp3` |
| Nhạc 12s | **User** gen (ElevenLabs Music) hoặc chọn royalty-free. Hoặc bật connector rồi nhắn "gen nhạc" | `KOLOR-2026-10-TOPCOAT_music_v1.mp3` |
| SFX ×2 | User | `_sfx-01_brush-swipe_v1.mp3` · `_sfx-02_shine-ting_v1.mp3` |

Tất cả thả vào `outputs/audio/`.

| Mốc | VO | Nhạc | SFX |
|---|---|---|---|
| 0.0–0.5s | — | vào, mức thường | — |
| 0.5–3.5s | vo-S01 | duck | sfx-01 ~0.7s |
| 3.5–6.5s | vo-S02 | duck | sfx-02 ~5.0s |
| 6.5–10.0s | vo-S03 | duck → nâng sau lời | — |

## C. Hướng dẫn dựng (cổng 3, Remotion)

| # | Cảnh | Timeline | Nối | Chữ (không em dash) | Âm |
|---|---|---|---|---|---|
| 1 | S01 | 0.0–3.5s | — | "ONE COAT" giữa-trên, 0.3–3.5s | vo-S01, sfx-01 |
| 2 | S02 | 3.5–6.5s | hard cut | "SUPER GLOSSY" / "NO-WIPE" 1/3 trên | vo-S02, sfx-02 |
| 3 | S03 | 6.5–10.0s | hard cut (hoặc flash trắng 2 frame) | logo trên · "Glossy Gel Top Coat" · "Shop now" dưới | vo-S03 |

- S03: ảnh official-06 vuông đặt giữa khung 9:16, nền kéo dài màu `#debdb8`, push-in 100→106%.
- Mốc từng cảnh chốt theo độ dài VO thật.
- Xuất: 1080×1920 · 30fps · H.264 · -14 LUFS · `KOLOR-2026-10-TOPCOAT_voiceover_nochar_glossy-top-coat_9x16_v1.mp4`

## D. Tiêu chí duyệt: theo mục D của `_prompts/handoff-template.md` + Meta compliance trong `CLAUDE.md`.
