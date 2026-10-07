# Audio plan — KOLOR-2026-10-STUDIO

Không VO. Nhạc + SFX thêm khi dựng; clip Veo mute.

## Bảng âm thanh
| Mốc | Scene | Nhạc | SFX | Đồng bộ hình |
|---|---|---|---|---|
| 0.0–3.0 | S01 | Pluck thưa, chưa có trống | sfx-01 swell 1.2s | Màu bắt đầu nở |
| 3.0–6.5 | S02 | Beat vào đúng 3.0s (cut) | sfx-02 tap ~5.0s | Nghiêng chai |
| 6.5–8.5 | S03 | Groove giữ | sfx-03 tick ×4 | Từng chữ hiện |
| 8.5–10.0 | S04 | Hit 8.5s → ring-out | sfx-04 pop 8.5s | End card |

## B. Nhạc nền
```
Duration: 12s (10s + 2s tail)
Mood/style/tempo: clean modern beauty, confident and light, 100 BPM
Instruments: soft synth pluck, warm sub bass, finger snaps, airy pad
Timeline: 0–3s sparse plucks only | 3s beat drops in (kick + snaps + bass) | 3–8.5s steady groove | 8.5s single bright hit then ring-out
Accent points: 3.0s (cut to model), 8.5s (end card)
Tail: 2s natural ring-out
Instrumental only, no vocals.
```
Nguồn: **Claude gen qua ElevenLabs MCP** — `eleven_music_v2_5`, flow `ACyreSGerJFaZvq7zyOW` (3 bản; bản 4 lỗi rate limit). **Đã chọn m1** (gen `LLHsa4ROg5cvtps8CvLV`) → `KOLOR-2026-10-STUDIO_music_v1.mp3`. Beat vào 3.5s → offset 0.5s khi dựng. Kết quả: worked. Lưu ý: node music mặc định `Instrumental=False` — prompt "no vocals" vẫn ra không lời, nhưng nên kiểm whisper.

## C. SFX
| Mã | Scene | Prompt (EN) | Chất | Dài | Mốc | Tránh |
|---|---|---|---|---|---|---|
| sfx-01 | S01 | soft airy swell, gentle shimmer rising | nhẹ, mềm, hơi vang | 1.5s | 1.2s | không "magic sparkle" lố |
| sfx-02 | S02 | single light tap of a small glass bottle on fingernail | khô, gần | 0.3s | ~5.0s | không vang |
| sfx-03 | S03 | four soft clean UI ticks, evenly spaced 0.5s | rất nhẹ | 2.0s | 6.5s | không chói |
| sfx-04 | S04 | soft rounded pop | ấm | 0.4s | 8.5s | không cartoon |

**Đã gen qua ElevenLabs MCP** (`eleven_text_to_sound_v2`, 2 take/loại, flow `ACyreSGerJFaZvq7zyOW`). Chọn take b cả 4 (gọn, transient rõ; click_a bị loãng 1.4s → loại). Mốc chốt: bloom 0.4s · click 4.8s · tick 6.5/6.9/7.3/7.7s · pop 8.5s. Kết quả: worked.

## D. Phối
-14 LUFS tổng · peak ≤ -1 dBTP · SFX nằm dưới nhạc ~3–6dB, chỉ nổi ở sfx-01 và sfx-04.
