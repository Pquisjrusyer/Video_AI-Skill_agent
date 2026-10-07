# Storyboard — Glass Skin Duo — "Sixty Seconds"

## Metadata

| Field | Thông tin |
|-------|-----------|
| **Campaign** | `KREIZI-2026-10-GLASSDUO` |
| **Duration tổng** | 10s |
| **Ratio** | 9:16 |
| **Format** | Product demo |

Ánh sáng chung cả 4 cảnh: nắng sáng ấm từ **frame-left**, ~4500K, bóng mềm sang phải. Bề mặt: đá travertine kem. Lời: xem `script.md`.

---

## Scene breakdown

| Mã | Thời gian | Dài | Mục đích | Hình đầu cảnh | 1 hành động chính | Cỡ cảnh · góc | Camera | Hình cuối cảnh | Nối sang | Chữ | Lời | Nhạc · SFX | Route | Rủi ro AI → đơn giản hoá |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 0.0–3.0s | 3.0s | Hook: da glow, nhịp bình thản | Maren cận mặt 3/4, mắt nhắm, 2 đầu ngón tay vừa chạm gò má | Ấn nhẹ đầu ngón tay lên má, vuốt hướng lên, mở mắt | Close-up, ngang mắt | Push-in rất chậm | Tay rời má, da ánh glow trong nắng | Hard cut | "2 steps. 60 seconds." | "Two steps. Sixty seconds." | Nhạc vào nhẹ | AI-VIDEO | Mặt biến dạng khi tay chạm → chỉ 1 động tác ấn, không xoa nhiều; không có sản phẩm trong khung |
| S02 | 3.0–6.0s | 3.0s | Bước 1: serum | Tay trái ngửa, tay phải cầm chai serum xanh, đầu bơm ngay trên đầu ngón tay | Ấn bơm 1 lần, giọt gel trong hơi xanh rơi lên đầu ngón tay | Macro tay + chai, góc 30° | Static | Giọt gel nằm trên đầu ngón tay | Hard cut | "Step 1 · Glass Skin Serum" | "Serum floods deep hydration." | SFX bơm nhẹ (tuỳ chọn) | AI-VIDEO | Label chữ méo khi chai chuyển động → chai gần như đứng yên, chỉ đầu bơm nhấn xuống; chất lỏng → 1 giọt duy nhất |
| S03 | 6.0–8.5s | 2.5s | Bước 2: booster | Hũ Moisture Booster mở nắp trên travertine, kem chóp mềm, đầu ngón trỏ ngay trên mặt kem | Ngón trỏ chạm và múc 1 chút kem lên | Macro, góc 45° từ trên | Static | Ngón tay nhấc lên, có kem trên đầu ngón | Hard cut | "Step 2 · Moisture Booster" | "Booster locks it in." | — | AI-VIDEO | Chữ KREIZI trên hũ méo → hũ không xoay, chữ hướng thẳng camera; kem dính tay sai → chỉ múc 1 lần |
| S04 | 8.5–10.0s | 1.5s | End card | Packshot cặp serum + hũ trên travertine, tảo xanh + đỏ, nửa trên trống | Chữ hiện dần, ảnh zoom rất nhẹ | Medium, ngang | Static (zoom code nhẹ) | Giữ khung | — (hết) | "The Glass Skin Duo" · "Hydrates · Smooths · Glows" · "For skin 40+" | "Hydrates. Smooths. Glows." | Nhạc ra | MOTION-GRAPHIC | Ảnh tĩnh + chữ, không mô phỏng chuyển động. Không có logo (brand-assets trống) |

Tổng: 3.0 + 3.0 + 2.5 + 1.5 = **10.0s** ✅. Mốc thời gian sẽ chỉnh theo độ dài VO thật ở cổng 3.

---

## Assembly notes

- S01→S02→S03→S04: hard cut (10s quá ngắn cho crossfade).
- Hướng sáng frame-left giữ nguyên cả 4 cảnh.

### Audio

| Loại | Có dùng? | Nguồn file | Scene |
|------|----------|------------|-------|
| Nhạc nền | Có | Claude gen qua ElevenLabs (cổng 2) → `KREIZI-2026-10-GLASSDUO_music_v1.mp3` | Toàn video |
| Voiceover | Có | Claude gen ElevenLabs (cổng 2) → `KREIZI-2026-10-GLASSDUO_vo-S01..S04_v1.mp3` | S01–S04 |
| SFX | Tuỳ chọn | User chọn → `KREIZI-2026-10-GLASSDUO_sfx-01_pump-click_v1.mp3` | S02 |
| Audio gốc clip | Không | mute | — |

---

## Danh sách ảnh

### A. Ảnh tham chiếu
| Mã | Nội dung | Vai trò | Dùng cho cảnh | Nguồn | Ref cần | Bắt buộc giữ |
|---|---|---|---|---|---|---|
| A-01 | Seed mặt Maren, chân dung ngực trở lên, nắng frame-left | Khoá nhận diện | S01 (và tay S02/S03) | **Tạo mới** | — | Theo `profile.md` |
| A-02 | `_products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png` | Khoá bao bì 2 sản phẩm | S02, S03, S04 | **Dùng trực tiếp** | — | — |

### B. Khung đầu video
| Mã | Nội dung | Vai trò | Cảnh | Nguồn | Ref cần + vai trò | Bắt buộc giữ |
|---|---|---|---|---|---|---|
| B-01 | Maren cận mặt, ngón tay chạm má, mắt nhắm | first frame | S01 | Tạo mới | A-01 (nhận diện) | Mặt, tóc, áo choàng |
| B-02 | Tay cầm chai serum, đầu bơm trên đầu ngón tay | first frame | S02 | Tạo mới | A-02 (bao bì), A-01 (tông da tay, tay áo) | Chai xanh mờ, nắp trắng, chữ label |
| B-03 | Hũ booster mở nắp, ngón trỏ trên mặt kem | first frame | S03 | Tạo mới | A-02 (bao bì), A-01 (tông da tay) | Hũ trắng mờ, chữ KREIZI rose-gold |
| B-04 | Packshot cặp sản phẩm 9:16, nửa trên trống | ảnh nền end card | S04 | Chỉnh sửa A-02 (mở rộng khung) | A-02 | Toàn bộ sản phẩm + label |

---

## Danh sách asset

| Asset | Loại | Nguồn | Tên file | Ai gen | Render (s) | Dùng (s) |
|---|---|---|---|---|---|---|
| A-01 | ảnh | gen mới | `KREIZI-2026-10-GLASSDUO_A-01_seed-maren_v1.png` | Claude (GPT Image) | — | — |
| B-01 | ảnh | gen mới | `KREIZI-2026-10-GLASSDUO_B-01_S01-cheek-press_v1.png` | Claude | — | — |
| B-02 | ảnh | gen mới | `KREIZI-2026-10-GLASSDUO_B-02_S02-serum-pump_v1.png` | Claude | — | — |
| B-03 | ảnh | gen mới | `KREIZI-2026-10-GLASSDUO_B-03_S03-booster-dip_v1.png` | Claude | — | — |
| B-04 | ảnh | chỉnh sửa | `KREIZI-2026-10-GLASSDUO_B-04_S04-packshot_v1.png` | Claude | — | — |
| S01 | clip | gen mới | `KREIZI-2026-10-GLASSDUO_S01_cheek-press_v1.mp4` | User (Veo 3.1) | 4 | 3.0 |
| S02 | clip | gen mới | `KREIZI-2026-10-GLASSDUO_S02_serum-pump_v1.mp4` | User (Veo 3.1) | 4 | 3.0 |
| S03 | clip | gen mới | `KREIZI-2026-10-GLASSDUO_S03_booster-dip_v1.mp4` | User (Veo 3.1) | 4 | 2.5 |
| VO | VO | gen mới | `KREIZI-2026-10-GLASSDUO_vo-S01..S04_v1.mp3` | Claude (ElevenLabs) | — | 10 |
| Nhạc | nhạc | gen mới | `KREIZI-2026-10-GLASSDUO_music_v1.mp3` | Claude (ElevenLabs) | — | 10 |
| SFX | SFX | tuỳ chọn | `KREIZI-2026-10-GLASSDUO_sfx-01_pump-click_v1.mp3` | User | — | <1 |

Reuse: `_assets/broll-library` không có clip Glass Skin Duo. Clip của Grace là nhân vật khác, không dùng chung. 3 clip AI-VIDEO đều gen mới.
