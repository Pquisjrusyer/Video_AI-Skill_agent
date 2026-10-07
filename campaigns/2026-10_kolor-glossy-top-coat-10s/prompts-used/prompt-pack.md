# Prompt pack — KOLOR-2026-10-TOPCOAT

> Thẻ ảnh viết ở cổng 1, **chưa gen**. Gen ở đầu cổng 2 bằng `_tools/gen-image.py`.
> Thứ tự: **Đợt 1: A-01** → QC pass → **Đợt 2: B-01 + B-02** (cùng edit từ A-01).
> Lưu vào `outputs/images/`. Ref sản phẩm: `_products/Kolor/kolor-glossy-top-coat/reference-images/`.

---

### A-01 — ảnh nền tay + móng satin
```
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality high (ảnh nền, khoá identity tay/móng)
Lưu về:            outputs/images/KOLOR-2026-10-TOPCOAT_A-01_nail-base-satin_v1.png
Phụ thuộc:         không
Lệnh gen:          --ratio 9:16 --quality high --ref top-coat_official-04.jpg

REFERENCE IMAGE ROLES
- Image 1 = top-coat_official-04.jpg — tư thế bàn tay đặt phẳng, tông da nâu ấm, dáng móng bo tròn ngắn-vừa. KHÔNG lấy màu đen, cọ, watermark

FRAME CONTENT
Bàn tay trái đặt phẳng, thả lỏng. 3 móng (trỏ, giữa, áp út) chiếm phần lớn khung. Màu gel đỏ cherry đã hơ,
finish SATIN hơi mờ: có ánh sáng nhưng không có vệt phản chiếu sắc. Không cọ, không lọ.

COMPOSITION AND CAMERA
Macro, nhìn 3/4 từ trên. Móng giữa ở chính giữa khung, ~30% chiều cao. Ngón tay chạy từ dưới-trái lên trên-phải.
Chừa 1/4 trên trống cho chữ, chừa khoảng trống bên phải móng giữa cho cọ đi vào ở B-01.

LIGHTING AND STYLE
Sáng cửa sổ khuếch tán mềm từ frame-left, ~5000K. Nền hồng blush #debdb8, mặt dưới tay là mặt bàn trắng mờ.
Ảnh chụp thật, da có vân và lỗ chân lông, không làm mịn.

MUST PRESERVE
Da nâu ấm, dáng móng bo tròn, 5 ngón đúng giải phẫu.

AVOID
Ngón thừa/thiếu, móng méo, da nhựa, móng bóng gương (đây là ảnh TRƯỚC top coat), watermark của ảnh ref.

PROMPT
Scene: soft blush pink backdrop (#debdb8) with a matte white tabletop, soft diffused window light from frame-left, about 5000K, gentle soft shadows.
Subject: a relaxed left hand resting flat on the tabletop, warm brown skin, short-to-medium rounded nails. The index, middle and ring fingernails fill most of the frame, painted with cured cherry red gel polish (#9e1b2c) with a SATIN, slightly muted finish: smooth and even color, soft diffuse sheen, no sharp mirror reflections yet, as if the top coat has not been applied.
Important Details: extreme macro, three-quarter top-down angle. The middle fingernail sits at the exact center of the frame and takes about 30 percent of the frame height. Fingers run from lower-left toward upper-right. Keep the top quarter of the frame empty backdrop for text, and leave clear empty space to the right of the middle nail. Real skin texture with fine lines and pores, natural cuticles, no retouching. Use Image 1 only as reference for the hand pose, skin tone and nail shape.
Use Case: first frame reference for a photoreal nail-care product video ad, vertical 9:16.
Constraints: anatomically correct hand with five fingers, no brush, no bottle, no other products, no glossy mirror highlights on the nails, no text, no logo, no watermark, no sparkle icon in the corner.

QC: ☐ tay đúng giải phẫu ☐ móng satin (không bóng gương) ☐ đỏ cherry đều ☐ sáng từ trái, nền blush ☐ chừa trên + phải móng giữa
Lỗi hay gặp → sửa (1 lần): móng ra bóng gương → "Change: make the nail finish satin and muted, remove sharp mirror highlights. Preserve: everything else."
Kết quả: worked (v1, 2026-10-05). Lệch thẻ: móng ~10% chiều cao khung thay vì 30%, màu hơi ngả đỏ gạch. Chấp nhận, không dùng lượt sửa.
```

---

### B-01 / S01 — cọ đầy gel trong lơ lửng trên móng giữa
```
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-TOPCOAT_B-01_S01-brush_v1.png
Phụ thuộc:         A-01 pass
Lệnh gen:          --ratio 9:16 --quality medium --ref A-01_v1.png --ref top-coat_official-03.jpg

REFERENCE IMAGE ROLES
- Image 1 = A-01 — ảnh gốc để edit
- Image 2 = top-coat_official-03.jpg — hình dạng cọ dẹt đen + cuống trong + gel trong suốt sánh. KHÔNG lấy icon/chữ

THAY ĐỔI:      thêm 1 cọ gel dẹt đen, cuống trong suốt, vào từ góc trên-phải (đi phía trên ngón áp út), đầu cọ phủ gel trong, lơ lửng ~3mm trên gốc móng giữa, CHƯA chạm
MỨC ĐỘ:        thêm vật, không đổi gì khác
GIỮ NGUYÊN:    tay, da, móng satin đỏ, nền, ánh sáng, khung hình
Khoảnh khắc:   ngay TRƯỚC khi cọ chạm móng (clip S01 bắt đầu từ đây)

PROMPT
Change: add one flat black nail gel brush with a clear transparent stem entering from the upper-right corner of the frame, passing above the ring finger. Its tip is loaded with thick, perfectly clear glossy gel and hovers about 3 mm above the base of the middle fingernail, angled down toward the cuticle, not touching the nail yet. A tiny bead of clear gel hangs at the tip. No hand or fingers holding the brush are visible, only the brush and stem.
Preserve: the hand, finger positions, skin tone and texture, the satin cherry red nails with no mirror highlights, the blush pink backdrop, the lighting from frame-left, framing, camera angle and 9:16 aspect ratio, exactly as in Image 1. Use Image 2 only for the brush shape and the look of the clear gel.
Constraints: no second brush, no bottle, no visible hand holding the brush, the brush does not touch the nail, no text, no icons, no watermark.

QC: ☐ chỉ có cọ, không thấy tay cầm ☐ cọ chưa chạm móng ☐ gel trong suốt ☐ A-01 giữ nguyên ☐ còn chỗ cho cọ quét xuống đầu móng
Lỗi hay gặp → sửa: cọ chạm móng / có tay cầm → "Change: lift the brush slightly so it clearly hovers above the nail, remove any hand. Preserve: everything else."
Kết quả: worked (v1). Cọ có sợi lông rõ, đẫm gel trong, không thấy tay cầm. Cọ cao hơn ~1cm so với thẻ (3mm) → Veo cho hạ xuống ở đầu clip.
```

---

### B-02 / S02 — móng bóng gương
```
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-TOPCOAT_B-02_S02-glossy_v1.png
Phụ thuộc:         A-01 pass
Lệnh gen:          --ratio 9:16 --quality medium --ref A-01_v1.png

REFERENCE IMAGE ROLES
- Image 1 = A-01 — ảnh gốc để edit

THAY ĐỔI:      cả 3 móng từ satin thành bóng như gương: lớp gel dày trong, phản chiếu sắc hình ô cửa sổ chữ nhật mềm
MỨC ĐỘ:        chỉ đổi finish bề mặt móng
GIỮ NGUYÊN:    màu đỏ, dáng móng, tay, da, nền, ánh sáng, khung hình
Khoảnh khắc:   ngay trước khi tay nghiêng, vệt sáng đang ở mép trái mỗi móng (clip S02 cho vệt trượt sang phải)

PROMPT
Change: give all three fingernails a thick, glass-like, mirror-glossy clear top coat. Each nail now shows a crisp, sharp reflection of a soft rectangular window, positioned near the LEFT edge of each nail, plus a smooth wet-look depth over the cherry red color.
Preserve: the exact cherry red color (#9e1b2c), nail shape and size, the hand, finger positions, skin tone and texture, the blush pink backdrop, lighting direction from frame-left, framing, camera angle and 9:16 aspect ratio, exactly as in Image 1.
Constraints: no brush, no bottle, no glitter, no chrome effect, no color change, no text, no watermark.

QC: ☐ bóng gương rõ, đọc là top coat chứ không phải chrome ☐ đỏ giữ nguyên ☐ vệt sáng ở mép trái ☐ tay khớp A-01
Lỗi hay gặp → sửa: ra hiệu ứng chrome/kim loại → "Change: keep the cherry red color fully visible under a clear glossy layer, no metallic effect. Preserve: everything else."
Kết quả: worked (v1). Bóng gương rõ, không chrome. Đỏ tươi hơn A-01 một chút → S01 cuối clip móng giữa bóng lên nên chênh màu khó thấy.
```

---


---

# Thẻ video (Veo 3.1) — viết theo ảnh thật đã pass

### S01 · KOLOR-2026-10-TOPCOAT_S01_one-coat_v1.mp4
```
Tool + cấu hình:   Veo 3.1 · image-to-video · 9:16 · 1080p
Render:            4s          Dùng trong bản dựng: ~0.2–3.7s = 3.5s
Lưu về:            outputs/videos/KOLOR-2026-10-TOPCOAT_S01_one-coat_v1.mp4

INPUT IMAGE ROLES
- First frame = outputs/images/KOLOR-2026-10-TOPCOAT_B-01_S01-brush_v1.png
- Last frame  = KHÔNG dùng (B-02 có cả 3 móng bóng, mâu thuẫn với "chỉ quét 1 móng")

STARTING FRAME
Cọ đẫm gel trong lơ lửng phía trên móng giữa, vào từ góc trên-phải. 3 móng đỏ finish satin. Tay đặt phẳng, đứng yên.

ACTION AND TIMING
0.0–0.7s: cọ hạ xuống, chạm gốc móng giữa sát da
0.7–2.6s: cọ kéo 1 đường chậm, đều từ gốc ra đầu móng giữa; gel trong trải ra, phần đã quét chuyển từ satin sang bóng gương, hiện phản chiếu ô cửa sổ
2.6–4.0s: cọ nhấc lên, rút ra khỏi khung về góc trên-phải; móng giữa bóng gương, các móng khác vẫn satin

CAMERA
Static, 100mm macro. Không zoom, không xoay.

CONTINUITY
Bàn tay đứng yên hoàn toàn, không đổi số ngón, dáng móng, tông da. Màu đỏ không đổi, chỉ đổi độ bóng.
Ánh sáng cửa sổ từ frame-left giữ nguyên. Nền hồng blush + mặt bàn trắng giữ nguyên. Không tay nào cầm cọ xuất hiện.

ENDING FRAME
Không còn cọ trong khung. Móng giữa bóng gương với vệt phản chiếu sắc, 2 móng kia satin. Giữ yên ~1s.

AUDIO CUES
Mọi âm thêm khi dựng → clip không âm.

AVOID
Bàn tay/ngón cầm cọ hiện ra · tay mẫu cử động · cọ quét nhiều lần hoặc quét sang móng khác · gel đổi màu/đục · móng đổi dáng · máy xoay · nền đổi màu.

PROMPT
Maintain the hand, nails and background from the first frame exactly; the hand stays completely still. Static 100mm macro shot, no camera movement. The flat black gel brush loaded with clear gel lowers and touches the base of the middle fingernail near the cuticle. In one slow, even stroke it glides from the base to the tip of the nail, laying down a smooth layer of perfectly clear gel. Wherever the brush has passed, the satin cherry red surface turns into a glass-like mirror gloss with a crisp reflection of the soft window light, while the color itself stays the same red. The brush then lifts and exits toward the upper-right corner of the frame. Final image: the middle nail is mirror-glossy, the other two nails remain satin, no brush in frame. Soft diffused window light from frame-left throughout. No hand holding the brush is ever visible.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.

QC: ☐ khớp first frame ☐ đúng 1 đường quét ☐ chỉ móng giữa bóng ☐ cọ rời khung ☐ tay mẫu đứng yên, không thấy tay cầm cọ ☐ nền/ánh sáng giữ nguyên
Lỗi hay gặp → sửa: tay cầm cọ hiện ra → thêm "The brush moves on its own, the frame shows only the brush tip and clear stem" · cả 3 móng bóng → thêm "only the middle nail changes"
```

---

### S02 · KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v1.mp4
```
Tool + cấu hình:   Veo 3.1 · image-to-video · 9:16 · 1080p
Render:            4s          Dùng trong bản dựng: ~0.3–3.3s = 3.0s
Lưu về:            outputs/videos/KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v1.mp4

INPUT IMAGE ROLES
- First frame = outputs/images/KOLOR-2026-10-TOPCOAT_B-02_S02-glossy_v1.png

STARTING FRAME
Cùng bàn tay, 3 móng đỏ bóng gương, vệt phản chiếu cửa sổ nằm phía trái mỗi móng.

ACTION AND TIMING
0.0–0.5s: yên
0.5–3.0s: cổ tay nghiêng rất nhẹ (~10°) sang phải; vệt phản chiếu cửa sổ trượt mượt từ mép trái sang mép phải từng móng, lần lượt trỏ → giữa → áp út
3.0–4.0s: dừng, giữ yên

CAMERA
Static, 100mm macro.

CONTINUITY
Ngón tay giữ nguyên vị trí tương đối, không co duỗi. Dáng móng, màu đỏ, tông da không đổi. Ánh sáng từ frame-left, nền giữ nguyên.
Hiệu ứng: vệt sáng sắc, trắng hơi ấm, trượt trái → phải từ 0.5s đến 3.0s, cường độ vừa, đọc như phản chiếu thật trên lớp bóng.

ENDING FRAME
Vệt sáng đã nằm phía phải mỗi móng. Tay đứng yên ~1s.

AUDIO CUES
Mọi âm thêm khi dựng → clip không âm.

AVOID
Ngón nhân đôi/đổi số ngón khi nghiêng · móng biến dạng · lấp lánh/glitter · hiệu ứng chrome · máy xoay · tay rời khỏi khung.

PROMPT
Maintain the hand, nails and background from the first frame exactly. Static 100mm macro shot, no camera movement. The hand stays relaxed on the tabletop; from 0.5 seconds the wrist tilts very slightly to the right, about ten degrees, fingers keeping their exact positions. As it tilts, the crisp reflection of the soft window slides smoothly across each mirror-glossy cherry red nail from its left edge to its right edge, index then middle then ring nail, like light gliding over glass. The red color, nail shapes and skin stay unchanged. By 3 seconds the movement stops and the hand holds still. Soft diffused window light from frame-left throughout.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.

QC: ☐ khớp first frame ☐ vệt sáng trượt trái → phải qua cả 3 móng ☐ ngón không đổi ☐ không chrome/glitter ☐ khung cuối yên
Lỗi hay gặp → sửa: tay cử động nhiều → bỏ nghiêng tay, thay bằng "the window light source moves slowly, the hand stays perfectly still"
```

### S03 — MOTION-GRAPHIC: dựng bằng Remotion ở cổng 3, không render ở tool ngoài. Nguồn: `top-coat_official-06.jpg` + `_brand/kolor-acrylic/Logo/logo_black.png`.

---

# Bản v2 — "quy trình thật" (2026-10-05, user yêu cầu clip thật hơn)

> Bản code (S01/S02 v1) bị user loại: "tạo video bằng code nó xấu". Concept mới: tay thợ cầm cọ quét thật (S01), rút tay khỏi đèn LED (S02).
> Video render bằng **Dreamina / Seedance** (free, dùng thương mại) — thẻ video viết SAU khi B-03, B-04 pass.
> Thứ tự: B-03 + B-04 cùng 1 đợt (cùng edit từ ảnh đã pass, không phụ thuộc nhau).

### B-03 / S01 — tay thợ cầm cọ, sắp quét móng giữa
```
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-TOPCOAT_B-03_S01-tech-brush_v1.png
Phụ thuộc:         A-01 (đã pass)
Lệnh gen:          --ratio 9:16 --quality medium --ref A-01_v1.png --ref top-coat_official-06.jpg --ref top-coat_official-04.jpg

REFERENCE IMAGE ROLES
- Image 1 = A-01 — ảnh gốc để edit (tay khách, móng satin đỏ, nền, ánh sáng)
- Image 2 = top-coat_official-06.jpg — nắp trắng + cuống trong + cọ dẹt đen của lọ Kolor (cọ liền nắp). KHÔNG lấy lọ, nền hồng
- Image 3 = top-coat_official-04.jpg — góc cọ tiến vào móng. KHÔNG lấy móng đen, watermark

THAY ĐỔI:      thêm tay phải của thợ nail vào từ góc trên-phải, ngón cái + trỏ + giữa cầm nắp trắng như cầm bút, cọ đẫm gel trong chạm nhẹ gốc móng giữa
MỨC ĐỘ:        thêm tay + cọ, không đổi gì của tay khách
GIỮ NGUYÊN:    tay khách, móng satin đỏ, da, nền, ánh sáng, khung hình
Khoảnh khắc:   cọ vừa đặt xuống gốc móng, CHƯA kéo (clip bắt đầu từ đây)

PROMPT
Change: add the right hand of a nail technician entering from the upper-right corner of the frame. Her thumb, index and middle fingers hold the white cylindrical cap of a gel polish bottle like a pen; from the cap extends a short clear stem and a flat black brush loaded with perfectly clear glossy gel. The brush tip rests lightly on the base of the client's middle fingernail near the cuticle, angled down along the nail, just about to pull forward. The technician's hand has a light-medium skin tone, short natural nails with a clear finish, relaxed and steady, wrist resting out of frame.
Preserve: the client's hand, finger positions, skin tone and texture, the satin cherry red nails with no mirror highlights, the blush pink backdrop, the soft window light from frame-left, framing, camera angle and 9:16 aspect ratio, exactly as in Image 1. Use Image 2 only for the white cap, clear stem and flat black brush, and Image 3 only for the brush angle.
Constraints: exactly two hands in frame (client and technician), anatomically correct fingers, no bottle body, no second brush, no gloves, no text, no logo, no watermark.

QC: ☐ đúng 2 bàn tay, ngón đúng giải phẫu ☐ thợ cầm nắp trắng tự nhiên ☐ cọ chạm gốc móng giữa ☐ tay khách giữ nguyên A-01 ☐ tay thợ không che móng giữa
Lỗi hay gặp → sửa: ngón tay thợ méo/thừa → "Change: fix the technician's fingers to a natural pen grip with five fingers. Preserve: everything else."
Kết quả: worked (v1). Cọ chạm mép phải móng giữa (thẻ ghi gốc móng) → prompt video cho cọ kéo dọc móng từ đó.
```

---

### B-04 / S02 — đầu ngón tay khách trong đèn LED, sắp rút ra
```
Tool + cấu hình:   GPT Image 2 · ratio 9:16 · quality medium
Lưu về:            outputs/images/KOLOR-2026-10-TOPCOAT_B-04_S02-lamp_v1.png
Phụ thuộc:         B-02 (đã pass)
Lệnh gen:          --ratio 9:16 --quality medium --ref B-02_v1.png

REFERENCE IMAGE ROLES
- Image 1 = B-02 — ảnh gốc để edit (tay, móng đỏ bóng gương, nền)

THAY ĐỔI:      thêm đèn LED hơ gel màu trắng dạng vòm ở phía trên-phải, phủ lên đầu các ngón tay; móng nằm ngay mép miệng đèn, hắt ánh sáng LED trắng-tím nhẹ
MỨC ĐỘ:        thêm vật lớn, tay và móng giữ nguyên
GIỮ NGUYÊN:    bàn tay, dáng móng, đỏ bóng gương, da, nền, ánh sáng chính
Khoảnh khắc:   ngay TRƯỚC khi rút tay ra (clip: tay kéo về dưới-trái, lộ hết móng bóng)

PROMPT
Change: add a white dome-shaped LED/UV nail curing lamp on the tabletop at the upper-right, its open front facing the hand. The client's fingertips rest just inside the lamp opening so the glossy cherry red nails sit right at the edge of the opening, lit by a soft cool white LED glow with a faint violet tint spilling from inside the lamp onto the nails and fingertips. The lamp is plain glossy white plastic with a smooth curved shell and no visible text, logo or display.
Preserve: the hand, finger positions, skin tone and texture, the nail shapes and the mirror-glossy cherry red color (#9e1b2c), the blush pink backdrop, the window light from frame-left, camera angle and 9:16 aspect ratio, exactly as in Image 1. The top quarter of the frame stays clear backdrop.
Constraints: no text or logo on the lamp, no extra hands, no brush, no bottle, nails still clearly visible at the lamp edge, no watermark.

QC: ☐ đèn trông thật, không chữ ☐ móng vẫn thấy ở mép đèn ☐ tay giữ nguyên B-02 ☐ đỏ bóng không đổi ☐ trên khung còn trống
Lỗi hay gặp → sửa: đèn che hết móng → "Change: move the lamp slightly so the nails sit at the edge of the opening, clearly visible. Preserve: everything else."
Kết quả: worked (v1). Đèn trắng không chữ, ánh LED hắt lên móng. Đỏ hơi ngả mận so với B-02, chấp nhận.
```

---

## Thẻ video v2 — Dreamina (Seedance) · image-to-video · 9:16 · 5s

> Cách dùng: dreamina.capcut.com → AI Video → Image to video → model Seedance → 9:16 → 5s. Tải ảnh khung đầu, dán PROMPT. Gen 2 bản/cảnh, chọn bản đạt QC.
> Clip tắt tiếng khi dựng (VO + nhạc + SFX thêm ở cổng 3).

### S01 · KOLOR-2026-10-TOPCOAT_S01_one-coat_v2.mp4
```
First frame:   outputs/images/KOLOR-2026-10-TOPCOAT_B-03_S01-tech-brush_v1.png
Dùng khi dựng: ~0.3–3.8s = 3.5s

PROMPT
Real salon footage, extreme macro, static camera. A nail technician's hand holds the white cap of a gel top coat brush. She presses the flat black brush gently onto the client's satin cherry red middle nail and pulls one slow, steady stroke along the nail from the cuticle to the free edge, laying down a thick layer of perfectly clear gel. Wherever the brush passes, the matte red surface instantly turns wet and glass-like, with a sharp reflection of soft window light. The bristles flex naturally and the gel self-levels smoothly. After the single stroke, she lifts the brush away toward the upper right. The client's hand stays completely still. Natural soft daylight from the left, blush pink background, realistic skin texture.

QC: ☐ đúng 1 đường quét trên móng giữa ☐ phần quét chuyển bóng, móng khác vẫn satin ☐ ngón tay thợ không méo khi cử động ☐ tay khách đứng yên ☐ cọ không xuyên vào móng
Sửa nếu lỗi: tay thợ biến dạng → thêm "her fingers keep the same pen grip throughout" · quét nhiều móng → thêm "only the middle nail is coated"
```

### S02 · KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v2.mp4
```
First frame:   outputs/images/KOLOR-2026-10-TOPCOAT_B-04_S02-lamp_v1.png
Dùng khi dựng: ~0.3–3.3s = 3.0s

PROMPT
Real salon footage, extreme macro, static camera. The client's hand rests with her fingertips just inside the opening of a white LED nail curing lamp, the cool white-violet light glowing on her cherry red nails. The lamp light switches off, then she slowly slides her hand out of the lamp toward the lower left and gently tilts her fingers toward the camera. Her cured nails are mirror-glossy, and a crisp reflection of the window light glides across each nail as the hand turns. Nobody wipes the nails. The lamp stays in place. Natural soft daylight from the left, blush pink background, realistic skin texture.

QC: ☐ tay rút ra mượt, không đổi số ngón ☐ móng bóng gương, vệt sáng lướt qua ☐ đèn đứng yên, không biến dạng, không hiện chữ ☐ màu đỏ giữ nguyên
Sửa nếu lỗi: tay méo khi xoay → bỏ "tilts her fingers", giữ "slides her hand out"
```
