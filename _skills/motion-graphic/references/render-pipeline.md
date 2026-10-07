# Render Pipeline — Remotion

## Config by placement

| Placement | Width x Height | Ratio | Recommended FPS |
|---|---|---|---|
| Reels / TikTok / Stories | 1080 x 1920 | 9:16 | 30 |
| Feed | 1080 x 1350 | 4:5 | 30 |
| Square / Carousel | 1080 x 1080 | 1:1 | 30 |

Set `width`/`height`/`fps` in `<Composition>` (Root.tsx) to match the placement the campaign brief requires — do not render 1 ratio and then crop by hand, unless intentional.

## Render commands

Render 1 scene separately for review:
```bash
npx remotion render src/index.ts Scene1KenBurns out/scene1-review.mp4
# then copy to campaigns/[campaign]/outputs/review/
```

Render the final assembly:
```bash
npx remotion render src/index.ts FinalAssembly out/final.mp4
```

Render with custom props (e.g. different headline text for an A/B test):
```bash
npx remotion render src/index.ts FinalAssembly out/final-v2.mp4 --props='{"headline":"30% off today"}'
```

## Checklist before exporting the final version

- [ ] Each scene's timing matches `storyboard.md`
- [ ] Text overlays use the approved claims in claim APPROVED trong `product-brief.md`
- [ ] Ratio/duration match the placement required in the brief
- [ ] No placeholder text/images left
- [ ] AI-VIDEO clips imported into the assembly are the approved versions (not drafts)
- [ ] Review at normal speed (not just fast scrubbing) to catch jerky transitions/frame jumps

## Saving files

```
Review renders (per scene / full review)  → campaigns/[campaign]/outputs/review/
Final assembly (passed the checklist)     → campaigns/[campaign]/outputs/final/
```

Naming follows the project's original convention:
```
[campaign-code]_[format]_[character]_[product]_[ratio]_v[version].mp4

E.g.:
2026-06-LAUNCH_motiongraphic_nochar_serum-A_9x16_v1.mp4
```

## When to install additional packages

- Importing a custom brand font → `@remotion/google-fonts` or self-host the font in `public/fonts/`
- Audio processing (mixing voiceover + background music) → `@remotion/media-utils`
- Need an existing Lottie animation → `@remotion/lottie`

Do not install packages outside the current task's scope — every added package increases install/render time.
