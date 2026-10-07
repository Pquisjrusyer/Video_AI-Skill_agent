# Audio Plan — KOLOR-2026-10-COMBO

> VO: Claude gen qua **connector ElevenLabs** (VO_TOOL=openai hết credit → lựa chọn kế). Nhạc + SFX: user tự chọn (MUSIC_TOOL=self).
> Mọi clip render với dòng "No dialogue, no music, no sound effects" → mute khi dựng; toàn bộ âm thêm ở Remotion.

## Bảng âm thanh

| Mốc | Scene | Lời đọc | Cách đọc · nhấn · nghỉ | Nhạc nền | SFX | Đồng bộ với hình | Chuyển sang cảnh sau | Tạo cùng clip / riêng |
|---|---|---|---|---|---|---|---|---|
| 0.4–3.0s | S01 | Two bottles. Endless sets. | Nghỉ sau "bottles", "Endless sets" chắc, hạ nhẹ | vào nhẹ từ 0s | sfx-01 cọ quét ~0.6s | nét cọ trên móng | cắt thẳng | riêng |
| 3.0–6.5s | S02 | Highly pigmented black. Smooth, even coverage. | Nhấn "black" | duck dưới lời | — | cọ phủ móng áp út | cắt thẳng | riêng |
| 6.5–9.0s | S03 | Cures fast under UV or LED. | Đều, nhanh vừa | duck | sfx-02 tick bật đèn ~7.3s | đèn bật | cắt thẳng | riêng |
| 9.0–13.0s | S04 | Then the top coat. Super glossy. No wipe. | Nghỉ sau "top coat", "No wipe" gọn | duck, nhạc nâng nhẹ ở 9.0s | sfx-01 cọ quét ~10.5s | móng satin thành bóng | cắt thẳng | riêng |
| 13.0–16.5s | S05 | Seals in your color. Helps prevent chipping. | Ấm, chậm | duck | sfx-03 ting nhẹ ~14.5s | vệt sáng lướt móng | crossfade 0.2s | riêng |
| 16.5–20.0s | S06 | The Kolor Combo. Black or white. | "Kolor" đọc như "color", không lên giọng | accent 16.5s, ring-out tới 20s | — | end card | fade out 0.5s | riêng |

## A. Voice-over

**1. Giọng (đã gen):**
- ElevenLabs connector · voice **Lyan – Clean Natural Explainer Female** · `voice_id: OHbs18UsFunlwffsTLNn` (từ `creative_list_voices`) · model `eleven_v3` · settings mặc định · 1 bản / câu · flow ElevenLabs: S01 OQOwosKqEcLyZ3ZZzuh9, S02 5j87YtC3z0wg6mc03rWA, S03 cukNl4eu1NtgNfpXRQkC, S04 dpK11DyuSvwAkMufPQ1Q, S05 AZYqgM55kU0qXGiBjjRz, S06 JyLSmeMz4D5ubQXd5oq9.
- Nữ Mỹ trẻ, tự nhiên, người trong nghề nói với nhau, không giọng quảng cáo. Giống giọng Blooming Gel (KOLOR-2026-10-BLOOM).

**2. Lời đọc sạch** → `outputs/audio/`:

| File | Text | Ước tính (s) | Slot (s) | Vừa? |
|---|---|---|---|---|
| `KOLOR-2026-10-COMBO_vo-S01_v1.mp3` | Two bottles. Endless sets. | 2.40 (thật) | 2.6 | ✅ |
| `KOLOR-2026-10-COMBO_vo-S02_v1.mp3` | Highly pigmented black. Smooth, even coverage. | 3.36 (thật) | 3.5 | ✅ |
| `KOLOR-2026-10-COMBO_vo-S03_v1.mp3` | Cures fast under UV or LED. | 2.80 (thật) | 2.5 | ⚠️ +0.3s → dựng: S03 2.9s, S04 bớt còn 3.6s |
| `KOLOR-2026-10-COMBO_vo-S04_v1.mp3` | Then the top coat. Super glossy. No wipe. | 3.28 (thật) | 4.0 | ✅ |
| `KOLOR-2026-10-COMBO_vo-S05_v1.mp3` | Seals in your color. Helps prevent chipping. | 2.64 (thật) | 3.5 | ✅ |
| `KOLOR-2026-10-COMBO_vo-S06_v1.mp3` | The Kolor Combo. Black or white. | 2.48 (thật) | 3.5 | ✅ |

## B. Nhạc nền — 1 bản xuyên suốt (user tự gen/chọn)

```
Duration: 22s (20s + 2s đuôi)
Mood/style/tempo: clean, confident minimal pop / lo-fi house, 100–105 BPM, bright but calm
Instruments: soft kick, muted claps, warm sub bass, airy synth pad, light pluck accents
Timeline: 0–3s soft intro (pad + pluck) | 3–9s groove enters lightly | 9–16.5s slight lift (add hi-hat) | 16.5–20s resolve, ring-out
Accent points: 9.0s (top coat bắt đầu) · 16.5s (end card)
VO space: keep 1–4 kHz clear, no lead melody over the voice
Tail: ring-out 2s
Instrumental only, no vocals.
```
Lưu: `outputs/audio/KOLOR-2026-10-COMBO_music_v1.mp3`. Royalty-free → kiểm license dùng cho ads.

## C. SFX (user tự gen/chọn)

| Mã | Scene | Prompt (EN) | Chất · cường độ | Dài | Mốc dự kiến | Tránh |
|---|---|---|---|---|---|---|
| sfx-01 | S01, S04 | soft nail polish brush stroke on a fingernail, close-mic, subtle | khô, nhỏ | 1.0s | 0.6s · 10.5s | tiếng sột soạt to |
| sfx-02 | S03 | small electronic click of a nail lamp switching on | nhỏ, gọn | 0.3s | ~7.3s | beep dài |
| sfx-03 | S05 | delicate glass shine ting, high and soft | sáng, rất nhẹ | 0.8s | ~14.5s | chuông to, vang dài |

Lưu: `outputs/audio/KOLOR-2026-10-COMBO_sfx-01_brush_v1.mp3` · `_sfx-02_lamp-click_v1.mp3` · `_sfx-03_shine-ting_v1.mp3`. Mốc chốt lại theo clip thật ở cổng 3.

## D. Phối âm
- VO trội hơn nhạc ~10–12 dB khi có lời; tổng −14 LUFS, peak ≤ −1 dBTP.
- Nhạc duck dưới lời, nâng nhẹ ở khoảng trống 0–0.4s và trước end card.
- Clip mute hoàn toàn.
