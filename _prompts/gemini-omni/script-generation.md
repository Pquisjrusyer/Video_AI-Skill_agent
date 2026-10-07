# Gemini Omni Prompt Library — Script Generation

> **Thư viện tham khảo — không phải deliverable.** Ở `/script`, Claude dùng các block dưới đây làm **khung để tự viết script** (không cần mở Gemini). Output → `campaigns/[campaign]/scripts/script.md` (theo `_prompts/templates/script-template.md`), dừng cổng B → UGC: chia thành thẻ take TopView; Voiceover: VO gen qua ElevenLabs ở `/assets` 4D.
> **Word budget:** VO/ElevenLabs ≈ 2.4 từ/giây (30s ≈ 70 từ). UGC/Google Flow ≤ 20 từ/take (8s). UGC/TopView ≈ 3.5 từ/giây, mỗi take < 40 từ.

---

## Master Script Prompt (UGC ngôi thứ nhất)

> Khung để Claude tự viết script UGC. Thay `[BRACKET]` trước khi dùng.

```
You are writing a video ad script for a DTC ecommerce brand on Meta Ads 
(Facebook + Instagram). The script will be delivered by an AI-generated 
character in a UGC-style video.

BRAND CONTEXT:
- Brand: [Tên brand]
- Product: [Tên sản phẩm + 1 câu mô tả]
- Target customer: [Paste từ target-audience.md — demographics + pain point chính]
- Tone: [Paste từ brand-brief.md — tone of voice]

APPROVED CLAIMS ONLY:
[Paste danh sách approved claims từ product-brief.md]

CHARACTER:
[Paste character name + backstory ngắn từ profile.md]

AD SPECIFICATIONS:
- Format: [Testimonial / Product demo + voiceover / Problem-solution]
- Duration: [15s / 20s / 30s] — split into takes: Google Flow ≤ 20 words per take (8s clip) · TopView ≈ 3.5 words/second, < 40 words per take
- Audience stage: [Cold / Warm / Retargeting]
- Key message to convey: [1 điều duy nhất muốn viewer nhớ]

SCRIPT STRUCTURE (follow this exactly):
- Hook (0–3s): Stop the scroll. Problem or curiosity-based. NO brand name.
- Body (3–[X]s): Problem → discovery → product benefit. Use customer language.
- Close ([X]–end): Result + CTA. Soft, not pushy.

OUTPUT FORMAT:
Provide:
1. Script with [SECOND MARKERS] at each transition
2. On-screen text suggestions (if any)
3. Director's note: 1–2 sentences on delivery style for this specific script
4. 3 alternative hook options

CONSTRAINTS:
- Write in first person, conversational English
- No corporate language ("innovative", "revolutionary", "game-changing")
- Max 2 sentences before first pause
- Hook must be completable in 3 seconds at natural speaking pace (~7 words max for first line)
- Do NOT start with brand name or product name
```

---

## Voiceover Script Prompt (ngôi thứ 3 — dùng cho `_workflows/voiceover-video-workflow.md`)

> Master Script Prompt ở trên là cho UGC ngôi thứ nhất. Video VO dẫn dắt dùng block này.

```
You are writing a third-person voiceover script for a DTC ecommerce video ad
on Meta Ads (Facebook + Instagram). No on-camera speaker — the narrator is
heard, not seen. Visuals are b-roll, product shots, and graphics.

BRAND CONTEXT:
- Brand: [Tên brand]
- Product: [Tên sản phẩm + 1 câu mô tả]
- Target customer: [Paste từ target-audience.md]
- Tone: [Paste từ brand-brief.md — tone of voice]

APPROVED CLAIMS ONLY:
[Paste danh sách approved claims từ product-brief.md]

AD SPECIFICATIONS:
- Duration: [15s / 20s / 30s] — word budget: 15s ≈ 35 words, 20s ≈ 48, 30s ≈ 70
- Audience stage: [Cold / Warm / Retargeting]
- Key message: [1 điều duy nhất muốn viewer nhớ]
- Angle: [VD: mechanism reveal / myth vs fact / everyday ritual / trust stack]

SCRIPT STRUCTURE:
- Hook (0–3s): one line, ~7 words max, curiosity or reframe. NO brand name.
- Turn (3–6s): the shift in perspective that makes the product make sense.
- Mechanism / benefit: approved claims only, in plain words.
- Proof / everyday use: one concrete, visual-able benefit.
- Close: trust point + soft CTA (no "Buy now", no urgency).

OUTPUT FORMAT:
1. Script with [SECOND MARKERS], one VO line per visual beat
2. For each line: a one-sentence visual suggestion (what is on screen)
3. On-screen text suggestions
4. VO direction: voice gender/age, accent, pace, where to pause
5. 3 alternative hooks

CONSTRAINTS:
- Second person ("your skin") or neutral narrator — never first person
- Every product statement must match an approved claim in meaning
- No corporate language ("innovative", "revolutionary", "game-changing")
- No insecurity framing, no instant-result promises
- Stay within the word budget — cut, never speed up
```

---

## Quick Hook Generator

> Dùng riêng khi chỉ cần generate hooks mới cho existing creative.

```
Generate 10 hooks for a [DURATION]-second Meta Ad for [PRODUCT].
Target: [CUSTOMER DESCRIPTION]
Core problem: [1 pain point từ target-audience.md]

Rules:
- Each hook completable in 3 seconds (~7 words max)
- Mix formats: Question / Statement / Observation / Scroll-stop visual cue
- No brand mention
- First-person where applicable
- Based on real customer language — NOT marketing language

Output: Numbered list. Each hook on one line. No explanation needed.
```

---

## Multimodal Direction Prompt (Gemini Omni — khi có ảnh sản phẩm)

```
[Upload: product image / lifestyle reference]

I need a 20-second UGC-style testimonial script for a Meta Ad.
The character will be holding or referencing this product.

Character: [Paste từ profile.md]
Audience: [Paste từ target-audience.md — 2–3 sentences]
Key benefit to highlight: [1 approved claim từ product-brief.md]

Write the script so it feels like the character is showing the product naturally 
during conversation — not like a product demo. 
The product should appear in the script as a prop, not the main subject.

Include: [TIME MARKERS], delivery notes in [brackets], 
and 1 camera direction note for when to show product.
```

---

## Iterative Edit Prompts (sau khi có draft)

**Shorten hook:**
```
The current hook is: "[CURRENT HOOK]"
It needs to be completable in 3 seconds. Rewrite it — keep the same intent, 
reduce to maximum 7 words for the opening line. Give me 3 options.
```

**Adjust tone:**
```
This script sounds too [salesy / formal / excited]. 
Rewrite it to sound more like [a friend texting / casual conversation / genuine confession].
Keep all the factual claims exactly the same.
```

**Add natural speech patterns:**
```
Insert natural conversational markers into this script to make it sound less scripted.
Add: occasional fillers ("honestly", "like", "I mean"), 
a natural pause before the key result line,
and a slight conversational redirect mid-script.
DO NOT change any factual content or approved claims.
```

---

## Script Review Checklist (trước cổng B)

- [ ] Hook xong trong ≤ 3 giây?
- [ ] Không có claim nào ngoài approved list?
- [ ] Không bắt đầu bằng tên brand?
- [ ] Ngôn ngữ tự nhiên — không corporate?
- [ ] Word count phù hợp với duration? (VO ≈ 2.4 từ/giây, 30s ≈ 70 từ · UGC/Flow ≤ 20 từ/take · UGC/TopView < 40 từ/take)
- [ ] CTA có ở cuối không? (soft CTA OK: "link in bio", "worth trying")

---

## Log — Scripts đã generate

| Date | Campaign | Format | Hook | Performance |
|------|----------|--------|------|-------------|
| | | | | |
