# Veo 3 Prompt Library — Product Demo & Lifestyle

> **Thư viện ý tưởng / tham khảo — không phải deliverable.** Output chuẩn ở `/assets` lượt 4C là thẻ `_prompts/veo3/video-prompt-card.md` (Veo 3.1 image-to-video từ first frame đã duyệt ở 4B, render 4/6/8s; độ dài render ≠ độ dài dùng). Người dùng tự render. Nếu file này mâu thuẫn với thẻ → theo thẻ.
>
> Mọi prompt dưới đây là **image-to-video từ first frame đã duyệt**: phần mô tả bối cảnh/đạo cụ dùng để viết prompt ảnh first frame (4A); trong prompt video chỉ giữ chuyển động + camera và mở bằng "Maintain the subject and scene from the first frame." 1 scene = 1 clip, tối đa 8s.

> **Khi dùng:** Tạo video cảnh dùng sản phẩm, không cần talking head. Dùng image từ Nano Banana Pro làm starting frame khi có thể.  
> **Best for:** Product showcase, how-to, lifestyle feel, B-roll.

---

## Base Template — Image-to-Video (recommended)

> **Workflow chuẩn:** Tạo still image từ Nano Banana Pro trước → dùng làm input cho Veo 3 → animate.

```
[UPLOAD: product image từ Nano Banana Pro]

Starting from this exact product image, animate the following motion:
[MOTION DESCRIPTION: e.g., 
- Slow close-up zoom in on the product label (2s)
- Camera pulls back to reveal product in context (3s)
- [SECONDARY ELEMENT: e.g., a hand enters frame from left, picks up the bottle] (3s)
]

Lighting: Match the lighting from the reference image — [e.g., warm, soft, left-side natural light]
Motion feel: [e.g., Slow, deliberate — editorial pace. No shake.]
Color: Maintain exact product colors from reference image. Do NOT alter product appearance.

Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Format: [4:5 | 1:1 | 9:16]
Duration: [4s / 6s / 8s]
```

---

## Variation 1 — Application Demo (hands only, no face)

```
Extreme close-up of clean, manicured hands (natural nails, no polish) 
holding a [PRODUCT DESCRIPTION: e.g., 30ml amber glass dropper bottle].
Warm bathroom counter — white marble surface, soft morning light from left.

Motion sequence:
1. (0–2s) Hands hold bottle, tip upside down — 2 drops fall onto fingertips
2. (2–5s) Fingertips press gently into skin (forearm or décolleté visible) — slow circular motion
3. (5–8s) Camera slowly pulls back — product bottle back in frame, sitting on marble, label sharp and legible

No face shown. Hands appear natural and relatable — not overly styled.
Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Format: 4:5 | Duration: 8s
```

> **Best for:** Skincare, supplement liquid, any product where application is a key selling point.

---

## Variation 2 — Lifestyle Scene (product in context)

```
A [SETTING: e.g., sun-drenched kitchen counter, late morning light].
[PRODUCT] sits on the counter next to [CONTEXTUAL PROPS: e.g., a ceramic mug, 
a small plant, folded linen napkin]. Everything styled naturally — lived-in, 
not overly art-directed.

A woman's hand (no face) enters from the right, picks up the product, 
examines it briefly, then sets it back down gently.

Camera: Slight push-in during hand movement. Final frame: product in focus, 
background soft bokeh.

Color palette: Warm neutrals — cream, beige, sage green.
Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Format: 4:5 | Duration: 6s
```

> **Best for:** Cold audience lifestyle ad. Sets aspirational context without direct selling.

---

## Variation 3 — Unboxing / First Impression (no face)

```
A clean white table. A [BRAND]-branded shipping box sits in center frame.
Hands enter and open the box, remove tissue paper, reveal the product inside.
Product is lifted out, turned to show front label (hold 2s — label legible).

Lighting: Bright overhead diffused light — clean, product photography feel.
Motion: Calm, deliberate. Not rushed. Focus on product reveal.
Audio: No dialogue, no music, no sound effects; quiet natural ambience only.
Format: 1:1 | Duration: 8s
```

> **Best for:** New product launch, retargeting warm traffic who've seen brand before.

---

## Tips khi làm Product Demo

- **Luôn bắt đầu từ Nano Banana Pro image** cho Image-to-Video — Veo 3 giữ product visual tốt hơn khi có reference
- **Veo 3 không ổn với pure product animation từ text** — nếu sản phẩm quan trọng, đừng để Veo tự tưởng tượng
- **Label text:** Nếu Veo hallucinate text trên label → sửa first frame ở 4B (label đúng, rõ) rồi render lại, hoặc cắt bỏ đoạn lỗi khi dựng ở /edit
- **Hand casting trong prompt:** "Natural manicured hands, natural nails" cho feel thật hơn "perfectly styled hands"

---

## Log — Prompts đã test

| Date | Variation | Result | Notes |
|------|-----------|--------|-------|
| | | | |
