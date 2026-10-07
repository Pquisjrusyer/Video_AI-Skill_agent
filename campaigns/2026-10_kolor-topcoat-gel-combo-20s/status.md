# Status — Kolor Top Coat & Gel Polish Combo — 20s

> Quy trình 3 cổng: `_workflows/production-steps.md`. Duyệt: "ok cổng 1/2/3".
> Brand: Kolor Acrylic · Code: `KOLOR-2026-10-COMBO` · Format: **Voiceover** ✅ (chốt 2026-10-07) · Biến thể: chỉ **Glossy** · Ratio: 9:16 · Duration: 20s

| Cổng | Gồm | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 1. Kế hoạch | `brief.md` · `scripts/script.md` · `scripts/storyboard.json/.md/.html` · thẻ ảnh trong `prompts-used/prompt-pack.md` | ✅ (duyệt bản chữ, chưa có ảnh minh hoạ) | jason.do | 2026-10-07 |
| 2. Ảnh | QC ảnh · thẻ video · `audio-plan.md` · VO · `handoff.md` | ☑ (chờ user render clip + nhạc/SFX) | | 2026-10-07 |
| 3. Final | kiểm file · review · `outputs/final/` | ☐ | | |

☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** User render S01–S05 trên Flow theo `outputs/review/clip-board.html` → thả vào `outputs/videos/` + chọn nhạc/SFX theo `audio-plan.md` → nhắn "clip đã thả vào" → Claude chạy lại clip-board → "ok cổng 2" → cổng 3.

## Asset
| Tên file | Loại | Ai gen | Xong | QC |
|---|---|---|---|---|
| `outputs/review/storyboard/KOLOR-2026-10-COMBO_P-S01..S05_v1.png` | ảnh minh hoạ | — | bỏ | User duyệt cổng 1 không cần ảnh minh hoạ |
| `outputs/images/KOLOR-2026-10-COMBO_A-01_client-hand_v1.png` | ref tay | Claude (Cloudflare Flux) | ✅ | worked |
| `…_B-01_S01-first-stroke_v1/v2.png` | first frame S01 | Claude (Cloudflare) | ✅ chấp nhận (test) | dùng v2; cọ chạm da, prompt video cho cọ đi lên móng |
| `…_B-02_S02-even-coverage_v1.png` | first frame S02 | Claude (Cloudflare) | ✅ chấp nhận (test) | dùng v1; dụng cụ giống nhíp + lem đen |
| `…_B-03_S03-led-cure_v2.png` | first frame S03 | Claude (Cloudflare) | ✅ | worked (v2) |
| `outputs/audio/KOLOR-2026-10-COMBO_vo-S01..S06_v1.mp3` | VO ×6 | Claude (ElevenLabs Lyan, eleven_v3) | ✅ | 2.40/3.36/2.80/3.28/2.64/2.48s. S03 vượt slot 0.3s → chỉnh timeline ở cổng 3. Chưa kiểm lời bằng whisper (máy thiếu RAM) |
| `outputs/videos/KOLOR-2026-10-COMBO_S01..S05_*_v1.mp4` | clip ×5 | User (Flow) | ☐ | |
| `outputs/audio/KOLOR-2026-10-COMBO_music_v1.mp3` + sfx-01..03 | nhạc + SFX | User | ☐ | |
| `…_B-04_S04-topcoat_v1/v2.png` | first frame S04 | Claude (Cloudflare) | ✅ chấp nhận (test) | dùng v2; cọ + giọt top coat trên da |
| `…_B-05_S05-mirror-shine_v1/v2.png` | first frame S05 | Claude (Cloudflare) | ✅ chấp nhận (test) | dùng v2; 1 móng còn loang |

## Vấn đề (mỗi ý 1 dòng)
- 2026-10-07 — Tạo mới `_products/Kolor/kolor-topcoat-gel-combo/` từ trang SP + 7 ảnh official. Claim còn DRAFT, duyệt cùng cổng 1.
- 2026-10-07 — Biến thể Matte dùng chai vàng logo "XEIJAYI NAIL" (brand khác) → user chốt chỉ làm Glossy.
- 2026-10-07 — Ảnh official-02 ghi "Non-toxic" → không dùng nguyên ảnh.
- 2026-10-07 — Key OpenAI hết credit (429) khi gen ảnh minh hoạ → chưa có ảnh. VO bằng OpenAI TTS ở cổng 2 cũng cần credit.
- 2026-10-07 — OpenAI vẫn `insufficient_quota` sau khi user nạp (chưa nhận) → user chọn Cloudflare (Flux 2 klein, miễn phí) qua popup. Model này kém với cảnh cọ + móng cận: 4/5 keyframe failed.
- 2026-10-07 — User: dự án để test → chấp nhận ảnh Flux đã có, không gen lại.
- 2026-10-07 — VO_TOOL=openai hết credit → gen VO bằng connector ElevenLabs (lựa chọn kế), giọng Lyan như Blooming Gel.
- 2026-10-07 — faster-whisper không chạy được lúc này (máy báo thiếu RAM / WinError 1450) → kiểm lời VO dời sang cổng 3.
