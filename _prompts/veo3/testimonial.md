# Veo 3 Prompt Library — Testimonial Ad

> ⛔ **Không dùng cho người nói — testimonial → `_workflows/ugc-workflow.md` (TopView). Chỉ tham khảo ý tưởng hình.**
> Các dòng thoại / "native dialogue audio" / thời lượng 12–30s bên dưới là di sản cũ, **không áp dụng**. Lời thoại tham khảo cho script UGC (`/script`); bối cảnh/ánh sáng/khung hình tham khảo cho ảnh avatar (thẻ `_prompts/nano-banana/image-prompt-card.md`). Clip Veo không người nói → thẻ `_prompts/veo3/video-prompt-card.md`.

> **Khi dùng:** Muốn tạo video người (nhân vật AI) nói trực tiếp vào camera về sản phẩm.  
> **Best for:** Cold audience testimonial, UGC-style ad, social proof creative.

---

## Base Template

> Chỉ tham khảo ý tưởng hình — không paste vào Veo.

```
[CHARACTER DESCRIPTION — paste từ character profile.md]

She is [SETTING: e.g., sitting on a couch in her living room / standing in her bathroom].
[LIGHTING: e.g., Soft natural light from the left, warm afternoon tone.]
[FRAMING: e.g., Medium close-up, slight eye-level angle. Handheld feel — very slight camera movement.]
Background: [VD: Blurred neutral living room — linen couch, indoor plants, warm beige tones.]

She speaks directly to camera, natural and conversational — NOT scripted-sounding.

She says:
"[DIALOGUE — paste từ script file hoặc viết trực tiếp]"

[SECONDARY ACTION — optional: e.g., She picks up the product bottle and shows it to camera briefly, then sets it down.]

[KHÔNG ÁP DỤNG — thoại/giọng do TopView tạo trong take UGC, không dùng Veo dialogue]

Format: [9:16 / 4:5 / 1:1]
Duration: [không áp dụng]
```

---

## Variation 1 — Morning Routine Hook

```
A woman in her early-to-mid 30s with dark brown wavy hair, light olive skin, 
minimal makeup, casual clothing. Warm, relatable appearance — not a model.

She is standing at her bathroom counter, morning light from a window to her left.
Medium close-up, slight handheld feel. Background: slightly blurred white 
bathroom — a few products visible on the shelf but not cluttered.

She speaks directly to camera, conversational and genuine:

"Okay so I've been doing this every morning for about three weeks now. 
I put two drops of this on before my moisturizer — that's it. 
And honestly? My skin just looks different. 
Like I'm not explaining it to people anymore, they're just... noticing."

She holds up a [PRODUCT DESCRIPTION] briefly while saying the last line, 
then smiles naturally and looks slightly off-camera.

[KHÔNG ÁP DỤNG — thoại/giọng do TopView tạo trong take UGC, không dùng Veo dialogue]

Format: 9:16 | Duration: [không áp dụng]
```

> **Best for:** Cold audience, skincare/beauty, problem-aware customers. Hook ở 3 giây đầu là "morning routine" micro moment.

---

## Variation 2 — Skeptic-to-Believer

```
A woman in her late 30s, warm brown skin, natural curly hair pulled back loosely,
no makeup or very minimal. Relaxed, real-person energy.

She is sitting on a couch in her living room, soft afternoon light.
Medium shot, eye level. Background: blurred neutral tones, bookshelf visible.

She speaks directly to camera, slightly leaning forward:

"I'll be honest — I almost didn't try this because I've been burned before. 
Like, spent a lot of money on things that did absolutely nothing for my skin.
[Pause, slight laugh] 
This was different though. And I genuinely don't say that."

She picks up [PRODUCT] from the side table, shows it briefly.

"[KEY BENEFIT CLAIM — from product brief approved list]"

"There's a money-back guarantee so I figured — why not. 
Just glad I did."

[KHÔNG ÁP DỤNG — thoại/giọng do TopView tạo trong take UGC, không dùng Veo dialogue]

Format: 9:16 | Duration: [không áp dụng]
```

> **Best for:** Warm audience, retargeting, overcoming "I've tried everything" objection.

---

## Variation 3 — Result Reveal (ngắn, punchier)

```
A woman in her early 30s, [ETHNICITY], [HAIR], casual outfit.
Close-up — face filling most of frame. Bright, natural lighting.
Handheld, intimate feel.

She looks at camera with a small smile:

"Three weeks ago my skin looked tired. I don't know how else to describe it.
[beat]
Now people are asking me what I changed."
[She tilts her head slightly, genuine]
"It's just this."
[Holds up product — 1 second]

[KHÔNG ÁP DỤNG — thoại/giọng do TopView tạo trong take UGC, không dùng Veo dialogue]
Format: 9:16 | Duration: [không áp dụng]
```

> **Best for:** Retargeting, upper funnel interest, thumb-stopping hook. Clip ngắn cho Stories/Reels.

---

## Tips khi dùng Testimonial prompts

- **Dialogue length (khi viết script UGC):** TopView ≈ 3.5 từ/giây, mỗi take < 40 từ — xem `_workflows/ugc-workflow.md`
- **Nếu lip sync lệch (take TopView):** tách take ngắn hơn
- **Consistent character:** Luôn dùng cùng character description block cho cùng 1 nhân vật xuyên campaign
- **Sau khi generate:** Kiểm tra ở 1.5x speed — lip sync phải khớp ở mọi tốc độ
- **Lưu prompt đã dùng** vào `campaigns/[tên]/prompts-used/` và ghi note kết quả

---

## Log — Prompts đã test

| Date | Variation | Result | Notes |
|------|-----------|--------|-------|
| | | | |
