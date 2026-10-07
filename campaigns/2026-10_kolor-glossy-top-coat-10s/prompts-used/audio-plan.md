# Audio Plan — KOLOR-2026-10-TOPCOAT

> **VO: Claude gen bằng OpenAI TTS** (`gpt-4o-mini-tts`, voice `nova`), 2026-10-05. User cho phép không dùng ElevenLabs. Nhạc vẫn là thẻ cho user (connector ElevenLabs không có).

## Bảng âm thanh

| Mốc | Scene | Lời đọc | Cách đọc · nhấn · nghỉ | Nhạc nền | SFX | Đồng bộ hình | Sang cảnh sau | Tạo cùng clip / riêng |
|---|---|---|---|---|---|---|---|---|
| 0.0–3.5s | S01 | "Dull to glass. One coat." | Vào lời ở ~0.5s. Nghỉ ngắn sau "glass." · "One coat." hạ giọng, chắc | Vào ngay 0s, nhẹ | sfx-01 quẹt cọ ~0.7–2.6s | "glass" rơi đúng lúc cọ đang quét | Hard cut | Riêng |
| 3.5–6.5s | S02 | "Super glossy. No wipe needed." | Nhấn "glossy" và "No wipe" | Duck dưới lời | sfx-02 "ting" khi vệt sáng qua móng giữa (~5.0s) | Lời khớp vệt sáng | Hard cut | Riêng |
| 6.5–10.0s | S03 | "Seals in your color. Kolor Glossy Top Coat." | Tên SP đọc rõ, không lên giọng | Nâng nhẹ, kết bằng 1 nốt ngân | — | Logo hiện khi đọc "Kolor" | Fade out | Riêng |

## A. Voice-over

**1. Chỉ dẫn giọng**
- Giọng: `Lyan – Clean Natural Explainer Female` (`OHbs18UsFunlwffsTLNn`), model `eleven_v3`. Cùng giọng campaign Blooming Gel để các ad Kolor nghe cùng 1 brand
- Nữ Mỹ 25–35, tự nhiên, như thợ nail nói với đồng nghiệp. Không giọng quảng cáo
- Tốc độ chậm vừa (~2 từ/s), ngắt rõ ở mỗi dấu chấm
- Phát âm: "Kolor" = "color" (/ˈkʌlər/)
- Không thêm lời, không "um", không hơi thở giả

**Đã gen (thay cho Lyan/ElevenLabs ở trên):** OpenAI `gpt-4o-mini-tts` · thử 2 giọng `coral` + `nova` · chọn **nova** cho cả 3 câu (coral S03 dài 4.09s, quá slot 3.5s). Instructions: nữ Mỹ cuối 20s, thợ nail nói với đồng nghiệp, tự nhiên, không bán hàng, "Kolor" đọc như "color". Bản thử: `outputs/audio/_takes/`.

| File | Dài file | Lời thật (whisper) | Slot | Vừa? |
|---|---|---|---|---|
| `vo-S01_v1.mp3` | 2.76s (lời 2.53s) | "Dull to glass, one coat." | 3.0s | ✅ |
| `vo-S02_v1.mp3` | 2.35s (lời 2.04s) | "Super glossy, no wipe needed." | 3.0s | ✅ |
| `vo-S03_v1.mp3` | 3.17s (lời 2.77s) | "Seals in your color, Kolor Glossy Top Coat." | 3.5s | ✅ |

**2. Lời đọc sạch (kế hoạch ban đầu)** — 1 câu 1 file, gen 2 bản/câu, chọn bản tự nhiên hơn:

| File (`outputs/audio/`) | Text | Ước tính | Slot | Vừa? |
|---|---|---|---|---|
| `KOLOR-2026-10-TOPCOAT_vo-S01_v1.mp3` | Dull to glass. One coat. | ~2.3s | 3.0s (sau 0.5s im) | ✅ |
| `KOLOR-2026-10-TOPCOAT_vo-S02_v1.mp3` | Super glossy. No wipe needed. | ~2.3s | 3.0s | ✅ |
| `KOLOR-2026-10-TOPCOAT_vo-S03_v1.mp3` | Seals in your color. Kolor Glossy Top Coat. | ~3.0s | 3.5s | ✅ (sát) |

## B. Nhạc nền — 1 bản xuyên suốt

Gen bằng ElevenLabs Music (`eleven_music_v2_5`) hoặc chọn bài royalty-free dùng được cho ads.

```
Duration: 12 seconds
Mood/style/tempo: clean, confident, modern beauty-studio groove, around 100 BPM, light and polished
Instruments: soft muted electric piano chords, tight finger snaps, subtle sub bass, a light glassy bell accent
Timeline: 0–3.5s sparse piano and snaps | 3.5–6.5s add sub bass and a soft shimmer | 6.5–10s full but light groove | 10–12s ring-out
Accent points: 5.0s a single glassy bell hit (shine sweep) · 6.5s light lift into the packshot
VO space: keep the 1–4 kHz range clear, no lead melody over the voice
Tail: natural ring-out 2s
Instrumental only, no vocals.
```
→ `outputs/audio/KOLOR-2026-10-TOPCOAT_music_v1.mp3`

## C. SFX (user tự gen/chọn — ElevenLabs Sound Effects hoặc thư viện)

| Mã | Scene | Prompt (EN) | Chất · cường độ | Dài | Mốc dự kiến | Tránh |
|---|---|---|---|---|---|---|
| sfx-01 | S01 | soft nail gel brush stroke gliding across a smooth nail, close-up ASMR, very subtle wet swipe | khô, gần, rất nhỏ | ~2s | 0.7–2.6s | tiếng cọ sơn tường, tiếng cào |
| sfx-02 | S02 | single delicate glass shine ting, bright and clean, short sparkle tail | trong, vừa | ~1s | ~5.0s | chuông to, phép thuật/cartoon |

→ `KOLOR-2026-10-TOPCOAT_sfx-01_brush-swipe_v1.mp3` · `KOLOR-2026-10-TOPCOAT_sfx-02_shine-ting_v1.mp3`. Mốc chốt lại theo clip thật ở cổng 3.

## D. Phối âm
- VO trội hơn nhạc ~10–12 dB khi có lời, tổng ~-14 LUFS, peak ≤ -1 dBTP.
- Nhạc duck dưới lời, nâng ở 0–0.5s và sau lời cuối.
- Clip Veo mute hoàn toàn.
