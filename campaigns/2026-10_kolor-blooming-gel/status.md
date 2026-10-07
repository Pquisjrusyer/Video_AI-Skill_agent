# Status — Kolor Blooming Gel — Cold Traffic TikTok

> Quy trình: `_workflows/production-steps.md`. Duyệt: nói với Claude "ok cổng [A–E]" hoặc "ok [4A–4E]".
> Brand: **Kolor Acrylic** (`_brand/kolor-acrylic/`) · Campaign code: `KOLOR-2026-10-BLOOM` · Format: **Voiceover** ✅ (chốt 2026-10-01, Tịnh) · Ratio: 9:16 · Duration: 15–20s

| Chặng | Lệnh | Người làm | Trạng thái | Duyệt bởi | Ngày | File |
|---|---|---|---|---|---|---|
| 1. Brief | `/start` | Claude | ✅ | ⛔ A: **Tịnh** | 2026-10-01 | `brief.md` |
| 2. Script | `/script` | Claude | ✅ | ⛔ B: **Tịnh** | 2026-10-01 | `scripts/script.md` |
| 3. Storyboard + asset | `/storyboard` | Claude | ✅ | ⛔ C: **Tịnh** | 2026-10-01 | `scripts/storyboard.md` |
| 4. Chuẩn bị asset | `/assets` | Claude | ◐ | xem bảng lượt | | `prompts-used/` |
| 5. Kiểm asset | `/check` | Claude | ✅ | ⛔ D: **Tịnh** | 2026-10-01 | `outputs/` |
| 6. Dựng & final | `/edit` | Claude | ◐ | ⛔ E: | | `outputs/final/` |

### Chặng 4 — các lượt
| Lượt | Nội dung | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 4A | Prompt ảnh | ✅ | **Tịnh** | 2026-10-01 |
| 4B | Duyệt ảnh | ✅ | **Tịnh** | 2026-10-01 |
| 4C | Prompt video | ✅ | **Tịnh** | 2026-10-01 |
| 4D | Âm thanh — Claude gen VO | ✅ | **Tịnh** | 2026-10-01 |
| 4E | Bộ bàn giao | ✅ | **Tịnh** | 2026-10-01 |

Trạng thái: ☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** Tịnh xem bản review `outputs/review/KOLOR-2026-10-BLOOM_review_vo-only_v1.mp4` → góp ý nhịp/chữ. Song song gen nhạc + 3 SFX. Có đủ nhạc/SFX thì dựng bản final (cổng E).

## Asset
| Tên file | Loại | Claude gen (VO) / Người gen | Xong | QC |
|---|---|---|---|---|
| `KOLOR-2026-10-BLOOM_A-04_nail-base_v1.png` | ảnh nền chuẩn | Người gen (GPT Image 2) | ✅ | ✅ Duyệt 2026-10-01. Đạt 5/6; cỡ cận nhỏ hơn thẻ (móng ~12–15% chiều cao thay vì 45%) — Tịnh chấp nhận |
| `KOLOR-2026-10-BLOOM_B-01_S01-dot_v1.png` | keyframe S01 | Người gen (GPT Image 2) | ✅ | ☑ Pass checklist. Lưu ý: giọt trông hơi rắn như hạt cườm — chờ quyết có chạy vòng sửa "liquid look" |
| `KOLOR-2026-10-BLOOM_B-02_S02-brush_v1.png` | keyframe S02 | Người gen (GPT Image 2) | ✅ | ✅ Pass sạch — không bàn tay, không đèn UV, cọ chưa chạm móng, gel trong suốt |
| `KOLOR-2026-10-BLOOM_B-03_S03-marble_v1.png` | keyframe S03 | Người gen (GPT Image 2) | ✅ | ☑ Pass checklist. Cùng lưu ý "hạt cườm" như B-01 |
| `KOLOR-2026-10-BLOOM_A-02_pattern-01..04_v1.png` | 4 ảnh hoạ tiết | Claude crop từ official-03 | ✅ | ✅ Crop 9:16 từ ảnh official, không gen lại. Nguồn 1024×1024 → mỗi ô chỉ 281×500 trước khi phóng lên 1152×2048 → hơi mềm nét |
| `KOLOR-2026-10-BLOOM_S01_dot-to-bloom_v1.mp4` | clip 6.0s | Người render (Veo 3.1) | ✅ | ☑ **Duyệt có điều kiện** 2026-10-01. Hiệu ứng nở đẹp, NHƯNG máy xoay (ngón ngang → dựng đứng), nền đổi sang xanh ngọc nửa sau, bàn tay đổi. Tịnh chấp nhận |
| `KOLOR-2026-10-BLOOM_S02_brush-coat_v1.mp4` | clip 6.0s | Người render (Veo 3.1) | ✅ | ✅ Sạch — đúng nhịp, không bàn tay, không đèn UV, máy đứng yên, nền + tông da giữ nguyên |
| `KOLOR-2026-10-BLOOM_S03_marble-spread_v1.mp4` | clip 4.0s | Người render (Veo 3.1) | ✅ | ✅ Loang marble tự nhiên, thời gian thật, nền + góc máy giữ nguyên |

| `KOLOR-2026-10-BLOOM_vo-S01..S05_v1.mp3` | VO 5 file | **Claude gen** (ElevenLabs), Tịnh tải về | ✅ | ☑ Tổng 20.51s. ⚠️ `vo-S01` có 2.15s im lặng giữa (dự kiến 1.1s) → cắt bớt ở `/edit`, không gen lại |

## Vấn đề / quay lại chặng trước
- **2026-10-01 — bản review dựng bằng ffmpeg, KHÔNG phải Remotion.** Mục đích chỉ để duyệt nhịp sớm. Bản final vẫn phải dựng bằng Remotion theo chuẩn project (`/edit`), code lưu ở `remotion-project/`.
- **2026-10-01 — S04 đổi 1 ảnh:** bỏ ảnh da báo, thay bằng móng marble crop từ `blooming-gel_official-02.jpg` (`A-02_pattern-marble_v1.png`). Lý do: lời khoá ở cổng B là "Florals, marble, croc, ombre" mà grid official-03 KHÔNG có marble — chữ và hình lệch nhau. Giờ 4 chữ khớp đúng 4 hình.
- **2026-10-01 — crop watermark phải sâu hơn dự kiến:** ✦ nằm ở y≈1155/1280, crop 6% không đủ. Đang crop xuống còn 626×1112 (bỏ 13% đáy + 13% hai bên).
- **2026-10-01** — Claude **không tải được** file VO từ ElevenLabs: egress của cả máy lẫn cloud đều chặn `storage.googleapis.com`. Người dùng phải tải tay từ flow. Áp dụng cho mọi campaign sau.
- **2026-10-01** — Mốc thời gian các scene **đã phân bổ lại** theo độ dài VO thật (bảng trong `prompts-used/audio-plan.md`). Tổng VO 19.84s, khớp brief; chỉ lệch phân bổ giữa các cảnh.
- **2026-10-01 — PHẢI XỬ LÝ Ở `/edit`:** cả 3 clip có **watermark ✦ góc dưới phải** → crop đáy ~6% hoặc che; nhớ chừa khi đặt chữ overlay.
- **2026-10-01 — PHẢI XỬ LÝ Ở `/edit`:** clip render ra **720×1280**, không phải 1080×1920 → phóng 1.5× khi dựng.
- **2026-10-01 — PHẢI XỬ LÝ Ở `/edit`:** S01 nửa sau nền ngả **xanh ngọc** và tông da sáng hơn S02/S03 → cân màu S01 về xám trung tính trước khi ghép, nếu không cắt S01→S02 sẽ nhảy tông.
- **2026-10-01** — VO đổi từ 1 file liền 20s sang **5 file theo scene** (lý do ghi trong `prompts-used/audio-plan.md`). Storyboard mục Audio đã lỗi thời ở điểm này.
- **2026-10-01** — 4 ảnh A-02 phóng từ nguồn 1024×1024 nên mềm nét. Muốn sắc hơn: tải ảnh gốc độ phân giải cao từ Shopify của Kolor (thêm `?width=2048` vào URL ảnh) rồi crop lại.
- **2026-10-01** — A-04 duyệt với cỡ cận nhỏ hơn thẻ. **Bù ở khâu dựng:** S01 push-in phải bắt đầu rộng và kết thúc chặt hơn bình thường để hiệu ứng loang đủ lớn trên màn hình điện thoại. Nhắc lại ở 4C (thẻ prompt video) và `/edit`.
- **2026-10-01** — `_brand/kolor-acrylic/brand-assets/` trống (chưa có logo/font/palette Kolor). Quyết định: **tạm bỏ logo** ở end card S05. Có file sau thì sửa code Remotion, không phải render lại clip nào.
- **2026-10-01** — `_assets/broll-library/` không có clip nail nào (toàn skincare) → 4 clip AI-VIDEO đều phải gen mới.
- **2026-10-01** — VO đã bị gen sớm sai quy trình (trước cổng 4D), flow ElevenLabs `sqMQ9wc5wVgWBjoo487f`. **Không dùng bản này.** Gen lại sau khi 4D duyệt.
- **2026-10-01** — Đã dựng brand context sơ bộ cho Kolor: `_brand/kolor-acrylic/brand-brief.md`. Còn thiếu: audience research nail tech (`target-audience.md` mới là placeholder), social proof, competitor research, brand assets. Chi tiết ở `brief.md` mục "Gap cần lấp".
