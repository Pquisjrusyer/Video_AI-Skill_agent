---
name: motion-graphic
description: Use this skill for every scene the storyboard tags MOTION-GRAPHIC, or for ads that are entirely static images + animated text/graphics (no real motion needed). Builds video with Remotion (a programmatic video framework using React) — NOT an AI image-to-video tool. This skill also handles the final ASSEMBLY step — stitching the AI-VIDEO clips (from _skills/video/) and the motion-graphic scenes together into 1 complete video. Trigger when the user needs animated text overlays, Ken Burns zoom/pan on a static image, transitions between images, an animated CTA end card, or says "assemble the video", "stitch the clips together", "build it with remotion/code".
---

# Motion Graphic — Remotion Engine

This skill does NOT create real motion inside an image (unlike Veo/Kling/Seedance). It is a code-based compositor/animator — like After Effects but written in React/TypeScript. Input is static images (already generated via Nano Banana/GPT Image) and/or existing video clips (from `_skills/video/`); output is 1 video assembled + animated with code.

Do not use this skill when a scene needs real organic motion (people, light physics, hand interaction) — that case belongs to `_skills/video/`. If it is not yet clear what each scene needs, go back to `_skills/scene-routing/` first.

---

## Two modes of using this skill

**Mode A — Build 1 motion-graphic scene from scratch**
Input: 1 static image + animation spec from `storyboard.md` (text overlay, transition, timing).
Output: 1 mp4 clip rendered separately for that scene.

**Mode B — Assembly (final step, always runs after every scene has a clip)**
Input: all rendered clips — both AI-VIDEO (from `_skills/video/`) and MOTION-GRAPHIC (from Mode A) — in the exact order and timing in `storyboard.md`.
Output: 1 complete video, assembled with `<OffthreadVideo>` (importing existing clips) interleaved with `<Sequence>` (self-rendered graphic scenes), with transitions between segments.

---

## Mandatory reading order

### Step 1 — always read first → [remotion-setup.md](references/remotion-setup.md)
How to initialize the project, the file structure in `remotion-project/`, how to import images/clips/audio from the campaign's `outputs/images/`, `outputs/videos/` and `outputs/audio/`.

### Step 2 — always read second → [animation-patterns.md](references/animation-patterns.md)
Catalog of reusable animation patterns: Ken Burns, spring entrance, typewriter text, transition, parallax, number count-up.

### Step 3 — read when rendering → [render-pipeline.md](references/render-pipeline.md)
Render commands, ratio/fps config per Meta/TikTok placement, pre-export checklist.

### Step 4 — read when the video has background music/voiceover → [audio-and-voice.md](references/audio-and-voice.md)
Importing background music, importing voiceover (Remotion does NOT generate speech — it needs an existing audio file from an external source), setting scene duration from voice length instead of hardcoding, ducking when both play together.

### Step 5 — read when you need sub text/captions/title cards → [caption-effects.md](references/caption-effects.md)
TikTok-style word-highlight sub text that follows the dialogue, kinetic title cards for hook/reveal lines (taken from the script's TEXT overlay column if present), emphasis glow for keywords. Includes copy-paste-ready component code (`CaptionOverlay.tsx`, `TitleCard.tsx`) — just change colors/sizes to match the brand.

---

## Mode A process (build 1 scene)

1. Read this scene's animation spec in `storyboard.md` (content, text overlay, in/out transitions, duration)
2. Check claims in the text overlay against the product's claim APPROVED trong `product-brief.md` — do not add unapproved claims
3. Write the Remotion component for the scene (following the patterns in `animation-patterns.md`)
4. Render this scene separately for review before adding it to the assembly

## Mode B process (assembly)

1. List every clip to assemble, in order, from `storyboard.md` (both AI-VIDEO and MOTION-GRAPHIC)
2. Import AI-VIDEO clips with `<OffthreadVideo src={...}>`, import MOTION-GRAPHIC scenes as the components built in Mode A
3. Place each segment in `<Sequence from={} durationInFrames={}>` with the exact timing in the storyboard
4. Apply transitions between segments per the "Assembly notes" in storyboard.md
5. Render the final file, save it to `outputs/final/`

---

## Automated post-production: b-roll, illustrations, loudnorm (Mode B, multi-take videos with speech)

For videos with speech throughout (multi-take UGC, or VO), do not time b-roll by hand:
- `_tools/post-edit/post_edit.py transcribe` → word-level transcript for each take/VO
- `_tools/post-edit/post_edit.py plan` → matches keywords (`_assets/broll-library/keywords.json` + the campaign's `scripts/visuals-keywords.json`), applies slot-selection rules, generates `visuals-plan.md` (for approval) + `visuals.json` (for Remotion)
- `_prompts/remotion/components/VisualsOverlay.tsx` → renders b-roll (7-frame fade, muted) + illustration cards from `visuals.json`. Place it between the video layer and the caption layer so captions are not covered
- `_tools/post-edit/post_edit.py loudnorm` → normalizes to -14 LUFS before saving to `outputs/final/`

Full process + rules: `_workflows/ugc-workflow.md` Steps 3.2, 7, 8.

---

## Constraints

- Do not add claims beyond claim APPROVED trong `product-brief.md`
- Keep the product imagery intact when animating — do not change label color/logo/shape
- Ratio/fps must match the specified placement (see `render-pipeline.md`)
- Before rendering the final version (Mode B) — present the plan (clip order, transitions, total duration) and wait for confirmation; do not overwrite existing files in `outputs/final/` on your own
- If an AI-VIDEO clip required for assembly is missing (not yet rendered by the user from the 4C/4E card) — stop and report; do not substitute a placeholder on your own
- If the storyboard requires a voiceover but there is no source audio file yet — stop and ask (Remotion does not generate speech); do not skip it or replace it with text-only on your own
- Always install/build in a temp directory, do NOT run `npm install` directly in `campaigns/[campaign]/remotion-project/` (see the reason in `remotion-setup.md`) — only sync `src/` + `package.json` back there after rendering is done
