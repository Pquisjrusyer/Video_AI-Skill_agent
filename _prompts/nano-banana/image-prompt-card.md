# Image Prompt Card — chuẩn thẻ prompt ảnh (lượt 4A)

> Dùng ở `/assets` lượt 4A cho **mọi ảnh cần tạo mới / chỉnh sửa** (mặc định GPT Image 2 — Claude gen ở cổng 2 theo `_skills/image/SKILL.md` → Gen GPT Image; Nano Banana chỉ khi user yêu cầu → user tự gen). Ảnh "Dùng trực tiếp" không cần thẻ.
> Syntax từng model vẫn theo `_skills/image/` (NB = văn xuôi tự nhiên, không thông số lens; GPT Image = 5-slot). Thẻ này là **khung nội dung bắt buộc** — phần PROMPT gom các mục lại thành prompt đúng syntax model.

```
### [IMAGE ID] / [SCENE ID]        VD: B-03 / S03
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium   (high nếu có label/chữ hoặc là seed)
Lưu về:            outputs/images/[campaign-code]_[image-id]_[mô-tả-ngắn]_v[n].png   (VD: 2026-06-LAUNCH_B-01_S01-mirror_v1.png)
Phụ thuộc:         [ảnh phải duyệt trước — VD: A-01 seed] → quyết định đợt gen
Lệnh gen:          --ratio 9:16 --quality medium --ref [Image 1] --ref [Image 2]   (ref đúng thứ tự bên dưới)

REFERENCE IMAGE ROLES
- Image 1 = [file] — vai trò: nhận diện / sản phẩm / bố cục / tư thế / chất liệu
- Image 2 = [file] — vai trò: ...
(Thứ tự ở đây = thứ tự --ref = "Image N" trong PROMPT. Ref chỉ là file có thật, đã pass QC. GPT Image tối đa 16 ref.)

FRAME CONTENT
Một khoảnh khắc tĩnh: chủ thể · biểu cảm · hướng nhìn · tư thế · vị trí từng tay · đạo cụ.
Nếu là khung đầu của clip có hành động: chọn khoảnh khắc NGAY TRƯỚC hoặc ĐẦU hành động, ghi rõ.

COMPOSITION AND CAMERA
Cỡ cảnh · góc máy · tiền cảnh/hậu cảnh · vị trí chủ thể · vùng trống cho chữ (vị trí cụ thể) · tỷ lệ.

LIGHTING AND STYLE
Nguồn sáng · hướng (frame-left/right) · nhiệt màu/hex · chất liệu · mức chân thực.
Hướng sáng phải KHỚP các cảnh liền kề trong storyboard.

MUST PRESERVE
Mặt/identity · bao bì (màu, dáng, chữ label) · trang phục · đạo cụ cố định.

AVOID
Chỉ lỗi liên quan trực tiếp ảnh này (VD: tay 6 ngón, label sai chữ, da bị làm mịn, sản phẩm thứ hai lọt khung).
Viết vào prompt bằng positive framing; giữ list này cho QC.

OUTPUT
Một ảnh đơn, đúng tỷ lệ. Không ghép bảng nhiều khung / contact sheet. Không tự thêm chữ quảng cáo, logo, watermark.

PROMPT  (copy nguyên văn)
...

QC (cổng 2, ngay sau gen): ☐ nhận diện ☐ sản phẩm/bao bì ☐ tay–tư thế–hướng nhìn ☐ texture–ánh sáng ☐ bố cục + khả năng diễn hoạt (chừa chỗ cho chuyển động sắp tới)
Lỗi hay gặp → prompt sửa (dùng cho 1 lần sửa duy nhất): ...
Kết quả: worked / needs adjustment / failed → note user tự sửa tay
```

## Khi CHỈNH SỬA ảnh có sẵn (thay vì tạo mới)
Thêm 3 dòng, thay cho FRAME CONTENT:
```
THAY ĐỔI:      [đúng 1 phần — VD: màu hũ kem]
MỨC ĐỘ:        [nhẹ / vừa / thay hẳn — VD: chỉ đổi màu, giữ nguyên dáng và vị trí]
GIỮ NGUYÊN:    [mọi thứ còn lại, liệt kê cụ thể]
```

## Quy tắc
- Ảnh contact sheet / nhiều góc → chỉ làm **tham chiếu (nhóm A)**, không bao giờ làm khung video.
- Khung trung gian / khung cuối chỉ tạo khi thực sự giúp kiểm soát (VD: sản phẩm phải dừng đúng vị trí) và tool video hỗ trợ last frame.
- Chuỗi phụ thuộc (seed → keyframe): duyệt ảnh nền tảng ở 4B trước, rồi mới gen ảnh dùng nó làm ref.
