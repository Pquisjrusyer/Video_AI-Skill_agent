# Status — Kolor Top Coat & Gel Polish Combo — 20s

> Quy trình 3 cổng: `_workflows/production-steps.md`. Duyệt: "ok cổng 1/2/3".
> Brand: Kolor Acrylic · Code: `KOLOR-2026-10-COMBO` · Format: **Voiceover** ✅ (chốt 2026-10-07) · Biến thể: chỉ **Glossy** · Ratio: 9:16 · Duration: 20s

| Cổng | Gồm | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 1. Kế hoạch | `brief.md` · `scripts/script.md` · `scripts/storyboard.json/.md/.html` · thẻ ảnh trong `prompts-used/prompt-pack.md` | ✅ (duyệt bản chữ, chưa có ảnh minh hoạ) | jason.do | 2026-10-07 |
| 2. Ảnh | QC ảnh · thẻ video · `audio-plan.md` · VO · `handoff.md` | ✅ (option 2: dùng clip v1, chưa có nhạc/SFX) | jason.do | 2026-10-07 |
| 3. Final | kiểm file · review · `outputs/final/` | ✅ (final v1, không nhạc) | jason.do | 2026-10-07 |

☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** Xong. Trước khi chạy ads: bật AI disclosure trên Meta, nghe lại 1.5x. Bản chạy thật nên render lại S04/S05 (prompt v2 `handoff.md` §E) + thêm nhạc/SFX + clip không watermark. Chạy xong → ghi `performance-notes.md`, campaign → `_archive/`.

## Asset
| Tên file | Loại | Ai gen | Xong | QC |
|---|---|---|---|---|
| `outputs/review/storyboard/KOLOR-2026-10-COMBO_P-S01..S05_v1.png` | ảnh minh hoạ | — | bỏ | User duyệt cổng 1 không cần ảnh minh hoạ |
| `outputs/images/KOLOR-2026-10-COMBO_A-01_client-hand_v1.png` | ref tay | Claude (Cloudflare Flux) | ✅ | worked |
| `…_B-01_S01-first-stroke_v1/v2.png` | first frame S01 | Claude (Cloudflare) | ✅ chấp nhận (test) | dùng v2; cọ chạm da, prompt video cho cọ đi lên móng |
| `…_B-02_S02-even-coverage_v1.png` | first frame S02 | Claude (Cloudflare) | ✅ chấp nhận (test) | dùng v1; dụng cụ giống nhíp + lem đen |
| `…_B-03_S03-led-cure_v2.png` | first frame S03 | Claude (Cloudflare) | ✅ | worked (v2) |
| `outputs/audio/KOLOR-2026-10-COMBO_vo-S01..S06_v1.mp3` | VO ×6 | Claude (ElevenLabs Lyan, eleven_v3) | ✅ | 2.40/3.36/2.80/3.28/2.64/2.48s. S03 vượt slot 0.3s → chỉnh timeline ở cổng 3. Whisper OK: lời đúng script (S03 nghe thêm "It" độ tin 0.29, giữ). Lời thật: 2.12/2.88/2.28/3.04/2.28/2.28s → S03 vừa slot |
| `outputs/videos/KOLOR-2026-10-COMBO_S01..S05_*_v1.mp4` | clip ×5 | User (Flow) | ✅ | 1080×1920 · 8s. S01 worked · S02 worked (lỗi nhíp từ ảnh) · S03 worked · S04 needs adjustment (top coat không lên móng) · S05 needs adjustment (tay đổi người từ 1.5s). Có watermark ✦ Flow. Chi tiết `handoff.md` §E |
| `outputs/audio/KOLOR-2026-10-COMBO_music_v1.mp3` + sfx-01..03 | nhạc + SFX | User | ☐ | chưa có → review-v1 không nhạc |
| `outputs/final/KOLOR-2026-10-COMBO_voiceover_nochar_topcoat-gel-combo_9x16_v1.mp4` | final | Claude (Remotion) | ✅ | = review-v1, user duyệt 2026-10-07 |
| `outputs/review/KOLOR-2026-10-COMBO_voiceover_nochar_topcoat-gel-combo_9x16_review-v1.mp4` | bản review | Claude (Remotion) | ✅ | 1080×1920 · 20.1s · −13.8 LUFS · review-board 6/6 OK. Clip phóng 1.18 giấu watermark ✦. S05 chậm 0.38x (0–1.33s) |
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
- 2026-10-07 — Remotion render lỗi khi để concurrency mặc định (máy thiếu tài nguyên) → render `--concurrency=2`. `post_edit.py loudnorm` lỗi trên Windows (gọi npx) → chạy ffmpeg loudnorm trực tiếp, cùng filter.
- 2026-10-07 — Compliance: claim trên màn hình + VO đều APPROVED · logo/nhãn từ ảnh official · 9:16 · chữ/CTA trong vùng an toàn Reels · không giá. Còn lại user làm khi đăng: bật AI disclosure. Không copy clip vào broll-library (clip có watermark Flow + dính sản phẩm).
