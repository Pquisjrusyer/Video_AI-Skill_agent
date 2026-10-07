# Prompt Pack — Kolor Blooming Gel — "One Dot" · lượt 4A (ảnh)

Model: **GPT Image 2** · quality `high` · size `1152×2048` (9:16) cho cả 4 ảnh.
Thứ tự: **A-04 trước → duyệt → rồi B-01/B-02/B-03** (cả 3 edit từ A-04).
Lưu tất cả vào: `campaigns/2026-10_kolor-blooming-gel/outputs/images/`

---

## A-04 — nền móng chuẩn ✅ ĐÃ DUYỆT

**Ref:** `_products/kolor-blooming-gel/reference-images/blooming-gel_official-02.jpg`
**Lưu:** `KOLOR-2026-10-BLOOM_A-04_nail-base_v1.png`

```
Create a photorealistic extreme macro product-demo photograph for a nail-care video ad.

Scene: seamless plain studio surface in light warm grey #f2f2f0, shot from directly
above, nothing else in the environment.

Subject: one single index finger lying horizontally across the frame, with a medium-long
almond-shaped nail coated in a cured nude-pink base gel. The nail surface is completely
bare and smooth — a clean glossy base ready to be worked on.

Important Details: mirror-glossy wet-look gel surface with one long thin specular
highlight running along the nail; large soft diffused light source from above and
slightly frame-left; neutral slightly cool white balance; real skin texture with visible
fingerprint ridges, knuckle creases and natural pores; soft contact shadow under the
finger; the nail occupies roughly 45 percent of the frame height and sits in the lower
middle, leaving clean empty surface in the upper third of the frame.

Use Case: product demo keyframe, looks like a real photograph taken in a nail studio.

Constraints: exactly one finger in frame, bare nail with no art and no color drops,
no bottle, no brush, no UV lamp, no hands other than this one, no text, no logo,
no watermark, no beauty retouching or plastic-smooth skin, keep the background a single
flat uninterrupted tone.
```

---

## B-01 / S01 — giọt màu vừa chạm móng

**Ref:** `outputs/images/KOLOR-2026-10-BLOOM_A-04_nail-base_v1.png` (ảnh gốc để edit)
**Lưu:** `KOLOR-2026-10-BLOOM_B-01_S01-dot_v1.png`

```
Edit the attached image.

Change: add exactly one single round droplet of deep rose-red gel polish #b0294a
sitting at the centre of the nail, still beaded up on the glossy surface with a crisp
sharp edge, as if it landed a fraction of a second ago and has not started to spread yet.

Preserve: the finger, nail shape, skin tone, skin texture, background tone, lighting
direction and quality, the long specular highlight on the nail, framing, camera angle
and aspect ratio — all exactly as in the original.

Constraints: exactly one droplet, no spreading or blooming yet, no brush strokes, no
bottle or brush in frame, no additional colors, no change to composition or crop,
no extra objects, no text, no watermark.
```

---

## B-02 / S02 — cọ vào khung, chưa chạm móng

**Ref 1:** `outputs/images/KOLOR-2026-10-BLOOM_A-04_nail-base_v1.png` (ảnh gốc để edit)
**Ref 2:** `_products/kolor-blooming-gel/reference-images/blooming-gel_official-04.jpg` (dáng cọ thật + độ trong của gel)
**Lưu:** `KOLOR-2026-10-BLOOM_B-02_S02-brush_v1.png`

```
Edit the attached image (Image 1), using Image 2 only as a reference for the brush shape
and the clarity of the gel.

Change: tilt the camera to a roughly 30-degree angled view of the same finger, and bring
a flat black nail-art brush into frame from the right edge, angled down toward the nail.
The brush tip is loaded with completely clear colorless gel that catches one small
highlight. The brush is still hovering just above the nail and has not touched it yet.

Preserve: the same single finger, almond nail shape, nude base gel, skin tone and skin
texture, flat light grey #f2f2f0 background, lighting direction from above frame-left,
neutral cool white balance, glossy wet-look nail surface, aspect ratio.

Important Details: the brush handle is matte soft-touch black; the gel on the tip is
water-clear and colorless; leave a clean empty band across the lower part of the frame
for a caption to be added later in editing.

Constraints: only the brush tip and a short section of the handle are visible — no hand,
no fingers holding the brush, no arm; no UV or LED lamp anywhere in frame; the brush does
not touch the nail; the gel is colorless; no product bottle in frame; no text, no logo,
no watermark.
```

---

## B-03 / S03 — chấm màu nâu khói, chưa loang

**Ref:** `outputs/images/KOLOR-2026-10-BLOOM_A-04_nail-base_v1.png` (ảnh gốc để edit)
**Lưu:** `KOLOR-2026-10-BLOOM_B-03_S03-marble_v1.png`

```
Edit the attached image.

Change: add exactly one round dot of smoky taupe-brown gel #6b5347 on the nail, placed
slightly off-centre toward the base of the nail, still holding its round shape with a
clean edge, not spread at all.

Preserve: the finger, almond nail shape, nude base gel, skin tone and texture, flat light
grey background, lighting direction and quality, the specular highlight on the nail,
top-down camera angle, framing and aspect ratio — exactly as in the original.

Important Details: leave a clean empty band across the lower part of the frame for a
caption to be added later in editing.

Constraints: exactly one dot, no marbling or spreading yet, no brush, no bottle, no other
colors on the nail, no change to crop or camera angle, no text, no logo, no watermark.
```

---

## A-02 — 4 ảnh crop (không gen, chỉ cắt)

**Ref:** `_products/kolor-blooming-gel/reference-images/blooming-gel_official-03.jpg`
Cắt 4 ô thành 4 file dọc 9:16, lấy móng làm tâm. Không gen lại, không retouch hoạ tiết.

| Ô | Hoạ tiết | Lưu |
|---|---|---|
| trên-trái | Hoa hồng đậm | `KOLOR-2026-10-BLOOM_A-02_pattern-01_v1.png` |
| dưới-trái | Croc đỏ | `KOLOR-2026-10-BLOOM_A-02_pattern-02_v1.png` |
| trên-phải | Da báo nâu | `KOLOR-2026-10-BLOOM_A-02_pattern-03_v1.png` |
| dưới-phải | Ombre hồng | `KOLOR-2026-10-BLOOM_A-02_pattern-04_v1.png` |

---

# Vòng sửa v2 — làm giọt/chấm trông như gel lỏng (B-01, B-03)

Lý do: ở v1 giọt và chấm đọc như vật thể rắn (hạt cườm) — mép quá đều, highlight tròn gọn.
Đây là khung đầu của clip mà hành động chính là loang màu, nên cần nó đọc như chất lỏng.
Edit từ chính ảnh **v1**, không phải từ A-04.

---

## B-01 v2 / S01

**Ref:** `outputs/images/KOLOR-2026-10-BLOOM_B-01_S01-dot_v1.png`
**Lưu:** `KOLOR-2026-10-BLOOM_B-01_S01-dot_v2.png`

```
Edit the attached image.

Change: make the red drop read as wet liquid gel instead of a solid bead. Flatten it
slightly so it sits lower on the nail, soften the outer edge where it meets the nail
surface into a very thin glossy meniscus with a faint darker rim, and stretch the
highlight into a soft elongated glint that follows the curve of the nail. The drop still
holds together as one single round pool and has not spread into a pattern.

Preserve: the drop's colour, size and position, the finger, nail shape, skin tone and
texture, background tone, lighting direction, the long specular highlight on the nail,
framing, camera angle and aspect ratio — exactly as in the original.

Constraints: still exactly one drop, no blooming or feathering into the base yet, no
brush, no bottle, no extra colors, no change to crop or camera angle, no text, no
watermark.
```

---

## B-03 v2 / S03

**Ref:** `outputs/images/KOLOR-2026-10-BLOOM_B-03_S03-marble_v1.png`
**Lưu:** `KOLOR-2026-10-BLOOM_B-03_S03-marble_v2.png`

```
Edit the attached image.

Change: make the brown dot read as wet liquid gel instead of a solid bead. Flatten it
slightly so it sits lower on the nail, soften the outer edge where it meets the nail
surface into a very thin glossy meniscus with a faint darker rim, and stretch the
highlight into a soft elongated glint that follows the curve of the nail. The dot still
holds together as one single round pool and has not spread into a marble pattern.

Preserve: the dot's colour, size and position, the finger, nail shape, skin tone and
texture, background tone, lighting direction, the long specular highlight on the nail,
top-down camera angle, framing and aspect ratio — exactly as in the original.

Constraints: still exactly one dot, no marbling or spreading yet, no brush, no bottle,
no extra colors, no change to crop or camera angle, no text, no watermark.
```

---

# Lượt 4C — prompt video (Veo 3.1)

Tool: **Veo 3.1 · image-to-video · 9:16 · 1080p**. Mỗi cảnh 1 clip riêng.
Lưu tất cả vào: `campaigns/2026-10_kolor-blooming-gel/outputs/videos/`
Audio: để trống theo mặc định project — VO, nhạc, SFX đều thêm lúc dựng.

> Nếu vòng sửa v2 của B-01/B-03 ra ổn thì dùng **v2** làm first frame thay cho v1.

---

## S01 — giọt rơi → nở thành hoa · render 6s · dùng 6.0s

**First frame:** `outputs/images/KOLOR-2026-10-BLOOM_B-01_S01-dot_v2.png` (chưa có thì dùng `_v1.png`)
**Lưu:** `KOLOR-2026-10-BLOOM_S01_dot-to-bloom_v1.mp4`

```
Maintain the subject from the first frame. Extreme macro, 100mm, one continuous slow
push-in that tightens through the whole shot so the nail fills noticeably more of the
frame by the end.

The red drop settles, its edge releasing into the clear gel. Pigment creeps outward in
soft feathered tendrils, opening into a loose organic watercolor bloom with petal-like
lobes and a denser core. The spread slows and stabilises in the last second. The long
specular highlight on the nail stays unbroken and slides slightly as the camera moves.
Light stays soft and diffused from above frame-left, neutral cool, no change in colour
temperature.

Ends with the bloom fully open and still, holding steady for the final half second.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 6 seconds.
```

**Tránh:** giọt lăn như viên bi · màu nở rồi co lại · nở đối xứng như bông hoa đồ hoạ · thêm giọt thứ hai · đổi góc máy · ngón tay cử động.

---

## S02 — cọ quét 1 lớp → rút ra → chấm màu rơi · render 6s · dùng 5.0s

**First frame:** `outputs/images/KOLOR-2026-10-BLOOM_B-02_S02-brush_v1.png`
**Lưu:** `KOLOR-2026-10-BLOOM_S02_brush-coat_v1.mp4`

```
Maintain the subject from the first frame. Macro, 100mm, static camera on the angled
view; only the brush and the gel move.

The black brush lowers onto the nail and draws one single even stroke of clear gel from
left to right, the wet film catching the light as it lays down. The brush lifts cleanly
and travels out of frame to the right. The nail is left with a smooth clear wet coat. A
moment later one single drop of deep rose-red gel falls from above into the centre of the
wet surface and beads up there, holding its shape without spreading.

Light stays soft and diffused from above frame-left, neutral cool. Do not alter the
brush colour, shape or finish.

Ends with the brush fully out of frame and the red drop resting on the clear coat, still.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 6 seconds.
```

**Tránh:** bàn tay hoặc ngón tay cầm cọ xuất hiện · đèn UV/LED lọt khung · cọ quét nhiều nhát · gel trên cọ bị ngả màu · giọt đỏ loang ngay · cọ chạm móng rồi quay lại.

---

## S03 — chấm nâu loang thành marble · render 4s · dùng 3.0s

**First frame:** `outputs/images/KOLOR-2026-10-BLOOM_B-03_S03-marble_v2.png` (chưa có thì dùng `_v1.png`)
**Lưu:** `KOLOR-2026-10-BLOOM_S03_marble-spread_v1.mp4`

```
Maintain the subject from the first frame. Extreme macro, 100mm, static top-down camera,
very slight push-in only.

The brown dot releases into the clear gel and drifts outward in smoky uneven veins,
thinning as it travels, leaving darker threads where the pigment pools and pale gaps
where it does not. The movement is slow and liquid, real time, never sped up. It settles
into a soft marbled pattern across the nail.

Light stays soft and diffused from above frame-left, neutral cool, unchanged. The
specular highlight on the nail stays unbroken.

Ends with the marble pattern settled and motionless, holding for the final half second.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Duration: 4 seconds.
```

**Tránh:** loang đều như gradient · loang rồi mất màu · thêm chấm thứ hai · đổi sang màu đỏ của S01 · cọ hoặc chai lọt khung · tua nhanh.
