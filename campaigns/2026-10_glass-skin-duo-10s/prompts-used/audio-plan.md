# Audio Plan — Glass Skin Duo — "Sixty Seconds" (cổng 2)

> Connector ElevenLabs **chưa bật** trên máy này (2026-10-02) → VO + nhạc là **thẻ để user tự gen** trên elevenlabs.io. Bật connector thì báo Claude, Claude gen lại theo đúng thẻ này.
> Clip Veo không tự sinh lời/nhạc/SFX. Mọi âm thanh thêm khi dựng.

## Bảng âm thanh

| Mốc | Scene | Lời | Cách đọc | Nhạc | SFX | Đồng bộ hình | Sang cảnh sau | Nguồn |
|---|---|---|---|---|---|---|---|---|
| 0.0–3.0s | S01 | "Two steps. Sixty seconds." | Nghỉ ~0.3s giữa 2 câu, hạ giọng cuối | Vào nhẹ, piano + pad | — | Lời bắt đầu ~0.3s, lúc ngón tay vuốt lên | Hard cut, nhạc liền | Riêng |
| 3.0–6.0s | S02 | "Serum floods deep hydration." | Nhấn nhẹ *deep* | Duck dưới lời | sfx-01 pump click khi bơm ấn (~3.6s, tuỳ chọn) | Lời rơi đúng lúc giọt gel rơi | Hard cut | Riêng |
| 6.0–8.5s | S03 | "Booster locks it in." | Đều, ấm | Duck | — | Lời khi ngón múc kem | Hard cut | Riêng |
| 8.5–10.0s | S04 | "Hydrates. Smooths. Glows." | 3 nhịp đều, *Glows* kéo nhẹ | Mở ra nhẹ, rồi fade | — | Chữ hiện theo từng từ | Fade out | Riêng |

## A. Voice-over

**1. Chỉ dẫn giọng** (chọn giọng / Voice Design trên ElevenLabs, không đọc ra):
- American English, giọng trung tính.
- Nữ 40–55, ấm, trầm vừa, hơi khàn nhẹ tự nhiên. Bình thản, tự tin.
- Như bạn thân nói nhỏ buổi sáng, không giọng quảng cáo, không cười trong giọng.
- Chậm: ~1.8–2 từ/giây. Nghỉ rõ giữa các câu ngắn.
- Model gợi ý: `eleven_multilingual_v2` · Stability ~0.55 · Similarity ~0.75 · Style ~0.15 · Speed 0.9.
- Gợi ý tìm trong Voice Library: lọc *Female · Middle-aged · American · Narration*, nghe thử câu "Two steps. Sixty seconds." chọn giọng ấm, không bóng bẩy.
- Không thêm lời, không "um", không hơi thở giả.

**2. Lời đọc sạch** — mỗi câu 1 file → `outputs/audio/`:

| File | Text | Ước tính (s) | Slot (s) | Vừa? |
|---|---|---|---|---|
| `KREIZI-2026-10-GLASSDUO_vo-S01_v1.mp3` | Two steps. Sixty seconds. | ~2.0 | 3.0 | ✅ |
| `KREIZI-2026-10-GLASSDUO_vo-S02_v1.mp3` | Serum floods deep hydration. | ~2.0 | 3.0 | ✅ |
| `KREIZI-2026-10-GLASSDUO_vo-S03_v1.mp3` | Booster locks it in. | ~1.6 | 2.5 | ✅ |
| `KREIZI-2026-10-GLASSDUO_vo-S04_v1.mp3` | Hydrates. Smooths. Glows. | ~1.9 | 1.5 | ⚠️ sát |

⚠️ S04 dài hơn slot. Cách xử lý ở cổng 3 (không sửa lời): rút S03 còn ~2.2s, S04 lên ~1.8s; vẫn đủ 10.0s. Nếu VO thật vẫn dài → cho S04 bắt đầu sớm 0.2s (đè đuôi S03).

## B. Nhạc nền — 1 bản xuyên suốt

```
Duration: 12 seconds
Mood/style/tempo: calm, warm, airy morning skincare ritual; gentle and optimistic; about 72 BPM
Instruments: soft felt piano, warm ambient pads, very light high shimmer; no drums, no bass drops
Timeline: 0–3s soft piano enters alone | 3–8.5s pads join quietly under the voice | 8.5–10s music opens slightly brighter on the end card | 10–12s gentle ring-out
Accent points: 8.5s small lift as the end card appears
VO space: keep the 1–4 kHz mid range open, no lead melody under the voice
Tail: natural ring-out about 2s
Instrumental only, no vocals.
```
File: `KREIZI-2026-10-GLASSDUO_music_v1.mp3` → `outputs/audio/`. Tự gen trên elevenlabs.io (Music) với prompt trên, hoặc chọn bài royalty-free (kiểm license dùng cho ads).

## C. SFX (tuỳ chọn)

| Mã | Scene | Prompt (EN) | Chất · cường độ | Dài | Mốc | Tránh |
|---|---|---|---|---|---|---|
| sfx-01 | S02 | Soft click of a cosmetic pump bottle pressed once, close-up, quiet bathroom | Nhựa nhẹ, nhỏ, khô, không vang | ~0.4s | ~3.6s (chốt theo clip thật) | Tiếng xịt khí, tiếng to |

File: `KREIZI-2026-10-GLASSDUO_sfx-01_pump-click_v1.mp3`.

## D. Phối âm
- Tổng ~-14 LUFS, peak ≤ -1 dBTP. VO trội hơn nhạc ~10–12 dB khi có lời.
- Nhạc duck dưới lời, nâng nhẹ ở 8.5s.
- Audio gốc của clip Veo: mute.
