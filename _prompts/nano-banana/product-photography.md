# Nano Banana Pro Prompt Library — Product Photography & Lifestyle Stills

> **Thư viện ý tưởng / tham khảo — không phải deliverable.** Output chuẩn ở `/assets` lượt 4A là thẻ `_prompts/nano-banana/image-prompt-card.md`: lấy ý tưởng ở đây rồi viết vào thẻ. Gen theo `_skills/image/SKILL.md` → Gen GPT Image. Nếu file này mâu thuẫn với thẻ → theo thẻ.

> **Khi dùng:** Tạo product images cho static ads, carousel, thumbnail, hoặc input image cho Veo 3 pipeline.  
> **Độ phân giải:** là cấu hình trên thẻ (mặc định 2K), không viết vào prompt. Commercial use OK.

---

## Base Template — Product Hero Shot

```
[UPLOAD: ảnh product thật — bất kỳ góc nào, kể cả ảnh điện thoại]

Studio product photography of [PRODUCT DESCRIPTION: e.g., a 30ml amber glass dropper bottle labeled "Glow Serum"].

Surface: [e.g., White marble with subtle veining]
Background: [e.g., Pure white, very slightly gradient — brighter at product, darker at edges]
Lighting: [e.g., Soft diffused light from upper-left. Single light source. Clean shadow under product.]
Angle: [e.g., 45-degree front-right angle, slightly above product eye-level]
Depth of field: [e.g., Product fully sharp. Background sharp.]
Product label: Fully legible, no distortion.
Product color: Maintain exactly as reference — do NOT alter.

Ultra sharp.
Commercial product photography quality.
No props, no hands.
```

---

## Variation 1 — Lifestyle In-Context Shot

```
[UPLOAD: product image]

Lifestyle product photography for a Meta Feed ad (4:5 ratio).

The product is placed [LOCATION: e.g., on a bathroom shelf / wooden bedside table / marble kitchen counter].
[PROPS: e.g., A small ceramic bowl, dried eucalyptus branch, and a folded white towel nearby — natural arrangement, not over-styled.]

Lighting: [e.g., Warm morning light from window to the left — soft shadows]
Color palette: [e.g., Warm neutrals — cream, sage green, warm white]
Mood: [e.g., Calm, minimal, aspirational but accessible — not luxury hotel]
Depth of field: [e.g., Product in focus. Background slightly blurred but context visible.]

Product label: Legible, not obscured.
4:5 ratio crop-ready.
No human visible.
```

> **Best for:** Feed single image ads, carousel first frame, lifestyle context creative.

---

## Variation 2 — In-Use Shot (Hands Only)

```
[UPLOAD: product image]

Close-up lifestyle photo: A woman's hand holding [PRODUCT DESCRIPTION].
Hand: Natural, clean — no nail polish or neutral/nude color. Warm skin tone.
[SETTING: e.g., Held against a bright window with outdoor greenery blurred behind]

Lighting: [e.g., Backlit from window — product silhouetted with warm edge light]
Focus: Sharp on product and hand. Background bokeh.
Grip: Relaxed, natural hold — [e.g., bottle held between thumb and index finger, label facing camera]

Color: Maintain product colors exactly.
4:5 ratio.
Commercial quality.
```

> **Best for:** In-use context without needing full character. Dùng làm input Veo 3 image-to-video tốt.

---

## Variation 3 — Before/After Visual (cho benefit-focused ads)

```
Create a split-composition product image for a Meta ad.

Left side (Before context): [e.g., Dull, slightly dry-looking skin texture — close-up, warm light]
Right side (After context): [e.g., Glowing, hydrated skin with soft light reflection]

Center: [PRODUCT] positioned at the dividing line, label visible.
No text on image (text will be added in Ads Manager).
Clean, medical-free aesthetic — NOT clinical. Warm, aspirational.
1:1 ratio.
```

> **Best for:** Minh hoạ benefit mà không cần claim trực tiếp. Dùng với headline text trong Ads Manager.

---

## Variation 4 — Carousel Multi-Product Flat Lay

```
[UPLOAD: multiple product images — up to 8]

Flat lay product photography for a carousel Meta ad.
All [X] products arranged together in a cohesive composition.
Surface: [e.g., White linen fabric — slight texture visible]
Arrangement: Products at slight angles, overlapping naturally. Not grid-perfect.
Lighting: Overhead diffused — even light, minimal shadows.
Color: Each product color maintained exactly.
Style: [e.g., Minimal, editorial — think Glossier or Aesop product imagery]
1:1 ratio (carousel format).
```

---

## Editing Prompts (sau khi generate xong)

**Đổi background giữ nguyên sản phẩm:**
```
Keep the product exactly as it is. Change only the background to: 
[VD: Outdoor sunlit terrace — blurred green plants, warm afternoon light]
Product lighting: adjust slightly to match new background mood.
```

**Điều chỉnh ánh sáng:**
```
The product looks too flat. Add:
- More defined shadow on the right side (subtle, not harsh)
- Slight highlight on the bottle's shoulder (top curve)
- Warm the overall color temperature by 10%
Product shape and label: do not alter.
```

**Thêm text overlay (nếu cần):**
```
Add the following text to the image:
Headline: "[TEXT]" — [position: bottom third, centered]
Font style: Clean sans-serif, white, all caps
Background: Very subtle dark gradient behind text only — so text is readable
Keep product and all other elements unchanged.
```

---

## Specs xuất file cho Meta Ads

| Format | Ratio | Minimum size | Use |
|--------|-------|-------------|-----|
| Feed single image | 4:5 | 1080×1350px | Primary feed placement |
| Square | 1:1 | 1080×1080px | Feed + Marketplace |
| Story/Reels thumbnail | 9:16 | 1080×1920px | Story static |
| Carousel | 1:1 | 1080×1080px | Multi-product |

---

## Log — Prompts đã test

| Date | Product | Variation | Result | Notes |
|------|---------|-----------|--------|-------|
| | | | | |
