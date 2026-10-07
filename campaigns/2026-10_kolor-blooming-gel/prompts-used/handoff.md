# Handoff Pack — Kolor Blooming Gel "One Dot" · lượt 4E

Campaign `KOLOR-2026-10-BLOOM` · 9:16 · ~19.5–20s · Brand: Kolor Acrylic
Tổng hợp nội dung **đã duyệt** ở 4A–4D. Không viết mới, không đổi lời, không đổi chuyển động.

> ⚠️ **CÒN THIẾU:** nhạc nền + 3 SFX chưa có trong `outputs/audio/`. Bản dựng chạy được không có chúng, nhưng chưa phải bản final.
> ⚠️ **Khác thường tự nhiên:** 3 clip Veo đã render xong TRƯỚC 4E (ngoài thứ tự chuẩn). Mục A dưới đây vì vậy là **hồ sơ clip đã có**, không phải lệnh render mới.

---

## A. Clip đã render

### S01 · `KOLOR-2026-10-BLOOM_S01_dot-to-bloom_v1.mp4`
```
Tool / model:        Veo 3.1 · image-to-video · 9:16
First frame:         outputs/images/KOLOR-2026-10-BLOOM_B-01_S01-dot_v1.png
Đã render:           6.016s · 720×1280
Dùng khi dựng:       0.00–6.016s (dùng trọn)
Âm tạo cùng clip:    không — MUTE khi dựng
Âm thêm sau:         vo-S01 · sfx-01 · music
Trạng thái QC:       ☑ duyệt có điều kiện — máy xoay ngoài ý muốn, nền ngả xanh ngọc nửa sau, bàn tay đổi
```

### S02 · `KOLOR-2026-10-BLOOM_S02_brush-coat_v1.mp4`
```
First frame:         outputs/images/KOLOR-2026-10-BLOOM_B-02_S02-brush_v1.png
Đã render:           6.016s · 720×1280
Dùng khi dựng:       cắt lấy ~4.4s đầu (bỏ đuôi sau khi giọt đã đọng)
Âm tạo cùng clip:    không — MUTE
Âm thêm sau:         vo-S02 · sfx-02 · music
Trạng thái QC:       ✅ sạch
```

### S03 · `KOLOR-2026-10-BLOOM_S03_marble-spread_v1.mp4`
```
First frame:         outputs/images/KOLOR-2026-10-BLOOM_B-03_S03-marble_v1.png
Đã render:           4.011s · 720×1280
Dùng khi dựng:       0.00–3.0s
Âm tạo cùng clip:    không — MUTE
Âm thêm sau:         vo-S03 · music
Trạng thái QC:       ✅ tốt
```

### S04 · MOTION-GRAPHIC
```
Dựng bằng Remotion ở /edit — không render ở tool ngoài.
Asset nguồn: outputs/images/KOLOR-2026-10-BLOOM_A-02_pattern-01..04_v1.png
Nội dung:    4 nhát cắt, mỗi nhát 1 hoạ tiết — hoa → croc đỏ → da báo → ombre, zoom rất nhẹ
Âm thêm sau: vo-S04 · sfx-03 · music
```

### S05 · MOTION-GRAPHIC — end card
```
Dựng bằng Remotion ở /edit — không render ở tool ngoài.
Asset nguồn: _products/kolor-blooming-gel/reference-images/blooming-gel_official-04.jpg
Nội dung:    packshot tĩnh, Ken Burns rất nhẹ, chữ hiện lên. KHÔNG có logo rời (đã chốt)
Âm thêm sau: vo-S05 · music
```

---

## B. Bộ âm thanh

### VO — ✅ đã có đủ 5 file trong `outputs/audio/`

Voice: `Lyan - Beauty, Lifestyle` (`OHbs18UsFunlwffsTLNn`) · model `eleven_v3`
Flow: https://elevenlabs.io/app/flows/JhefK85zKFVRTei6EY4y

| File | Text | Dài thật |
|---|---|---|
| `vo-S01` | One dot. That's the whole flower. *(nghỉ)* You didn't paint that. It bloomed. | 6.27s |
| `vo-S02` | Clear blooming gel over your cured base. Drop your color in. | 3.71s |
| `vo-S03` | It spreads itself. In seconds. | 3.16s |
| `vo-S04` | Florals, marble, croc, ombre. One bottle. | 3.97s |
| `vo-S05` | Crystal clear, never yellows. Kolor Acrylic. | 3.40s |

⚠️ `vo-S01` có **2.15s im lặng** ở giữa (2.09–4.24s) → cắt còn ~1.1s khi dựng, file thành ~5.2s.
⚠️ Mỗi file dư 0.15–0.28s im lặng ở đuôi → cắt sạch.

### Nhạc nền — ⚠️ CHƯA CÓ
Prompt đầy đủ: `prompts-used/audio-plan.md` mục B. 22s, minimal beauty bed, instrumental.
Lưu về: `outputs/audio/KOLOR-2026-10-BLOOM_music_v1.mp3`

### SFX — ⚠️ CHƯA CÓ (3 file)
Prompt đầy đủ: `prompts-used/audio-plan.md` mục C.
`sfx-01` giọt rơi · `sfx-02` cọ lướt · `sfx-03` 4 tiếng cut
Lưu về: `outputs/audio/KOLOR-2026-10-BLOOM_sfx-0X_..._v1.mp3`

### Timeline phối âm

| Mốc | VO | Nhạc (mức) | SFX | Ghi chú |
|---|---|---|---|---|
| 0.00–5.20 | vo-S01 (đã cắt nghỉ) | vào nhẹ, duck dưới lời | sfx-01 @ ~0.4s | Khoảng lặng giữa ~1.1s — nhạc nâng nhẹ ở đó |
| 5.20–8.90 | vo-S02 | giữ, duck | sfx-02 @ ~5.6s | |
| 8.90–12.00 | vo-S03 | nhích lên nhẹ ở 8.9s | — | |
| 12.00–15.90 | vo-S04 | rõ hơn cho 4 nhát cắt | sfx-03 ×4 @ 12.0/12.9/13.8/14.7 | |
| 15.90–19.30 | vo-S05 | thưa dần | — | |
| 19.30–19.50 | — | ring-out, fade | — | |

> Mốc trên tính theo VO **đã cắt khoảng lặng**. Chốt lại bằng số thật khi dựng.

---

## C. Hướng dẫn dựng

| # | Cảnh | In–out timeline | Cắt / nối | Chữ hiển thị · thời điểm · vị trí | Âm đồng bộ |
|---|---|---|---|---|---|
| 1 | S01 clip | 0.00–5.20 | mở lạnh, không fade in | — | vo-S01, sfx-01 |
| 2 | S02 clip | 5.20–8.90 | hard cut | `1 coat. Don't cure.` — lower third, chữ nhỏ, 5.6–8.5s | vo-S02, sfx-02 |
| 3 | S03 clip | 8.90–12.00 | hard cut | `it blends itself` — lower third, 9.2–11.8s | vo-S03 |
| 4 | S04 motion | 12.00–15.90 | cut khớp nhịp nhạc | `Florals · Marble · Croc · Ombre` — hiện dần từng từ khớp 4 nhát cắt | vo-S04, sfx-03 |
| 5 | S05 motion | 15.90–19.50 | crossfade ~6 frame | `KOLOR ACRYLIC` + `Blooming Gel · 15ml` — center | vo-S05 |

**Logo / CTA:** không có logo rời (chốt 2026-10-01). End card chỉ chữ + packshot. Không nút CTA trong video — CTA đặt ở phần caption của ad.

**Cân màu & độ sáng — bắt buộc:**
- **S01 phải cân về xám trung tính.** Nửa sau clip ngả xanh ngọc và tông da sáng hơn S02/S03. Không cân thì cắt S01→S02 nhảy tông rõ.
- Giữ nhiệt màu chung trung tính-hơi lạnh cho cả 5 cảnh
- Không đẩy saturation da

**Xử lý kỹ thuật bắt buộc:**
- **Crop đáy ~6% mọi clip** để bỏ watermark ✦ góc dưới phải. Đặt chữ overlay phải tránh vùng này
- Clip gốc 720×1280 → phóng lên **1080×1920**
- Mute toàn bộ audio gốc của clip

**Xuất:** 9:16 · 1080×1920 · 30fps · H.264 · −14 LUFS
Tên file: `KOLOR-2026-10-BLOOM_voiceover_nochar_blooming-gel_9x16_v1.mp4` → `outputs/final/`

---

## D. Tiêu chí duyệt video

- ☐ Đúng thời lượng (15–20s) + tỷ lệ 9:16
- ☐ Thông điệp rõ: màu tự loang, không cần vẽ
- ☐ Sản phẩm nhất quán — bao bì và chữ nhãn đúng 100% ở S05
- ☐ Không méo tay, chuyển động bất thường, hoạ tiết biến dạng
- ☐ Khung cuối đứng yên, không giật
- ☐ Chỉ dùng claim APPROVED trong `product-brief.md` — **không có "Made in USA"**
- ☐ Chữ đọc được trên điện thoại (xem ở kích thước thật)
- ☐ VO không gấp, không bị cắt chữ
- ☐ Nhạc không lấn lời; SFX khớp hình
- ☐ **Watermark ✦ đã bị crop hết** ở cả 5 cảnh
- ☐ Không khung đen, nhấp nháy, âm đứt đoạn
- ☐ Không nhắc giá, không rating/review
- ☐ Meta Ads compliance: bật AI disclosure trong Ads Manager · file nằm trong `outputs/final/`
