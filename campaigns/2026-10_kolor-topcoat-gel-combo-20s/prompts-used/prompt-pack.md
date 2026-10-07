# Prompt Pack — KOLOR-2026-10-COMBO

> Thẻ ảnh (cổng 1, chưa gen). Gen ở đầu cổng 2 sau "ok cổng 1": GPT Image 2 qua `_tools/gen-image.py`, mỗi ảnh tối đa 1 gen + 1 sửa.
> Thứ tự gen: **Đợt ①** A-01 → QC → **Đợt ②** B-01…B-05 (song song, cùng dùng A-01 làm Image 1).
> Ref sản phẩm: `_products/Kolor/kolor-topcoat-gel-combo/reference-images/combo_official-01.jpg` (gọi tắt **official-01**).
> Look chung + hình từng cảnh: `scripts/storyboard.json`. Thẻ video chốt viết ở cổng 2 sau khi ảnh pass.

---

### A-01 / S01–S05 — tay khách (ref đồng nhất)
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality high (ảnh nền, dùng làm ref cho 5 ảnh)
Lưu về:            outputs/images/KOLOR-2026-10-COMBO_A-01_client-hand_v1.png
Phụ thuộc:         không → đợt ①
Lệnh gen:          --ratio 9:16 --quality high

REFERENCE IMAGE ROLES
- (không ref)

FRAME CONTENT
Tay trái khách đặt phẳng, thả lỏng, các ngón hơi xoè, mu bàn tay hướng lên. Móng trần tự nhiên, sạch, ngắn-vừa, dáng vuông bo. Không nhẫn, không vòng.

COMPOSITION AND CAMERA
Top-down hơi chếch, tay chiếm 2/3 khung giữa-dưới, cổ tay vào từ dưới-trái. 1/3 trên trống.

LIGHTING AND STYLE
Sáng ban ngày khuếch tán từ frame-left, nền xám rất nhạt #f2f2f2, mặt bàn trắng. Ảnh thật, da có lỗ chân lông, nếp gấp đốt ngón.

MUST PRESERVE
Da nâu ấm trung bình · dáng móng · 5 ngón.

AVOID
Da bị làm mịn · móng dài nhọn · ngón thừa/thiếu · trang sức.

OUTPUT
Một ảnh đơn 9:16, không chữ, không watermark.

PROMPT
```
Scene: bright nail studio, plain very light grey seamless background (#f2f2f2), white table surface.
Subject: a client's left hand resting flat and relaxed on the table, back of the hand up, fingers slightly spread, clean bare natural nails, short-to-medium length, rounded-square shape.
Important Details: warm medium-brown skin with real skin texture, visible knuckle creases and pores, soft diffused daylight from frame-left, gentle contact shadow, slightly angled top-down view, hand occupying the lower two thirds, wrist entering from lower-left, empty top third.
Use Case: photoreal reference image of a hand for a nail product ad, looks like a real photo.
Constraints: exactly five fingers, no jewelry, no nail polish, no text, no watermark, no skin smoothing.
```

QC: ☐ 5 ngón, khớp tự nhiên ☐ móng trần ngắn-vừa vuông bo ☐ da thật, không mịn nhựa ☐ sáng từ trái ☐ 1/3 trên trống
Lỗi hay gặp → sửa: da bị làm mịn → "Change: restore natural skin texture with visible pores and creases. Preserve: hand pose, nail shape, lighting, background."
Kết quả: worked (Cloudflare Flux 2 klein, OpenAI hết quota). v1 dùng làm ref. Lưu ý: ref này làm Flux bám bố cục tay đặt phẳng, khung rộng

---

### B-01 / S01 — cọ đen chạm gốc móng giữa
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-COMBO_B-01_S01-first-stroke_v1.png
Phụ thuộc:         A-01 → đợt ②
Lệnh gen:          --ratio 9:16 --quality medium --ref A-01

REFERENCE IMAGE ROLES
- Image 1 = A-01 — vai trò: da, dáng tay, dáng móng của khách

FRAME CONTENT
Khoảnh khắc NGAY TRƯỚC nét cọ: đầu cọ đầy gel đen chạm gốc móng giữa, móng còn trần. Tay thợ vào từ phải, cầm nắp trắng trụ thon.

COMPOSITION AND CAMERA
Macro, móng giữa ở tâm khung, 1/3 trên trống cho chữ "2 BOTTLES. / ENDLESS SETS.". Chừa chỗ phía đầu móng cho cọ đi hết nét.

LIGHTING AND STYLE
Như A-01 (trái, #f2f2f2).

MUST PRESERVE
Tay khách theo Image 1 · nắp trắng · cọ dẹt đen.

AVOID
Gel lan ra da · cọ tròn/to · tay thứ ba.

OUTPUT
Một ảnh đơn 9:16, không chữ.

PROMPT
```
Scene: bright nail studio table, plain light grey seamless background (#f2f2f2), white surface.
Subject: extreme close-up of the client's hand from Image 1 resting flat, nails bare and natural. A nail technician's fingers enter from frame-right holding a slim white cylindrical bottle cap with a flat black gel brush loaded with thick jet-black gel; the brush tip touches the cuticle of the middle fingernail, the nail itself still bare.
Important Details: keep the skin tone, hand shape and nail shape from Image 1; soft diffused daylight from frame-left; glossy bead of black gel on the brush tip; middle nail at frame center with room toward the free edge for the stroke; empty top third for text.
Use Case: vertical 9:16 first frame for an image-to-video gel polish ad, photoreal.
Constraints: exactly two hands, five fingers each, gel only on the brush, no text, no logos, no watermark.
```

QC: ☐ tay khớp A-01 ☐ cọ dẹt + nắp trắng ☐ gel chưa chạm da ☐ 5 ngón ☐ còn chỗ cho nét cọ
Lỗi hay gặp → sửa: gel đã dính lên móng/da → "Change: the nail is still completely bare, black gel only on the brush tip. Preserve: hands, brush position, lighting, framing."
Kết quả: failed. v1: gel đen trên khớp ngón · v2: đầu cọ vẫn chạm da đốt ngón, không tới móng. → user tự gen: xem mục "Tự gen" cuối file

---

### B-02 / S02 — 2 móng đen, cọ chạm móng áp út, chai mờ
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality high (có nhãn chai)
Lưu về:            outputs/images/KOLOR-2026-10-COMBO_B-02_S02-even-coverage_v1.png
Phụ thuộc:         A-01 → đợt ②
Lệnh gen:          --ratio 9:16 --quality high --ref A-01 --ref official-01

REFERENCE IMAGE ROLES
- Image 1 = A-01 — vai trò: tay khách
- Image 2 = official-01 — vai trò: chai Super Black (chai BÊN PHẢI) — dáng, nhãn quấn xám than, nắp trắng

FRAME CONTENT
Móng trỏ + giữa đen phủ kín; cọ đen chạm gốc móng áp út còn trần. Chai Super Black đứng thẳng, mờ phía sau-phải.

COMPOSITION AND CAMERA
Cận, 3 móng đầu ở giữa khung, chai ở hậu cảnh lệch phải. 1/3 trên trống cho "HIGHLY PIGMENTED".

LIGHTING AND STYLE
Như A-01.

MUST PRESERVE
Tay theo Image 1 · chai theo Image 2 bên phải (thân trắng, nhãn xám than, chữ trắng "kolor" / "GEL POLISH" / "SUPER BLACK").

AVOID
Chai Top Coat lọt khung · lớp đen loang/vệt · chữ nhãn sai.

OUTPUT
Một ảnh đơn 9:16, không thêm chữ ngoài nhãn chai.

PROMPT
```
Scene: bright nail studio table, plain light grey seamless background (#f2f2f2), white surface.
Subject: close-up of the client's hand from Image 1 resting flat; index and middle nails fully coated in smooth, opaque jet-black gel polish; a technician's flat black gel brush from frame-right touches the cuticle of the bare ring nail. In soft focus at back right stands only the right-hand bottle from Image 2: white body with a charcoal-black wrap label, white "kolor" logo, "GEL POLISH" and a "SUPER BLACK" pill, tall white cylindrical cap.
Important Details: keep skin tone and nail shape from Image 1; black coats streak-free with a soft sheen; soft daylight from frame-left; bottle shallow depth of field but recognisable; empty top third for text.
Use Case: vertical 9:16 first frame for an image-to-video gel polish ad, photoreal.
Constraints: exactly one bottle, matching the Super Black bottle in Image 2, two hands only, five fingers each, no added text, no watermark.
```

QC: ☐ tay khớp A-01 ☐ chai đúng Super Black, chỉ 1 chai ☐ đen kín đều ☐ 5 ngón ☐ 1/3 trên trống
Lỗi hay gặp → sửa: lọt cả 2 chai → "Change: remove the white Top Coat bottle, keep only the Super Black bottle. Preserve: hands, nails, lighting, framing."
Kết quả: failed. v1: dụng cụ giống nhíp + đầu ngón lem đen (nhãn chai đạt) · v2: Cloudflare chặn nhầm 2 lần. → user tự gen

---

### B-03 / S03 — tay ở miệng đèn LED
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-COMBO_B-03_S03-led-cure_v1.png
Phụ thuộc:         A-01 → đợt ②
Lệnh gen:          --ratio 9:16 --quality medium --ref A-01

REFERENCE IMAGE ROLES
- Image 1 = A-01 — vai trò: tay khách

FRAME CONTENT
Tay 4 móng đen (ngón cái ngoài khung), đầu ngón vừa tới miệng đèn LED trắng trơn dáng vòm, đèn CHƯA bật (clip sẽ bật đèn).

COMPOSITION AND CAMERA
Góc 3/4 ngang, đèn bên phải, cổ tay bên trái. 1/3 trên trống cho "UV/LED CURE".

LIGHTING AND STYLE
Như A-01.

MUST PRESERVE
Tay theo Image 1 · đèn trắng trơn.

AVOID
Chữ/logo trên đèn · ngón xuyên vỏ đèn.

OUTPUT
Một ảnh đơn 9:16, không chữ.

PROMPT
```
Scene: bright nail studio table, plain light grey seamless background (#f2f2f2), white surface.
Subject: the client's hand from Image 1 with four fingers coated in glossy jet-black gel polish, thumb out of frame, fingertips just at the opening of a compact plain white dome-shaped UV/LED nail lamp placed on frame-right; the lamp is switched off.
Important Details: keep skin tone and nail shape from Image 1; three-quarter side angle; wrist entering from frame-left; soft daylight from frame-left; matte white lamp shell with a smooth curved opening; empty top third for text.
Use Case: vertical 9:16 first frame for an image-to-video gel polish ad, photoreal.
Constraints: lamp completely plain with no text, buttons or logos; one hand, fingers outside the lamp shell; no watermark.
```

QC: ☐ tay khớp A-01 ☐ đèn trơn không chữ ☐ 4 móng đen ☐ ngón không xuyên vỏ
Lỗi hay gặp → sửa: đèn có chữ → "Change: remove all text and logos from the lamp. Preserve: hand, nails, lamp shape, lighting, framing."
Kết quả: needs adjustment → v2 worked: tay đưa vào miệng đèn, đèn trơn. Dùng `_v2`

---

### B-04 / S04 — cọ top coat chạm gốc móng giữa, móng đen satin
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-COMBO_B-04_S04-topcoat_v1.png
Phụ thuộc:         A-01 → đợt ②
Lệnh gen:          --ratio 9:16 --quality medium --ref A-01

REFERENCE IMAGE ROLES
- Image 1 = A-01 — vai trò: tay khách

FRAME CONTENT
Khoảnh khắc NGAY TRƯỚC nét top coat: 4 móng đen satin (chưa bóng), cọ đầy gel trong suốt chạm gốc móng giữa.

COMPOSITION AND CAMERA
Macro, móng giữa ở tâm. 1/3 trên trống cho "SUPER GLOSSY / NO-WIPE".

LIGHTING AND STYLE
Như A-01. Móng satin để clip thấy rõ chuyển sang bóng gương.

MUST PRESERVE
Tay theo Image 1 · nắp trắng · cọ dẹt đen · gel trong suốt.

AVOID
Móng đã bóng gương sẵn · gel có màu.

OUTPUT
Một ảnh đơn 9:16, không chữ.

PROMPT
```
Scene: bright nail studio table, plain light grey seamless background (#f2f2f2), white surface.
Subject: extreme close-up of the client's hand from Image 1 with four jet-black nails in a soft satin, low-shine finish. A technician's fingers from frame-right hold a slim white cylindrical cap with a flat black brush loaded with crystal-clear top coat gel; the brush tip touches the cuticle of the middle nail.
Important Details: keep skin tone and nail shape from Image 1; soft diffused daylight from frame-left; satin black nails show only a faint diffuse sheen; a clear glossy bead of gel on the brush; middle nail at frame center; empty top third for text.
Use Case: vertical 9:16 first frame for an image-to-video gel top coat ad, photoreal.
Constraints: exactly two hands, five fingers each, top coat completely colorless, no text, no watermark.
```

QC: ☐ tay khớp A-01 ☐ móng satin (chưa bóng) ☐ gel trong ☐ 5 ngón
Lỗi hay gặp → sửa: móng đã bóng → "Change: make the black nails a soft satin low-shine finish. Preserve: hands, brush, lighting, framing."
Kết quả: failed. v1 + v2: đầu cọ và giọt top coat nằm trên da ngón áp út, không ở gốc móng giữa. → user tự gen

---

### B-05 / S05 — móng đen bóng gương, 2 chai phía sau
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality high (có nhãn chai)
Lưu về:            outputs/images/KOLOR-2026-10-COMBO_B-05_S05-mirror-shine_v1.png
Phụ thuộc:         A-01 → đợt ②
Lệnh gen:          --ratio 9:16 --quality high --ref A-01 --ref official-01

REFERENCE IMAGE ROLES
- Image 1 = A-01 — vai trò: tay khách
- Image 2 = official-01 — vai trò: 2 chai (Top Coat trái, Super Black phải) — dáng, nhãn, nắp

FRAME CONTENT
Tay giơ nghiêng về máy, 4 móng đen bóng gương có vệt sáng dài. 2 chai đứng cạnh nhau mờ phía sau.

COMPOSITION AND CAMERA
Tay giữa-dưới, chai hậu cảnh thấp. 1/3 trên trống cho "SEALS IN COLOR".

LIGHTING AND STYLE
Như A-01, thêm 1 vệt phản chiếu cửa sổ dài trên móng.

MUST PRESERVE
Tay theo Image 1 · 2 chai đúng Image 2 (thứ tự trái/phải, nhãn).

AVOID
Chai thứ 3 · nhãn sai chữ · móng có hoa văn.

OUTPUT
Một ảnh đơn 9:16, không thêm chữ ngoài nhãn chai.

PROMPT
```
Scene: bright clean studio, plain light grey seamless background (#f2f2f2), white surface.
Subject: the client's hand from Image 1 raised and angled toward the camera, four mirror-glossy jet-black nails with crisp window reflections. Behind the hand in soft focus, the two bottles from Image 2 stand side by side: the white Top Coat bottle on the left (black "kolor", "GEL POLISH", black "TOP COAT" pill) and the Super Black bottle with charcoal wrap label on the right, both with tall white cylindrical caps.
Important Details: keep skin tone and nail shape from Image 1; soft daylight from frame-left; one long bright highlight running across the nails; hand in the center-lower area; bottles in the lower background; empty top third for text.
Use Case: vertical 9:16 first frame for an image-to-video gel polish ad, photoreal.
Constraints: exactly two bottles matching Image 2 in the same left-right order, one hand, five fingers, no nail art, no added text, no watermark.
```

QC: ☐ tay khớp A-01 ☐ đúng 2 chai, đúng thứ tự, nhãn nhận ra được ☐ móng bóng gương ☐ 5 ngón
Lỗi hay gặp → sửa: nhãn chai sai → "Change: correct both bottle labels to match Image 2 exactly. Preserve: hand, nails, highlight, lighting, framing."
Kết quả: failed. v1: 2 móng loang trong · v2: móng áp út vẫn loang, tay đặt phẳng thay vì giơ lên. → user tự gen

---

### S06 — end card
Không gen. Dùng ảnh thật `combo_official-01.jpg` → `combo_official-05.jpg` trong Remotion (cổng 3).

---

## Tự gen — B-01, B-02, B-04, B-05 (đã hết lượt 1 gen + 1 sửa)

Lỗi chung: model Flux theo bố cục A-01 (mu bàn tay, khung rộng) nên móng quá nhỏ, cọ rơi xuống da. Khi tự gen:
- Công cụ: ChatGPT (GPT Image) hoặc Google Flow (Nano Banana, tạo ảnh ngay trong Flow trước khi render clip).
- Đính kèm: `outputs/images/KOLOR-2026-10-COMBO_A-01_client-hand_v1.png` chỉ để lấy **màu da**; B-02, B-05 đính thêm `_products/Kolor/kolor-topcoat-gel-combo/reference-images/combo_official-01.jpg`.
- Dán PROMPT của thẻ, thêm 1 câu đầu: `Use Image 1 only for skin tone. Frame tightly on the fingertips: the nails fill the center of the frame, the back of the hand is mostly out of frame.`
- Lưu về đúng tên ở dòng "Lưu về" của thẻ, đổi `_v1` → `_v3`.
