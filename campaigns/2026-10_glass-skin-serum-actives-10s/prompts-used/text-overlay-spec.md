# Text Overlay Spec — `KREIZI-2026-10-ACTIVES` (user tự chèn chữ)

> Video gốc không chữ: `outputs/review/KREIZI-2026-10-ACTIVES_review_v2_notext.mp4` (1080×1920 · 30fps · 10s · có VO + nhạc).
> Toạ độ tính trên khung 1080×1920, gốc (0,0) ở góc trái trên. Mọi chữ đều là claim APPROVED, **không sửa câu chữ** (đổi câu → hỏi lại để check claim). Không dùng em dash.

## Style chung

| Thuộc tính | Giá trị |
|---|---|
| Font | **Cormorant Garamond** (Google Fonts), SemiBold 600 cho nhãn/tiêu đề nhỏ, Medium 500 cho câu chính |
| Màu S01–S02 | Nâu đậm `#4A2E22` |
| Màu S03 | Trắng `#FFFFFF` + bóng mờ `0 2px 18px rgba(0,30,40,0.55)` |
| Effect vào mặc định | **Fade + trượt lên**: opacity 0→1 và dịch từ +18px về 0, dài ~0.45s (14 frame), ease-out mềm, không nảy |
| Effect ra | Fade out 0.27s (8 frame), hoặc biến mất theo cut cảnh |
| Vùng an toàn | Chừa ~250px dưới cùng (UI Reels/caption Meta) và ~120px trên cùng |

## Timeline chữ

| # | Vào (s) | Ra (s) | Chữ (nguyên văn) | Vị trí | Cỡ · weight | Effect |
|---|---|---|---|---|---|---|
| 1 | 0.30 | 2.60 | Green / Seaweed (2 dòng) | Căn giữa x=155, top y=790 (ngay trên quả cầu xanh lá) | 48px · 600 · line-height 1.05 | Fade + trượt lên. Ra: fade 2.60–2.87 |
| 2 | 0.70 | 2.60 | Red / Algae (2 dòng) | Căn giữa x=408, top y=790 (trên quả cầu hồng) | 48px · 600 | Như #1 |
| 3 | 1.10 | 2.60 | Niacinamide | Căn giữa x=663, top y=790 (trên quả cầu trong) | 48px · 600 | Như #1 |
| 4 | 1.50 | 2.60 | Hyaluronic / Acid (2 dòng) | Căn giữa x=925, top y=790 (trên quả cầu xanh dương) | 48px · 600 | Như #1 |
| 5 | 2.00 | 3.50 (cut) | Four actives. / One glow. (2 dòng) | Căn giữa ngang, top y=250 | 92px · 500 · line-height 1.05 | Fade + trượt lên, giữ đến hết cảnh, tan theo crossfade sang S02 |
| 6 | 3.80 | 6.00 (cut) | HYALURONIC ACID (dòng trên) + Holds up to 1,000x its weight in water (dòng dưới) | Khung bo góc 28px, nền kem `rgba(250,246,240,0.86)`, padding 30×36px, cách trái/phải 90px, đáy khung cách đáy video 230px | Dòng trên 40px · 600 · IN HOA · letter-spacing 2px. Dòng dưới 54px · 500, cách dòng trên 8px | Cả khung fade + trượt lên. Ra theo hard cut |
| 7 | 6.60 | 10.00 | Luminous Glass Skin Serum | Căn giữa ngang, top y≈120 | 74px · 600 · trắng + bóng | Fade + trượt lên |
| 8 | 7.20 | 10.00 | Designed for skin 40+ | Ngay dưới #7, cách 14px | 48px · 500 · trắng + bóng | Fade + trượt lên |
| 9 | 8.00 | 10.00 | KREIZI BEAUTY | Dưới #8, cách 26px | 34px · 600 · letter-spacing 12px · trắng + bóng | Fade + trượt lên |

**S03 (6.0–10s):** bản có chữ có thêm 1 lớp gradient tối ở phần trên để chữ trắng dễ đọc: `linear-gradient(180deg, rgba(5,30,36,0.55) 0%, rgba(5,30,36,0) 28%)`, phủ toàn khung từ 6.0s. Bản không chữ đã bỏ lớp này, bạn thêm lại nếu chữ khó đọc.

## Mốc VO để canh chữ

| VO | Giây | Lời |
|---|---|---|
| vo-S01 | 0.3–1.9 | "Four actives... One glow." |
| vo-S02 | 3.8–5.2 | "Serum floods deep hydration." |
| vo-S03 | 6.2–9.9 | "Luminous Glass Skin Serum. Designed for skin forty plus." |

Cut cảnh: S01→S02 crossfade 3.50–3.70s · S02→S03 hard cut 6.00s.

## Timeline âm thanh (khi tự ghép trên bản không tiếng)

Video hình trơn (không chữ, không tiếng): `outputs/review/KREIZI-2026-10-ACTIVES_review_v4_notext_noaudio.mp4`. File âm thanh ở `outputs/audio/`.

| File | Đặt ở giây | Cắt / dùng | Âm lượng (gợi ý) |
|---|---|---|---|
| `KREIZI-2026-10-ACTIVES_vo-S01_v1.mp3` | 0.30 | cả file (lời 0–1.54s) | 100% |
| `KREIZI-2026-10-ACTIVES_vo-S02_v1.mp3` | 3.80 | cả file (lời 0–1.36s) | 100% |
| `KREIZI-2026-10-ACTIVES_vo-S03_v1.mp3` | 6.20 | cả file, cắt ở 10.0s (lời 0–3.68s) | 100% |
| `KREIZI-2026-10-ACTIVES_music_v1.mp3` | 0.00 | cắt ở 10.0s, fade out 9.5–10.0s | ~42%, hạ còn ~13% khi có VO (ducking) |
| `KREIZI-2026-10-ACTIVES_sfx-01_bubble-pop_v1.mp3` | 1.05 · 1.20 · 1.35 · 1.50 (4 lần) | cả file 0.5s | 55% · 45% · 50% · 42% |
| `KREIZI-2026-10-ACTIVES_sfx-02_droplet_v1.mp3` | 3.45 | lấy đoạn 1.4–2.2s trong file | 90% |
| `KREIZI-2026-10-ACTIVES_sfx-03_underwater-whoosh_v1.mp3` | 5.95 | cả file 0.5s | 60% |

Xuất xong: chuẩn hoá -14 LUFS, peak ≤ -1 dBTP.
