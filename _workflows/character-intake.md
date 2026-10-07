# Bước nhân vật (cổng 1 — chỉ khi video có người)

> Chạy sau Bước 0 nhận brief, trước khi viết script. Mục tiêu: **chốt đúng 1 nhân vật, có ảnh + mô tả chi tiết**, rồi khoá lại cho mọi ảnh / clip sau. Làm nhanh: hỏi gom 1 lần, không giải thích dài.

## 1. Hỏi (AskUserQuestion, 1 lượt 2 câu)

**"Video này dùng nhân vật thế nào?"**
- **Nhân vật có sẵn trong dự án** → liệt kê `_characters/*/` (tên + 1 dòng mô tả từ `profile.md`) để chọn
- **Import ảnh nhân vật của tôi** → user kéo ảnh vào chat hoặc chỉ file trong thư mục (1–5 ảnh; tốt nhất có 1 ảnh mặt rõ, chính diện)
- **Tạo nhân vật mới** → Claude đề xuất từ brief + `target-audience.md`
- **Không có nhân vật** (chỉ tay / sản phẩm) → bỏ qua bước này; cảnh có tay người vẫn ghi tông da + dáng móng/tay vào `storyboard.json` → `look`

**"Nhân vật xuất hiện kiểu nào?"** (chọn nhiều được)
- Nói trước camera (UGC) · Cầm / dùng sản phẩm, có mặt · Chỉ thấy tay · Xuất hiện ngắn trong b-roll

Brief đã ghi rõ → bỏ câu tương ứng.

## 2. Thẻ nhân vật — luôn có ẢNH + MÔ TẢ CHI TIẾT

Lưu `_characters/<tên>/profile.md` (theo `_characters/_template/profile.md`) + ảnh ở `_characters/<tên>/reference-images/`:

| Ảnh | Mục đích |
|---|---|
| `<tên>-face-ref-01.png` — mặt cận chính diện, sáng đều | **Ảnh gốc nhận diện** — Image 1 của MỌI ảnh có nhân vật |
| `<tên>-half-body-01.png` — nửa người, trang phục chuẩn | khoá trang phục, dáng |
| `<tên>-in-scene-01.png` — trong bối cảnh quay của campaign | khoá ánh sáng, bối cảnh |

**Mô tả chi tiết** (EN để chép vào prompt + dịch VI để duyệt): tuổi · sắc tộc · tông da (+ hex) · khuôn mặt (dáng mặt, mắt, mũi, môi, nét riêng: nốt ruồi, tàn nhang…) · tóc (màu, độ dài, kiểu) · dáng người · trang phục + phụ kiện · **tay và móng** (dáng móng, độ dài, màu — quan trọng với nail) · tính cách / cách nói · **mô tả giọng** (1 câu EN, chép nguyên văn vào mọi take UGC).
Khối EN này gọi là **IDENTITY LOCK** — chép **nguyên văn, không rút gọn** vào mọi prompt ảnh / video có nhân vật.

Theo lựa chọn ở mục 1:
- **Có sẵn:** dùng ảnh + profile đã có. Thiếu ảnh nào trong 3 ảnh trên → gen bổ sung từ face-ref (ảnh minh hoạ cổng 1).
- **Import:** chép ảnh user vào `reference-images/` (đặt đúng tên), **viết mô tả từ chính ảnh** — chỉ tả cái nhìn thấy, không bịa. Không gen lại mặt; ảnh user là gốc. Thiếu góc nào → gen bổ sung **từ ảnh user** (Image 1 = ảnh user).
- **Tạo mới:** gen 3 ảnh (`gen-image.py --quality medium`, cảnh mặt cận `--quality high`) theo mô tả. Đây là ảnh duyệt ở cổng 1; được duyệt thì dùng luôn làm ảnh gốc, không gen lại ở cổng 2.

Thẻ nhân vật hiện **ở đầu `storyboard.html`** (ảnh + mô tả EN/VI) để user duyệt cùng kế hoạch. ⛔ User xác nhận "đúng nhân vật" trước khi viết script.

## 3. Khoá nhân vật — không để sai

1. Mọi ảnh có nhân vật: `--ref <tên>-face-ref-01.png` là **Image 1** (vai trò: nhận diện), thêm `--require-ref` → `gen-image.py` **không cho** chuyển sang nhà cung cấp không nhận ảnh tham chiếu (popup chỉ hiện nhà có ref).
2. Mọi prompt ảnh / video có nhân vật: dán **IDENTITY LOCK** nguyên văn + câu "Maintain the exact same person as Image 1 / the first frame".
3. QC mỗi ảnh có mục bắt buộc ☐ **Đúng nhân vật**: so với face-ref — dáng mặt, mắt, tóc, tông da, nét riêng, móng tay. Lệch → sửa 1 lần (`Change: match the face of Image 1 exactly`), vẫn lệch → dừng ảnh đó, báo user.
4. Clip (TopView / Higgsfield / Flow): ảnh khung đầu phải là ảnh đã pass QC nhận diện. Bảng clip hiện face-ref cạnh khung hình clip để soi.
5. Nhân vật dùng lại ở campaign sau → đọc `_characters/<tên>/profile.md`, không viết lại mô tả.
