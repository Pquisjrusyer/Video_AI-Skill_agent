# Storyboard — KOLOR-2026-10-STUDIO

| Duration | Ratio | Format |
|---|---|---|
| 10.0s | 9:16 | Product demo (không VO) |

Ánh sáng chung mọi cảnh: softbox lớn **frame-left**, khuếch tán, ~5200K trung tính; nền xám nhạt `#E9E9EB` trơn; bóng đổ mềm sang phải. Chữ: xem `script.md`.

## Scene breakdown

| Mã | Thời gian | Mục đích | Hình đầu | 1 hành động chính | Cỡ · góc | Camera | Hình cuối | Nối | Chữ | Nhạc · SFX | Route | Rủi ro AI → đơn giản hoá |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 0.0–3.0 (3.0s) | HOOK | B-01: cận ngón trỏ Nia, móng trắng sữa phủ gel trong ướt, đầu cọ chấm vừa đặt 1 chấm hồng | Chấm hồng nở ra thành bông hoa 5 cánh mềm | Macro, nhìn thẳng xuống móng hơi nghiêng | Đứng yên (tripod) | Hoa hồng đã nở, cọ rút khỏi khung | Hard cut on beat | One dot. / Watch it bloom. | Beat vào ở 0.0 · SFX "bloom" swell 1.2s | AI-VIDEO | Màu loang = vật lý chất lỏng (lý do AI-VIDEO). Campaign trước: máy tự xoay + nền đổi màu → khoá "locked-off camera, background stays the same grey". Giọt trông như hạt cườm → ảnh đầu tả giọt "sunk flush into wet clear gel" |
| S02 | 3.0–6.5 (3.5s) | Model + sản phẩm | B-02: Nia ngực-lên, cầm chai cạnh má (tay phải), móng hoa hồng thấy rõ, mặt 3/4 nhìn xuống móng | Nia ngước nhìn camera, mỉm cười nhẹ, nghiêng chai về phía ống kính một chút | Medium close-up, ngang mắt | Push-in rất chậm | Nia nhìn camera, chai + móng sắc nét | Hard cut | Colors disperse into organic patterns — in seconds. | SFX click nhẹ khi nghiêng chai | AI-VIDEO | Chỉ 1 tay trong khung (bớt lỗi ngón). Chữ label dễ méo khi chai chuyển động → động tác nghiêng nhỏ, chai giữ hướng thẳng camera |
| S03 | 6.5–8.5 (2.0s) | Versatile looks | B-03: bàn tay xoè (mu bàn tay), 4 móng 4 kiểu + ngón cái trơn | Ảnh tĩnh, Remotion push-in chậm 100→106% | Cận bàn tay | (code) | như đầu | Hard cut | Florals · Marble · Snake print · Watercolor (hiện lần lượt) | 4 tick nhẹ theo chữ | MOTION-GRAPHIC | Ảnh tĩnh + zoom + chữ → không cần Veo (bớt 1 render, tránh 4 hoạ tiết biến dạng khi chuyển động) |
| S04 | 8.5–10.0 (1.5s) | End card | Packshot official-01 (1500px), nền mở rộng `#F3F3F3` | Chai scale 96→100% + chữ hiện | Packshot giữa khung | (code) | End card đứng yên | — | Kolor Blooming Gel · Even Blooming · Long Lasting · Shop now | Nhạc kết + soft pop | MOTION-GRAPHIC | Dùng ảnh thật → label đúng 100% |

Tổng: 3.0 + 3.5 + 2.0 + 1.5 = **10.0s** ✓

## Audio
| Loại | Dùng | Nguồn | Scene |
|---|---|---|---|
| Nhạc nền | Có | Người dùng chọn theo prompt ở cổng 2 → `KOLOR-2026-10-STUDIO_music_v1.mp3` | Toàn video |
| VO | Không | — | — |
| SFX | Có | Người dùng chọn → `_sfx-01_bloom` · `_sfx-02_click` · `_sfx-03_tick` · `_sfx-04_pop` | S01–S04 |
| Audio gốc Veo | Không | mute | — |

## Danh sách ảnh

### A. Tham chiếu
| Mã | Nội dung | Dùng cho | Nguồn | Ref | Bắt buộc giữ |
|---|---|---|---|---|---|
| A-01 | Seed mặt + tay Nia (chân dung beauty, tay chạm cằm) | B-01, B-02, B-03 | **Tạo mới** (đợt 1) | — | Khuôn mặt, tông da, móng ngắn oval |
| A-02 | Chai Blooming Gel | B-02 | Dùng trực tiếp `blooming-gel_official-01.jpg` | — | Dáng, màu, chữ label |
| A-03 | 4 hoạ tiết hoa / da báo / croc / ombre | B-01, B-02, B-03 | Dùng trực tiếp `blooming-gel_official-03.jpg` | — | Kiểu loang mềm, bóng |
| A-04 | Marble khói | B-03 | Dùng trực tiếp `blooming-gel_official-02.jpg` | — | Vân marble |

### B. Khung video
| Mã | Nội dung | Vai trò | Cảnh | Nguồn | Ref |
|---|---|---|---|---|---|
| B-01 | Cận ngón trỏ, chấm hồng vừa đặt | first frame | S01 | Tạo mới (đợt 2) | A-01 (tông da), A-03 (màu hồng) |
| B-02 | Nia cầm chai cạnh má | first frame | S02 | Tạo mới (đợt 2) | A-01, A-02, A-03 |
| B-03 | Bàn tay xoè 4 hoạ tiết | ảnh tĩnh S03 | S03 | Tạo mới (đợt 2) | A-01, A-03, A-04 |
| B-04 | Packshot | ảnh tĩnh S04 | S04 | Dùng trực tiếp `blooming-gel_official-01_2048.jpg` | — |

## Danh sách asset

| Asset | Loại | Nguồn | Tên file | Ai | Render (s) | Dùng (s) |
|---|---|---|---|---|---|---|
| A-01 | ảnh | gen mới | `KOLOR-2026-10-STUDIO_A-01_nia-seed_v1.png` | Người dùng | — | — |
| B-01 | ảnh | gen mới | `KOLOR-2026-10-STUDIO_B-01_S01-dot_v1.png` | Người dùng | — | — |
| B-02 | ảnh | gen mới | `KOLOR-2026-10-STUDIO_B-02_S02-nia-bottle_v1.png` | Người dùng | — | — |
| B-03 | ảnh | gen mới | `KOLOR-2026-10-STUDIO_B-03_S03-hand-patterns_v1.png` | Người dùng | — | — |
| S01 | clip | Veo | `KOLOR-2026-10-STUDIO_S01_dot-bloom_v1.mp4` | Người dùng | 4 | 3.0 |
| S02 | clip | Veo | `KOLOR-2026-10-STUDIO_S02_nia-bottle_v1.mp4` | Người dùng | 4 | 3.5 |
| S03 · S04 | motion-graphic | Remotion | `remotion-project/` | Claude | — | 2.0 · 1.5 |
| Nhạc | audio | chọn | `KOLOR-2026-10-STUDIO_music_v1.mp3` | Người dùng | — | 10.0 |
| SFX ×4 | audio | chọn | `KOLOR-2026-10-STUDIO_sfx-0[1–4]_[tên]_v1.mp3` | Người dùng | — | — |

B-roll library: không có clip nail studio có model → gen mới. Clip S03 marble của campaign `KOLOR-2026-10-BLOOM` khác tay/nền nên không ghép được.
