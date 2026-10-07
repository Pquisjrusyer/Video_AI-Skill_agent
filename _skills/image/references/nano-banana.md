# Nano Banana — Specific Rules

Nano Banana 2 (Flash, $0.04) and Nano Banana Pro (Gemini 3 Pro, $0.15). "Thinking" models — they understand intent, physics, composition.

## Prompt style

Natural language, 1-2 paragraphs. Free-form structure, but ordering helps:
**Subject + Action + Location/context + Composition + Style**

```
A cinematic wide shot of a futuristic sports car speeding through a rainy
Tokyo street at night. Neon signs reflect off wet pavement and metallic
chassis. Format: 16:9.
```

## What NOT to specify

- Numerical lens parameters: **50mm, 85mm, f/2.8, ISO 400** — NB ignores them. Use descriptions instead: "shallow depth of field", "wide-angle distortion".
- Tag soup: "cool, modern, 4k, cinematic" — write it as a coherent sentence.

## Unique capabilities

### Image Grounding (NB2 only)
NB2 searches the internet for real images before generating. Architecturally accurate specific locations, correct species of animals/plants.

```
Generate a cinematic, golden-hour photograph of [SPECIFIC REAL PLACE].
Ensure the architectural details, the spire, the surrounding square, and
the landscape are accurate to reality.
```

**Works for:** buildings, bridges, squares, animal species, plant species, insects.
**Does not work for:** specific people.

### Extreme Aspect Ratios (NB2 only)

1:8, 8:1, 1:4, 4:1 — for banners, scrolls, comic strips.

```
Create a 4-panel horizontal comic strip (aspect ratio 4:1).
The story follows [CHARACTER] doing [ACTION] that ends with a twist.
Use a vibrant comic book style. Keep character design consistent.
```

Standard: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9.

### Thinking Mode

OFF by default. Turn it on only for:
- Muddled results that require reasoning
- Complex infographics with spatial logic
- Grounding + spatial reasoning at the same time

### Multi-Reference (up to 14 images)

```
[Image 1: face]
[Image 2: outfit]
[Image 3: background]
Combine: face from Image 1, outfit style from Image 2, setting from Image 3.
Match lighting and perspective.
```

### JSON for complex scenes (5+ elements)

```json
{
  "subject": {"description": "main subject", "expression": "emotion/pose"},
  "photography": {"angle": "eye-level", "shot_type": "waist-up", "aspect_ratio": "16:9"},
  "background": {"setting": "location", "lighting": "soft natural"}
}
```

## Editing with Nano Banana

Conversational, no masks:

```
Remove [OBJECT] from this image.
Fill with [LOGICAL REPLACEMENT] matching surroundings.
Keep [PRESERVED ELEMENTS] exactly the same.
```

After generation, add changes iteratively:
- "Make it warmer"
- "Increase contrast"
- "Soften background, add blur"
- "Change headline color to #3b82f6"

## Text Rendering

- SOTA across 100+ languages.
- Fonts can be named: "Century Gothic 12px", "Brush Script", "Impact", "Heavy blocky sans-serif".
- Multiple languages in one frame works.
- Hack: for complex text — first ask the model to **write the text**, then in a separate prompt "insert this text into the image".

## Resolution / Cost

| Resolution | Usage |
|------------|---------------|
| 0.5K | Cheapest, batch and A/B variants |
| 1K | Default |
| 2K | Final selection |
| 4K | Print, hero assets |

**Workflow:** run variants at `0.5K` flash → select → regenerate the winner at `2K`/`4K`.

## When to switch NB2 → NBP

- NB2 can't handle a complex multi-layered prompt.
- You need 14 references at once.
- Photoreal with very fine work on materials and light.
