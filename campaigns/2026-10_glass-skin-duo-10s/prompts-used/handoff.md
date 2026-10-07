# Handoff — Glass Skin Duo — "Sixty Seconds" (cổng 2)

> Prompt video copy nguyên văn từ `prompt-pack.md` → mục "Thẻ video". Prompt âm thanh từ `audio-plan.md`. File này chỉ là danh sách việc + thứ tự.

## A. Việc của user

### 1. Render 3 clip Veo 3.1 (image-to-video · 9:16 · 1080p · 4s · không last frame)
| Scene | Ảnh first frame (`outputs/images/`) | Prompt | Lưu về `outputs/videos/` | Kiểm khung cuối |
|---|---|---|---|---|
| S01 | `KREIZI-2026-10-GLASSDUO_B-01_S01-cheek-press_v1.png` | prompt-pack §S01 | `KREIZI-2026-10-GLASSDUO_S01_cheek-press_v1.mp4` | Mắt mở, tay ra khỏi khung, mặt không trôi |
| S02 | `KREIZI-2026-10-GLASSDUO_B-02_S02-serum-pump_v1.png` | prompt-pack §S02 | `KREIZI-2026-10-GLASSDUO_S02_serum-pump_v1.mp4` | 1 giọt gel trên đầu ngón, label không nhoè |
| S03 | `KREIZI-2026-10-GLASSDUO_B-03_S03-booster-dip_v1.png` | prompt-pack §S03 | `KREIZI-2026-10-GLASSDUO_S03_booster-dip_v1.mp4` | Ngón nhấc lên có kem, chữ KREIZI không méo |

Clip lỗi → mô tả lỗi cho Claude (cảnh · giây · lỗi), Claude viết prompt sửa theo mẫu trong `_prompts/handoff-template.md`. Không render lại cảnh đã đạt.

### 2. Âm thanh → `outputs/audio/`
- **VO** 4 file `vo-S01..S04` — chỉ dẫn giọng + lời ở `audio-plan.md` §A. (Hoặc bật connector ElevenLabs, Claude gen giúp.)
- **Nhạc** `KREIZI-2026-10-GLASSDUO_music_v1.mp3` — prompt ở `audio-plan.md` §B.
- **SFX** pump click (tuỳ chọn) — `audio-plan.md` §C.

### 3. (Tuỳ chọn) Logo Kreizi
Thả `logo-kreizi.svg`/`.png` nền trong vào `_brand/kreizi-beauty/brand-assets/` → end card có logo. Không có thì end card chỉ chữ.

## B. Timeline phối âm (dự kiến, chốt theo VO thật)
| Mốc | VO | Nhạc | SFX |
|---|---|---|---|
| 0.0–3.0 | vo-S01 từ ~0.3s | vào nhẹ | — |
| 3.0–6.0 | vo-S02 | duck | sfx-01 ~3.6s |
| 6.0–8.3 | vo-S03 | duck | — |
| 8.3–10.0 | vo-S04 | lift nhẹ → fade | — |

## C. Hướng dẫn dựng (Claude làm ở cổng 3, Remotion)
| # | Cảnh | In–out timeline | Nối | Chữ (lower third, không em dash) |
|---|---|---|---|---|
| 1 | S01 | 0.0–3.0 | hard cut | "2 steps. 60 seconds." |
| 2 | S02 | 3.0–6.0 | hard cut | "Step 1 · Glass Skin Serum" |
| 3 | S03 | 6.0–8.3 | hard cut | "Step 2 · Moisture Booster" |
| 4 | S04 end card | 8.3–10.0 | fade out | "The Glass Skin Duo" · "Hydrates · Smooths · Glows" · "For skin 40+" (nửa trên) |

- S04: ảnh thật `_products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png` (1:1) đặt nửa dưới khung, nền kem `#EFE6DA` phía trên (lấy mẫu màu tường từ ảnh khi dựng), zoom code 1.00→1.03.
- Cân màu: ấm ~4500K, giữ tông da tự nhiên, khớp 3 clip.
- Xuất: 1080×1920 · 30fps · H.264 · -14 LUFS · `outputs/final/KREIZI-2026-10-GLASSDUO_productdemo_maren_glass-skin-duo_9x16_v1.mp4`.

## D. Tiêu chí duyệt
☐ 10s, 9:16 ☐ Maren nhất quán ☐ chai xanh + hũ trắng đúng, label không méo ☐ tay không lỗi ☐ chỉ claim APPROVED ☐ chữ đọc được trên điện thoại ☐ VO không gấp ☐ nhạc không lấn lời ☐ AI disclosure bật khi đăng Meta
