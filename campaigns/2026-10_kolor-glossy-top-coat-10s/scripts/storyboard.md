# Storyboard — KOLOR-2026-10-TOPCOAT

## Metadata

| Field | Thông tin |
|-------|-----------|
| **Campaign** | `KOLOR-2026-10-TOPCOAT` |
| **Duration tổng** | 10.0s |
| **Ratio** | 9:16 |
| **Format** | Voiceover · Mixed (2 AI-VIDEO + 1 MOTION-GRAPHIC) |

**Look chung:** macro móng tay, nền hồng blush `#debdb8` + mặt bàn trắng (khớp ảnh official-06 dùng ở end card). Sáng mềm từ **frame-left**, cửa sổ khuếch tán, ~5000K. Tay da nâu ấm như ảnh official, móng ngắn-vừa bo tròn, màu gel **đỏ cherry `#9e1b2c`**: đỏ lên feed nổi và vệt bóng hiện rõ.

## Scene breakdown

| Mã | Bắt đầu–Kết thúc | Dài | Mục đích | Hình đầu cảnh | 1 hành động chính | Cỡ cảnh · góc | Camera | Hình cuối cảnh | Nối sang | Chữ | Lời đọc | Nhạc · SFX | Route | Rủi ro AI → đơn giản hoá |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 0.0–3.5s | 3.5s | Hook: thấy mờ hoá bóng | B-01: 3 móng đỏ finish satin (chưa top coat), cọ dẹt đen đầy gel trong lơ lửng ngay trên móng giữa, vào từ frame-right | Cọ quét **1 đường** dọc móng giữa từ gốc ra đầu móng; phần đã quét thành bóng gương, phần chưa quét vẫn satin | Macro, 3/4 từ trên | Static | Móng giữa bóng gương, cọ nhấc ra khỏi khung bên phải | Hard cut | "ONE COAT" | "Dull to glass. One coat." | Nhạc vào từ 0s · SFX quẹt cọ nhẹ | AI-VIDEO | Bàn tay cầm cọ dễ méo → **không cho thấy tay cầm cọ**, chỉ cọ + cuống trong vào từ mép khung. Gel lỏng: yêu cầu 1 đường, chậm. Tay mẫu đứng yên |
| S02 | 3.5–6.5s | 3.0s | Proof "super glossy" | B-02: cùng bàn tay, 3 móng trong khung đã bóng gương, có phản chiếu ô cửa sổ | Tay nghiêng rất chậm ~10°, **vệt sáng cửa sổ trượt dọc qua từng móng** | Macro, cùng cỡ S01 | Static | Vệt sáng đã trượt qua hết các móng | Hard cut (hoặc flash trắng 2 frame) | "SUPER GLOSSY" / "NO-WIPE" | "Super glossy. No wipe needed." | SFX "ting" nhẹ đúng lúc vệt sáng qua móng giữa | AI-VIDEO | Tay nghiêng có thể đổi số ngón / dáng móng → chỉ nghiêng cổ tay rất nhẹ, ngón giữ nguyên. Phản chiếu có thể chập chờn → chấp nhận nếu không méo móng |
| S03 | 6.5–10.0s | 3.5s | Packshot + brand | Ảnh official-06 (lọ trắng mở nắp, cọ nhỏ giọt, nền hồng) đặt giữa khung 9:16, nền kéo dài bằng màu `#debdb8` | Push-in chậm 100→106% + chữ hiện lần lượt | Packshot | Zoom số (Remotion) | Logo + tên + "Shop now" đứng yên ≥1s | Kết thúc | logo kolor (trên) · "Glossy Gel Top Coat" · "Shop now" (dưới) | "Seals in your color. Kolor Glossy Top Coat." | Nhạc kết · không SFX | MOTION-GRAPHIC | Ảnh thật nên label đúng 100%. Ảnh 1200px vuông phóng lên rộng 1080 → đủ nét |

> Route S03: ảnh tĩnh + chữ + logo = MOTION-GRAPHIC theo rules §3. Giữ label lọ đúng 100% quan trọng hơn chuyển động thật.

## Assembly notes

- S01→S02: hard cut (cùng cỡ cảnh, cùng hướng sáng → nhảy mượt).
- S02→S03: hard cut hoặc flash trắng 2 frame trùng SFX "ting".
- Duration từng cảnh chốt theo độ dài VO thật ở cổng 3.

### Audio

| Loại | Có dùng? | Nguồn | Scene |
|------|----------|-------|-------|
| Nhạc nền | Có | Claude gen ElevenLabs Music (cổng 2) → `KOLOR-2026-10-TOPCOAT_music_v1.mp3` | Toàn video, duck khi có VO |
| Voiceover | Có | Claude gen ElevenLabs (cổng 2) → `KOLOR-2026-10-TOPCOAT_vo-S01..S03_v1.mp3` | S01–S03 |
| SFX | Có | User tự chọn theo thẻ cổng 2 → `_sfx-01_brush-swipe_v1.mp3`, `_sfx-02_shine-ting_v1.mp3` | S01, S02 |
| Audio gốc clip Veo | Không | mute | |

## Danh sách ảnh

### A. Ảnh tham chiếu
| Mã | Nội dung | Vai trò | Dùng cho | Nguồn | Ref | Bắt buộc giữ | Prompt |
|---|---|---|---|---|---|---|---|
| A-01 | Bàn tay + 3 móng đỏ cherry **satin** (chưa top coat), nền blush, 9:16 | Ảnh nền khoá tay/móng/nền/ánh sáng cho B-01, B-02 | S01, S02 | Tạo mới | official-04 (tư thế tay, da, dáng móng) | da nâu ấm, móng bo tròn ngắn-vừa | `prompt-pack.md` §A-01 |
| official-06 | Packshot lọ mở nắp nền hồng | End card | S03 | **Dùng trực tiếp** | | | — |
| logo_black.png | Logo kolor | End card | S03 | **Dùng trực tiếp** | | | — |

### B. Khung đầu video
| Mã | Nội dung | Vai trò | Dùng cho | Nguồn | Ref | Bắt buộc giữ | Prompt |
|---|---|---|---|---|---|---|---|
| B-01 | A-01 + cọ dẹt đen đầy gel trong lơ lửng trên móng giữa | first frame | S01 | Chỉnh sửa A-01 | A-01 (base) · official-03 (cọ + gel trong) | mọi thứ của A-01 | §B-01 |
| B-02 | A-01, cả 3 móng bóng gương + phản chiếu cửa sổ | first frame | S02 | Chỉnh sửa A-01 | A-01 (base) | tay, dáng móng, màu đỏ, nền | §B-02 |

> Tuỳ chọn ở cổng 2: dùng B-02 làm **last frame** cho S01 (Veo 3.1 first+last frame) để móng giữa bóng đúng kiểu S02.

## Danh sách asset

| Asset | Loại | Nguồn | Tên file | Ai gen | Render (s) | Dùng (s) |
|---|---|---|---|---|---|---|
| A-01 | ảnh | gen mới | `KOLOR-2026-10-TOPCOAT_A-01_nail-base-satin_v1.png` | Claude (GPT Image 2) | | |
| B-01 | ảnh | edit A-01 | `KOLOR-2026-10-TOPCOAT_B-01_S01-brush_v1.png` | Claude (GPT Image 2) | | |
| B-02 | ảnh | edit A-01 | `KOLOR-2026-10-TOPCOAT_B-02_S02-glossy_v1.png` | Claude (GPT Image 2) | | |
| S01 | clip | Veo 3.1 | `KOLOR-2026-10-TOPCOAT_S01_one-coat_v1.mp4` | User | 4 | 3.5 |
| S02 | clip | Veo 3.1 | `KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v1.mp4` | User | 4 | 3.0 |
| S03 | MG | ảnh thật official-06 + logo | Remotion | Claude | — | 3.5 |
| VO | VO ×3 | ElevenLabs | `KOLOR-2026-10-TOPCOAT_vo-S01..S03_v1.mp3` | Claude | | |
| Nhạc | nhạc | ElevenLabs Music | `KOLOR-2026-10-TOPCOAT_music_v1.mp3` | Claude | | |
| SFX ×2 | SFX | user chọn | `_sfx-01_brush-swipe_v1.mp3` · `_sfx-02_shine-ting_v1.mp3` | User | | |

B-roll library: không có clip nail (`keywords.json` 0 kết quả) → gen mới cả 2 clip.
