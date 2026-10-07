# Sub Text / Caption Effects — TikTok-style word-highlight + Title Card

> Read this file in Mode B (assembly) when the video has voiceover/TTS and needs: animated sub text (word-by-word), a kinetic title card for a hook/reveal line, or emphasis glow for keywords. Distilled from 1 real UGC campaign — verified working across 5 renders (v1→v5).

---

## When to use what

| Need | Component | Required input |
|---|---|---|
| Sub text that follows the dialogue, with the word being spoken highlighted | `CaptionOverlay` | Full text of the take + per-word timestamps (`<take>.words.json`) or real frame count (`durationInFrames` from `scripts/visuals.json` (`post_edit.py plan`) or `npx remotion ffprobe` in the temp project, never `mdls`) |
| An important hook/reveal line that needs big text standing alone in the frame (not regular sub text) | `TitleCard` | The specific line of text (usually taken from the "TEXT overlay" column in the original script if present) + display timing/length |
| Specific keywords that need to pop more than other words in the sub text (amounts of money, condition names, ingredient names...) | `emphasisWords` prop of `CaptionOverlay` | List of words (strings), matched case-insensitively with punctuation stripped |

**Selection principle:** If the original script (from Gemini Omni or provided by the user) already has a "TEXT overlay"/"Visual overlay" column that spells out on-screen text (separate from the dialogue) → always build a `TitleCard` for exactly that line, do not skip it — this is the clearest signal of where the "highlight" moments in the video are, no guessing needed.

---

## Installation

```bash
npm install @remotion/captions
```

This package is only used for the **`Caption` type** to structure the data (text/startMs/endMs) — do NOT use `createTikTokStyleCaptions()` if you use the even-timing estimation approach below, because that function groups by real pauses (silence detection), while evenly estimated timing has no real silence data to group correctly.

---

## Approach 1 (default, lazy) — evenly estimated timing by pace

Use when: the take has no `.words.json` yet and you want to finish fast, accepting small errors where the character pauses/stresses.

Formula: `wordFrame(i) = round((i / total_word_count) × real_take_frames)` — the real length is the take's `durationInFrames` from `scripts/visuals.json` (`post_edit.py plan`) or `npx remotion ffprobe` in the temp project, never `mdls`; do NOT use the estimated seconds from the script.

⚠️ Errors concentrate in sentences with dramatic pauses (e.g. "Turns out... it was hollow") — if you hear significant drift, switch to Approach 2.

## Approach 2 (more accurate) — real word timestamps from `post_edit.py transcribe`

Use when: you need accurate karaoke captions (client request, or takes with many dramatic pauses). Do NOT install whisper.cpp — reuse the per-word timestamps already produced by `python3 _tools/post-edit/post_edit.py transcribe <take files>` (UGC workflow Bước 7), saved next to each take as `<take>.words.json` (`[{word, start, end}]` in seconds). Convert to frames with `Math.round(sec × fps)`. If the file is missing, run `transcribe` first.

---

## Component: `CaptionOverlay.tsx` (word-highlight, copy-paste then adjust style to the brand)

```tsx
import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

type Props = {
  text: string;
  durationInFrames: number;
  chunkSize?: number; // words per page, default 4 — readable on mobile, not cluttered
  emphasisWords?: string[];
};

const buildPages = (text: string, durationInFrames: number, chunkSize: number) => {
  const words = text.trim().split(/\s+/);
  const n = words.length;
  const wordFrame = (i: number) => Math.round((i / n) * durationInFrames);

  const pages: { start: number; end: number; words: { text: string; start: number; end: number }[] }[] = [];
  for (let i = 0; i < n; i += chunkSize) {
    const chunk = words.slice(i, i + chunkSize);
    const chunkWords = chunk.map((w, j) => ({
      text: w,
      start: wordFrame(i + j),
      end: wordFrame(i + j + 1),
    }));
    pages.push({ start: chunkWords[0].start, end: chunkWords[chunkWords.length - 1].end, words: chunkWords });
  }
  return pages;
};

const normalize = (w: string) => w.toLowerCase().replace(/[.,!?;:]/g, '');

export const CaptionOverlay: React.FC<Props> = ({ text, durationInFrames, chunkSize = 4, emphasisWords = [] }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const pages = React.useMemo(() => buildPages(text, durationInFrames, chunkSize), [text, durationInFrames, chunkSize]);
  const emphasisSet = React.useMemo(() => new Set(emphasisWords.map(normalize)), [emphasisWords]);

  const page = pages.find((p) => frame >= p.start && frame < p.end) ?? pages[pages.length - 1];
  if (!page) return null;

  const pageProgress = spring({ frame: frame - page.start, fps, config: { damping: 200, stiffness: 300 }, durationInFrames: 8 });

  return (
    <div style={{ position: 'absolute', bottom: '14%', left: 0, right: 0, display: 'flex', justifyContent: 'center', padding: '0 8%', opacity: pageProgress, transform: `translateY(${(1 - pageProgress) * 12}px)` }}>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '0.35em', fontFamily: 'Arial Black, Helvetica, sans-serif', fontWeight: 900, fontSize: 56, lineHeight: 1.15, textAlign: 'center' }}>
        {page.words.map((w, i) => {
          const isActive = frame >= w.start && frame < w.end;
          const isEmphasis = emphasisSet.has(normalize(w.text));
          const pop = isActive && isEmphasis ? spring({ frame: frame - w.start, fps, config: { damping: 9, stiffness: 260, mass: 0.5 } }) : 1;
          return (
            <span key={i} style={{
              display: 'inline-block',
              color: isActive ? '#F0C674' : '#FFFFFF', // change #F0C674 to the brand color
              WebkitTextStroke: '2px rgba(0,0,0,0.75)',
              textShadow: isActive && isEmphasis ? '0 0 24px rgba(240,198,116,0.9), 0 3px 10px rgba(0,0,0,0.55)' : '0 3px 10px rgba(0,0,0,0.55)',
              transform: `scale(${isActive && isEmphasis ? 1 + pop * 0.28 : 1})`,
            }}>
              {w.text}
            </span>
          );
        })}
      </div>
    </div>
  );
};
```

**Use in Assembly:** place `<CaptionOverlay>` inside each take's `<Sequence>` (the frame is automatically local 0..durationInFrames thanks to `useCurrentFrame()` inside the Sequence), no manual offset calculation needed.

---

## Component: `TitleCard.tsx` (kinetic title, for hook/reveal lines)

```tsx
import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

type Props = { lines: string[]; durationInFrames: number };

export const TitleCard: React.FC<Props> = ({ lines, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const scale = spring({ frame, fps, config: { damping: 12, stiffness: 180, mass: 0.6 } });
  const fadeOut = interpolate(frame, [durationInFrames - 12, durationInFrames], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <div style={{ position: 'absolute', top: '20%', left: 0, right: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '0 10%', opacity: fadeOut, transform: `scale(${scale})` }}>
      {lines.map((line, i) => (
        <div key={i} style={{
          fontFamily: 'Arial Black, Helvetica, sans-serif', fontWeight: 900,
          fontSize: 104, // big, clearly readable in the mobile feed — 72px was criticized as "too small" in the first review
          lineHeight: 1.08,
          color: '#FFC940', // bright gold — plain white was criticized as "not standing out" in the first review
          textAlign: 'center',
          WebkitTextStroke: '4px rgba(0,0,0,0.9)',
          textShadow: '0 0 30px rgba(255,201,64,0.65), 0 8px 20px rgba(0,0,0,0.65)',
        }}>
          {line}
        </div>
      ))}
    </div>
  );
};
```

**Use in Assembly:** wrap in `<Sequence from={0} durationInFrames={...}>` nested inside the take's Sequence, shown at the start of the take (usually 2.5-3s) then fading out on its own — it does not cover the sub text because `TitleCard` is anchored at `top: 20%` and `CaptionOverlay` at `bottom: 14%`.

---

## Build checklist (add to the render-pipeline.md checklist)

- [ ] The duration used for each take is the **real** number (`durationInFrames` from `scripts/visuals.json` (`post_edit.py plan`) or `npx remotion ffprobe` in the temp project, never `mdls`), not an estimate from the script
- [ ] If the original script has a TEXT overlay column → a `TitleCard` has been built for the correct line, in the correct take
- [ ] Emphasis words (if any) match the spelling in the take's text exactly (matched case-insensitively, punctuation stripped — see the `normalize` function)
- [ ] Play it back with sound and check whether it matches the rhythm — if there is significant drift in sentences with dramatic pauses, switch to Approach 2 (`.words.json`)
- [ ] Colors/sizes follow the real brand colors (do not keep the default `#F0C674`/`#FFC940` if the brand is different) — these 2 colors are examples used for Kreizi Beauty (gold/warm tone), not universal standard colors
