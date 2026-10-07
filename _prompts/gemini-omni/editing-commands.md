# Gemini Omni Prompt Library — Video Editing Commands

> ⛔ **Không thuộc quy trình chuẩn — dựng/chữ/nhạc ở `/edit` (Remotion). Chỉ dùng phần Quality Check làm checklist tham khảo.** (Thư viện tham khảo — không phải deliverable.)
>
> **Khi dùng (cũ):** Đã có video draft từ Veo 3, cần chỉnh mà không rebuild từ đầu.  
> **Lưu ý quan trọng:** Gemini Omni Flash giới hạn 10 giây/clip. Nếu video dài hơn, upload từng đoạn.

---

## Pacing & Timing Edits

```
[Upload video]

Edit this video:
1. The transition at [TIMESTAMP] is too fast — extend it by 0.5 seconds
2. Hold the final frame for 1 second longer before fading
3. Keep everything else exactly the same
```

```
[Upload video]

The overall pacing feels rushed. Slow it down by approximately 15% 
without changing the pitch of the audio.
```

---

## Audio Edits

```
[Upload video + audio track]

Replace the background audio in this video with the uploaded music track.
Keep the dialogue audio exactly as-is.
Music should sit under dialogue — dialogue volume dominant.
Fade music in at 0s, fade out at [Xs].
```

```
[Upload video]

The dialogue audio has slight background noise. 
Clean it up — reduce room noise by ~30%, keep voice natural.
Do not alter the voice character or timing.
```

---

## Visual Adjustments

```
[Upload video]

Apply a color grade to this video:
- Warmer shadows (slight amber shift)
- Cooler highlights (desaturate slightly)
- Overall: "warm golden hour" feel
Maintain skin tone accuracy — do not over-orange the complexion.
```

```
[Upload video]

The product in this video appears slightly overexposed in the [TIMESTAMP] section.
Reduce exposure on the product only — keep the surrounding scene unchanged.
```

---

## Crop & Format

```
[Upload video — 16:9 or 1:1]

Reformat this video for 9:16 (vertical) Meta Reels/Stories.
Priority crop: Keep the face/product in frame at all times.
If there are scenes where this isn't possible, zoom in slightly rather than cropping face.
Add black bars if needed only as a last resort.
```

---

## Add Text Overlay

```
[Upload video]

Add the following text overlays:
- [0–3s]: "[HOOK TEXT]" — large, bold, white, centered, slight drop shadow
- [15–18s]: "[CTA TEXT, e.g., 'Link in comments']" — smaller, white, lower third
Font: Clean modern sans-serif
Do not cover the face or product at any point.
```

---

## Audio-to-Video Sync (Gemini Omni specialty)

```
[Upload: still images x3] + [Upload: 15s music track]

Create a 15-second product reveal video from these images.
Sync image transitions to the beat of the music.
- Image 1: hold for [X beats]
- Image 2: transition on [beat X]
- Image 3: final hold + slight zoom

Motion on each image: slow Ken Burns effect — zoom in 5–8%
Color: Match warmth across all images for cohesive feel.
End frame: product image, logo/name centered.
Format: 4:5
```

---

## Quality Check Before Final Export

```
[Upload video]

Review this video and tell me:
1. Are there any visible artifacts or glitches?
2. Does the lip sync look natural throughout? Flag any timestamps where it's off.
3. Is the product clearly visible and not distorted?
4. Does the audio feel natural — any robotic or unnatural speech patterns?

Output: List of issues found with timestamps. If none, confirm "Ready to export."
```
