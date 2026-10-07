# Shot Variation Strategies — Nano Banana / GPT Image 2

> **Thư viện ý tưởng / tham khảo — không phải deliverable.** Output chuẩn ở `/assets` lượt 4A là thẻ `_prompts/nano-banana/image-prompt-card.md`: lấy ý tưởng ở đây rồi viết vào thẻ. Gen theo `_skills/image/SKILL.md` → Gen GPT Image. Nếu file này mâu thuẫn với thẻ → theo thẻ.

Last updated: 2026-05-27

> Khi gen N shots của cùng 1 sản phẩm với cùng 1 style, dùng các chiến lược bên dưới
> để đảm bảo mỗi ảnh khác biệt — tránh N ảnh trông giống nhau.

---

## 1. ANGLE VARIATIONS

| Angle | Mô tả | Dùng khi |
|---|---|---|
| Overhead 90° | Nhìn thẳng từ trên xuống, không perspective | Flatlay, skincare, beauty |
| 45° tabletop | Classic product angle, ~45° phía trên eye level | Mọi sản phẩm — safe default |
| Eye-level / straight-on | Camera ngang tầm sản phẩm | Packaging-forward, fragrance |
| Low angle looking up | Camera dưới sản phẩm, nhìn lên | Hero shots, dramatic |
| Three-quarter angle | Thấy cả depth và form | Bottles, jars, boxes |
| Extreme close-up / partial crop | Abstract, chỉ thấy 1 phần | Texture shots, label detail |

---

## 2. COMPOSITION VARIATIONS

| Composition | Mô tả |
|---|---|
| Product centered, generous negative space | Premium, breathing room |
| Product offset left or right | Rule of thirds — dynamic |
| Multiple units (2–3 sản phẩm cùng loại) | Arranged in a group — range feel |
| Product + minimal prop | 1 botanical / ingredient / object liên quan đến use context |
| Product partially out of frame | Chỉ thấy 70% — creates scale and energy |
| Product with cap/lid off or open | Shows interior, signals use |

---

## 3. SURFACE AND STAGING VARIATIONS

- Thay đổi surface material trong cùng style (vd: pale marble vs. dark marble nếu style cho phép)
- Thêm water drop / light mist trên sản phẩm → cho skincare/beauty
- Thêm hero ingredient (hemp leaf, coffee grounds, raw cocoa) làm single prop gần sản phẩm
- **In-context**: sản phẩm trên bathroom shelf / bên ly nước / trên folded towel
- **Pure isolation**: sản phẩm không có prop, tập trung vào packaging

---

## 4. LIGHTING MICRO-VARIATIONS

Giữ nguyên Style Descriptor nhưng adjust nhỏ trong shot description:

| Variation | Cách viết trong prompt |
|---|---|
| Tăng shadow depth | "deeper shadow plane, near-black on shadow side" |
| Thêm rim light | "thin rim light catching the right edge of the bottle" |
| Shift light direction | "light source shifted to directly overhead rather than side" |
| Mist/wet surface | "surface lightly misted, product has a few water droplets" |

---

## 5. SHOT NAMING CONVENTION (slugs)

Đặt tên shot theo format: `[angle]-[surface]-[context]`

Ví dụ:
- `overhead-marble-isolation`
- `45-degree-warm-window`
- `flatlay-with-botanical`
- `closeup-label-detail`
- `lifestyle-bathroom-shelf`
- `hero-dark-studio`
- `three-quarter-concrete`

---

## Checklist trước khi gen

- [ ] Mỗi shot có Style Descriptor (copy nguyên từ style-descriptor-framework.md)
- [ ] Mỗi shot có product description cụ thể (shape, color, label, material)
- [ ] Mỗi shot có shot-type template phù hợp (từ shot-type-templates.md)
- [ ] Fidelity anchor ở cuối mỗi prompt
- [ ] Lỗi cần QC theo category (đưa vào mục AVOID của thẻ, không dán vào prompt)
- [ ] Shot names khác nhau, không trùng
- [ ] Ít nhất 2–3 trong 4 variation dimensions được dùng để tạo sự khác biệt
