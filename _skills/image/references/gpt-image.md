# GPT Image 2 — Specific Rules

OpenAI production default: `gpt-image-2`. Migration-only: `gpt-image-1.5`, `gpt-image-1`. Budget: `gpt-image-1-mini`.

## Prompt structure — 5 slots

GPT Image 2 responds most strongly to a split into sections. Write with labels, not as a continuous block of text.

```
Scene: location, time of day, background, environment
Subject: primary focus — who or what is central
Important Details: materials, textures, lighting, camera angle, mood, composition
Use Case: editorial, product mockup, UI, poster, infographic
Constraints: what must NOT change/appear (no watermarks, preserve face, no extra text)
```

> "The fifth slot is where most mediocre prompts fail silently." Without explicit constraints the model drifts.

### Minimal example

```
Scene: small Lisbon florist storefront at blue hour, wet cobblestones
Subject: woman in navy apron locking the front door, half-turned to camera
Important Details: warm interior glow spilling onto pavement, 50mm feel,
  soft contact shadows, brushed brass door handle, "Florista" hand-painted sign
Use Case: editorial photography
Constraints: no extra signage, no people in background, no text other than the sign
```

## Anti-Slop Rules

GPT Image 2 is especially sensitive to the quality of the wording. Vague praise = a degraded result.

| ❌ Don't write | ✅ Write |
|-----------|---------|
| stunning, incredible, epic, gorgeous, masterpiece | overcast daylight, brushed aluminum, chipped paint, 50mm feel |
| "minimalist brutalist luxury photoreal" (style tags) | "cream background, heavy black sans-serif, asymmetrical type block, one hero object, generous negative space" |
| "like an Apple ad" | concrete visual facts |
| moody language in which the functional requirements get lost | a direct statement: "image must contain a transit kiosk" |

## Quality Settings — the fidelity / latency lever

| Setting | When |
|---------|-------|
| `quality: low` | High-volume, previews, exploratory, latency-sensitive, draft |
| `quality: medium` | **Default starting point** |
| `quality: high` | Small/dense text, infographics, portraits, identity-sensitive edits, brand assets |

Project rule: `medium` by default, `high` for readable label/text or character seeds. Never `low` for a video keyframe. Only 1 fix allowed per image, so pick the right quality up front.

## Sizes (gpt-image-2)

- Max edge: <3840px
- Both sides: multiples of 16
- Aspect ratio: max 3:1 (long:short)
- Total pixels: 655 360 – 8 294 400
- Reliable upper bound: 2560×1440

**Common sizes:**
- Portrait 1024×1536
- Landscape 1536×1024
- Square 1024×1024
- 2K 2560×1440

> GPT Image 2 CANNOT do extremes like 1:8 / 8:1 — go to Nano Banana.

## Text in Image

- Literal text in `"..."` or ALL CAPS.
- Font, size, color, position — explicitly.
- Difficult words and brands: spell them out letter by letter.
- Protection against junk: "**no extra words, no duplicate text, no watermarks**".
- For unreadable small text: "**100 percent readable and physically believable**".
- Small/dense/multi-font → `quality: high` is mandatory.

## Editing — two-column logic

> Project dùng `_tools/gen-image.py --ref` (OpenAI `images/edits`, nhiều ảnh tham chiếu). `mask_image_url` / `input_fidelity` chưa hỗ trợ trong script.

```
Change: [single concrete change]
Preserve: face, identity, pose, lighting, framing, background, geometry, text, layout
Constraints: no extra objects, no redesign, no drift
```

**Edit rules:**
- **One edit per iteration.** Don't try to change everything at once.
- **Repeat the preserve list every iteration.** Otherwise it drifts.
- **Surgical edits:** explicitly list what NOT to touch (saturation, contrast, layout, arrows, labels, camera angle).
- `mask_image_url` chưa hỗ trợ trong `gen-image.py` — sửa cục bộ bằng prompt `Change / Preserve`.

### Edit patterns

**Virtual try-on:** "Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows so outfit looks naturally worn."

**Object removal:** "Remove [X]. Do not change anything else." (`input_fidelity: high` is an API-only reference for gpt-image-1.5/1; in gpt-image-2 high fidelity is the default).

**Lighting/weather swap:** "Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, geometry, camera angle, object placement."

**Interior swap:** "Swap [furniture]. Preserve camera angle, lighting, shadows, surrounding context. Photorealistic contact shadows."

## Multi-Image — up to 16 refs

Index with a **role**, not just a number:
```
Image 1: base scene
Image 2: jacket reference (apply only the jacket fabric/cut to subject in Image 1)
Image 3: lighting reference (apply golden-hour quality from Image 3)
```

## Style Transfer

Don't write abstractly ("minimalist", "editorial"). Name the concrete visual properties of the reference: palette, edge treatment, silhouette, shadow handling, plane logic.

## World Knowledge

GPT Image 2 can infer context: "Bethel, NY, August 1969" → it will derive a Woodstock aesthetic. Use it: give a historical/cultural anchor, don't spell out every detail.

## Iteration Strategy

- Start with a **clean** base prompt.
- One change per round. "Make lighting warmer", "remove extra tree", "restore original background".
- On drift — list the invariants again.
- For long prompts — labeled sections, not one wall of text.

## Use-Case Templates

### Photoreal Editorial
```
Scene: [location, time, weather]
Subject: [who, action, framing]
Important Details: [lens feel, light source, surface wear, imperfections, real texture]
Use Case: editorial photograph, looks like a real photo
Constraints: no glamorization, no heavy retouching, no studio gloss
```

### Product Mockup (Clean Background)
```
Scene: plain white opaque background
Subject: [product] centered
Important Details: crisp silhouette, no halos/fringing, light contact shadow,
  preserve label legibility exactly, preserve geometry
Use Case: product mockup
Constraints: no restyling, only background removal + light polish
```

### UI Mockup
```
Scene: [device frame, e.g. iPhone 15 Pro]
Subject: [screen/app name] — describe AS IF IT EXISTS, not concept art
Important Details: layout, hierarchy, real interface elements, exact copy in quotes,
  typography behavior, spacing, state
Use Case: shipped product screenshot
Constraints: no sketch language, no placeholder text, no Lorem Ipsum
Quality: high (for small UI text)
```

### Marketing Creative with Text
```
Scene: [environment]
Subject: [hero element]
Important Details: [composition, palette, mood]
Use Case: ad creative for [audience]
Text: "EXACT HEADLINE" in [font style], [color], [position]
      "exact subhead" in [font style], [color], [position]
Constraints: no extra text, no duplicate text, no watermarks, no unrelated logos
Quality: high
```

### Infographic / Diagram
```
Title: "[TITLE]"
Content flow: [step 1] → [step 2] → [step 3]
Visual format: [layout type — flowchart, pyramid, isometric, etc.]
Use Case: educational infographic for [audience]
Constraints: readable labels at all sizes, clear hierarchy, no clutter,
  no decorative noise, ample whitespace
Quality: high
Size: 1536×1024
```

## Migration from Older GPT-Image

- Prompts mostly carry over as-is.
- After migrating — check quality, latency, retry rate; retune.
- `gpt-image-1-mini` — only if the main goal is lowering batch cost on low-risk tasks.
