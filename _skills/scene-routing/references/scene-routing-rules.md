# Scene Routing Rules — AI-VIDEO vs MOTION-GRAPHIC

Rules for deciding the route tag for each scene in the storyboard. Read this file BEFORE tagging any ambiguous scene.

---

## 1. Core principle

> Route MOTION-GRAPHIC only when the scene is **genuinely simple** — pure graphics/text, with no organic physical motion that needs to be simulated (text overlay, transitions between static images, animated numbers, logo/end card/CTA). Everything else defaults to AI-VIDEO.

Why the default flips to AI-VIDEO when ambiguous: Remotion/code animation produces simplistic, unrealistic imagery (lacking lighting physics, material, organic motion) — for Meta ads it usually does not reach the required quality. Use MOTION-GRAPHIC only when the scene is inherently graphic (do not try to simulate real motion with code). Before deciding to generate anything new, always check `_assets/broll-library/index.md` — if a suitable AI-VIDEO clip already exists, reuse it; only generate if none exists.

---

## 2. Tag AI-VIDEO when the scene has

- A person speaking/performing (testimonial, lip-sync, dialogue)
- Hands/a person physically interacting with the product (holding, opening the cap, pouring out, applying to skin...) and needing realistic body motion
- Camera movement following organic action that cannot be reproduced by formula (e.g., following a person's footsteps, panning after a sudden action)
- Real, changing lighting/material physics needed (flowing water, rising smoke, fabric swaying in the wind)
- Facial expression is the emotional focus of the scene

## 3. Tag MOTION-GRAPHIC when the scene has

Only the pure-graphic cases below — not for simulating real physical motion with code:

- Static product/lifestyle image + animated text overlay (headline, offer, price)
- Transition/wipe/slide between multiple static images
- Animated numbers/stats (numeric before/after, price count-up, %)
- Logo reveal, end card, CTA button
- Quote card / text-based testimonial (not a person speaking)

Zoom/pan into an image (Ken Burns) and turntable product rotation **are no longer MOTION-GRAPHIC by default** — see section 4; the default is now AI-VIDEO unless the user explicitly asks for MOTION-GRAPHIC.

## 4. Ambiguous cases — how to handle

| Case | Default route | Why |
|---|---|---|
| Zoom from wide shot into the product, no hands | AI-VIDEO | Real lighting/depth/material gives better ad quality than simulated Ken Burns — check broll-library before generating |
| Zoom + hand holding the product at the same time | AI-VIDEO | Needs organic hand motion |
| Catalog-style 360° product rotation | AI-VIDEO | Real shadow/reflection/lighting physics while rotating — code rotate transforms easily look fake, unless the user asks for MOTION-GRAPHIC |
| Person rotating the product to show its angles | AI-VIDEO | Real hand motion + expression |
| Text testimonial as a quote card (not a person speaking) | MOTION-GRAPHIC | This is a graphic, not video of a real person |
| Opening shot "hand reaches into frame" | AI-VIDEO | Needs natural hand motion |
| Before/after comparison of 2 static images (as pure stats/slide graphic) | MOTION-GRAPHIC | This is a graphic presenting data, not simulating physical motion |

## 5. When genuinely unsure

If it is still unclear after applying the table above, ask the user instead of guessing — state the trade-off clearly: "AI-VIDEO is more realistic and better suited to ad quality, but takes render time + risks the product drifting/morphing (reduce this risk by checking `_assets/broll-library/index.md` before generating new); MOTION-GRAPHIC is fast with precise frame-by-frame control, but only fits when the scene is inherently graphic/text, not a simulation of real physical motion."
