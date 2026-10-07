# Audio Plan — `KREIZI-2026-10-ACTIVES`

> Cổng 2, 2026-10-02. VO + nhạc đã gen qua ElevenLabs và tải về `outputs/audio/`. Flow: https://elevenlabs.io/app/flows/FbTGtBnOcgDJTusOFfoY

## Bảng âm thanh

| Mốc | Scene | Lời đọc | Cách đọc | Nhạc nền | SFX | Đồng bộ với hình | Chuyển sang cảnh sau | Tạo cùng clip / riêng |
|---|---|---|---|---|---|---|---|---|
| 0.0–3.5s | S01 | "Four actives... One glow." (VO 0.3–1.9s) | Chậm, nghỉ sau "actives" | Vào nhẹ từ 0s, piano thưa | sfx-01 bong bóng vỡ ×4, ~2.0–2.8s | Mỗi tiếng vỡ khớp 1 quả cầu chạm da | Crossfade 6 frame | Riêng |
| 3.5–6.0s | S02 | "Serum floods deep hydration." (VO 3.8–5.2s) | Nhấn nhẹ "deep hydration" | Pad dày lên | sfx-02 giọt gel chạm da, ~3.9s | Khớp lúc ngón chạm gel | Hard cut theo sfx-03 | Riêng |
| 6.0–10.0s | S03 | "Luminous Glass Skin Serum. Designed for skin forty plus." (VO 6.2–9.9s) | Ấm, chắc, hạ giọng cuối câu | Lên đỉnh ~6.5s, fade 9.5–10s | sfx-03 whoosh dưới nước, 6.0s | Khớp cut vào chai serum | Hết | Riêng |

## A. Voice-over

**Giọng:** Matilda, Knowledgable Professional (premade) · `voice_id: XrExE9yKIg1WjnnlVkGX` · model `eleven_multilingual_v2` · settings mặc định.
> Giọng đề xuất đầu tiên là Meshell (`4uXpMV2FG1JKkCQKIdSH`, library) nhưng cần gói Creator trở lên nên không gen được.

| File | Text | Dài thật (s) | Lời nói (whisper) | Slot (s) | Vừa? |
|---|---|---|---|---|---|
| `KREIZI-2026-10-ACTIVES_vo-S01_v1.mp3` | Four actives... One glow. | 2.12 | 0.00–1.54 | 3.5 | ✅ |
| `KREIZI-2026-10-ACTIVES_vo-S02_v1.mp3` | Serum floods deep hydration. | 1.91 | 0.00–1.36 | 2.5 | ✅ |
| `KREIZI-2026-10-ACTIVES_vo-S03_v1.mp3` | Luminous Glass Skin Serum. Designed for skin forty plus. | 4.26 | 0.00–3.68 | 4.0 | ✅ (sau khi chỉnh timeline) |

## B. Nhạc nền

File chọn: `KREIZI-2026-10-ACTIVES_music_v1.mp3` (12.0s, `eleven_music_v2_5`). Bản dự phòng: `music-alt_v1.mp3`.
Lý do chọn: whisper không bắt được vocal. Độ lớn lên dần và đạt đỉnh ở 5–7s (khoảng -23 dB), khớp lúc chai serum xuất hiện, rồi fade sau 8s. Bản alt đạt đỉnh ở 3–5s rồi tắt dần trước khi vào packshot.

```
Prompt: 12-second instrumental for a calm luxury skincare ad. Airy, clean, serene, around 70 BPM. Soft felt piano notes, shimmering glassy pads, subtle underwater bubble textures, light celesta sparkle. 0-4s delicate sparse piano and glassy shimmer. 4-7s warm pad swells gently. 7-10s opens up, brighter and fuller, a soft resolving chord. 10-12s gentle ring-out fade. Keep the mid range open for a female voiceover. Instrumental only, no vocals.
```

## C. SFX — user tự gen/chọn → `outputs/audio/`

| Mã | Scene | Prompt (EN) | Chất · cường độ | Dài | Mốc dự kiến | Tránh |
|---|---|---|---|---|---|---|
| `KREIZI-2026-10-ACTIVES_sfx-01_bubble-pop_v1.mp3` | S01 | Four soft delicate glassy bubble pops in quick succession, clean studio, no reverb tail | Nhẹ, trong | ~1s | 2.0–2.8s | Tiếng bóp nhựa, quá to |
| `KREIZI-2026-10-ACTIVES_sfx-02_droplet_v1.mp3` | S02 | A single soft gel droplet pressed on skin, subtle moist touch, close-up | Rất nhẹ | ~0.5s | 3.9s | Tiếng nước bắn |
| `KREIZI-2026-10-ACTIVES_sfx-03_underwater-whoosh_v1.mp3` | S03 | Gentle underwater whoosh with rising bubbles, calm deep water | Vừa, trầm | ~1.5s | 6.0s | Ồn, tiếng sóng biển |

Mốc SFX chốt lại theo clip thật ở cổng 3.

## D. Phối âm
VO trội hơn nhạc 10–12 dB khi có lời, nhạc nâng nhẹ ở khoảng trống. Tổng -14 LUFS, peak ≤ -1 dBTP. Audio gốc của clip Veo mute.
