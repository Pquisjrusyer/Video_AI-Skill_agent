# Shot Type Templates — Nano Banana / GPT Image 2

> **Thư viện ý tưởng / tham khảo — không phải deliverable.** Output chuẩn ở `/assets` lượt 4A là thẻ `_prompts/nano-banana/image-prompt-card.md`: lấy ý tưởng ở đây rồi viết vào thẻ. Gen theo `_skills/image/SKILL.md` → Gen GPT Image. Nếu file này mâu thuẫn với thẻ → theo thẻ.

Last updated: 2026-05-27

> Mỗi shot prompt = **Style Descriptor** + **Product description** + **Shot-type template** + **Fidelity anchor**
> Luôn kết thúc bằng fidelity anchor: "Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design."

---

## Cấu trúc chung

```
[Style Descriptor]   ← Nano Banana: mở đầu bằng chủ thể + hành động, Style Descriptor có thể đứng sau
[Product description — shape, color, label, material, finish, distinctive details]
[Shot-type template bên dưới]
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

---

## 1. ON-MODEL SHOT
> Best for: Fashion, jewelry, accessories, wearables — sản phẩm được mặc hoặc cầm bởi người

```
A [age] [ethnicity] [gender] model wearing/holding/using [product description],
photographed [angle — from behind / three-quarter / front-facing / etc.].
[Pose direction — standing contemplatively / walking / sitting / looking away from camera / etc.]
[Environment context from style descriptor].
The [product key visual element] is sharp and the focal point of the image.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

**Ví dụ điền:**
```
A 28-year-old Asian woman wearing a white linen oversized shirt,
photographed from three-quarter angle, looking slightly away from camera.
Standing in a minimalist studio with warm window light from the right.
The embroidery detail on the left chest pocket is sharp and the focal point of the image.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

---

## 2. FLATLAY SHOT
> Best for: Skincare, beauty, small products, food ingredients — góc nhìn 90° từ trên xuống

```
Overhead 90° flat lay photograph. [Product description] placed [position — centered /
offset to right / arranged in a diagonal line / etc.] on [surface from style descriptor].
[Props nếu có — kept minimal, 1–3 items that relate to the product's ingredients/use/story].
All elements in focus from edge to edge. [Any text on packaging] must be legible.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

**Ví dụ điền:**
```
Overhead 90° flat lay photograph. A 50ml amber glass serum bottle with gold dropper cap
placed centered on white Calacatta marble surface.
Minimal props: three small dried chamomile flowers arranged loosely to the bottom-left.
All elements in focus from edge to edge. The label text "RESTORE SERUM" must be legible.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

---

## 3. LIFESTYLE SCENE SHOT
> Best for: Home, F&B, wellness, candles, bất kỳ sản phẩm nào — sản phẩm trong môi trường tự nhiên

```
[Product description] placed in [environment — modern kitchen counter / bathroom marble shelf /
bedside table / art gallery space / café table / etc.].
[Environmental details — morning light through window / steam from coffee / blurred background
elements that create context].
Product is the clear subject but feels natural in the environment, not staged.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

**Ví dụ điền:**
```
A matte black ceramic candle jar with cream label placed on a raw oak bedside table.
Morning light streaming through a sheer curtain to the left, casting a soft shadow.
Blurred background shows white linen pillows and a small stack of books.
Product is the clear subject but feels natural in the environment, not staged.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

---

## 4. HERO / PRODUCT-ONLY SHOT
> Best for: Electronics, packaging-forward products, supplements — sản phẩm là toàn bộ chủ đề

```
[Product description] [orientation — standing upright / angled 15° toward camera / cap removed
showing contents / etc.].
[Surface detail from style descriptor]. No props — product is the sole subject.
[Lighting drama — dramatic side light / rim light on edge / gradient backdrop / etc.].
Every detail of packaging and label is crisp and readable.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

**Ví dụ điền:**
```
A white supplement bottle with minimalist black label standing upright, angled 15° toward camera.
Pure white seamless background. No props — product is the sole subject.
Hard single-source side light from camera left creating a defined shadow plane.
Every detail of packaging and label is crisp and readable.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

---

## 5. IN-USE / ACTION SHOT
> Best for: F&B (food plated), skincare (texture swatch), fashion (movement shot) — sản phẩm đang được dùng

```
[Product description] being [action — applied to skin showing texture / poured into glass /
plated as finished dish / worn while walking through city / etc.].
[Context that shows the product's function or experience].
Motion or action feels natural, not frozen or posed.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

**Ví dụ điền:**
```
A 30ml face oil bottle with a few drops being dispensed onto fingertips, showing the golden oil texture.
Close-up showing the product against clean skin, warm studio light highlighting the oil's luminosity.
Motion or action feels natural, not frozen or posed.
Use the attached product image as reference — do not alter product colors, label text, typography, or packaging design.
```

---

## Lỗi cần QC theo category (đưa vào mục AVOID của thẻ, không dán vào prompt)

Dùng base + category-specific làm checklist QC; trong prompt viết bằng positive framing:

**Base:** `blurry, wrong colors, altered design, text errors, distorted shape, unrealistic, cartoon style, overly saturated`

| Category | Thêm vào |
|---|---|
| Fashion/Apparel | `wrong fabric texture, missing embroidery detail, wrong garment shape, floating fabric` |
| Skincare/Beauty | `wrong bottle shape, illegible label, wrong cap color, unrealistic liquid, wrong transparency` |
| F&B/Food | `unappetizing, wrong food color, plastic-looking food, unrealistic packaging` |
| Home/Lifestyle | `wrong proportions, unrealistic materials, toy-like scale` |
| Electronics | `wrong ports, wrong screen content, unrealistic reflections` |
| Jewelry | `wrong metal color, missing gemstone detail, unrealistic sparkle` |

---

## Cấu hình

Tool / độ phân giải / tỷ lệ / ảnh ref ghi ở dòng "Tool + cấu hình" và mục REFERENCE IMAGE ROLES của thẻ (`image-prompt-card.md`) — không đưa vào prompt.

