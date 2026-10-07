# Prompt pack — KOLOR-2026-10-STUDIO

> Phần 1: thẻ ảnh (cổng 1). Phần 2: thẻ video — viết ở cổng 2 sau khi ảnh pass.
> Tool: **ChatGPT (GPT Image 2)**, quality high, khung **9:16** (không có 9:16 → chọn 2:3 dọc, Claude crop khi dựng; bố cục đã chừa lề).
> Ref nằm ở `_products/kolor-blooming-gel/reference-images/`. Đính đúng thứ tự Image 1, 2, 3… như thẻ.

**Thứ tự gen:** Đợt 1 = **A-01** → gửi Claude QC → pass → Đợt 2 = B-01, B-02, B-03 (đính A-01 đã pass).

---

## Phần 1 — Thẻ ảnh

### A-01 / seed Nia
Tool + cấu hình: GPT Image 2 · high · 9:16
Lưu về: `outputs/images/KOLOR-2026-10-STUDIO_A-01_nia-seed_v1.png`
Phụ thuộc: —

REFERENCE IMAGE ROLES — không đính ref (tạo nhân vật mới).

FRAME CONTENT — Nia (`_characters/nia/profile.md`) chân dung beauty, mặt nhìn thẳng camera, biểu cảm điềm tĩnh, môi khép mỉm nhẹ. Tay phải đưa lên, đầu ngón chạm nhẹ đường cằm, mu bàn tay hướng camera → thấy rõ 4 móng. Móng almond ngắn-vừa, sơn nude trong bóng, chưa có hoạ tiết.
COMPOSITION AND CAMERA — Ngực-lên, ngang mắt, mặt ở 1/3 trên-giữa, tay ở giữa khung. Nền trơn kín khung.
LIGHTING AND STYLE — Softbox lớn frame-left, khuếch tán, 5200K; nền xám nhạt `#E9E9EB`; bóng mềm sang phải. Ảnh chụp studio thật, da còn lỗ chân lông và texture tự nhiên.
MUST PRESERVE — (ảnh gốc của nhân vật — các ảnh sau giữ theo ảnh này).
AVOID (QC) — da làm mịn như sáp · mặt cân đối quá hoàn hảo · ngón thừa/thiếu, khớp ngón sai · nhẫn/vòng tay · tóc rủ che mặt.
OUTPUT — 1 ảnh đơn, không chữ, không logo, không watermark.

PROMPT (copy nguyên văn)
```
Scene: seamless light grey studio backdrop (#E9E9EB) filling the whole frame, large softbox from frame-left, diffused neutral 5200K light, soft shadow falling to the right.
Subject: a woman in her late 20s with warm medium-deep brown skin, black hair pulled back into a sleek low bun with a clean middle part, soft defined brows, minimal makeup with soft brown liner and a nude-rose lip, small gold hoop earrings, black ribbed sleeveless top. She looks straight into the camera with a calm, quietly confident expression and closed lips with a slight smile. Her right hand is raised, fingertips lightly touching her jawline, back of the hand toward the camera so four fingernails are clearly visible. Nails: short-medium almond shape, sheer glossy nude polish, no nail art.
Important Details: chest-up framing at eye level, face in the upper-middle third, hand in the center of the frame. Natural skin texture with visible pores and fine detail on face and knuckles, light even sheen, realistic hand anatomy with five fingers and natural knuckle creases. 85mm portrait lens feel, sharp focus on eyes and nails.
Use Case: studio beauty editorial photograph for a nail brand, looks like a real photo.
Constraints: one single image, 9:16 vertical. No rings, no bracelets, no text, no logo, no watermark. No heavy retouching, no airbrushed skin.
```
QC: ☐ nhận diện rõ, đáng dùng lại ☐ tông da ấm đúng ☐ tay 5 ngón, khớp tự nhiên ☐ texture da thật ☐ ánh sáng frame-left
Lỗi hay gặp → sửa: da sáp → thêm `"slight skin imperfections, visible pores on cheeks and nose"` · tay lỗi → gen lại riêng tay bằng edit: `Change: only the right hand to a natural relaxed pose. Preserve: face, hair, lighting, background.`

---

### B-01 / S01 — chấm màu
Tool + cấu hình: GPT Image 2 · high · 9:16
Lưu về: `outputs/images/KOLOR-2026-10-STUDIO_B-01_S01-dot_v1.png`
Phụ thuộc: A-01 pass

REFERENCE IMAGE ROLES
- Image 1 = `KOLOR-2026-10-STUDIO_A-01_nia-seed_v1.png` — tông da, dáng móng
- Image 2 = `blooming-gel_official-03.jpg` — chỉ lấy màu hồng đậm + độ bóng của ô hoa (trên-trái)

FRAME CONTENT — **khoảnh khắc ngay đầu hành động**: đầu cọ chấm nail art đen vừa nhấc lên khỏi giữa móng, để lại 1 chấm tròn nhỏ màu hồng đậm. Chấm **chìm phẳng trong lớp gel trong còn ướt**, viền hơi loang nhẹ (chưa thành hoa). Móng nền trắng sữa bóng.
COMPOSITION AND CAMERA — Macro ngón trỏ, móng chiếm ~40% chiều cao khung, nằm giữa-dưới; ngón từ cạnh dưới đi lên. Cọ vào từ góc trên-phải. 1/3 trên trống cho chữ.
LIGHTING AND STYLE — như A-01: softbox frame-left, `#E9E9EB`, 5200K.
MUST PRESERVE — tông da + dáng móng của Image 1.
AVOID (QC) — chấm trông như hạt cườm/giọt nổi (lỗi campaign trước) · móng nhỏ trong khung (lỗi campaign trước) · thấy đèn UV · thêm ngón/tay thứ hai.
OUTPUT — 1 ảnh đơn, không chữ, không logo.

PROMPT
```
Scene: seamless light grey studio backdrop (#E9E9EB), large softbox from frame-left, diffused neutral 5200K light, soft shadow to the right.
Subject: macro close-up of one index finger of the woman from Image 1, same warm medium-deep brown skin tone and same short almond nail shape. The nail has a cured milky-white glossy base covered with a fresh, wet, perfectly clear gel layer that catches a long specular highlight. The tip of a fine black nail-art dotting brush is just lifting away from the center of the nail, leaving one small round dot of hot pink gel (#E8336D, same pink as the flower nail in Image 2). The pink dot has sunk flush into the wet clear layer, level with the surface, its edge starting to feather softly outward.
Important Details: the finger enters from the bottom edge and points upward; the nail fills about 40 percent of the frame height, positioned in the center to lower-center. The brush enters from the top-right corner. Upper third of the frame is clean backdrop. Real skin texture and cuticle detail, glossy wet gel surface, macro lens feel with shallow depth of field, nail in sharp focus.
Use Case: macro product-demo photograph, looks like a real photo, first frame of a video.
Constraints: one single image, 9:16 vertical. Only one finger in frame. The pink dot is flat and wet inside the clear gel, not a raised bead. No lamp, no text, no logo, no watermark.
```
QC: ☐ tông da khớp A-01 ☐ móng đủ lớn ☐ chấm phẳng-ướt, không hạt cườm ☐ cọ chưa che móng ☐ 1/3 trên trống
Lỗi hay gặp → sửa: chấm như hạt cườm → edit `Change: only the pink dot — make it a flat wet stain soaked into the clear gel with a soft feathered edge. Preserve: everything else.`

---

### B-02 / S02 — Nia cầm chai
Tool + cấu hình: GPT Image 2 · high · 9:16
Lưu về: `outputs/images/KOLOR-2026-10-STUDIO_B-02_S02-nia-bottle_v1.png`
Phụ thuộc: A-01 pass

REFERENCE IMAGE ROLES
- Image 1 = `KOLOR-2026-10-STUDIO_A-01_nia-seed_v1.png` — mặt, tóc, trang phục, tông da
- Image 2 = `blooming-gel_official-01.jpg` — chai: dáng, màu, chữ label
- Image 3 = `blooming-gel_official-03.jpg` — hoạ tiết hoa hồng (ô trên-trái)

FRAME CONTENT — **khoảnh khắc ngay trước hành động**: Nia mặt 3/4 sang trái khung, mắt nhìn xuống móng tay mình. Tay phải giơ cạnh má cầm chai Blooming Gel thẳng đứng giữa ngón cái và 2 ngón (kiểu official-02), mặt label quay thẳng camera. 4 móng thấy rõ: nền hồng nhạt sữa, mỗi móng 1 bông hoa hồng đậm loang mềm.
COMPOSITION AND CAMERA — Medium close-up ngực-lên, ngang mắt. Mặt 1/3 trên, chai + tay giữa khung, ngang cằm. 1/3 dưới (vai, áo) để đặt chữ.
LIGHTING AND STYLE — như A-01.
MUST PRESERVE — mặt Nia (Image 1) · chai: đen bóng, nắp mờ, chữ trắng in thẳng lên thân, thứ tự chữ `kolor` / `UV/LED SOAK OFF` / `GEL POLISH` / `BLOOMING GEL` (khung bo tròn) / `EVEN BLOOMING` `LONG LASTING` / `0.5 oz/15 ml`.
AVOID (QC) — chữ label méo/bịa · chai nghiêng mạnh · 2 tay trong khung · đổi mặt.
OUTPUT — 1 ảnh đơn, không chữ quảng cáo, không logo ngoài chữ có sẵn trên chai.

PROMPT
```
Scene: seamless light grey studio backdrop (#E9E9EB), large softbox from frame-left, diffused neutral 5200K light, soft shadow to the right.
Subject: the same woman from Image 1 — keep her facial features, skin tone, sleek low bun, gold hoops and black ribbed sleeveless top exactly the same. Her face is turned three-quarters toward frame-left, eyes looking down at her own nails, calm soft expression. Her right hand is raised beside her cheek holding the gel polish bottle from Image 2 upright between thumb and two fingers, label facing straight to the camera. The bottle matches Image 2 exactly: glossy black squared glass bottle, tall matte black cap, white text printed directly on the glass reading "kolor" with small "acrylic", "UV/LED SOAK OFF", "GEL POLISH", "BLOOMING GEL" inside a rounded outline box, "EVEN BLOOMING" and "LONG LASTING" with small icons, "0.5 oz/15 ml". Her four visible nails are short almond, milky pale pink base with a soft blooming hot pink five-petal flower on each nail, glossy, in the style of the top-left nail in Image 3.
Important Details: medium close-up from chest up at eye level. Face in the upper third, hand and bottle in the center at chin height, lower third is shoulders and top. Natural skin texture with visible pores, realistic hand anatomy, sharp focus on face, nails and bottle label. 85mm portrait lens feel.
Use Case: studio beauty editorial photograph for a nail brand, first frame of a video.
Constraints: one single image, 9:16 vertical. Only one hand in frame. Bottle text 100 percent readable and identical to Image 2, no extra words, no duplicate text. No rings, no added logo, no watermark.
```
QC: ☐ cùng mặt A-01 ☐ chữ label đúng từng dòng ☐ chai thẳng, label nhìn camera ☐ 1 tay, 5 ngón ☐ hoa hồng trên móng ☐ 1/3 dưới trống
Lỗi hay gặp → sửa: label sai chữ → edit `Change: only the bottle — replace it with the exact bottle from Image 2, same size and angle. Preserve: face, hand, nails, lighting, background.`

---

### B-03 / S03 — 4 hoạ tiết
Tool + cấu hình: GPT Image 2 · high · 9:16
Lưu về: `outputs/images/KOLOR-2026-10-STUDIO_B-03_S03-hand-patterns_v1.png`
Phụ thuộc: A-01 pass

REFERENCE IMAGE ROLES
- Image 1 = `KOLOR-2026-10-STUDIO_A-01_nia-seed_v1.png` — tông da, dáng tay
- Image 2 = `blooming-gel_official-03.jpg` — hoa (trên-trái), croc đỏ (dưới-trái), ombre hồng (dưới-phải)
- Image 3 = `blooming-gel_official-02.jpg` — marble khói (móng giữa + út)

FRAME CONTENT — Mu bàn tay phải Nia, ngón xoè nhẹ, đầu ngón hướng lên. Trỏ = hoa hồng · giữa = marble khói nâu trên nude · áp út = vảy rắn đỏ trên kem · út = watercolor ombre hồng · cái = trắng sữa trơn.
COMPOSITION AND CAMERA — Cận bàn tay, tay ở 2/3 dưới, cổ tay ra cạnh dưới. 1/3 trên trống cho chữ. Nhìn thẳng.
LIGHTING AND STYLE — như A-01.
MUST PRESERVE — tông da Image 1 · từng hoạ tiết đúng ngón.
AVOID (QC) — hoạ tiết lẫn sang ngón khác · móng dài/nhọn khác A-01 · ngón thừa · trang sức.
OUTPUT — 1 ảnh đơn, không chữ.

PROMPT
```
Scene: seamless light grey studio backdrop (#E9E9EB), large softbox from frame-left, diffused neutral 5200K light, soft shadow to the right.
Subject: the back of the right hand of the woman from Image 1, same warm medium-deep brown skin tone, fingers gently spread, fingertips pointing up. Short almond glossy gel nails, each with a different soft blooming design: index finger — hot pink five-petal flower on milky pale pink, like the top-left nail in Image 2; middle finger — smoky brown marble on nude, like the marble nails in Image 3; ring finger — red snake print cells on cream, like the bottom-left nail in Image 2; little finger — hot pink watercolor ombre fading to white, like the bottom-right nail in Image 2; thumb — plain glossy milky white.
Important Details: the hand fills the lower two thirds of the frame, wrist exiting the bottom edge; the upper third is clean backdrop. Straight-on view, all five nails in sharp focus, glossy top coat highlights. Natural skin texture with visible knuckle creases, realistic hand anatomy with five fingers.
Use Case: studio nail-art product photograph, looks like a real photo.
Constraints: one single image, 9:16 vertical. Each design only on its own nail. No rings, no bracelet, no text, no logo, no watermark.
```
QC: ☐ tông da khớp ☐ 4 hoạ tiết đúng ngón, nhìn rõ ☐ 5 ngón ☐ 1/3 trên trống
Lỗi hay gặp → sửa: 1 móng sai hoạ tiết → edit chỉ móng đó, `Preserve: hand, other four nails, lighting, background.`

---

## Phần 2 — Thẻ video (S01, S02)
Đã viết theo B-01, B-02 thật — prompt copy-ready nằm trong `handoff.md` §A (không chép lại ở đây).

## Kết quả ảnh
| Ảnh | Kết quả | Ghi chú |
|---|---|---|
| A-01 | worked | Nhận diện rõ, texture da thật. Tông da ra medium brown (nhạt hơn mô tả) — lấy ảnh này làm chuẩn |
| B-01 | worked (có lưu ý) | Móng đủ lớn ✓. Chấm hồng vẫn hơi nổi khối như hạt — prompt "flush" chưa đủ; chấp nhận vì Veo sẽ loang |
| B-02 | worked | Label đúng từng dòng, 1 tay, hoa trên móng. Chai hơi nhỏ trong khung (~13% chiều cao) |
| B-03 | — | chưa gen |
