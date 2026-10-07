# Render Pipeline — Remotion

## Config by placement

| Placement | Width x Height | Ratio | Recommended FPS |
|---|---|---|---|
| Reels / TikTok / Stories | 1080 x 1920 | 9:16 | 30 |
| Feed | 1080 x 1350 | 4:5 | 30 |
| Square / Carousel | 1080 x 1080 | 1:1 | 30 |

Set `width`/`height`/`fps` in `<Composition>` (Root.tsx) to match the placement the campaign brief requires — do not render 1 ratio and then crop by hand, unless intentional.

## Render commands (bộ dùng chung — `remotion-setup.md`)

```bash
python3 _tools/remotion.py check  campaigns/<c>                     # kiểm timeline.json + đủ file
python3 _tools/remotion.py stills campaigns/<c>                     # khung giữa mỗi cảnh + ảnh ghép (1 lần đóng gói, ~20s)
python3 _tools/remotion.py review campaigns/<c>                     # outputs/review/<code>_review_vN.mp4
python3 _tools/remotion.py final  campaigns/<c> --name <tên>.mp4 [--extra 4:5]   # outputs/final/ + -14 LUFS + bản phụ
```
Kích thước theo `width` / `height` trong `timeline.json`; bản phụ khác tỷ lệ dùng `--extra` (không crop tay). Không gọi `npx remotion render / still` từng khung — mỗi lệnh đóng gói lại từ đầu.

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
