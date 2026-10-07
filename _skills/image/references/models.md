# Model Selection — Nano Banana vs GPT Image 2

The skill writes prompts for two model families. They think differently — the choice of model changes the structure of the prompt.

## TL;DR

> **Project default: GPT Image 2** (Claude generates via `_tools/gen-image.py`). The table below only matters when the user asks for Nano Banana or the shot needs a ratio beyond 3:1.

| Task | Model |
|--------|--------|
| Real place/object (with grounding) | **Nano Banana** (NB2/NBP) |
| Complex scene with physics/composition | **Nano Banana Pro** |
| Long horizontal/vertical formats (1:8, 8:1, 4:1) | **Nano Banana** (only NB supports extremes) |
| Cheap mass generation | **Nano Banana 2** or **gpt-image-1-mini** |
| Photorealism with fine typography/UI | **GPT Image 2** |
| Precise editing with preservation (try-on, swap, weather) | **GPT Image 2** (it has the best identity preservation in editing) |
| Small dense text in frame | **GPT Image 2** (`quality: high`) |
| Brand print materials / posters with EXACT TEXT | **GPT Image 2** |
| Storyboards, comics (sequences) | **Nano Banana** (extreme ratios + thinking) |
| Storyboard focused on typography | **GPT Image 2** |
| Style transfer described in words (no reference image attached) | **GPT Image 2** (concrete visual targets) |
| Render from 14+ references | **Nano Banana Pro** (up to 14) or **GPT Image 2** (up to 16) |

## When each one wins

### Nano Banana wins at
- **Image grounding.** NB2 searches the internet for real images before generating — accurate architecture of a specific temple, bridge, square; specific species of animals, plants. GPT Image 2 does not do this.
- **Extreme aspect ratios.** 1:8, 8:1, 1:4, 4:1 — banners, scrolls, comic strips. GPT Image 2 maxes out at 3:1.
- **"Thinking" mode.** Complex infographics with spatial logic.
- **Price/speed.** NB2 = $0.04/img.

### GPT Image 2 wins at
- **Identity preservation in edit.** You change clothes / weather / background — face, pose, geometry don't drift. The two-column logic (change / preserve) works like a contract.
- **Fine text in frame.** Small captions, legends, footnotes, multi-font layouts. Renders sharper at `quality: high`.
- **UI mockups and product screenshots.** Hierarchy, real interface elements, readable labels.
- **Structured 5-slot prompt.** A clear split into Scene/Subject/Details/Use case/Constraints gives predictability.
- **The `quality` lever.** low/medium/high — a deliberate trade-off between speed and fidelity.

### Where both models are equally good
- Photorealistic portraits.
- Product shots on a neutral background.
- Minimalist posters.
- Editorial photography.

## Differences in prompt syntax

| Aspect | Nano Banana | GPT Image 2 |
|--------|-------------|-------------|
| Prompt style | Natural language, 1-2 paragraphs | 5-slot with section labels |
| Camera/lens | **Do not specify** numbers (50mm, f/2.8) — NB ignores them | "50mm feel" is OK, but as a high-level look |
| "Stunning/epic/masterpiece" | Ignored, does no harm | **Anti-slop**: harmful, makes the result worse |
| Text in image | `"..."` in quotes, font + position | `"..."` or ALL CAPS + "no extra words / no duplicate text" |
| Negative framing | Use positive framing | Use positive framing + an explicit preserve list |
| Complex scenes | JSON for 5+ elements | 5-slot template with sections |
| Edit | "Keep X same, change Y" | "Change: X / Preserve: Y / Constraints: Z" — repeat preserve every iteration |
| Multiple references | Up to 14, index them | Up to 16, index with role ("Image 1: base", "Image 2: jacket reference") |

## Cost (rough guide)

| Model | Price | Notes |
|--------|------|---------|
| Nano Banana 2 (Flash) | ~$0.04/img | Default for most tasks |
| Nano Banana Pro | ~$0.15/img | Complex scenes, up to 14 refs |
| GPT Image 2 (`low`) | cheap | Latency-sensitive, previews |
| GPT Image 2 (`medium`) | moderate | Default for GPT Image |
| GPT Image 2 (`high`) | more expensive | Small text, brand-sensitive, photorealism |
| gpt-image-1-mini | cheap | High-volume exploratory generation |

> GPT Image: Claude runs generation (`_skills/image/SKILL.md` → Gen GPT Image). Nano Banana: self-gen card only.
