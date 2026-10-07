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

---

## E. Phản hồi clip v1 (2026-10-07, Claude QC: 5 khung/clip + whisper VO)

| Cảnh / mốc | Lỗi quan sát được | Nguyên nhân có thể | Prompt sửa / cách chỉnh khi dựng | Giữ nguyên |
|---|---|---|---|---|
| Tất cả · góc dưới phải | Watermark ✦ của Flow/Veo | (suy đoán) tài khoản Flow gói thường | Test: giữ. Bản chạy thật: render gói không watermark hoặc che khi dựng | — |
| S01 · 1.5–5s | Cọ sơn móng áp út thay vì móng giữa | khung đầu cọ nằm giữa 2 ngón | Không cần sửa. Dựng: lấy 1.6–4.6s | nét đen trên móng, tay đứng yên |
| S02 · cả clip | Dụng cụ giống nhíp (lỗi sẵn từ ảnh B-02) | ảnh khung đầu | Test: chấp nhận. Dựng: lấy 0.5–4.0s | chai Super Black, móng đen kín |
| S03 | Đạt: đèn bật, móng sáng trong đèn | — | Dựng: lấy 0.8–3.7s | toàn bộ |
| S04 · cả clip | Cọ + giọt top coat ở trên da ngón, không lên móng; không thấy móng chuyển bóng | khung đầu B-04 cọ trên da, Veo giữ nguyên | Render lại v2 với prompt dưới, HOẶC test: dùng 0–3.6s và để VO + chữ "SUPER GLOSSY" gánh | 4 móng đen satin |
| S05 · từ ~1.5s | Tay đổi người: da nâu chuyển sang da sáng, móng dài nhọn | prompt cho tay nhấc + xoay → Veo vẽ lại tay | Render lại v2 với prompt dưới, HOẶC test: lấy 0–1.4s, làm chậm 0.4x cho đủ 3.5s | khung đầu 0–1.4s |
| VO S03 | Whisper nghe "It cures…" (chữ "It" độ tin 0.29, dài 0.08s) | (suy đoán) tiếng hơi đầu câu bị nghe nhầm | Giữ, nghe lại khi review cổng 3 | — |

**Prompt S04 v2** (Flow · Frames to Video · cùng ảnh B-04 v2):
```
Maintain the subject from the first frame. Within the first second the brush lifts off the finger and lands on the middle fingernail at the cuticle. From 1 to 4 seconds the brush sweeps clear top coat over the middle fingernail from cuticle to tip; the black nail surface it covers turns mirror-glossy with a sharp white reflection. The coating stays only on the nail. The client's hand stays completely still. Static 100mm macro camera, soft daylight from frame-left.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
```

**Prompt S05 v2** (Flow · Frames to Video · cùng ảnh B-05 v2):
```
Maintain the subject from the first frame exactly: the same hand, the same warm medium-brown skin, the same short glossy black nails. The hand stays resting on the table and does not move. Only a soft bright window highlight glides slowly from left to right across the glossy nails between 1 and 3 seconds. The bottles stay still in soft focus. Static camera.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
```
Lưu v2: `outputs/videos/KOLOR-2026-10-COMBO_S04_topcoat-glass_v2.mp4` · `…_S05_mirror-shine_v2.mp4`.
