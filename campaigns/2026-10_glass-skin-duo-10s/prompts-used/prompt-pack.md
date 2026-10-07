# Prompt Pack — Glass Skin Duo — "Sixty Seconds" · thẻ ảnh (cổng 1)

Model: **GPT Image 2** · 9:16 (1152×2048).
Đợt gen: **Đợt 1:** A-01 + B-04 (không phụ thuộc nhau) → QC A-01 → **Đợt 2:** B-01, B-02, B-03.
Lưu tất cả vào `campaigns/2026-10_glass-skin-duo-10s/outputs/images/`.
A-02 = `_products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png` (dùng trực tiếp, không gen).

---

### A-01 / seed Maren
Tool + cấu hình: GPT Image 2 · 9:16 · quality **high** (seed)
Lưu về: `KREIZI-2026-10-GLASSDUO_A-01_seed-maren_v1.png`
Phụ thuộc: không
Lệnh gen: `--ratio 9:16 --quality high`

FRAME CONTENT: Maren nhìn thẳng camera, biểu cảm bình thản, khoé môi hơi cười. Hai tay không trong khung.
COMPOSITION AND CAMERA: chân dung ngực trở lên, ngang mắt, mặt ở 1/3 trên, nền tường be mờ.
LIGHTING AND STYLE: nắng sáng ấm frame-left ~4500K, bóng mềm sang phải, ảnh chụp thật.
MUST PRESERVE: theo `_characters/maren/profile.md`.
AVOID: da làm mịn kiểu nhựa, trang điểm đậm, trông như người mẫu trẻ nhuộm tóc bạc, sản phẩm trong khung.

PROMPT
```
Scene: bright bathroom in a coastal California home in the early morning, warm beige plaster wall softly out of focus behind her.

Subject: a woman in her late 50s, chest-up portrait, looking straight into the camera with a calm, quietly confident expression and the faint start of a smile. Natural silver-grey shoulder-length wavy hair with a few darker strands, tucked behind her left ear. Light hazel eyes, soft natural brows with some grey. Light warm sun-kissed skin with real texture: visible pores, fine lines around the eyes and mouth, a few light freckles on the cheeks. Healthy dewy sheen on the cheekbones, no makeup. Ivory waffle-knit robe open at the collarbone, small gold stud earrings.

Important Details: warm morning sunlight from frame-left around 4500K, soft shadow falling to the right side of her face, 85mm portrait feel, shallow depth of field, eye level, her face sits in the upper third of the frame. Real skin detail is the priority.

Use Case: character reference portrait for a skincare video ad, looks like a real unretouched photograph.

Constraints: exactly one person, hands not in frame, no skincare products in frame, no text, no logo, no watermark, no beauty retouching, no plastic-smooth skin, no heavy makeup, keep her looking her real age.
```
QC: ☐ tuổi ~58 thật ☐ texture da thật ☐ tóc bạc tự nhiên ☐ ánh sáng frame-left ☐ áo + khuyên tai đúng
Sửa 1 lần (nếu lỗi): "Change: make the skin texture more natural, visible pores and fine lines. Preserve: face, hair, pose, lighting, framing."

---

### B-01 / S01 — ấn ngón tay lên gò má
Tool + cấu hình: GPT Image 2 · 9:16 · quality **high** (mặt)
Lưu về: `KREIZI-2026-10-GLASSDUO_B-01_S01-cheek-press_v1.png`
Phụ thuộc: A-01 pass
Lệnh gen: `--ratio 9:16 --quality high --ref outputs/images/KREIZI-2026-10-GLASSDUO_A-01_seed-maren_v1.png`

REFERENCE IMAGE ROLES: Image 1 = A-01 — nhận diện (mặt, tóc, áo, khuyên tai).
FRAME CONTENT: khoảnh khắc **đầu hành động**: mắt nhắm nhẹ, 2 đầu ngón (giữa + áp út) tay phải vừa chạm gò má trái của khung (má gần nắng), chưa vuốt.
COMPOSITION AND CAMERA: close-up 3/4 mặt quay về frame-left, ngang mắt. Mặt chiếm ~55% chiều cao, nằm 2/3 trên. 1/4 dưới khung là cổ + áo choàng (chừa chỗ chữ lower third).
LIGHTING AND STYLE: như A-01; nắng chiếu vào má, da ánh dewy.
MUST PRESERVE: mặt Maren, tóc, áo choàng, khuyên tai.
AVOID: tay 6 ngón, ngón tay lún vào má, sản phẩm trong khung.

PROMPT
```
Using the woman from Image 1. Keep her facial features, hair, skin texture, robe and earrings exactly the same as Image 1.

Scene: same bright coastal bathroom in the early morning, warm beige wall softly out of focus.

Subject: close-up of her face in a three-quarter view turned toward frame-left, eyes gently closed, relaxed expression. The fingertips of her right hand (middle and ring finger only) are just touching her cheekbone, resting lightly, about to press upward. The touch is light, the skin is not pushed in.

Important Details: warm morning sunlight from frame-left around 4500K falls across her cheek and makes the freshly applied skincare look dewy and luminous, real visible pores and fine lines, soft shadow to the right. 100mm feel, eye level, her face fills the upper two thirds of the frame, the bottom quarter shows her neck and the ivory waffle robe collar. Natural short bare nails, realistic hand with five fingers.

Use Case: first frame of a skincare video ad, real photograph look.

Constraints: exactly one person, exactly one hand in frame with five fingers, no bottle or jar in frame, no text, no logo, no watermark, no beauty retouching, no plastic skin, do not change her face.
```
QC: ☐ cùng người với A-01 ☐ 5 ngón, chạm nhẹ ☐ glow tự nhiên ☐ chừa 1/4 dưới ☐ không sản phẩm

---

### B-02 / S02 — bơm serum lên đầu ngón tay
Tool + cấu hình: GPT Image 2 · 9:16 · quality **high** (label)
Lưu về: `KREIZI-2026-10-GLASSDUO_B-02_S02-serum-pump_v1.png`
Phụ thuộc: A-01 pass
Lệnh gen: `--ratio 9:16 --quality high --ref _products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png --ref outputs/images/KREIZI-2026-10-GLASSDUO_A-01_seed-maren_v1.png`

REFERENCE IMAGE ROLES: Image 1 = A-02 — bao bì chai serum (chỉ chai xanh). Image 2 = A-01 — tông da tay + tay áo choàng.
FRAME CONTENT: khoảnh khắc **ngay trước** khi ấn bơm: tay phải cầm thân chai, ngón trỏ đặt trên đầu bơm; tay trái ngửa, 2 đầu ngón ngay dưới vòi bơm.
COMPOSITION AND CAMERA: macro tay + chai, góc nhìn xuống ~30°, chai ở giữa, label hướng thẳng camera. Nền: bàn travertine kem mờ. 1/4 dưới trống cho chữ.
LIGHTING AND STYLE: nắng frame-left ~4500K, bóng sang phải; chai kính mờ bắt sáng mềm.
MUST PRESERVE: chai kính MỜ xanh da trời nhạt, vai tròn, đầu bơm + nắp TRẮNG, chữ trắng "KREIZI / BEAUTY", "LUMINOUS / GLASS SKIN SERUM".
AVOID: chai trong suốt, chữ label sai, hũ booster trong khung, giọt serum đã rơi.

PROMPT
```
Use Image 1 only as the reference for the serum bottle: the frosted powder-blue glass bottle with rounded shoulders, white pump and white collar, and white printed text. Use Image 2 only for the skin tone of the hands and the ivory waffle robe sleeve.

Scene: warm cream travertine bathroom counter in early morning, background softly blurred beige.

Subject: macro close-up of two hands of a woman in her late 50s. Her right hand holds the serum bottle upright with the index finger resting on top of the white pump, about to press it. Her left hand is held palm up just below the pump nozzle, middle and ring fingertips together, ready to catch a drop. The ivory waffle robe sleeve is visible at the wrist. Nothing has been dispensed yet.

Important Details: bottle label faces the camera straight on and reads exactly "KREIZI" with "BEAUTY" below, then "LUMINOUS" and "GLASS SKIN SERUM" in white letters, 100 percent readable and physically believable. Frosted glass catches soft light. Warm morning sunlight from frame-left around 4500K, soft shadows to the right. Real hand texture: visible knuckle lines, slight veins, natural short bare nails. Camera looking down at about 30 degrees, the bottle in the centre, the bottom quarter of the frame is calm blurred counter.

Use Case: first frame of a skincare product demo video ad, real photograph look.

Constraints: exactly one bottle, no moisturizer jar in frame, two hands with five fingers each, no drop dispensed yet, no extra words, no duplicate text, no watermark, keep the bottle frosted powder-blue and the pump white.
```
QC: ☐ chai đúng màu/dáng ☐ chữ label đúng ☐ 2 tay 5 ngón ☐ chưa có giọt ☐ chừa chỗ cho tay ấn xuống
Sửa 1 lần (nếu label sai): edit chính ảnh này, "Change: correct only the bottle label text to KREIZI / BEAUTY / LUMINOUS / GLASS SKIN SERUM, matching Image 1. Preserve everything else."

---

### B-03 / S03 — ngón tay múc Moisture Booster
Tool + cấu hình: GPT Image 2 · 9:16 · quality **high** (label)
Lưu về: `KREIZI-2026-10-GLASSDUO_B-03_S03-booster-dip_v1.png`
Phụ thuộc: A-01 pass
Lệnh gen: `--ratio 9:16 --quality high --ref _products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png --ref outputs/images/KREIZI-2026-10-GLASSDUO_A-01_seed-maren_v1.png`

REFERENCE IMAGE ROLES: Image 1 = A-02 — bao bì hũ booster + kem đánh bông. Image 2 = A-01 — tông da tay.
FRAME CONTENT: khoảnh khắc **ngay trước** khi chạm: hũ mở nắp, kem trắng chóp mềm; ngón trỏ tay phải lơ lửng ~1cm trên mặt kem.
COMPOSITION AND CAMERA: macro, nhìn xuống ~45°, hũ ở giữa-dưới, chữ "KREIZI" hướng thẳng camera. Nắp hũ đặt nghiêng cạnh hũ. 1/4 dưới chừa chỗ chữ (bề mặt đá).
LIGHTING AND STYLE: như B-02.
MUST PRESERVE: hũ kính MỜ TRẮNG, thấp, miệng rộng, chữ "KREIZI" rose-gold serif letter-spacing rộng; kem trắng đánh bông chóp mềm.
AVOID: hũ sai màu, chữ sai, chai serum trong khung, ngón tay đã lún vào kem.

PROMPT
```
Use Image 1 only as the reference for the moisturizer jar: the short wide-mouth frosted white glass jar with "KREIZI" printed in rose-gold serif letters with wide letter spacing, and the whipped white cream with soft peaks. Use Image 2 only for the skin tone of the hand.

Scene: warm cream travertine bathroom counter in early morning, a small sprig of green seaweed and red algae lying to the right, background softly blurred beige.

Subject: the open jar sits on the counter, its white lid resting at an angle beside it. The jar is full of whipped white cream with soft swirled peaks. The index finger of a woman's right hand (late 50s, natural short bare nail) hovers about one centimetre above the cream, about to dip in. Not touching yet.

Important Details: the word "KREIZI" on the jar faces the camera straight on, rose-gold, 100 percent readable and physically believable. Camera looking down at about 45 degrees, jar in the centre of the lower half. Warm morning sunlight from frame-left around 4500K, soft shadows to the right, real skin texture on the finger. Bottom quarter of the frame shows calm travertine surface.

Use Case: first frame of a skincare product demo video ad, real photograph look.

Constraints: exactly one jar, no serum bottle in frame, one hand only, finger not touching the cream yet, no extra words, no duplicate text, no watermark, keep the jar frosted white and the lettering rose-gold.
```
QC: ☐ hũ đúng ☐ chữ KREIZI đúng ☐ kem chóp mềm ☐ ngón chưa chạm ☐ 1 tay

---

### B-04 / S04 — packshot end card (chỉnh sửa A-02) — ❌ HUỶ, không gen (xem Kết quả gen)
Tool + cấu hình: GPT Image 2 · 9:16 · quality **high** (label)
Lưu về: `KREIZI-2026-10-GLASSDUO_B-04_S04-packshot_v1.png`
Phụ thuộc: không
Lệnh gen: `--ratio 9:16 --quality high --ref _products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png`

THAY ĐỔI: mở rộng khung 1:1 → 9:16, thêm tường be phía trên.
MỨC ĐỘ: chỉ mở rộng nền, sản phẩm không đổi.
GIỮ NGUYÊN: chai + hũ (dáng, màu, chữ), khối travertine, tảo xanh + đỏ, vòng gương đồng, hướng nắng.

PROMPT
```
Edit the attached image.

Change: extend the canvas to a tall 9:16 vertical frame. Place the existing product group (serum bottle, moisturizer jar, travertine block, seaweed and red algae) in the lower half of the frame, and continue the soft warm beige wall with the same diffused sunlight and window-shadow pattern upward to fill the empty upper half.

Preserve: the serum bottle, the jar, all label text exactly as in the original, their size relative to each other, the travertine block, the seaweed and algae, the brass mirror arc, the lighting direction from frame-left and the colour palette.

Constraints: no new objects, no added text, no logo, no watermark, no redesign of the packaging, the upper half stays calm and empty for headline text.
```
QC: ☐ label giữ nguyên ☐ nửa trên trống, sạch ☐ không vật thể lạ ☐ nối nền liền mạch

---

## Kết quả gen (cổng 2, 2026-10-02)
| Ảnh | Kết quả | Ghi chú |
|---|---|---|
| A-01 | **worked** (v1) | Đúng tuổi, texture da thật, tóc bạc, áo + khuyên tai. Đã copy → `_characters/maren/reference-images/maren-face-ref-01.png` |
| B-01 | **worked** (v1) | Cùng người với A-01. 4 ngón chạm má (thẻ ghi 2 ngón), tự nhiên, chấp nhận |
| B-02 | **worked** (v1) | Label đúng từng chữ (soi bản gốc). Chưa có giọt, tay ở đúng vị trí |
| B-03 | **worked** (v1) | Chữ KREIZI rose-gold đúng, ngón chưa chạm kem. Mép phải có vật trắng mờ ở hậu cảnh, không ảnh hưởng |
| B-04 | **không gen** | Theo `_skills/image/SKILL.md` mục 6: end card cần label đúng 100% → dùng ảnh thật A-02 ghép trong Remotion (cổng 3) |

---

# Thẻ video — Veo 3.1 (cổng 2, viết theo ảnh đã pass)

Chung cho cả 3 thẻ: **Veo 3.1 · image-to-video · 9:16 · 1080p · render 4s**. Không dùng last frame. Âm thanh: clip **không tự sinh lời/nhạc/SFX**, VO + nhạc + SFX thêm khi dựng.
Lưu về `outputs/videos/`.

### S01 · `KREIZI-2026-10-GLASSDUO_S01_cheek-press_v1.mp4`
Render: 4s · Dùng: ~0.3–3.3s = 3.0s
INPUT: First frame = `outputs/images/KREIZI-2026-10-GLASSDUO_B-01_S01-cheek-press_v1.png`
STARTING FRAME: mắt nhắm, 4 đầu ngón tay phải đặt nhẹ trên gò má, áo choàng trắng.
ACTION AND TIMING: 0.0–2.0s ấn nhẹ, vuốt chậm lên phía thái dương · 2.0–2.8s nhấc tay ra khỏi khung · 2.8–4.0s mở mắt, thở ra, cười nhẹ.
CAMERA: push-in rất chậm, 100mm.
CONTINUITY: mặt Maren, tóc, áo; nắng frame-left ~4500K; da không bị kéo méo khi tay ấn.
ENDING FRAME: mặt 3/4, mắt mở, tay đã ra khỏi khung, má ánh dewy trong nắng, giữ yên ~1s.
AVOID: mặt trôi, ngón tay lún sâu, xoa nhiều vòng, thêm sản phẩm vào khung.

PROMPT
```
Maintain the subject from the first frame. Very slow push-in, 100mm portrait lens. Her fingertips press gently into her cheekbone and glide slowly upward toward her temple, the skin moving only slightly under the light touch. Around 2 seconds her hand lifts away and leaves the frame. She opens her eyes softly, exhales through her nose, and a faint calm smile forms. Warm morning sunlight from frame-left catches the fresh dewy sheen on her cheek, a few loose silver strands drift slightly. Real skin texture with visible pores and fine lines, no retouching. Ends on her face in three-quarter view, eyes open, hand out of frame, holding still.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
QC: ☐ cùng mặt với B-01 suốt clip ☐ tay ra khỏi khung trước 3s ☐ không méo má ☐ ending đúng

### S02 · `KREIZI-2026-10-GLASSDUO_S02_serum-pump_v1.mp4`
Render: 4s · Dùng: ~0.2–3.2s = 3.0s
INPUT: First frame = `outputs/images/KREIZI-2026-10-GLASSDUO_B-02_S02-serum-pump_v1.png`
STARTING FRAME: tay phải cầm chai, ngón trỏ trên đầu bơm; tay trái ngửa dưới vòi.
ACTION AND TIMING: 0.0–1.0s ngón trỏ ấn bơm xuống 1 lần · 1.0–2.0s 1 giọt gel trong, hơi xanh, có bọt khí nhỏ rơi xuống đầu ngón tay trái · 2.0–4.0s nhả bơm, giữ yên.
CAMERA: static, 100mm macro.
CONTINUITY: "Do not alter product color, label, or packaging shape." Chai đứng thẳng, label hướng camera suốt clip.
ENDING FRAME: giọt gel nằm trên đầu ngón tay trái, chai đứng yên, giữ ~1.5s.
AVOID: chai xoay, chữ label nhoè, nhiều giọt / tia phun, gel bay ngược.

PROMPT
```
Maintain the hands and the serum bottle from the first frame. Static 100mm macro shot. Her index finger presses the white pump down once with a soft, steady push. A single drop of clear gel with a faint blue tint and tiny suspended bubbles falls from the nozzle and lands on the fingertips of her open left hand, settling into a small glossy bead. The pump rises back up and both hands stay still. The bottle stays upright with its label facing the camera the whole time. Do not alter product color, label, or packaging shape. Warm morning sunlight from frame-left, soft shadows on the travertine counter. Ends on the single gel bead resting on her fingertips, holding still.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
QC: ☐ label giữ nguyên ☐ đúng 1 giọt ☐ chai không xoay ☐ tay không méo

### S03 · `KREIZI-2026-10-GLASSDUO_S03_booster-dip_v1.mp4`
Render: 4s · Dùng: ~0.3–2.8s = 2.5s
INPUT: First frame = `outputs/images/KREIZI-2026-10-GLASSDUO_B-03_S03-booster-dip_v1.png`
STARTING FRAME: hũ mở, kem chóp mềm, ngón trỏ lơ lửng trên mặt kem.
ACTION AND TIMING: 0.0–1.2s ngón trỏ hạ xuống, chạm và múc 1 chút kem · 1.2–2.5s nhấc ngón lên về phía trên-phải, đầu ngón có kem · 2.5–4.0s giữ yên.
CAMERA: static, 100mm macro.
CONTINUITY: "Do not alter product color, label, or packaging shape." Hũ không xoay, chữ KREIZI hướng camera.
ENDING FRAME: ngón tay nhấc lên với 1 chút kem trắng, mặt kem có vết lõm gọn, giữ ~1.5s.
AVOID: hũ dịch chuyển, chữ méo, kem chảy lỏng, thêm tay thứ hai.

PROMPT
```
Maintain the jar, cream and hand from the first frame. Static 100mm macro shot. Her index finger lowers slowly, touches the whipped white cream and scoops a small soft dollop, leaving a neat shallow dent in the swirled surface. The finger lifts away toward the upper right with the thick cream holding its shape on the fingertip. The jar does not move and the rose-gold KREIZI lettering stays facing the camera. Do not alter product color, label, or packaging shape. Warm morning sunlight from frame-left, soft window shadows across the travertine, seaweed sprig still beside the jar. Ends on the lifted fingertip with a dollop of cream above the open jar, holding still.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
QC: ☐ chữ KREIZI giữ nguyên ☐ kem đặc, giữ chóp ☐ hũ đứng yên ☐ 1 tay

### S04 · end card — MOTION-GRAPHIC
Dựng bằng Remotion ở cổng 3, không render tool ngoài. Nguồn: ảnh thật `_products/Kreizi/glass-skin-duo/reference-images/duo-hero-serum-booster-01.png` đặt nửa dưới khung 9:16, nền kem phía trên, chữ theo `script.md`.
