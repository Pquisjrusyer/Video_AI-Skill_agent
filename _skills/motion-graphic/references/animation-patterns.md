# Animation Patterns — Remotion

Catalog of reusable patterns. Each pattern is 1 small component, combined according to the storyboard. Copy the matching pattern; do not rewrite from scratch every time.

---

## 1. Ken Burns (zoom/pan on a static image)

```tsx
import { Img, interpolate, useCurrentFrame, useVideoConfig, staticFile } from 'remotion';

export const KenBurns: React.FC<{src: string}> = ({src}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const scale = interpolate(frame, [0, durationInFrames], [1, 1.15]);
  const translateX = interpolate(frame, [0, durationInFrames], [0, -30]);

  return (
    <Img
      src={staticFile(src)}
      style={{
        width: '100%', height: '100%', objectFit: 'cover',
        transform: `scale(${scale}) translateX(${translateX}px)`,
      }}
    />
  );
};
```

Use for: hero shot scenes, product zoom, lifestyle backgrounds.

## 2. Spring entrance (text/logo pop-in)

```tsx
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

const frame = useCurrentFrame();
const {fps} = useVideoConfig();
const scale = spring({frame, fps, config: {damping: 12, stiffness: 200}});

<div style={{transform: `scale(${scale})`, opacity: scale}}>
  {children}
</div>
```

Use for: headline appearing, logo reveal, badge/offer callout.

## 3. Typewriter text

```tsx
const frame = useCurrentFrame();
const charsPerFrame = 0.8;
const visibleChars = Math.floor(frame * charsPerFrame);
const displayText = fullText.slice(0, visibleChars);
```

Use for: text-based testimonial quote cards (not videos of a person speaking), lead-in captions.

## 4. Transition between scenes (crossfade)

```tsx
import { Sequence, interpolate, useCurrentFrame } from 'remotion';

const TRANSITION_FRAMES = 15;

const CrossfadeOut: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame,
    [durationInFrames - TRANSITION_FRAMES, durationInFrames],
    [1, 0]
  );
  return <div style={{opacity}}>{children}</div>;
};
```

Use in Assembly.tsx when moving from this scene to another. The transition type (crossfade/wipe/hard cut) comes from the "Assembly notes" in storyboard.md.

## 5. Number count-up (price, %, stat)

```tsx
const frame = useCurrentFrame();
const value = Math.round(interpolate(frame, [0, 60], [0, targetNumber], {
  extrapolateRight: 'clamp',
}));
```

Use for: before/after %, sale price countdown, customer stats.

## 6. Lower-third text bar

```tsx
<div style={{
  position: 'absolute', bottom: '15%', left: 0, right: 0,
  background: 'linear-gradient(transparent, rgba(0,0,0,0.6))',
  padding: '20px', textAlign: 'center',
}}>
  <span style={{color: 'white', fontWeight: 'bold', fontSize: 48}}>{text}</span>
</div>
```

Use for: headline/CTA overlay on images/clips, keeping the exact font/colors from `_brand/<brand>/brand-assets/`.

## 7. Parallax layer (separate background + foreground layers)

```tsx
const bgTranslate = interpolate(frame, [0, durationInFrames], [0, -20]);
const fgTranslate = interpolate(frame, [0, durationInFrames], [0, -60]);
// background moves slower than foreground → creates fake depth
```

Use for: lifestyle scenes with multiple layers (background + separately cut-out product).

---

## General principles when applying patterns

- Timing is always calculated in frames (frame = seconds × fps); do not hardcode seconds in animation logic
- Every animation should have easing (use `spring` or `interpolate` with `easing`); avoid rigid linear motion unless intentional
- Keep animation speed/bounciness consistent across scenes within the same video — reference 1 shared `theme.ts` file for spring config, colors, and fonts if the video has ≥3 motion-graphic scenes
