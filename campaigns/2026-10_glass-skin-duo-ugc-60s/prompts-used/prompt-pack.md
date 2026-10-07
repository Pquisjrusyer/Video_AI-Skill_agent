# Prompt Pack — `KREIZI-2026-10-HONEST` (thẻ ảnh, cổng 1)

> Gen ở cổng 2, chạy từ gốc project. `C=campaigns/2026-10_glass-skin-duo-ugc-60s` · `P=_products/Kreizi/glass-skin-duo/reference-images`
> Đợt 1: A-01 seed + R-01 → đợt 2: A-02, A-03, A-04, A-05 (ref A-01 đã pass).
> Bối cảnh chung (khớp mọi take): phòng tắm sáng buổi sáng, tường kem, gương khung gỗ sồi bên trái, khăn trắng treo + chậu cây xanh nhỏ phía sau mờ, nắng mềm từ cửa sổ frame-left ~5000K. Khung dọc 9:16, Dana ngồi giữa, mặt ở 1/3 trên, ngang tầm mắt camera (kiểu selfie đặt trên kệ).

---

### A-01 — Seed mặt Dana
`--ratio 9:16 --quality high --ref $C/outputs/images/KREIZI-2026-10-HONEST_A-00_ref-dana-look_v1.png` → `$C/outputs/images/KREIZI-2026-10-HONEST_A-01_seed-dana_v1.png`
Image 1 = A-00: chỉ lấy khuôn mặt, tóc, tông da, trang phục. Không lấy chai serum.
```
Use Image 1 only as the reference for the woman's face, hair, skin tone and cardigan. Do not include the bottle or her hands.

Scene: bright bathroom in soft morning light, cream wall, warm blurred background.
Subject: head-and-shoulders portrait of a woman in her early fifties with chin-to-shoulder-length wavy brown hair with a few grey strands, blue-grey eyes, light warm skin with real texture (visible pores, fine lines around the eyes and forehead, faint freckles), natural healthy sheen, minimal makeup, soft rosy lips. Moss-green open knit cardigan over a cream t-shirt. She looks straight into the camera with a calm, frank, slightly warm expression, mouth closed.
Important Details: eye-level camera, face centred in the upper third, soft window light from frame-left around 5000K, natural shadows, real photograph look.
Use Case: character identity reference for a UGC video series.
Constraints: no hands, no products, no text, no watermark, no airbrushed or plastic skin, no heavy makeup, keep her looking early fifties.
```
**Dịch:** Chân dung từ vai trở lên của Dana (đầu 50, tóc nâu gợn sóng có vài sợi bạc, mắt xanh xám, da thật có lỗ chân lông, nếp nhăn nhẹ, tàn nhang mờ). Cardigan xanh rêu, áo thun kem. Nhìn thẳng camera, bình thản, ấm. Phòng tắm sáng, nắng mềm từ trái. Không tay, không sản phẩm, không làm mịn da.
QC: ☐ giống A-00 ☐ tuổi ~50 ☐ da texture thật ☐ không tay/sản phẩm

### A-02 — Take A1, A2 (tay trống, đang nói)
`--ratio 9:16 --quality medium --ref $C/outputs/images/KREIZI-2026-10-HONEST_A-01_seed-dana_v1.png` → `..._A-02_take-A-talk_v1.png`
```
Use Image 1 as the identity reference: keep this exact woman, face, hair, skin texture and cardigan.

Scene: bright bathroom in the morning, cream wall, oak-framed mirror on the left, a white towel hanging and a small green plant softly blurred behind her, soft window light from frame-left around 5000K.
Subject: the woman sits facing the camera at eye level, framed from mid-chest up, face in the upper third, mouth relaxed and slightly open as if about to speak, one hand raised loosely at chest height in a natural talking gesture, the other out of frame. Calm, frank expression.
Important Details: looks like a phone selfie video still propped on a shelf, natural colours, real skin texture, shallow depth of field.
Use Case: first frame of a talking-head UGC skincare video.
Constraints: no products in frame, no text, no watermark, five fingers on the visible hand, no plastic skin.
```
**Dịch:** Dana ngồi đối diện camera ngang tầm mắt, khung từ giữa ngực trở lên, miệng hé như sắp nói, 1 tay giơ nhẹ ngang ngực kiểu đang nói chuyện. Phòng tắm sáng: tường kem, gương khung gỗ sồi bên trái, khăn trắng + chậu cây mờ phía sau. Như khung hình video selfie đặt trên kệ. Không sản phẩm.
QC: ☐ identity khớp A-01 ☐ tay đúng ☐ không sản phẩm ☐ miệng tự nhiên (TopView lip-sync được)

### A-03 — Take B, E (cầm serum)
`--ratio 9:16 --quality high --ref $C/outputs/images/KREIZI-2026-10-HONEST_A-01_seed-dana_v1.png --ref $P/serum-in-hand-outdoor-01.png` → `..._A-03_take-B-serum_v1.png`
```
Image 1 is the identity reference: keep this exact woman. Image 2 is the reference for the serum bottle only: frosted powder-blue glass bottle with rounded shoulders, white pump and white collar, white printed text.

Scene: same bright bathroom as before, cream wall, oak-framed mirror on the left, soft window light from frame-left.
Subject: the woman faces the camera from mid-chest up and holds the serum bottle in one hand at chest height, label turned straight toward the camera, fingers wrapped around the lower half so the label stays visible. Calm, slight smile, mouth relaxed.
Important Details: the bottle label reads exactly "KREIZI" with "BEAUTY" below, then "LUMINOUS" and "GLASS SKIN SERUM", white letters, 100 percent readable and physically believable. Frosted powder-blue glass, not mint, not transparent. Real hand texture, short bare nails.
Use Case: first frame of a UGC skincare video, real photograph look.
Constraints: exactly one product, no jar, no extra words, no duplicate text, no watermark, five fingers, keep the bottle colour powder blue.
```
**Dịch:** Dana cầm chai serum 1 tay ngang ngực, label quay thẳng camera, ngón tay ôm nửa dưới để không che chữ. Mỉm cười nhẹ. Chai kính mờ màu xanh da trời nhạt (không mint, không trong suốt), bơm trắng, chữ trắng đúng: KREIZI / BEAUTY / LUMINOUS / GLASS SKIN SERUM. Chỉ 1 sản phẩm.
QC: ☐ identity ☐ chai powder blue ☐ label đúng chữ ☐ 1 sản phẩm ☐ tay đúng

### A-04 — Take C (cầm hũ Moisture Booster)
`--ratio 9:16 --quality high --ref $C/outputs/images/KREIZI-2026-10-HONEST_A-01_seed-dana_v1.png --ref $P/duo-hero-serum-booster-01.png` → `..._A-04_take-C-booster_v1.png`
```
Image 1 is the identity reference: keep this exact woman. Use Image 2 only for the moisturizer jar: a short wide-mouth frosted white glass jar with the word "KREIZI" in rose-gold widely spaced serif letters. Ignore the serum bottle in Image 2.

Scene: same bright bathroom, cream wall, oak-framed mirror on the left, soft window light from frame-left.
Subject: the woman faces the camera from mid-chest up and holds the closed jar in her palm at chest height, lettering turned toward the camera. Calm, slight smile, mouth relaxed.
Important Details: jar lettering reads exactly "KREIZI" in rose-gold, 100 percent readable. Frosted white glass. Real hand texture, short bare nails.
Use Case: first frame of a UGC skincare video, real photograph look.
Constraints: exactly one product, no serum bottle, no extra words, no watermark, five fingers, keep the jar frosted white with rose-gold lettering.
```
**Dịch:** Dana cầm hũ Moisture Booster đóng nắp trong lòng bàn tay ngang ngực, chữ quay ra camera. Hũ kính mờ trắng, miệng rộng, chữ KREIZI màu rose-gold font serif giãn rộng. Không có chai serum.
QC: ☐ identity ☐ hũ trắng chữ rose-gold đúng ☐ không có chai serum ☐ tay đúng

### A-05 — Take D1, D2 (cận mặt, chạm má)
`--ratio 9:16 --quality high --ref $C/outputs/images/KREIZI-2026-10-HONEST_A-01_seed-dana_v1.png` → `..._A-05_take-D-glow_v1.png`
```
Use Image 1 as the identity reference: keep this exact woman, face, hair and skin texture.

Scene: same bright bathroom, soft window light from frame-left, background softly blurred.
Subject: closer framing, from the collarbone up, face filling the upper half. She gently touches her cheekbone with two fingertips and looks into the camera with a relaxed, quietly pleased expression, mouth relaxed.
Important Details: her skin shows a healthy, dewy, hydrated sheen on the cheekbones and forehead catching the window light, while keeping real texture: pores, fine lines and faint freckles stay visible. Real photograph look.
Use Case: first frame of a UGC skincare video.
Constraints: no products, no text, no watermark, no airbrushing, no wrinkle removal, five fingers.
```
**Dịch:** Cận hơn, từ xương quai xanh trở lên. Dana chạm nhẹ 2 đầu ngón vào gò má, nhìn camera, vẻ thư thái hài lòng. Da bóng khoẻ, ẩm ở gò má và trán nhưng vẫn giữ texture thật (lỗ chân lông, nếp nhăn nhẹ, tàn nhang). Không sản phẩm, không xoá nếp nhăn.
QC: ☐ identity ☐ da bóng nhưng vẫn texture thật ☐ tay đúng

### R-01 — B-roll: ngón tay lấy kem booster (first frame Veo)
`--ratio 9:16 --quality high --ref $P/duo-hero-serum-booster-01.png` → `..._R-01_booster-scoop_v1.png`
```
Use Image 1 only for the moisturizer jar and its whipped white cream: short wide-mouth frosted white glass jar, "KREIZI" in rose-gold widely spaced serif letters. Ignore the serum bottle.

Scene: cream travertine bathroom counter, soft morning window light from frame-left, blurred warm background.
Subject: macro close-up of the open jar filled with soft whipped white cream in gentle peaks; an index fingertip of a woman in her fifties hovers about one centimetre above the cream, not touching yet.
Important Details: jar lettering "KREIZI" in rose-gold faces the camera, 100 percent readable; real fingertip texture, short bare nail; camera looks down at about 30 degrees.
Use Case: first frame of a product b-roll clip, real macro photograph.
Constraints: one jar only, no serum bottle, finger not touching the cream, no extra text, no watermark.
```
**Dịch:** Cận macro hũ booster mở nắp trên bàn đá travertine kem, kem trắng đánh bông thành chóp mềm. Đầu ngón trỏ phụ nữ ~50 tuổi lơ lửng cách mặt kem ~1cm, chưa chạm. Chữ KREIZI rose-gold quay ra camera. Camera nhìn xuống ~30°. Chỉ 1 hũ.
QC: ☐ hũ đúng ☐ chữ KREIZI rose-gold ☐ ngón chưa chạm

---

## Bổ sung 2026-10-05 (user góp ý: take C tự nhiên hơn + đổi tư thế A2, D2)

### A-04 v2 — Take C cầm hũ + apply
`--quality high --ref A-01 seed --ref A-06_ref-pose-apply-cream_v1.png (user gửi, chỉ lấy tư thế) --ref $P/duo-hero-serum-booster-01.png` → `A-04_take-C-booster_v2.png` · worked
```
Image 1 is the identity reference: keep this exact woman, her face, hair, skin texture, moss-green cardigan and cream t-shirt. Image 2 is the reference for pose only: one hand holds an open cream jar low near the chest, the other hand's fingertips gently apply cream on the cheekbone. Do not copy the face, hair, makeup, nails or clothing from Image 2. Image 3 is the reference for the jar only: short wide-mouth frosted white glass jar with "KREIZI" in rose-gold widely spaced serif letters, filled with whipped white cream.

Scene: the same bright bathroom as before, cream wall, oak-framed mirror on the left, soft morning window light from frame-left around 5000K.
Subject: the woman faces the camera from mid-chest up. Her left hand holds the open jar naturally at lower chest height, fingers wrapped around the side, lettering turned toward the camera. Her right hand's index and middle fingertips rest lightly on her cheekbone, where a thin, slightly translucent streak of white cream is visible. Relaxed, quietly pleased expression, small closed-mouth smile, eyes looking into the camera.
Important Details: jar lettering reads exactly "KREIZI" in rose-gold, 100 percent readable. Real skin texture with pores, fine lines and faint freckles, natural sheen. Short natural bare nails, real knuckle texture. Looks like a phone selfie video still.
Use Case: first frame of a UGC skincare video, real photograph look.
Constraints: exactly one product, no serum bottle, no glamour makeup, no manicure colour, no extra text, no watermark, five fingers on each hand, the hand on the cheek does not cover the mouth.
```
**Dịch:** Dana tay trái cầm hũ mở nắp ngang ngực, chữ KREIZI quay ra camera; 2 đầu ngón tay phải chạm gò má, có vệt kem mỏng. Cười nhẹ, nhìn camera. Tư thế lấy theo ảnh user gửi, mặt/tóc/áo giữ của Dana.

### A-07 — Take A2 (đổi tư thế)
`--quality medium --ref A-02_take-A-talk_v1.png` → `A-07_take-A2-talk_v1.png` · worked
```
Image 1 is the base photo: keep this exact woman, face, hair, skin texture, clothing, bathroom background, lighting and framing.

Change: change only her pose for a different talking moment: she leans slightly toward the camera with her head tilted a little to one side, both hands loosely together in front of her chest with fingertips lightly touching, as if explaining something sincerely. Mouth relaxed and slightly open, mid-sentence, eyebrows gently raised.

Preserve: identity, face shape, hair, skin texture, cardigan and t-shirt, background, light direction and colour, camera height and crop.
Constraints: no products, no text, no watermark, five fingers on each hand, no new objects.
```
**Dịch:** Giữ nguyên Dana + phòng tắm, chỉ đổi tư thế: hơi nghiêng người về camera, đầu nghiêng nhẹ, 2 tay chụm đầu ngón trước ngực như đang giải thích chân thành, miệng hé đang nói.

### A-08 — Take D2 (đổi tư thế)
`--quality high --ref A-05_take-D-glow_v1.png` → `A-08_take-D2-proof_v1.png` · worked
```
Image 1 is the base photo: keep this exact woman, face, hair, skin texture, clothing, bathroom background and lighting.

Change: change only her pose: her hand comes down from her cheek; she turns her body slightly to a three-quarter angle while her face stays toward the camera, one hand resting relaxed at her collarbone, a warm confident small smile, mouth relaxed and slightly open as if speaking. Keep the close framing from the collarbone up, and the healthy dewy sheen on her cheekbones with real skin texture.

Preserve: identity, face shape, hair, skin texture and freckles, cardigan and t-shirt, background, light direction and colour.
Constraints: no products, no text, no watermark, five fingers, no airbrushing.
```
**Dịch:** Giữ nguyên Dana, khung cận từ xương quai xanh: tay rời má, đặt nhẹ ở xương quai xanh, người xoay 3/4, mặt vẫn nhìn camera, cười tự tin nhẹ, da vẫn bóng khoẻ có texture thật.

### A-09 — Take E cầm 2 sản phẩm
`--quality high --ref A-01 seed --ref A-03_take-B-serum_v1.png --ref A-04_take-C-booster_v2.png` → `A-09_take-E-duo_v1.png` · worked (2 label đúng)
```
Image 1 is the identity reference: keep this exact woman, face, hair, skin texture, moss-green cardigan, cream t-shirt and the bathroom background. Image 2 is the reference for the serum bottle exactly as she holds it: frosted powder-blue glass bottle, white pump and collar, white text "KREIZI", "BEAUTY", "LUMINOUS", "GLASS SKIN SERUM". Image 3 is the reference for the moisturizer jar exactly: frosted white glass jar, open, whipped white cream, "KREIZI" in rose-gold widely spaced serif letters.

Scene: the same bright bathroom, cream wall, oak-framed mirror on the left, soft morning window light from frame-left around 5000K.
Subject: the woman faces the camera from mid-chest up, warm confident closed-mouth smile. She holds the serum bottle upright in her right hand at shoulder height on one side of her face, and the closed moisturizer jar in her left hand at the same height on the other side, both products turned so their labels face the camera, a little apart from her face so nothing covers her mouth or chin. Relaxed shoulders, natural grip.
Important Details: the serum label reads exactly "KREIZI" / "BEAUTY" / "LUMINOUS" / "GLASS SKIN SERUM" in white; the jar reads exactly "KREIZI" in rose-gold; both 100 percent readable and physically believable. Each product keeps its own colour: powder-blue bottle, frosted white jar. Real hand texture, short bare nails, five fingers on each hand.
Use Case: first frame of a UGC skincare video, call-to-action moment, real photograph look.
Constraints: exactly two products, no extra products, no swapped colours, no extra words, no duplicate text, no watermark, hands do not cover the mouth.
```
**Dịch:** Dana cười tự tin, tay phải cầm chai serum, tay trái cầm hũ booster ở 2 bên, label quay ra camera, không che miệng. Chai xanh da trời nhạt chữ trắng, hũ trắng chữ KREIZI rose-gold. Đúng 2 sản phẩm.

### A-09 v2 — Take E, hũ đóng nắp
`--quality high --ref A-09_take-E-duo_v1.png --ref $P/booster-jar-closed-packshot-01.png (user gửi)` → `A-09_take-E-duo_v2.png` · worked (hết lượt)
```
Image 1 is the base photo. Image 2 is the exact reference for the moisturizer jar: closed jar with a smooth matte white screw lid, frosted translucent glass body, and "KREIZI" in widely spaced copper-orange letters.

Change: replace only the open jar in her left hand with the closed jar from Image 2, same size as before, held the same way at the same height, lettering "KREIZI" facing the camera, matching the copper-orange colour and letter spacing of Image 2. No cream visible.

Preserve: the woman, her face, expression, hair, skin texture, cardigan and t-shirt, her right hand and the serum bottle exactly as they are including its label text, her left hand pose and fingers, the background, lighting and framing.

Constraints: exactly two products, the jar lettering reads exactly "KREIZI", no extra text, no watermark, five fingers on each hand, no other changes.
```
**Dịch:** Giữ nguyên ảnh v1, chỉ thay hũ mở nắp bằng hũ đóng nắp trắng mờ, thân kính mờ, chữ KREIZI màu đồng cam, cùng kích thước và cách cầm.

### A-10 — Take E gen mới từ ref gốc (thay A-09 bị noise do sửa nối tiếp)
`--quality high --ref A-01 seed --ref $P/serum-in-hand-outdoor-01.png --ref $P/booster-jar-closed-packshot-01.png` → `A-10_take-E-duo-clean_v1.png` · worked (label đủ dòng, chữ hũ đồng cam đúng)
```
Image 1 is the identity reference: keep this exact woman, face, hair, skin texture, moss-green cardigan and cream t-shirt. Image 2 is the reference for the serum bottle only: frosted powder-blue glass bottle with rounded shoulders, white pump and white collar, white printed text. Image 3 is the exact reference for the moisturizer jar: closed jar with a smooth matte white screw lid, frosted translucent glass body, "KREIZI" in widely spaced copper-orange letters.

Scene: bright bathroom in the morning, cream wall, oak-framed mirror on the left, a white towel hanging and a small green plant softly blurred behind her, soft window light from frame-left around 5000K.
Subject: the woman faces the camera from mid-chest up with a warm, confident closed-mouth smile. She holds the serum bottle upright in her right hand and the closed jar in her left hand, both at lower chest height on either side of her body, labels facing the camera, natural relaxed grip, nothing covering her mouth or chin.
Important Details: serum label reads exactly "KREIZI" / "BEAUTY" / "LUMINOUS" / "GLASS SKIN SERUM" in white; jar reads exactly "KREIZI" in copper-orange; both 100 percent readable. Sharp focus on her face and both products, crisp clean detail, fine natural skin texture with pores, fine lines and faint freckles, no grain or noise. Real hand texture, short bare nails, five fingers on each hand. Looks like a high-quality phone selfie video still.
Use Case: first frame of a UGC skincare video, call-to-action moment, real photograph look.
Constraints: exactly two products, no extra products, no swapped colours, no extra words, no duplicate text, no watermark, no blur, no compression artifacts.
```
**Dịch:** Dana cười tự tin, tay phải cầm chai serum, tay trái cầm hũ booster đóng nắp trắng ngang ngực 2 bên, label quay ra camera. Gen mới từ seed + ảnh sản phẩm thật (không sửa từ ảnh gen cũ) để ảnh nét, không noise.

### A-11 — Take E, identity từ ảnh model gốc user gửi (A-00b)
`--quality high --ref A-00b_ref-dana-original_v1.png --ref $P/serum-in-hand-outdoor-01.png --ref $P/booster-jar-closed-packshot-01.png` → `A-11_take-E-duo-original_v1.png` · worked (label 2 SP đúng, đủ dòng)
```
Image 1 is the identity reference: keep this exact woman, her face, hair, skin texture, moss-green cardigan, cream t-shirt and the bathroom background exactly as in Image 1. Ignore the bottle she holds in Image 1. Image 2 is the reference for the serum bottle only: frosted powder-blue glass bottle with rounded shoulders, white pump and white collar, white printed text. Image 3 is the exact reference for the moisturizer jar: closed jar with a smooth matte white screw lid, frosted translucent glass body, "KREIZI" in widely spaced copper-orange letters.

Scene: bright bathroom in the morning, cream wall, oak-framed mirror on the left, a white towel hanging and a small green plant softly blurred behind her, soft window light from frame-left around 5000K.
Subject: the woman faces the camera from mid-chest up with a warm, confident closed-mouth smile. She holds the serum bottle upright in her right hand and the closed jar in her left hand, both at lower chest height on either side of her body, labels facing the camera, natural relaxed grip, nothing covering her mouth or chin.
Important Details: serum label reads exactly "KREIZI" / "BEAUTY" / "LUMINOUS" / "GLASS SKIN SERUM" in white; jar reads exactly "KREIZI" in copper-orange; both 100 percent readable. Sharp focus on her face and both products, crisp clean detail, fine natural skin texture with pores, fine lines and faint freckles, no grain or noise. Real hand texture, short bare nails, five fingers on each hand. Looks like a high-quality phone selfie video still.
Use Case: first frame of a UGC skincare video, call-to-action moment, real photograph look.
Constraints: exactly two products, no extra products, no swapped colours, no extra words, no duplicate text, no watermark, no blur, no compression artifacts.
```
**Dịch:** Như A-10 nhưng lấy mặt/tóc/áo/phòng tắm theo ảnh model gốc user gửi, bỏ chai trong ảnh gốc. Tay phải cầm serum, tay trái cầm hũ đóng nắp, label quay ra camera.
