# Remotion — Setup & Project Structure

## What Remotion is (reminder so there is no confusion)

Remotion (remotion.dev) is a framework for writing videos in React/TypeScript. It does not generate motion from static images like an AI video model — it renders each frame with code, based on time (frame number), like After Effects but with code instead of a drag-and-drop timeline.

## Initializing the project

Each campaign that uses motion-graphic has its own `remotion-project/` folder (sibling to `scripts/`, `prompts-used/`, `outputs/`) — but this is only where the final SOURCE CODE is stored, not where npm is installed/run.

> **IMPORTANT — do not skip:** Do NOT run `npm install` directly in `campaigns/[campaign]/remotion-project/` (this directory syncs with the user's machine). Verified in practice: `node_modules` contains thousands of small files, and this synced filesystem refuses to delete them (`Operation not permitted`) after installation, leaving junk that cannot be cleaned up. Always follow the 2-step process:
>
> 1. **Build & render in a temp directory** (e.g. `/tmp/[campaign-slug]-remotion`) — run `npm install`, write code, and render here.
> 2. **Sync only the source back to `remotion-project/`** — copy `package.json`, `package-lock.json`, `src/`, do NOT copy `node_modules/`. Copy review renders into `outputs/review/` and the final into `outputs/final/`. `remotion-project/` always exists after `/edit`.

```bash
mkdir -p /tmp/[campaign-slug]-remotion/src/scenes /tmp/[campaign-slug]-remotion/public/{images,clips,audio}
cd /tmp/[campaign-slug]-remotion
npm install remotion @remotion/cli
# add @remotion/transitions if the assembly needs crossfade/wipe between scenes
# copy approved assets into public/ (at /edit) — STUDIO = the AI Studio project root
cp "$STUDIO/campaigns/[campaign]/outputs/images/"* public/images/
cp "$STUDIO/campaigns/[campaign]/outputs/videos/"* public/clips/
cp "$STUDIO/campaigns/[campaign]/outputs/audio/"* public/audio/
```

After rendering is done and reviewed:
```bash
# Copy the video into the campaign (real path in AI Studio)
cp out/final.mp4 "campaigns/[campaign]/outputs/final/[campaign-code]_[format]_[character]_[product]_[ratio]_v[version].mp4"   # e.g. 2026-06-LAUNCH_motiongraphic_hero-quote-cta_9x16_v1.mp4
# Sync source code (NOT node_modules) back to remotion-project/ to keep it for later edits/re-renders
cp package.json package-lock.json "campaigns/[campaign]/remotion-project/"
cp -r src "campaigns/[campaign]/remotion-project/"
```

## File structure in `remotion-project/`

```
remotion-project/
├── package.json
├── remotion.config.ts        shared config (fps, codec...)
├── public/                   (temp project only) copied from outputs/images, outputs/videos, outputs/audio
│   ├── images/
│   ├── clips/
│   └── audio/
└── src/
    ├── Root.tsx               registers every Composition (each scene + the final assembly)
    ├── scenes/
    │   ├── Scene1KenBurns.tsx
    │   ├── Scene2TextOverlay.tsx
    │   └── ...
    └── Assembly.tsx           composition that assembles all scenes per storyboard.md
```

## Registering Compositions (Root.tsx)

```tsx
import { Composition } from 'remotion';
import { Scene1KenBurns } from './scenes/Scene1KenBurns';
import { Assembly } from './Assembly';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Scene1KenBurns"
        component={Scene1KenBurns}
        durationInFrames={90}   // 3s @ 30fps
        fps={30}
        width={1080}
        height={1920}           // 9:16
      />
      <Composition
        id="FinalAssembly"
        component={Assembly}
        durationInFrames={450}  // total video duration, calculated from the storyboard
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
```

## Importing assets from the campaign

Copy generated images (Nano Banana/GPT Image) from `campaigns/[campaign]/outputs/images/` into `remotion-project/public/images/`. Copy rendered AI-VIDEO clips from `outputs/videos/` into `remotion-project/public/clips/`. In code, use `staticFile()`:

```tsx
import { staticFile } from 'remotion';
const imgSrc = staticFile('images/hero-shot.jpg');
const clipSrc = staticFile('clips/testimonial-sarah-scene1.mp4');
```

Do not import images/clips directly from `outputs/` via a relative path outside `remotion-project/` — Remotion can only serve assets inside `public/`.

## Minimum TypeScript/React knowledge needed

- `useCurrentFrame()` — gets the current frame to compute animation over time
- `useVideoConfig()` — gets fps/width/height/durationInFrames
- `interpolate(frame, [inputRange], [outputRange])` — maps a frame to an animated value (opacity, scale, translate)
- `spring({frame, fps, config})` — animation with natural easing (used for entrance/pop-in)
- `<Sequence from={} durationInFrames={}>` — places a child segment at the right time position in the parent composition (used for assembly)
- `<OffthreadVideo src={}>` — imports and renders an existing video clip into the composition (unlike `<Video>`, it renders more accurately for export)
