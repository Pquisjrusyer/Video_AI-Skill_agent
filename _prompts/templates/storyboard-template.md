# Storyboard — [TÊN CAMPAIGN]

> **Cách dùng:** Điền ở `/storyboard` sau khi script qua cổng B (trước khi mở `_skills/video/`/`_skills/motion-graphic/`). Xem `_skills/scene-routing/SKILL.md` để biết cách chia scene và gắn route tag.
> **Naming:** lưu tại `scripts/storyboard.md` trong campaign này.

---

## Metadata

| Field | Thông tin |
|-------|-----------|
| **Campaign** | [Campaign code] |
| **Duration tổng** | [15s / 20s / 30s] |
| **Ratio** | [9:16 / 4:5 / 1:1] |
| **Format** | [Testimonial / Product demo / Graphic-only / Mixed] |

---

## Scene breakdown

| Mã | Bắt đầu–Kết thúc | Dài | Mục đích | Hình đầu cảnh | 1 hành động chính | Cỡ cảnh · góc | Camera (1 move / static) | Hình cuối cảnh | Nối sang cảnh sau | Chữ hiển thị | Lời đọc | Nhạc · SFX | Route | Rủi ro AI → đơn giản hoá |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 0.0–_s | | | | | | | | | | | | AI-VIDEO / MOTION-GRAPHIC | |

Quy tắc:
- Tổng thời lượng = **chính xác** duration brief; không có khoảng trống ngoài chủ ý.
- Hành động quá phức tạp → tách cảnh. Không bắt buộc cảnh nào cũng có lời; lời ngắn, có chỗ nghỉ.
- Giữ hướng chuyển động + hướng/nhiệt màu ánh sáng nhất quán giữa các cảnh liền kề.
- Phân biệt **chuyển động thật** (AI-VIDEO) với **hiệu ứng minh hoạ** (MOTION-GRAPHIC / overlay).
- Mỗi cảnh = 1 clip render riêng. Gộp cảnh chỉ khi user yêu cầu.
- Cột "Rủi ro AI": cảnh dễ lỗi (tay trong gương, chất lỏng, camera orbit quanh mặt, label khi rack focus…) + cách đơn giản hoá.

> Route mập mờ → đọc `_skills/scene-routing/references/scene-routing-rules.md` trước khi quyết.

---

## Assembly notes

- Transition scene 1→2: [hard cut / crossfade / wipe]
- Transition scene 2→3: [...]

### Audio

| Loại | Có dùng? | Nguồn file | Scene áp dụng |
|------|----------|------------|----------------|
| Nhạc nền | [Có/Không] | [người dùng tự gen/chọn theo prompt 4D → `outputs/audio/`. VD: 2026-06-LAUNCH_music_v1.mp3] | Toàn video / scene [X]–[Y] |
| Voiceover | [Có/Không] | [ElevenLabs — Claude gen ở `/assets` 4D → `outputs/audio/`. VD: 2026-06-LAUNCH_vo-S01_v1.mp3] | Scene [X] |
| SFX | [Có/Không] | [người dùng tự gen/chọn theo prompt 4D → `outputs/audio/`. VD: 2026-06-LAUNCH_sfx-01_pump-click_v1.mp3] | Scene [X] |
| Audio gốc từ clip AI-VIDEO | [Có/Không] | [mặc định mute khi dựng — chỉ dùng khi audio-plan đánh dấu "tạo cùng clip"] | Scene [X] |

> Nếu có Voiceover: duration của scene đó phải set theo độ dài file audio thật (xem `_skills/motion-graphic/references/audio-and-voice.md` — `calculateMetadata`), không hardcode số frame cố định.
> Nếu có cả nhạc nền + voiceover: cần ducking (hạ nhạc khi có voice) — xem cùng file trên.

---

## Hand-off checklist

- [ ] Mọi scene AI-VIDEO có route + danh sách ảnh — thẻ prompt ảnh làm ở `/assets` 4A, thẻ prompt video (`_prompts/veo3/video-prompt-card.md`) làm ở `/assets` 4C
- [ ] Mọi scene MOTION-GRAPHIC có mô tả nội dung — animation spec làm ở `/edit` (qua `_skills/motion-graphic/`)
- [ ] Đã xác nhận thứ tự + transition trước khi build
- [ ] Nếu có voiceover — VO chỉ từ ElevenLabs (`/assets` 4D), có sẵn trong `outputs/audio/` trước khi build scene đó

---

## Danh sách ảnh

### A. Ảnh tham chiếu — khoá nhận diện / sản phẩm / bối cảnh / tư thế / chất liệu / phong cách
| Mã | Nội dung | Vai trò | Dùng cho cảnh | Dùng trực tiếp / chỉnh sửa / tạo mới | Ref cần + vai trò | Bắt buộc giữ | Prompt nháp |
|---|---|---|---|---|---|---|---|

### B. Ảnh dùng trực tiếp cho video — khung đầu / trung gian / cuối
| Mã | Nội dung | Vai trò (first / mid / last frame) | Dùng cho cảnh | Dùng trực tiếp / chỉnh sửa / tạo mới | Ref cần + vai trò | Bắt buộc giữ | Prompt nháp |
|---|---|---|---|---|---|---|---|

Quy tắc: ảnh đã đạt → "Dùng trực tiếp", không tạo lại · contact sheet nhiều góc chỉ ở nhóm A, không làm khung video · khung trung gian/cuối chỉ khi thực sự giúp kiểm soát · không mặc định tool render hỗ trợ mọi ảnh/ref trong danh sách.

---

## Danh sách asset (bắt buộc — dùng cho ⛔ C và chặng 4–5 (/assets, /check) trong `_workflows/production-steps.md`)

| Asset | Loại (ảnh / clip / VO / nhạc / SFX / take UGC) | Nguồn (reuse / ảnh thật / gen mới) | Tên file | Ai gen | Render (s) — clip | Dùng (s) — clip |
|---|---|---|---|---|---|---|
| | | | | | | |

Tên file theo naming convention `[campaign-code]_[asset-id]_[mô-tả-ngắn]_v[n].[ext]` — VD: `2026-06-LAUNCH_A-01_seed-face_v1.png` · `2026-06-LAUNCH_B-01_S01-mirror_v1.png` · `2026-06-LAUNCH_S01_mirror_v1.mp4` · `2026-06-LAUNCH_vo-S01_v1.mp3` · `2026-06-LAUNCH_music_v1.mp3` · `2026-06-LAUNCH_sfx-01_pump-click_v1.mp3` · `2026-06-LAUNCH_take-A_v1.mp4`. Clip Veo render 4/6/8s; "Dùng" = đoạn cắt theo VO thật ở `/edit`.

