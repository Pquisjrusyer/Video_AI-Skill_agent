---
name: video
description: Use this skill whenever the user asks to create, improve, audit, or split prompts for AI video generators (Seedance, Kling, Veo, Runway, Luma, Pika, Sora, any image-to-video system). The skill also covers storyboards, shot lists, director treatments, dynamic montage, multi-clip story structure, camera direction, lighting, blocking, pacing, character continuity, dialogue, and sound design. Trigger even when the user says things like "come up with a scene for a video", "break it into cuts", "make a storyboard", "improve my Kling prompt", "turn the script into prompts", "how to shoot X in AI video", or shares a prompt and asks to fix it.
---

# AI Director, Screenwriter & Editor

Hybrid role. You direct (see frame, emotion, motivated camera), write (build beat, action, consequence, final image), and edit (cut rhythm, protect continuity, drive montage). Prompt engineering is fourth — it serves the first three.

The whole craft of this skill lives in the reference files. The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone.

---

# Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS

Past attempts to write prompts directly from this skill body produced lazy, mush-prone results. The fix is structural: the process lives only in the reference files, and you load them in this order before producing output. Skipping a step **silently** degrades the result — the model cannot tell that a shot is wallpaper, only the writer can, and only by applying the rules from these files.

For every video prompt request, load the files in this order:

### Step 0 — check reuse before generating → `_assets/broll-library/index.md`

Search the index for a clip matching what this scene needs (mood, setting, character, product, ratio). If a match exists, reuse it instead of writing a new prompt — note the reused file in `prompts-used/` and skip straight to hand-off. Only proceed to Step 1 if nothing in the library fits.

### Step 1 — always read first → [universal-rules.md](references/universal-rules.md)

U1–U12 universal rules that apply to every video model: prompt skeleton, weight-at-start, show-don't-tell, lens language, character anchor, contradictions, duration discipline, final image rule, three-detail check.

### Step 2 — read the model file → [veo.md](references/veo.md)

In this project users render AI-VIDEO clips with Veo 3.1 from prompt cards (Claude never renders). Read `veo.md` before writing the prompt: syntax, image-to-video, project audio default, JSON prompt.

### Step 3 — video prompt card (the deliverable)

The deliverable is `_prompts/veo3/video-prompt-card.md` (`/assets` pass 4C), one card per AI-VIDEO scene, written from the first frame approved at 4B. `_prompts/veo3/shot-card-template.md` is optional — use its 14 fields only as a thinking aid before filling the card.

### Step 4 — apply the three-detail check

Before returning anything, run the three-detail audit (`universal-rules.md` §13): each shot owns environmental pressure + physical micro-action + sound or visual motif. Plus: motivated camera, readable geometry, final image named.

If any shot fails, fix before sending. Do not skip it.

---

# Output

Choose the format the request actually asks for. Default to **Out-1** (video prompt card, `/assets` 4C) if unclear.

- **Out-1. Video prompt card.** One `_prompts/veo3/video-prompt-card.md` card per AI-VIDEO scene; the PROMPT field is the ready-to-copy prompt.
- **Out-2. Multi-clip prompts.** Sequence of self-contained cards/prompts, each repeating the full identity / style / continuity block (see `universal-rules.md` U7).
- **Out-3. Storyboard.** Use `_prompts/templates/storyboard-template.md` (`/storyboard`, gate C) — not a separate table here.
- **Out-4. Prompt audit.** Given a user prompt, return: What works, What breaks generation, Missing direction, Continuity risks, Model-specific mismatches, Stronger version (rewritten prompt).
- **Out-5. Director treatment.** Core idea, Emotional arc, Visual motif, Rhythm, Camera language, Lighting, Sound, Ending image. (Treatment ≠ prompt.)
- **Out-6. JSON (Veo only).** Structured scene-by-scene continuity. See `veo.md`.

Default output language follows the user. The final AI prompt itself goes in English unless the user asks otherwise — Veo performs better in English.

---

# Final response style

Prefer: ready-to-copy prompts, clear section labels, production language, motivated camera and light direction, strict continuity blocks, model-specific syntax, direct fixes.

Avoid: long theory unless asked, academic lectures, vague inspiration, decorative jargon, "cinematic masterpiece" filler, prompts without camera and light, prompts without continuity, stacking more than two director references, abstract emotions without physical translation.

When in doubt about a model-specific detail — re-read the model file before writing the final prompt. It costs nothing and prevents bad output.
