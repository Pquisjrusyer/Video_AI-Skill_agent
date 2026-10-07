# Handoff — KOLOR-2026-10-COMBO (cổng 2)

> Prompt video + ảnh khung đầu + cài đặt: **chỉ ở bảng clip** (`prompts-used/clips.json` → `outputs/review/clip-board.html`). File này không chép lại prompt.

## A. Render (user, Google Flow — test)

5 clip S01–S05 theo bảng clip: Flow → Veo 3.1 → Frames to Video → upload ảnh khung đầu → 9:16 → dán prompt EN → tải 1080p → `outputs/videos/` đúng tên ở cột "Lưu về". S06 = Remotion, không render.
Ảnh khung đầu là ảnh Flux có lỗi đã biết (ghi ở `notes_vi` từng cảnh), user chấp nhận vì dự án test.

## B. Bộ âm thanh

- **VO (đã có):** `outputs/audio/KOLOR-2026-10-COMBO_vo-S01..S06_v1.mp3` · ElevenLabs Lyan (`OHbs18UsFunlwffsTLNn`, `eleven_v3`). Chi tiết + độ dài thật: `audio-plan.md` §A.
- **Nhạc nền (user):** prompt ở `audio-plan.md` §B → `outputs/audio/KOLOR-2026-10-COMBO_music_v1.mp3`.
- **SFX (user):** 3 mã ở `audio-plan.md` §C → `outputs/audio/`.

| Mốc | VO | Nhạc (mức) | SFX | Ghi chú |
|---|---|---|---|---|
| 0.0–0.4s | — | intro, mức đầy | sfx-01 0.6s | thấy cọ trước khi có lời |
| 0.4–2.8s | S01 (2.40s) | duck −12 dB | | |
| 3.0–6.4s | S02 (3.36s) | duck | | |
| 6.5–9.3s | S03 (2.80s) | duck | sfx-02 ~7.3s | S03 kéo tới 9.4s |
| 9.5–12.8s | S04 (3.28s) | duck, lift nhẹ 9.4s | sfx-01 ~10.5s | |
| 13.0–15.6s | S05 (2.64s) | duck | sfx-03 ~14.5s | |
| 16.6–19.1s | S06 (2.48s) | accent 16.5s, ring-out | | fade out 19.5–20s |

## C. Hướng dẫn dựng (Remotion, cổng 3)

| # | Cảnh | Timeline | Lấy từ clip | Chữ (không em dash) · vị trí | Âm |
|---|---|---|---|---|---|
| 1 | S01 | 0.0–3.0s | đoạn có nét cọ trên móng (~1.5–4.5s) | "2 BOTTLES." / "ENDLESS SETS." · 1/3 trên · 0.4s | VO S01 |
| 2 | S02 | 3.0–6.5s | ~0.5–4.0s | "HIGHLY PIGMENTED" · 1/3 trên | VO S02 |
| 3 | S03 | 6.5–9.4s | quanh lúc đèn bật (~0.3–3.2s) | "UV/LED CURE" · 1/3 trên | VO S03 + sfx-02 |
| 4 | S04 | 9.4–13.0s | đoạn quét bóng (~1.5–5.1s) | "SUPER GLOSSY" / "NO-WIPE" · 1/3 trên | VO S04 + sfx-01 |
| 5 | S05 | 13.0–16.5s | ~0.8–4.3s | "SEALS IN COLOR" · 1/3 trên | VO S05 + sfx-03 |
| 6 | S06 | 16.5–20.0s | ảnh `combo_official-01.jpg` → crossfade 0.3s sang `-05.jpg` ở 18.3s | logo kolor trên · "Top Coat + Gel Polish Combo" / "Black or White" / nút "Shop now" dưới | VO S06 |

- Cắt thẳng giữa S01–S05; S05 → S06 crossfade 0.2s.
- Màu: giữ nền xám nhạt trung tính, không đẩy saturation da; khớp độ sáng giữa các clip.
- Không giá trên màn hình. Không dùng ảnh official-02, 04, 06, 07.
- Xuất: 1080×1920 · 30fps · H.264 · −14 LUFS · `outputs/final/KOLOR-2026-10-COMBO_voiceover_nochar_topcoat-gel-combo_9x16_v1.mp4`.

## D. Tiêu chí duyệt

Theo `_prompts/handoff-template.md` §D + Meta compliance trong `CLAUDE.md` (AI disclosure bật · claim chỉ APPROVED · logo/chữ nhãn đúng · 9:16 · chỉ upload từ `outputs/final/`).
