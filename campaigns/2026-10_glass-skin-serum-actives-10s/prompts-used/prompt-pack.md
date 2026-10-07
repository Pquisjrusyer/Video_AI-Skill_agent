# Prompt Pack — `KREIZI-2026-10-ACTIVES`

> Cổng 1: thẻ ảnh (chưa gen). Gen ở đầu cổng 2 bằng `_tools/gen-image.py`, chạy từ thư mục gốc project.
> `C=campaigns/2026-10_glass-skin-serum-actives-10s`
> A-01, A-02 = ảnh user gửi, đã lưu ở `$C/outputs/images/`. A-02 dùng trực tiếp cho S03, không gen.
> **Đợt gen:** đợt 1 = B-01 + B-03 (song song) → đợt 2 = B-02 (edit từ B-01 đã pass).
> Thẻ video viết ở cổng 2, sau khi ảnh pass.

---

### B-01 / S01 — 4 hoạt chất lơ lửng trên mặt da (first frame)
Tool + cấu hình: GPT Image 2 · 9:16 · quality medium
Lưu về: `$C/outputs/images/KREIZI-2026-10-ACTIVES_B-01_S01-actives-above-skin_v1.png`
Phụ thuộc: không (đợt 1)
Lệnh gen: `--ratio 9:16 --quality medium --ref $C/outputs/images/KREIZI-2026-10-ACTIVES_A-01_ref-skin-cross-section_v1.png`

REFERENCE IMAGE ROLES: Image 1 = A-01. Lấy phong cách minh hoạ, bảng màu, chất liệu và dáng 4 quả cầu.
FRAME CONTENT: 4 quả cầu trong suốt lơ lửng thành hàng hơi cong, cách mặt da một khoảng ngắn, chưa chạm da. Từ trái sang: (1) cầu xanh lá có nhành tảo xanh, (2) cầu hồng nhạt có nhành tảo đỏ, (3) cầu trong suốt có mô hình phân tử trắng, (4) cầu xanh dương nhạt có mô hình phân tử xanh dương.
COMPOSITION AND CAMERA: gần hơn A-01. Mặt cắt da chiếm nửa dưới khung, chủ yếu là các lớp biểu bì phía trên. Chỉ thấy phần đầu của 1–2 nang lông, **không thấy lớp mỡ**. 4 quả cầu ở khoảng 38–48% chiều cao khung, to hơn trong A-01. 1/4 trên cùng là nền trắng trơn để đặt chữ. Nhìn ngang, hơi chếch từ trên xuống.
LIGHTING AND STYLE: minh hoạ 3D y khoa sạch, sáng mềm từ trên, nền trắng ngà, da tông kem/hồng đào, quả cầu bóng như thuỷ tinh.
MUST PRESERVE: phong cách và bảng màu A-01, nội dung đúng của 4 quả cầu.
AVOID: chữ/nhãn trong ảnh, mũi tên, quả cầu đã chạm hoặc chìm vào da, lớp mỡ vàng, máu đỏ đậm.

PROMPT
```
Use Image 1 as the reference for illustration style, colour palette, skin-layer rendering and the look of the four glass spheres.

Scene: clean bright white studio background, soft even light from above, a 3D medical-illustration cross-section of human skin.

Subject: four transparent glass-like spheres floating in a gentle curved row just above the skin surface, not touching it. From left to right: a pale green sphere holding small fronds of green seaweed; a pale pink sphere holding a fine branch of red algae; a clear sphere holding a simple white ball-and-stick molecule model; a pale blue sphere holding a blue ball-and-stick molecule model. The spheres are glossy with soft highlights and tiny droplets on their surface.

Important Details: the skin cross-section fills the lower half of the frame and is framed closer than Image 1, showing mainly the upper skin layers: the thin top layer with fine flaky texture, then the pink cellular layer below, with the tops of one or two hair shafts. No fat layer is visible. Cream and peach skin tones, soft translucent rendering. The spheres sit between 38 and 48 percent of the frame height and are larger than in Image 1. The top quarter of the frame is plain soft white, empty. Camera at eye level with the surface, tilted slightly down.

Use Case: first frame of a skincare video ad, 3D scientific illustration.

Constraints: no text, no labels, no arrows, no logos, no watermark; the spheres must not touch or sink into the skin; no yellow fat layer; no deep blood vessels in the foreground.
```
QC: ☐ đúng style A-01 ☐ 4 quả cầu đúng nội dung + thứ tự ☐ quả cầu chưa chạm da ☐ không lớp mỡ ☐ 1/4 trên trống ☐ không chữ
Sửa 1 lần (lỗi hay gặp là quả cầu đã chìm vào da): edit ảnh này, "Change: move all four spheres up so they float clearly above the skin surface with a small gap. Preserve everything else."
Kết quả: worked (v1 pass QC 2026-10-02)

---

### B-02 / S01 — mặt da ngậm nước, bóng như kính (last frame)
Tool + cấu hình: GPT Image 2 · 9:16 · quality medium
Lưu về: `$C/outputs/images/KREIZI-2026-10-ACTIVES_B-02_S01-glass-surface_v1.png`
Phụ thuộc: **B-01 pass** (đợt 2)
Lệnh gen: `--ratio 9:16 --quality medium --ref $C/outputs/images/KREIZI-2026-10-ACTIVES_B-01_S01-actives-above-skin_v1.png`

THAY ĐỔI: 4 quả cầu biến mất. Lớp trên cùng của da căng mọng, mịn, phủ màng nước trong, phản sáng như kính.
MỨC ĐỘ: vừa. Chỉ đổi quả cầu + bề mặt lớp trên cùng.
GIỮ NGUYÊN: bố cục, góc máy, khung, nền trắng, các lớp da bên dưới, nang lông, bảng màu, ánh sáng.

PROMPT
```
Change: remove the four floating spheres completely. Make only the outermost skin layer look plump, smooth and hydrated: its flaky texture becomes a smooth even surface covered by a thin clear film of water with a bright glass-like reflection running along it, and a few tiny clear droplets resting on top.

Preserve: the exact framing, camera angle and crop of Image 1, the white background, the empty top quarter, every skin layer below the outermost one, the hair shafts, the colour palette, the illustration style and the lighting.

Constraints: the water stays on the outermost layer only, nothing travels into the deeper layers; no arrows, no text, no labels, no new objects, no redesign.
```
QC: ☐ khung y hệt B-01 ☐ quả cầu đã biến mất ☐ bóng như kính chỉ ở lớp trên cùng ☐ lớp dưới không đổi ☐ không chữ/mũi tên
Sửa 1 lần (nếu khung lệch so với B-01): gen lại với thêm câu "The image must align pixel for pixel with Image 1 except the outermost layer."
Kết quả: worked (v1 pass QC 2026-10-02)

---

### B-03 / S02 — giọt gel serum trên mu bàn tay (first frame)
Tool + cấu hình: GPT Image 2 · 9:16 · quality medium
Lưu về: `$C/outputs/images/KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v1.png`
Phụ thuộc: không (đợt 1)
Lệnh gen: `--ratio 9:16 --quality medium --ref _products/Kreizi/glass-skin-duo/reference-images/serum-texture-callout-01.png`

REFERENCE IMAGE ROLES: Image 1 = `serum-texture-callout-01.png`. **Chỉ** lấy chất gel (trong, hơi xanh, có bọt khí nhỏ). Không lấy chữ, callout hay bố cục.
FRAME CONTENT: khoảnh khắc **ngay trước** khi tán. Mu bàn tay trái của phụ nữ ~58 tuổi nằm ngang. 1 giọt gel cỡ hạt đậu nằm trên mu bàn tay. Đầu ngón trỏ tay phải lơ lửng ~1cm phía trên giọt gel, chưa chạm.
COMPOSITION AND CAMERA: macro, nhìn xuống ~30°. Giọt gel ở giữa khung, hơi cao hơn tâm. Mu bàn tay chéo khung từ trái dưới sang phải trên. Chỉ thấy đầu ngón trỏ từ góc phải trên. 1/3 dưới là phần da/nền mờ, trống để đặt chữ.
LIGHTING AND STYLE: ánh sáng ban ngày mềm từ frame-left ~5000K, nền kem/trắng ngà mờ (nối được với nền trắng của S01). Ảnh chụp thật.
MUST PRESERVE: da có texture thật (lỗ chân lông, nếp nhăn nhỏ ở khớp, vài đốm nắng nhạt), móng ngắn tự nhiên không sơn, gel trong hơi xanh có bọt khí.
AVOID: da bị làm mịn, tay thừa ngón, ngón đã chạm gel, nhẫn/vòng, chai serum trong khung, chữ.

PROMPT
```
Use Image 1 only as the reference for the serum texture: a clear gel with a faint blue tint and many tiny suspended air bubbles. Ignore all text, callouts and layout in Image 1.

Scene: soft natural daylight from frame-left around 5000K, plain softly blurred warm ivory background.

Subject: macro close-up of the back of the left hand of a woman in her late fifties, lying flat and angled diagonally from lower left to upper right. A single pea-sized drop of clear, faintly blue serum gel with tiny air bubbles sits on the back of her hand, slightly above the centre of the frame. The tip of her right index finger enters from the upper right and hovers about one centimetre above the drop, not touching it yet.

Important Details: real mature skin texture: visible pores, fine crease lines over the knuckles, a few faint sun spots, slightly visible veins; natural short bare nails. The gel drop is glossy and domed, catching a small bright highlight from the left. Camera looks down at about 30 degrees, shallow depth of field, the bottom third of the frame is calm blurred skin and background.

Use Case: first frame of a skincare video ad, real macro photograph look.

Constraints: only one hand and one fingertip in frame, five fingers on the visible hand, the finger is not touching the gel, no rings or bracelets, no bottle in frame, no text, no watermark, no airbrushed or plastic skin.
```
QC: ☐ tay đúng giải phẫu ☐ ngón chưa chạm ☐ gel trong hơi xanh có bọt ☐ da có texture thật ☐ 1/3 dưới trống ☐ không chữ
Sửa 1 lần (lỗi hay gặp là ngón tay đã chạm gel hoặc da bị làm mịn): edit ảnh này, đổi đúng 1 lỗi, "Preserve everything else."
Kết quả: needs adjustment → v2 worked (2026-10-02). v1 bị chê gel trông như viên bi 3D; v2 edit v1 với ref texture `A-03_ref-serum-texture_v1.png` (user gửi) → vũng serum lỏng mỏng, trong, ngả xanh, có bọt khí. **Dùng `_v2` cho S02.**
Lệnh v2: `--ratio 9:16 --quality medium --ref $C/outputs/images/KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v1.png --ref $C/outputs/images/KREIZI-2026-10-ACTIVES_A-03_ref-serum-texture_v1.png`
PROMPT v2
```
Image 1 is the base photo. Image 2 is the reference for the serum texture only: a translucent liquid gel with a soft white-to-powder-blue gradient, glossy wet highlights and many tiny suspended air bubbles.

Change: replace the round, domed, glass-bead-like drop on the back of the hand with a realistic small puddle of freshly dispensed liquid serum, matching the texture of Image 2. It is thin and fluid, sitting flat on the skin with a slightly irregular soft edge and a gentle teardrop shape, about the size of a fingertip, translucent so the skin texture shows through it, faint powder-blue tint, wet glossy highlight from the left, tiny bubbles inside. It looks like a real photographed serum, not a 3D render.

Preserve: the hand, its pose and position, the skin texture with pores, creases and sun spots, the hovering index fingertip not touching the serum, the ivory background, the lighting from frame-left, the framing and the empty bottom third.

Constraints: one serum puddle only, no glass bead or sphere shape, no drips running off the hand, no text, no watermark, no other changes.
```

---
---

# Thẻ video (cổng 2, viết theo ảnh thật đã pass)

> User tự render trên Veo 3.1 (Google AI Studio / Flow). Bỏ file vào `outputs/videos/` đúng tên. Audio clip mute khi dựng.

### S01 · `KREIZI-2026-10-ACTIVES_S01_actives-to-glass_v1.mp4`
Tool + cấu hình: Veo 3.1 · image-to-video, **first + last frame** · 9:16 · 1080p
Render: 6s (tool chỉ cho 8s khi có last frame thì render 8s) · Dùng: 3.5s, cắt khúc có quả cầu tan + mặt da bóng
Lưu về: `outputs/videos/KREIZI-2026-10-ACTIVES_S01_actives-to-glass_v1.mp4`
INPUT IMAGE ROLES: First frame = `B-01_S01-actives-above-skin_v1.png` · Last frame = `B-02_S01-glass-surface_v1.png`
STARTING FRAME: 4 quả cầu lơ lửng trên mặt da, chưa chạm.
ACTION AND TIMING: 0–2s quả cầu trôi thẳng xuống · 2–3.5s chạm lớp ngoài cùng, tan thành nước trong · 3.5–6s mặt da phẳng, căng, vệt sáng lướt trái sang phải.
CAMERA: static (last frame cùng khung với first frame). Push-in nhẹ thêm ở Remotion nếu cần.
CONTINUITY: giữ style minh hoạ, bảng màu, thứ tự + nội dung 4 quả cầu. Nước chỉ ở lớp ngoài cùng.
ENDING FRAME: khớp B-02, giữ yên ~0.5s.
AUDIO CUES: không tạo cùng clip. VO, nhạc, SFX thêm khi dựng.
AVOID: quả cầu chìm xuống sâu / vào nang lông, mũi tên, chữ, giải phẫu biến dạng, đổi màu da.

PROMPT
```
Maintain the illustration style, skin layers and the four glass spheres from the first frame. Static camera, no zoom. From 0 to 2 seconds, the four spheres drift slowly straight down toward the skin surface, keeping their order and contents. From 2 to 3.5 seconds, each sphere gently touches the outermost skin layer and softly melts into clear water, which spreads in a thin film across the outermost layer only. From 3.5 to 6 seconds, the outermost layer becomes smooth and plump, and a bright glass-like reflection glides along the surface from left to right while a few tiny droplets settle on top. The water stays on the outermost layer; the deeper layers, hair shafts and colours do not change. No text, no arrows, no labels.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 6 seconds.
```
QC: ☐ khớp first frame ☐ quả cầu tan ở bề mặt, không chìm sâu ☐ khung cuối khớp B-02 ☐ không chữ/mũi tên ☐ không méo giải phẫu
Lỗi hay gặp → sửa: quả cầu chìm sâu → thêm vào đầu prompt "The spheres never pass below the outermost layer." · tool không nhận last frame → bỏ last frame, giữ nguyên prompt.

---

### S02 · `KREIZI-2026-10-ACTIVES_S02_hand-gel-spread_v1.mp4`
Tool + cấu hình: Veo 3.1 · image-to-video · 9:16 · 1080p
Render: 4s · Dùng: 2.5s
Lưu về: `outputs/videos/KREIZI-2026-10-ACTIVES_S02_hand-gel-spread_v1.mp4`
INPUT IMAGE ROLES: First frame = `B-03_S02-hand-gel-drop_v3.png`
STARTING FRAME: vũng serum lỏng mỏng trên mu bàn tay, đầu ngón trỏ ngay phía trên, chưa chạm.
ACTION AND TIMING: 0–1s ngón hạ xuống, ấn nhẹ vào giọt gel · 1–3s tán thành vệt mỏng bằng 2 nét ngắn chậm · 3–4s ngón rời khung lên góc phải trên, da để lại ánh bóng ẩm.
CAMERA: static macro, 100mm macro.
CONTINUITY: tay dưới nằm yên, 5 ngón, texture da giữ nguyên. Gel trong hơi xanh, tán mỏng, không chảy. Sáng từ frame-left.
ENDING FRAME: vệt gel mỏng bóng ẩm trên da, không còn ngón tay trong khung.
AUDIO CUES: không tạo cùng clip.
AVOID: thừa/thiếu ngón, da bị làm mịn, gel chảy giọt, tay dưới cử động.

PROMPT
```
Maintain the hand, skin texture and serum gel from the first frame. Static macro shot, 100mm macro lens. From 0 to 1 second, the right index fingertip lowers and gently touches the small pool of clear, milky-streaked serum gel. From 1 to 3 seconds, it spreads the serum in two short, slow strokes into a thin, wet, sheer layer with soft glossy ridges across the back of the hand. From 3 to 4 seconds, the finger lifts away out of frame to the upper right, leaving a smooth dewy sheen on the skin that catches the soft light from the left. The lower hand stays completely still with five fingers; the skin keeps its real pores and fine lines. The serum is a real fluid gel: it spreads thin, stays glossy and does not drip.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
QC: ☐ khớp first frame ☐ tay đúng giải phẫu cả clip ☐ gel tán mỏng, để lại ánh bóng ☐ ngón rời khung cuối clip ☐ da không bị làm mịn
Lỗi hay gặp → sửa: ngón biến dạng khi tán → bỏ "two strokes", chỉ "presses and spreads once in a single slow stroke".

---

### S03 · `KREIZI-2026-10-ACTIVES_S03_serum-underwater_v1.mp4`
Tool + cấu hình: Veo 3.1 · image-to-video · 9:16 · 1080p
Render: 4s · Dùng: 4.0s (end card chữ chồng từ 6.6s)
Lưu về: `outputs/videos/KREIZI-2026-10-ACTIVES_S03_serum-underwater_v1.mp4`
INPUT IMAGE ROLES: First frame = `A-02_serum-underwater_v1.png`
STARTING FRAME: chai serum giữa tảo xanh + tảo đỏ dưới nước, tia nắng góc phải trên.
ACTION AND TIMING: cả clip: bọt khí li ti bay lên, tia nắng lung linh, tảo đung đưa nhẹ. Chai đứng yên.
CAMERA: push-in rất chậm, 50mm.
CONTINUITY: "Do not alter product color, label, or packaging shape." Chai kính mờ xanh nhạt, nắp + bơm trắng, chữ label rõ.
ENDING FRAME: như đầu, gần hơn chút, label nét, giữ yên 1s cuối.
AUDIO CUES: không tạo cùng clip.
AVOID: label nhoè/đổi chữ, chai trôi/xoay, bọt khí che label.

PROMPT
```
Maintain the serum bottle, its label and the underwater scene from the first frame. Very slow push-in, 50mm lens. Tiny air bubbles rise gently past the bottle, the sunbeams from the upper right shimmer softly through the water, and the green seaweed fronds and red algae sway slightly in a slow current. The bottle stays completely still and upright, label sharp and facing the camera; no bubble passes in front of the label. Do not alter product color, label, or packaging shape. Hold the final second steady.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
QC: ☐ khớp first frame ☐ label đúng + nét cả clip ☐ chai không trôi ☐ chuyển động nước tự nhiên
Lỗi hay gặp → sửa: label méo → bỏ push-in, "static camera". Vẫn méo → dựng bằng ảnh tĩnh A-02 + Ken Burns ở Remotion.

---

### B-03 v3 / S02 — USER TỰ SỬA TAY (hết lượt gen của Claude)
Lý do: user góp ý 2026-10-02, texture serum thật gần ref `A-04_ref-serum-on-skin_v1.png` hơn: gel trong pha trắng sữa, mỏng, đặc vừa, có vệt gợn khi tán, bóng ướt, bọt khí li ti, gần như không ngả xanh.
Làm trên chatgpt.com (GPT Image): đính kèm **ảnh 1** = `outputs/images/KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v2.png`, **ảnh 2** = `outputs/images/KREIZI-2026-10-ACTIVES_A-04_ref-serum-on-skin_v1.png`, rồi dán prompt dưới. Chọn tỷ lệ dọc 9:16.
Lưu về: `outputs/images/KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v3.png`

PROMPT v3 (dán vào chatgpt.com)
```
Image 1 is the base photo. Image 2 is the reference for the serum texture only.

Change: replace the serum on the back of the hand with serum that matches Image 2 exactly: a sheer, clear gel with soft milky-white cloudy streaks, slightly thick and viscous, glossy and wet, with a few tiny air bubbles and gentle ridges where it pools. Almost no blue tint. It sits as one small, freshly dispensed pool about the size of a fingertip, slightly thicker in the centre and thinning to a soft irregular edge, the skin texture visible through it. It must look like a real macro photograph of skincare on skin, not a 3D render.

Preserve: the hand, its pose and position, the real skin texture with pores, creases and sun spots, the hovering right index fingertip that is not touching the serum, the warm ivory background, the soft light from the left, the framing and the empty bottom third. Keep the vertical 9:16 frame.

Constraints: one serum pool only, no drips running off the hand, no glass bead or sphere shape, no text, no watermark, no other changes.
```
QC: ☐ texture giống A-04 (trong + vệt trắng sữa) ☐ ngón chưa chạm ☐ tay đúng giải phẫu ☐ khung giữ như v2
Kết quả: **worked** — user sửa tay, QC 2026-10-02: texture trong + vệt trắng sữa đúng A-04, ngón chưa chạm, tay đúng giải phẫu, khung giữ như v2. **Dùng `_v3` cho S02.**

---

### S03 — sửa label (user yêu cầu 2026-10-02)
Clip v1 sai chữ label: INPUSED → INFUSED · ALGAIE → ALGAE · 50 mL → 30 mL. Chữ đúng (theo ảnh A-02):
`KREIZI` / `BEAUTY` / `LUMINOUS` / `GLASS SKIN SERUM` / `INFUSED WITH GREEN` / `SEAWEED AND RED ALGAE` / `1 fl.oz./30 mL`

**Cách 1 — Edit clip có sẵn** (Runway Aleph · Kling O1/O3 Edit · tool video-edit có ô reference image). Input video = `outputs/videos/KREIZI-2026-10-ACTIVES_S03_serum-underwater_v1.mp4`, reference = `outputs/images/KREIZI-2026-10-ACTIVES_A-02_serum-underwater_v1.png`. Lưu `..._S03_serum-underwater_v2.mp4`.
```
Correct only the printed text on the serum bottle label so it matches the reference image exactly. The white label text, top to bottom, must read: "KREIZI", "BEAUTY", "LUMINOUS", "GLASS SKIN SERUM", "INFUSED WITH GREEN", "SEAWEED AND RED ALGAE", "1 fl.oz./30 mL". Same thin white sans-serif lettering, same size, spacing and position as the reference. Keep the text sharp and stable on the bottle in every frame, following the bottle's movement. Do not change anything else: same bottle shape and frosted powder-blue colour, white pump, seaweed, red algae, bubbles, sunbeams, water motion, camera move, lighting and timing.
```

**Cách 2 — Render lại bằng Veo 3.1** (image-to-video, first frame = A-02, 9:16, 4s). Camera tĩnh, chai đứng yên để label ít bị vẽ lại. Lưu `..._S03_serum-underwater_v2.mp4`.
```
Maintain the serum bottle, its label text and the underwater scene exactly as in the first frame. Static camera, no zoom, no camera movement. The bottle stays completely still and upright, label facing the camera, every letter unchanged and sharp: "KREIZI", "BEAUTY", "LUMINOUS", "GLASS SKIN SERUM", "INFUSED WITH GREEN SEAWEED AND RED ALGAE", "1 fl.oz./30 mL". Only the environment moves: tiny air bubbles rise gently around the bottle but never in front of the label, the sunbeams from the upper right shimmer softly, and the seaweed and red algae sway slightly in a slow current. Do not alter product color, label, text, or packaging shape.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```
QC: soi chữ ở khung đầu / giữa / cuối. Còn sai → dựng S03 bằng ảnh A-02 + Ken Burns (bản review v1).

---

### S03-alt · `KREIZI-2026-10-ACTIVES_S03_model-holding-serum_v1.mp4` (user đề xuất 2026-10-05, thay cảnh chai dưới nước)
Tool + cấu hình: Veo 3.1 · image-to-video · 9:16 · 1080p
Render: 6s · Dùng: 4.0s (6.0–10.0s trên timeline, chọn đoạn đẹp nhất). Chữ end card đặt ở 1/3 trên (vùng tường trống).
INPUT IMAGE ROLES: First frame = `outputs/images/KREIZI-2026-10-ACTIVES_A-05_model-holding-serum_v1.png` (user gửi)
STARTING FRAME: phụ nữ ~45, tóc nâu xoăn ngắn, cardigan xanh rêu, nhìn thẳng camera, mỉm cười nhẹ, 2 tay cầm chai serum ngang cằm, phòng tắm sáng.
ACTION AND TIMING: 0–1.5s đứng yên, chớp mắt tự nhiên, nụ cười ấm dần · 1.5–4s nghiêng đầu rất nhẹ về phía chai, hít thở nhẹ, mắt vẫn nhìn camera · 4–6s gật đầu nhẹ 1 lần, cười tươi hơn chút, giữ yên.
CAMERA: static, khoá máy, không zoom. (Push-in làm label bị vẽ lại → không dùng.)
CONTINUITY: tay + chai **đứng yên tuyệt đối**, label hướng thẳng camera. Chỉ đầu, mắt, môi (khép), tóc và vai chuyển động nhẹ. Ánh sáng ban ngày mềm từ cửa sổ frame-left.
ENDING FRAME: như đầu cảnh, nụ cười rõ hơn, giữ yên ~1s.
AUDIO CUES: không tạo cùng clip. VO-S03 + nhạc thêm khi dựng.
AVOID: miệng mấp máy như đang nói, xoay/nghiêng chai, ngón tay trượt, chữ label đổi, mặt biến dạng khi nghiêng đầu.

PROMPT
```
Maintain the woman, her face, hair, clothing, both hands and the serum bottle exactly as in the first frame. Locked-off static camera, no zoom, no camera movement. From 0 to 1.5 seconds she stays still, blinks naturally and her soft smile slowly warms. From 1.5 to 4 seconds she tilts her head very slightly toward the bottle and takes a gentle breath, eyes still looking into the camera. From 4 to 6 seconds she gives one small, calm nod and her smile becomes a little brighter, then she holds still. Her lips stay closed; she does not speak. Her hands and the serum bottle remain completely still: the bottle does not move, tilt or rotate, the label keeps facing the camera with every letter unchanged and sharp. A few strands of hair move slightly. Soft daylight from the window on the left stays constant. Do not alter product color, label, text, or packaging shape.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 6 seconds.
```
QC: ☐ khớp first frame ☐ chai + tay không trôi/xoay ☐ label không đổi chữ (soi đầu/giữa/cuối) ☐ miệng khép, không mấp máy ☐ mặt giữ nhận diện khi nghiêng đầu
Lỗi hay gặp → sửa: label vẫn đổi → bỏ đoạn nghiêng đầu, chỉ giữ "blinks and smiles" · miệng mấp máy → thêm "mouth fully closed and relaxed the entire time".
Lưu ý ảnh gốc: chai ngả xanh mint (chai thật powder blue) · dòng "INFUSED WITH GREEN / SEAWEED AND RED ALGAE" đã hơi nhoè từ ảnh gốc.
