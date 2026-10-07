# Nano Banana Pro Prompt Library — Lifestyle Still (No Product Focus)

> **Thư viện ý tưởng / tham khảo — không phải deliverable.** Output chuẩn ở `/assets` lượt 4A là thẻ `_prompts/nano-banana/image-prompt-card.md`: lấy ý tưởng ở đây rồi viết vào thẻ. Gen theo `_skills/image/SKILL.md` → Gen GPT Image. Nếu file này mâu thuẫn với thẻ → theo thẻ.

> **Khi dùng:** Tạo ảnh lifestyle cho brand context — không phải product shot thuần. Người dùng sản phẩm, environment shots, mood imagery.  
> **Best for:** First frame của video, carousel slide 2–4, brand awareness static.

---

## Variation 1 — Person Using Product (no face)

```
[UPLOAD: product image]

Lifestyle photography for a Meta Feed ad.
A woman's hands and forearms visible — [ETHNICITY, e.g., warm olive skin tone].
She is [ACTION: e.g., applying the serum to her cheek — fingertips gently pressing in].
Product is nearby or in one hand — label visible.

Setting: [e.g., Bathroom counter, morning light]
Clothing visible (forearm only): [e.g., White cotton robe sleeve]
Composition: [e.g., Close-up — hands and product fill frame, slight blur at edges]
Lighting: [e.g., Soft natural light from left — warm morning tone]

4:5 ratio, photorealistic, editorial quality.
Do not show face.
Product: maintain exact appearance from reference.
```

---

## Variation 2 — Aspirational Environment (no person, no product)

```
Create a lifestyle still image that establishes the brand aesthetic.

Scene: [e.g., A beautifully styled bathroom shelf]
Elements: [e.g., Small white ceramic containers, dried eucalyptus, 
  folded linen towels in cream and sage, soft morning light]
No product visible (this will be used as background reference only).

Mood: [e.g., Calm, minimal, curated without being sterile]
Lighting: [e.g., Soft window light from left, warm shadows]
Color palette: [e.g., White, cream, sage, warm wood tones]
4:5 ratio, photorealistic.
```

> **Use case:** Tạo background reference cho Nano Banana product shots sau đó.

---

## Variation 3 — Before/After Context Shot (chỉ cho static, không bao giờ làm khung video)

```
Create a two-image diptych (side by side, 1:1 ratio each, combined into 2:1):

LEFT IMAGE — "Before" context:
[e.g., Close-up of skin texture — slightly dull, dry patches visible, 
  no makeup. Warm neutral lighting. Realistic, not clinical.]

RIGHT IMAGE — "After" context:  
[e.g., Same angle, same lighting — skin glowing, hydrated appearance, 
  slight natural luminosity. Healthy, not airbrushed.]

No text overlay. No product visible.
Consistent lighting and color temperature across both.
Realistic and relatable — not medical illustration style.
```

> **Use case:** Visual proof of concept without making a direct claim. Text added in Ads Manager.

---

## Variation 4 — Gifting / Occasion Context

```
[UPLOAD: product image]

Lifestyle photo: [PRODUCT] presented as a gift.

Styling: Product placed inside a clean white gift box with tissue paper.
A simple kraft tag reads "[SHORT MESSAGE: e.g., 'For you']".
Surrounding: [e.g., Dried flowers, ribbon, soft linen background]
Lighting: [e.g., Soft overhead, slightly warm — gift/celebration mood]
Composition: Product gift box centered, slight angle. Clean.

4:5 ratio. No text overlay. No hands.
Product label visible through open box lid.
```

> **Use case:** Holiday, Mother's Day, gifting campaign.

---

## Editing Prompts (post-generation)

**Maintain consistency across campaign:**
```
This image is part of a [X]-image campaign set. 
The reference images are [UPLOAD previous images].
Match: color temperature, lighting direction, background mood.
Only change: [the specific element you want different]
```

**Adjust for different ratio:**
```
Recompose this image for [1:1 / 9:16] ratio.
Priority: Keep [product / hands / face] in frame.
Extend [left/right/top/bottom] background to fill new ratio.
Match existing lighting and color in extended area.
```
