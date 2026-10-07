# Style Descriptor Framework — Nano Banana / GPT Image 2

> **Thư viện ý tưởng / tham khảo — không phải deliverable.** Output chuẩn ở `/assets` lượt 4A là thẻ `_prompts/nano-banana/image-prompt-card.md`: lấy ý tưởng ở đây rồi viết vào thẻ. Gen theo `_skills/image/SKILL.md` → Gen GPT Image. Nếu file này mâu thuẫn với thẻ → theo thẻ.

Last updated: 2026-05-27

> Style Descriptor là đoạn văn 75–110 từ set toàn bộ visual parameters của shoot.
> Không bắt buộc đặt đầu prompt — chủ thể + hành động dẫn đầu, Style Descriptor theo sau.

---

## Format chuẩn

```
[LIGHTING]. [COLOR/GRADE]. [SURFACE AND BACKGROUND]. [CAMERA SPEC]. [MOOD ADJECTIVES].
```

> **CAMERA SPEC:** thông số lens/f-stop chỉ dùng cho GPT Image. Nano Banana: tả bằng lời (shallow depth of field, soft creamy background blur…), không ghi số lens.

Không nhất thiết phải thành 5 câu riêng biệt — viết thành đoạn văn chảy tự nhiên — nhưng 5 yếu tố phải có đủ.

---

## 7 Dimensions để phân tích style từ ảnh reference

### 1. LIGHTING
- **Quality**: Hard (shadow sắc cạnh) hay Soft (shadow mờ, diffused)?
- **Direction**: Front / Side / Back / Overhead / Under
- **Source**: Window natural / Overcast / Studio strobe / Continuous LED / Candle/lamp
- **Shadow**: Deep hay subtle? Hard edge hay feathered? Warm/cool/neutral?
- **Highlight**: Specular highlights crisp hay soft? Blown out hay retained detail?

### 2. COLOR & GRADING
- **Temperature**: Warm (amber/gold) / Cool (blue/cyan) / Neutral
- **Saturation**: Desaturated / Muted / Natural / Pushed vivid
- **Palette**: List 3–6 màu dominant với mô tả cụ thể (không nói "green" — nói "muted sage")
- **Contrast**: High (deep blacks) / Low (lifted blacks / matte finish)
- **Grade style**: Clean digital / Film emulation / Matte-fade / Crushed-moody / Warm editorial / Desaturated editorial / Split-tone

### 3. COMPOSITION & FRAMING
- **Camera angle**: Overhead 90° / High angle / Eye level / Low angle / 45° tabletop
- **Product placement**: Centered dominant / Centered small / Offset / Cropped
- **Negative space**: Generous / Balanced / Tight
- **Depth cues**: Flat (tất cả cùng depth) hay Layered (foreground/midground/background)

### 4. SURFACE, BACKGROUND & ENVIRONMENT
- **Background type**: Seamless / Environmental / Textured flat / Gradient / Solid color
- **Surface material**: Marble (loại nào?) / Concrete / Stone / Wood / Linen / Velvet / Glass / Acrylic
- **Surface finish**: Light/dark? Matte/polished? Có reflect sản phẩm không?
- **Props**: Natural (botanicals, stones) / Lifestyle (cups, towels) / Abstract / None

### 5. DEPTH OF FIELD & FOCUS
- **Depth**: Shallow / Moderate / Deep
- **Bokeh**: Smooth creamy / Slightly textured / None (f-stop như f/1.2–2.0, f/2.8–4.0 chỉ ghi cho GPT Image)
- **Lens character**: Clean modern / Slightly vintage / Cinematic

### 6. TEXTURE, GRAIN & FINISH
- **Film grain**: Absent / Subtle / Moderate / Heavy
- **Overall finish**: Polished / Raw organic / Clinical minimal / Warm tactile

### 7. MOOD & ATMOSPHERE
- **Energy**: Calm/meditative / Bright/energetic / Moody/intimate / Luxurious/restrained / Playful/expressive
- **Time feel**: Morning / Midday / Late afternoon / Evening / Timeless
- **5 adjectives cụ thể**: không dùng "nice" hay "clean" — dùng "austere", "luminous", "earthy", "clinical", "meditative", "decadent", "intimate", "raw"...

---

## Dấu hiệu Style Descriptor TỐT vs. YẾU

| ✅ TỐT | ❌ YẾU |
|---|---|
| "Hard single-source side lighting from camera left" | "beautiful lighting" |
| "Near-black shadows — blacks fully crushed, no lift" | "moody atmosphere" |
| "85mm f/2.8, moderate depth of field" | "nice bokeh" |
| "Raw white oak surface, slightly textured" | "minimalist" |
| "Warm amber specular on reflective surfaces" | "clean look" |
| Dưới 120 từ | Quá dài, loãng |

---

## Thư viện Style Descriptors mẫu

### Dark Studio / Luxury Fragrance
```
Hard single-source side lighting from camera left, creating a defined shadow plane across 60% of the image.
Deep tonal contrast with near-black shadows — blacks are fully crushed, no lift.
Color palette: near-black background, warm amber specular highlights on any reflective surface, minimal midtones.
Matte seamless background with no visible texture.
Shot at 85mm f/2.8, moderate depth of field, full product sharp, background pure black.
Austere, precise, covetable.
```

### Warm Morning Lifestyle / Wellness Brand
```
Soft directional window light from camera right, warm and natural with a gentle golden bias.
Shadows are present but feathered and low-contrast, never deep.
Color grade: lifted blacks (matte finish), warm cream and honey tones dominating, slight fade in highlights.
Surface is raw white oak or light linen, slightly textured.
Background soft and out of focus — warm interior space, no hard details.
Shot at 50mm f/2.0, shallow depth of field, bokeh is smooth and warm.
Intimate, tactile, unhurried.
```

### Flat Overhead / Editorial Beauty
```
Overhead 90° shot, soft diffused studio light from directly above, essentially shadowless.
Color palette is controlled and graphic — one dominant background color (matte surface, no texture),
product and any props rendered with full detail and even exposure.
No depth of field effect — flat lay, all elements in focus from edge to edge.
Color grade is clean and neutral, no film emulation, saturation slightly below natural.
Shot at 50mm f/8 equivalent, crisp, no aberration.
Considered, graphic, controlled.
```

### Raw Concrete / Streetwear Product
```
Hard overhead or 45° light, industrial quality — single-source flash or bare strobe.
Deep, hard-edged shadows.
Color grade: cool, slightly desaturated, grey-blue cast in neutrals, shadows almost black.
Background and surface are rough poured concrete or dark aggregate stone — texture is prominent and celebrated, grain is heavy.
No props. Product rendered sharply with specular highlights clipping white.
Shot at 35mm f/5.6, everything in focus, no bokeh.
Gritty, stark, uncompromising.
```

### Soft Studio / Skincare Hero
```
Large softbox from upper-left, wrapping around the subject with gentle shadow falloff and no hard edges.
Highlights are soft and retained — not blown.
Color grade: cool-neutral, slightly desaturated, clean digital — no film grain, no color cast.
Background is pure white or very pale grey seamless.
Surface is white acrylic or pale marble — slightly reflective, giving a gentle mirror reflection of the product base.
Shot at 100mm macro equivalent, f/4.0, product sharp throughout, background clean and featureless.
Clinical, precise, trustworthy.
```

---

## Cách tạo Style Descriptor mới từ ảnh reference

1. Phân tích ảnh qua 7 dimensions trên
2. Viết notes ngắn cho từng dimension
3. Tổng hợp thành 1 đoạn văn 75–110 từ theo format: LIGHTING → COLOR → SURFACE → CAMERA → MOOD
4. Test bằng cách đọc lại: nếu vẫn còn từ mơ hồ (nice, clean, beautiful) → thay thế bằng mô tả kỹ thuật cụ thể

---

## Lưu ý khi dùng

- Style Descriptor không nhắc đến sản phẩm — chỉ describe môi trường và ánh sáng
- 1 Style Descriptor dùng cho tất cả shots trong cùng 1 shoot
- Nếu muốn thay đổi vibe giữa các shots → tạo Style Descriptor riêng, không chỉnh sửa từng prompt
