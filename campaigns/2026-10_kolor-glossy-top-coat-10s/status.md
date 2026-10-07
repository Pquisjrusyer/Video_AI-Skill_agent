# Status — Kolor Glossy Top Coat — 10s

> Quy trình 3 cổng: `_workflows/production-steps.md`. Duyệt: "ok cổng 1/2/3".
> Brand: Kolor Acrylic · Code: `KOLOR-2026-10-TOPCOAT` · Format: **Voiceover** ✅ (chốt 2026-10-05) · Ratio: 9:16 · Duration: 10s

| Cổng | Gồm | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 1. Kế hoạch | `brief.md` · `scripts/script.md` · `scripts/storyboard.md` · thẻ ảnh trong `prompts-used/prompt-pack.md` | ✅ | jason.do | 2026-10-05 |
| 2. Ảnh | QC ảnh · thẻ video · `audio-plan.md` · VO · `handoff.md` + clip, nhạc, SFX (Claude làm) | ☑ | | 2026-10-05 |
| 3. Final | kiểm file · review · `outputs/final/` | ☐ | | |

☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** User render S01 v2 + S02 v2 trên Dreamina (Seedance) theo `prompt-pack.md` → "Thẻ video v2" → thả vào `outputs/videos/` → Claude QC → "ok cổng 2".

## Asset
| Tên file | Loại | Ai gen | Xong | QC |
|---|---|---|---|---|
| `KOLOR-2026-10-TOPCOAT_A-01_nail-base-satin_v1.png` | ảnh nền | Claude (GPT Image 2, high) | ✅ | worked. Móng nhỏ hơn thẻ (~10% khung), chấp nhận |
| `KOLOR-2026-10-TOPCOAT_B-01_S01-brush_v1.png` | first frame S01 | Claude (GPT Image 2) | ✅ | worked |
| `KOLOR-2026-10-TOPCOAT_B-02_S02-glossy_v1.png` | first frame S02 | Claude (GPT Image 2) | ✅ | worked |
| `KOLOR-2026-10-TOPCOAT_B-03_S01-tech-brush_v1.png` | first frame S01 v2 | Claude (GPT Image 2) | ✅ | worked. Tay thợ cầm nắp trắng, cọ chạm mép móng giữa |
| `KOLOR-2026-10-TOPCOAT_B-04_S02-lamp_v1.png` | first frame S02 v2 | Claude (GPT Image 2) | ✅ | worked. Đèn LED trắng không chữ |
| `KOLOR-2026-10-TOPCOAT_S01_one-coat_v2.mp4` | clip 5s | User (Dreamina/Seedance) | ☐ | |
| `KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v2.mp4` | clip 5s | User (Dreamina/Seedance) | ☐ | |
| `…_S01_one-coat_v1.mp4` | clip code | Claude | ❌ | User loại: dựng bằng code xấu |
| `…_S02_shine-sweep_v1.mp4` | clip code | Claude | ❌ | User loại |
| `KOLOR-2026-10-TOPCOAT_vo-S01..S03_v1.mp3` | VO ×3 | Claude (OpenAI TTS, nova) | ✅ | ☑ Lời đúng script, vừa slot (2.53/2.04/2.77s lời) |
| `KOLOR-2026-10-TOPCOAT_music_v1.mp3` | nhạc 12s | Claude (tổng hợp bằng code, `prompts-used/synth-audio.py`) | ✅ | ☑ Không vocal, 100 BPM, accent 5.0s + 6.5s. Chất nhạc synth đơn giản |
| `KOLOR-2026-10-TOPCOAT_sfx-01_brush-swipe_v1.mp3` · `_sfx-02_shine-ting_v1.mp3` | SFX ×2 | Claude (tổng hợp bằng code) | ✅ | ☑ 2.0s · 1.2s |

## Vấn đề (mỗi ý 1 dòng)
- 2026-10-05 — Tạo mới `_products/Kolor/kolor-glossy-top-coat/` từ trang SP + 6 ảnh official. Claim còn DRAFT, duyệt cùng cổng 1.
- 2026-10-05 — Ảnh official-04 có watermark ✦ (ảnh AI) → chỉ dùng làm ref tư thế, không dùng trực tiếp.
- 2026-10-05 — Ảnh official-03 ghi "Non-toxic" → không dùng nguyên ảnh trong video.
- 2026-10-05 — Connector ElevenLabs chưa thấy trong session lúc tạo campaign → cần bật trước cổng 2 (VO + nhạc).
- 2026-10-05 — `_tools/gen-image.py` lỗi in tiếng Việt trên Windows (cp1252) sau khi đã lưu ảnh → đã thêm reconfigure stdout UTF-8. Máy Windows: đã tạo `python3.exe` cạnh `python.exe`.
- 2026-10-05 — Cổng 2: connector ElevenLabs vẫn không có → VO + nhạc thành thẻ cho user tự gen.
- 2026-10-05 — VO gen bằng OpenAI TTS thay ElevenLabs (user cho phép: "không cần thiết là trên eleven lab"). Giọng khác Lyan của Blooming Gel.
- 2026-10-05 — faster-whisper trên máy này phải chạy `device="cpu"` (không có CUDA/cublas).
- 2026-10-05 — User yêu cầu Claude gen luôn clip + SFX + nhạc (thay quy ước user tự gen). Máy chỉ có OPENAI_API_KEY → clip dùng Sora 2 Pro (prompt chuyển từ thẻ Veo: `prompts-used/S0x_sora.txt`), nhạc + SFX tổng hợp bằng numpy.
- 2026-10-05 — Lệnh Sora bị auto mode chặn (script tự đọc `~/.config/ai-studio/.env`). Chờ user.
- 2026-10-05 — Sora không dùng được: API trả 404, OpenAI đã tắt Sora API từ 2026-09-24. Đã xoá `_tools/sora-video.py`. Quyền `Bash(python _tools/sora-video.py:*)` trong `~/.claude/settings.json` của user giờ thừa, user có thể xoá.
- 2026-10-05 — User yêu cầu gen video không cần Sora, không có API video nào khác → S01/S02 dựng bằng code (numpy + PyAV) từ ảnh đã duyệt, hiệu ứng chỉ trong vùng móng (mask theo màu đỏ). Đổi so với storyboard: S01 bỏ cọ quét (chỉ còn chuyển satin → bóng), S02 tay không nghiêng. Route thực tế = MOTION-GRAPHIC. Muốn có cọ thật → render Veo theo `handoff.md` §A, thay file `_v2`.
- 2026-10-05 — User loại clip dựng bằng code, muốn "thật hơn, đúng quy trình sơn". Concept v2: S01 tay thợ cầm cọ quét thật (B-03), S02 rút tay khỏi đèn LED (B-04). Render bằng Dreamina/Seedance (free, dùng thương mại theo review — user kiểm điều khoản). Lời VO giữ nguyên.
