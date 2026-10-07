# Status — Kolor Blooming Gel — Studio Model 10s

> Quy trình 3 cổng: `_workflows/production-steps.md`. Duyệt: "ok cổng 1/2/3".
> Brand: Kolor Acrylic · Code: `KOLOR-2026-10-STUDIO` · Format: **Product demo** ✅ (chốt 2026-10-01, Tịnh) · Ratio: 9:16 · Duration: 10s · Nhân vật: `nia` (mới)

| Cổng | Gồm | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 1. Kế hoạch | `brief.md` · `scripts/script.md` · `scripts/storyboard.md` · thẻ ảnh trong `prompts-used/prompt-pack.md` | ✅ | Tịnh (gen ảnh theo thẻ) | 2026-10-01 |
| 2. Ảnh | QC ảnh · thẻ video · `audio-plan.md` · `handoff.md` (không VO) | ◐ chờ B-03 | | |
| 3. Final | kiểm file · review · `outputs/final/` | ☑ review v4 (nhạc + SFX) chờ duyệt | | |

☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** Tịnh xem `outputs/review/KOLOR-2026-10-STUDIO_review_music-sfx_v4.mp4` → góp ý · chốt "Marble" vs ảnh da báo → "ok cổng 3" → Claude xuất final.

## Asset
| Tên file | Loại | Ai gen | Xong | QC |
|---|---|---|---|---|
| `KOLOR-2026-10-STUDIO_A-01_nia-seed_v1.png` | seed | Người dùng | ✅ | ✅ pass — copy sang `_characters/nia/reference-images/nia-face-ref-01.png` |
| `KOLOR-2026-10-STUDIO_B-01_S01-dot_v1.png` | first frame S01 | Người dùng | ✅ | ✅ pass — chấm hơi nổi khối, chấp nhận |
| `KOLOR-2026-10-STUDIO_B-02_S02-nia-bottle_v1.png` | first frame S02 | Người dùng | ✅ | ✅ pass — label đúng |
| `KOLOR-2026-10-STUDIO_S01_dot-bloom_v1.mp4` | clip 4s | Người dùng | ✅ | ✅ pass — máy đứng yên, nền giữ xám, hoa nở ~0.3–2.0s. 720p + watermark ✦ |
| `KOLOR-2026-10-STUDIO_S02_nia-bottle_v1.mp4` | clip 4s | Người dùng | ✅ | ✅ Tịnh chấp nhận label nhoè (S04 dùng ảnh thật). Chuyển động + mặt đạt; chữ label nhoè từ khung đầu ("kolör", dòng nhỏ vỡ) — do 720p, không phải do chuyển động. 720p + watermark ✦ |
| `KOLOR-2026-10-STUDIO_B-03_S03-hand-patterns_v1.png` (QC) | ảnh tĩnh S03 | Người dùng | ✅ | ⚠️ móng giữa ra **da báo**, không phải marble → lệch chữ "Marble" |
| `KOLOR-2026-10-STUDIO_music_v1.mp3` | nhạc | Claude (ElevenLabs MCP, Claude tự chọn + tải) | ✅ | Bản m1/3: không vocal (whisper), beat vào 3.5s → offset 0.5s khi dựng. m2 beat trễ 4.5s + tắt 8.5s; m3 beat sớm 2.0s |
| `_sfx-01..04_*` | SFX | Claude (ElevenLabs MCP, take b mỗi loại) | ✅ | bloom 0.4s · click 4.8s · tick ×4 6.5–7.7s · pop 8.5s — cắt/fade trong Remotion |
| `outputs/review/KOLOR-2026-10-STUDIO_review_music-sfx_v4.mp4` | review nhạc + SFX | Claude | ✅ | -14 LUFS, peak -2.4 dBFS |
| `outputs/review/KOLOR-2026-10-STUDIO_review_music_v3.mp4` | bản review có nhạc | Claude | ✅ | -14 LUFS, nhạc fade in/out |
| `outputs/review/KOLOR-2026-10-STUDIO_review_no-music_v2.mp4` | bản nháp không nhạc | Claude | ✅ | v2: sửa nút CTA lệch, bỏ em dash ở S02. 10.0s · 1080×1920 · watermark đã cắt |
| `KOLOR-2026-10-STUDIO_B-03_S03-hand-patterns_v1.png` | ảnh tĩnh S03 | Người dùng | ☐ | |

## Vấn đề (mỗi ý 1 dòng)
- Áp dụng bài học `KOLOR-2026-10-BLOOM`: giọt "hạt cườm", móng nhỏ trong khung, Veo xoay máy/đổi nền, watermark ✦ + 720p ở clip Veo → đã viết sẵn vào thẻ ảnh; xử lý watermark/720p ở cổng 3.
- Chưa có logo Kolor → end card chỉ có chữ.
- 2026-10-01 — tên file B-02 bị dư " .png" → Claude đã sửa. Nhắc: đặt tên đúng thẻ.
- 2026-10-01 — S02 label nhoè ngay khung 0.05s (B-02 gốc sắc nét) → nguyên nhân: Veo xuất 720p, không phải chuyển động. Prompt sửa chuyển động không giúp.
- 2026-10-01 — clip đã render trước khi có B-03 + "ok cổng 2" — chấp nhận vì S01/S02 không phụ thuộc B-03.
- 2026-10-01 — nhạc gen qua ElevenLabs MCP (flow `ACyreSGerJFaZvq7zyOW`, 3 bản) theo yêu cầu Tịnh. Quy trình đổi: nhạc nền do Claude gen qua MCP.
- 2026-10-01 — Claude TẢI ĐƯỢC file từ storage.googleapis.com trên máy này (ghi chú cũ "bị chặn" chỉ đúng ở môi trường khác) → nhạc/VO Claude tự tải về.
