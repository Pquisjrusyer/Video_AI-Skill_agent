# Handoff — `KREIZI-2026-10-ACTIVES` (cổng 2)

> Việc của bạn: render 3 clip Veo theo mục A, chọn 3 SFX theo mục B, rồi bỏ file vào `outputs/videos/` và `outputs/audio/` **đúng tên**. Xong nhắn "clip đã thả vào".
> Ảnh đầu vào nằm trong `outputs/images/`. Prompt copy nguyên văn từ `prompt-pack.md` → mục "Thẻ video".

## A. Bảng render

| Clip | Ảnh đầu vào | Render | Dùng | Lưu về `outputs/videos/` |
|---|---|---|---|---|
| S01 | First = `KREIZI-2026-10-ACTIVES_B-01_S01-actives-above-skin_v1.png` · Last = `KREIZI-2026-10-ACTIVES_B-02_S01-glass-surface_v1.png` | 6s (8s nếu tool bắt buộc khi có last frame) | 3.5s | `KREIZI-2026-10-ACTIVES_S01_actives-to-glass_v1.mp4` |
| S02 | First = `KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v3.png` | 4s | 2.5s | `KREIZI-2026-10-ACTIVES_S02_hand-gel-spread_v1.mp4` |
| S03 | First = `KREIZI-2026-10-ACTIVES_A-02_serum-underwater_v1.png` | 4s | 4.0s | `KREIZI-2026-10-ACTIVES_S03_serum-underwater_v1.mp4` |

Tất cả: Veo 3.1 · image-to-video · 9:16 · 1080p · audio của clip sẽ bị mute.

**Kiểm nhanh khi render xong:**
- S01: quả cầu tan **ở bề mặt**, không chìm xuống nang lông hay lớp sâu. Không có chữ hoặc mũi tên.
- S02: tay đủ 5 ngón suốt clip, gel tán mỏng, không chảy.
- S03: chữ trên label chai không méo.
Lỗi → xem dòng "Lỗi hay gặp → sửa" dưới mỗi thẻ video.

## B. Âm thanh

| File | Trạng thái |
|---|---|
| `vo-S01_v1.mp3` · `vo-S02_v1.mp3` · `vo-S03_v1.mp3` | ✅ Claude đã gen + tải (giọng Matilda) |
| `music_v1.mp3` | ✅ Claude đã gen + chọn (alt: `music-alt_v1.mp3`) |
| `sfx-01_bubble-pop_v1.mp3` · `sfx-02_droplet_v1.mp3` · `sfx-03_underwater-whoosh_v1.mp3` | ☐ **Bạn gen/chọn**, prompt ở `audio-plan.md` §C |

Timeline phối âm: xem `audio-plan.md` → Bảng âm thanh.

## C. Hướng dẫn dựng (Claude làm ở cổng 3)

| # | Cảnh | Timeline | Nối | Chữ | Âm |
|---|---|---|---|---|---|
| 1 | S01 | 0.0–3.5s | → crossfade 6 frame | 4 nhãn hoạt chất 0.3–2.4s · "Four actives. One glow." 2.0–3.5s, top third | vo-S01 0.3s · sfx-01 · nhạc vào |
| 2 | S02 | 3.5–6.0s | → hard cut | "Hyaluronic Acid" / "Holds up to 1,000x its weight in water" 3.8–6.0s, lower third | vo-S02 3.8s · sfx-02 |
| 3 | S03 | 6.0–10.0s | hết | "Luminous Glass Skin Serum" / "Designed for skin 40+" / "KREIZI BEAUTY" 6.6–10s, top third, trắng | vo-S03 6.2s · sfx-03 · nhạc đỉnh rồi fade |

Không em dash trên màn hình. Không logo (brand-assets trống). Xuất 1080×1920 · 30fps · H.264 · -14 LUFS → `outputs/final/KREIZI-2026-10-ACTIVES_voiceover_nochar_glass-skin-serum_9x16_v1.mp4`.

## D. Tiêu chí duyệt
Theo `_prompts/handoff-template.md` §D + Meta compliance trong `CLAUDE.md` (bật AI disclosure).
