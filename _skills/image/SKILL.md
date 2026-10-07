---
name: image
description: >
  Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2. Writes the prompt card, then
  generates GPT Image 2 (project default) via _tools/gen-image.py. Use when: "draw", "generate
  an image", "image prompt", "prompt for an image", blog covers, slides, posters,
  product shots, UI mockups, storyboards, character sheets, edit/colorize, style transfer,
  vision analysis, image-to-prompt, nb, NBP, NB2, gpt-image-2, 
  ecommerce product photography, fashion editorial, food/beverage ads, cinematic portraits.
  Do NOT use for: video (use video skill), 3D models, audio, non-image tasks.
---

# Image Prompting — Nano Banana & GPT Image 2

This skill writes image prompts, then (GPT Image) Claude generates them with `_tools/gen-image.py` — see **Gen GPT Image** below. **Default model = GPT Image 2.** Nano Banana only when the user asks for it or the shot needs an extreme ratio (beyond 3:1) → self-gen card.

The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone. The actual rules — what the models reward, what they punish, how to phrase a 5-slot template, when to add `quality: high`, when to use image grounding — live only in the reference files.

---

# Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS

Past attempts to write prompts directly from this skill body produced lazy, generic results. Each model has its own physics; common rules collapse into mush when applied without model-specific syntax. Read in this order before producing any prompt:

### Step 0 — check reuse before generating → `_assets/broll-library/index.md`

Search the index for an existing image matching what's needed (mood, setting, character, product, ratio). If a match exists, reuse it instead of writing a new prompt — note the reused file in `prompts-used/` and stop here. Only proceed to Step 1 if nothing in the library fits.

### Step 1 — always read first → [models.md](references/models.md)

Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot template, quality settings, which features exist (image grounding only on NB, EXACT TEXT discipline only on GPT Image, etc.).

If the user named a model — use it. Otherwise GPT Image 2. State the model in the card header.

Default: **GPT Image 2**. Nano Banana only if the user names it or the ratio is beyond 3:1 — then output a self-gen card (user generates on the web UI, drops the file into `outputs/images/`) and skip the Gen section.

### Step 2 — read **one** model file (the one you picked)

- **Nano Banana** → [nano-banana.md](references/nano-banana.md)
  Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mode. JSON for 5+ elements. Up to 14 reference images. Why you must NOT write `50mm / f-stop / ISO` numbers.

- **GPT Image 2** → [gpt-image.md](references/gpt-image.md)
  5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop banned-words list. `quality: low / medium / high` as a deliberate fidelity lever. Size constraints (multiples of 16, max 3:1, up to 2560×1440). Two-column edit logic (Change / Preserve / Constraints). Up to 16 reference images with explicit roles.

The model file is non-negotiable. Skipping it is the single biggest cause of weak prompts.

### Step 3 — always read after the model file → [golden-rules.md](references/golden-rules.md)

Universal rules that apply to both models: start with a verb, positive framing, hex colors, quote text, edit don't re-roll, one change per iteration, reference images.

### Step 4 — characters (when needed)

- Character continuity across multiple images / character seed → [characters.md](references/characters.md)

---

# Output format

The deliverable is the image prompt card: `_prompts/nano-banana/image-prompt-card.md` (`/assets` pass 4A). Fill every section of that card. This skill supplies only the model-specific PROMPT syntax inside it (natural prose for Nano Banana, 5-slot for GPT Image 2) plus the model / quality / size line for "Tool + cấu hình". Save path on the card: `outputs/images/` (or the path on the card).

For edits, the card's THAY ĐỔI / MỨC ĐỘ / GIỮ NGUYÊN block carries the explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana); inside the PROMPT it reads:

```
Change: <one concrete thing>
Preserve: <face, pose, lighting, framing, geometry, ...>
Constraints: <no extra objects, no drift, ...>
```

---

# Gen GPT Image — Claude chạy (cổng 2, sau "ok cổng 1")

Không gen ở cổng 1: kế hoạch chưa duyệt thì ảnh dễ thành bỏ.

1. **Báo trước 1 lần:** liệt kê các ảnh sắp gen (ID · ratio · quality · số ref), chia đợt theo phụ thuộc. User OK mới chạy. Không báo giá.
2. **Gen theo thứ tự phụ thuộc:** đợt ① ảnh nền (seed nhân vật, ảnh sản phẩm) → QC → pass mới sang đợt ② (keyframe dùng ① làm ref). Các ảnh cùng đợt, không phụ thuộc nhau → chạy song song (nhiều lệnh Bash trong 1 lượt).
3. **Mỗi ảnh:** lưu PROMPT của thẻ (nguyên văn) vào file `<image-id>.txt` trong scratchpad, rồi chạy:
   ```bash
   python3 _tools/gen-image.py --prompt-file <id>.txt --out <dòng "Lưu về" trên thẻ> --ratio 9:16 --quality medium --ref <Image 1> --ref <Image 2>
   ```
   - `--ref` **đúng thứ tự** REFERENCE IMAGE ROLES trên thẻ (Image 1 = `--ref` đầu tiên).
   - `--quality`: `medium` mặc định · `high` khi ảnh có chữ/label cần đọc được hoặc là seed nhân vật · không dùng `low` cho ảnh làm khung video.
4. **QC** (thumbnail `sips -Z 768`) theo checklist QC trên thẻ.
   - Pass → ghi `worked` cạnh thẻ trong `prompt-pack.md`.
   - Lỗi → **1 lần sửa duy nhất**: edit sửa đúng 1 lỗi nặng nhất, `--ref <ảnh v1>` làm Image 1 + ref gốc, prompt dạng `Change / Preserve / Constraints`, lưu `_v2`. Ghi `needs adjustment`.
   - v2 vẫn lỗi → **dừng ảnh đó**, không gen nữa. Ghi `failed` + note cho user tự sửa tay: lỗi gì, ở đâu, gợi ý sửa (prompt edit để dán vào chatgpt.com, hoặc sửa trong Photoshop/Canva). Tiếp tục ảnh khác.
5. **Exit code của script:**
   | Code | Nghĩa | Làm |
   |---|---|---|
   | 0 | OK | QC |
   | 2 | Bộ lọc an toàn chặn | Viết lại prompt 1 lần (bỏ từ nhạy cảm về da/cơ thể, mô tả trung tính) — lần chạy bị chặn không tính lượt. Vẫn chặn → note user tự gen |
   | 3 | Hết lượt (đã gen + sửa) | Note user tự sửa tay như bước 4 |
   | 4 | Thiếu key / key sai / hết credit | Dừng gen cả loạt, báo user 1 lần ("đổi key OpenAI" hoặc nạp Billing). Các ảnh còn lại → thẻ tự gen |
   | 1 | Lỗi khác (file ref không thấy, mạng sau 3 lần thử, ghi đè) | Sửa nguyên nhân theo thông báo rồi chạy lại |
6. **Label sản phẩm:** luôn đưa ảnh sản phẩm thật (`_products/<sku>/reference-images/`) làm ref, `quality: high`, mỗi ảnh chỉ 1 sản phẩm. Packshot / end card cần label đúng 100% → dùng ảnh thật ghép ở Remotion, không gen.
7. Log mọi lượt gen (kèm prompt): `outputs/images/_gen-log.jsonl` — dùng để lặp lại ảnh đạt và đối chiếu Usage trên platform.openai.com.

---

# Final response style

Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano Banana).

Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars" — invert to positive), external comparisons ("like Apple ad" — describe the visual properties instead), numerical lens parameters in Nano Banana prompts (it ignores them).
