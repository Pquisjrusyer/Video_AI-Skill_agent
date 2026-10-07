---
name: scene-routing
description: Use this skill FIRST for any video ad with 2 or more scenes — before opening _skills/video/ (writing AI video prompts) or _skills/motion-graphic/ (Remotion code). Splits the video into a list of scenes and assigns a route tag (AI-VIDEO or MOTION-GRAPHIC) to each scene, so downstream skills know how each scene should be handled. Trigger when the user says "make a storyboard", "split the video into scenes", "how should this video flow", "plan video ad", or any time you are preparing to produce a video with more than 1 shot.
---

# Storyboard — Pre-production Router

This skill's role is NOT to write prompts or code. It is the decision layer that sits BEFORE both `_skills/video/` and `_skills/motion-graphic/` — it answers the question "which scenes does this video consist of, and what source should each scene be produced with" before any prompt or code is written.

This is a LIGHTWEIGHT storyboard (routing-level), distinct from the detailed video prompt card (`_prompts/veo3/video-prompt-card.md`, written at `/assets` 4C) — that one GOES DEEP into camera/blocking for each individual scene that was tagged AI-VIDEO at this step. Do not confuse the two layers.

---

## Before you start

Read according to the project's CLAUDE.md rules:
1. `campaigns/[campaign]/brief.md` — hook direction, key message, audience stage
2. `_products/<brand>/<sku>/product-brief.md` — approved claims
3. `_brand/<brand>/target-audience.md` — customer language (xác định brand qua `_products/<brand>/<sku>/product-brief.md`)
4. The written script (if any) in `scripts/`
5. `_assets/broll-library/index.md` — which clips already exist and can be reused instead of generating new ones for the corresponding scene

---

## Process

### Step 1 — Split into scenes

Based on the total duration (usually 15–30s) and the script/concept, split into consecutive scenes. The number of scenes depends on the content — usually 3–6 scenes for a 15–30s ad. Each scene has: a time range, main content (what is happening on screen), and a text overlay if any.

### Step 2 — Assign a route tag to each scene

For each scene, answer: **does this scene need REAL motion** (a person moving/speaking, the product being held/physically interacted with, the camera moving along with organic action, real lighting/depth physics needed)?

- Yes → tag `AI-VIDEO` (will be handled with `_skills/video/`)
- No, only a static image + animated text/graphics/transitions → tag `MOTION-GRAPHIC` (will be handled with `_skills/motion-graphic/`)

Read [scene-routing-rules.md](references/scene-routing-rules.md) to handle ambiguous cases — the default now leans toward AI-VIDEO (realistic quality suits ads better); MOTION-GRAPHIC is used only when the scene is genuinely pure graphics/text (do not simulate real physical motion with code).

### Step 3 — Preview image per scene, then save the storyboard

1. For every scene, generate ONE low-quality preview image (`gen-image.py --quality low`, correct ratio, planned framing/lighting) → `outputs/review/storyboard/[code]_P-S01_v1.png`. Scenes using a real photo (packshot, logo) point to that photo instead. Previews are for approval only — never used as video frames, never counted against the 1 gen + 1 fix limit.
2. Write `campaigns/[campaign]/scripts/storyboard.json` following `_prompts/templates/storyboard-template.md` (scene codes S01, S02…), including for every scene: purpose, tool + render/use seconds, image prompt (`prompt_en` + `prompt_vi`), draft video prompt (`video_prompt_en` + `video_prompt_vi`), dialogue/VO (`line_en` + `line_vi`, copied verbatim from the script's per-scene table), on-screen text and output filename — the same information as the clip board, so any prompt can be copied to another platform.
3. Run `python3 _tools/storyboard.py campaigns/[campaign]` → `storyboard.md` + `storyboard.html`.
4. Ask the user where to view `storyboard.html` (AskUserQuestion): **Xem tại đây** → rendered file card (display: render) · **Mở trên trình duyệt** → `sh _tools/open-browser.sh scripts/storyboard.html` (copy image / open folder only work there). Do not send separate image links.

### Step 4 — Hand-off

The storyboard is part of gate 1 (plan) — continue to the image cards, stop at the end of gate 1. After approval:
- Every scene tagged `AI-VIDEO` → gate 2: real first-frame image (generated + QC) → video prompt card `_prompts/veo3/video-prompt-card.md`, via `_skills/video/SKILL.md` reading order, FOR THIS SCENE ONLY.
- Every scene tagged `MOTION-GRAPHIC` → gate 3, Mode A of `_skills/motion-graphic/SKILL.md` — animation spec + code for this scene only.
- Assembly of all scenes into 1 video → gate 3 (Assembly mode of `_skills/motion-graphic/SKILL.md`).

---

## Output format

`storyboard.json` per `_prompts/templates/storyboard-template.md` → rendered by `_tools/storyboard.py`. Never hand-write `storyboard.md`.

---

## Constraints

- Do not decide the route on your own if the case is ambiguous — always read `scene-routing-rules.md` before assigning a tag.
- Do not skip this step when the video has ≥2 scenes, even if the user does not explicitly ask to "make a storyboard" — if the task is "make a 15s video ad", run through this routing step first by default.
- One scene = one rendered clip by default. Never merge scenes into a single clip unless the user asks — propose it as an option instead.
- Fill every field of each scene in `storyboard.json` (image, visual_vi, vo, onscreen, route, prompt_en, prompt_vi; camera/transition/AI-risk go in `notes_vi`); total duration must equal the brief exactly.
- Process products (nail, skincare, makeup): scenes follow the real steps (apply → cure/absorb → result). Reduce motion complexity to lower AI risk — never drop the core action (e.g. the hand holding the brush).
- The storyboard at this step does NOT yet need detailed camera/lighting for AI-VIDEO scenes — that belongs to the video prompt card at `/assets` 4C.
