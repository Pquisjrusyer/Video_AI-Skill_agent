import React from 'react';
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import ENDS from './ends.json';

// KREIZI-2026-10-HONEST · UGC Flow 60s · không chữ, không nhạc (user tự thêm)
const f = (s: number) => Math.round(s * 30);
const ORDER = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'] as const;
const ENDCARD = f(3);
const starts: Record<string, number> = {};
let acc = 0;
for (const k of ORDER) { starts[k] = acc; acc += f((ENDS as Record<string, number>)[k]); }
export const SCENES_END = acc;
export const TOTAL = acc + ENDCARD;

const fill: React.CSSProperties = {width: '100%', height: '100%', objectFit: 'cover'};

// B-roll đè hình (giữ giọng của cảnh chính), mốc theo whisper
const BROLL = [
  {scene: 'S4', at: 6.3, dur: 1.3, src: 'clips/actives3d.mp4', from: 2.6},   // "marine extracts"
  {scene: 'S5', at: 2.2, dur: 2.5, src: 'clips/R-01.mov', from: 0.6},        // "locks it in and smooths the surface"
];
const SFX = [
  {at: () => starts.S4 + f(0.6), file: 'sfx-01_soft-swipe', vol: 0.3, dur: 1.5},
  {at: () => starts.S5 + f(2.3), file: 'sfx-01_soft-swipe', vol: 0.25, dur: 1.5},
  {at: () => SCENES_END, file: 'sfx-03_end-chime', vol: 0.5, dur: 1.0},
];

const Fade: React.FC<{len: number; children: React.ReactNode}> = ({len, children}) => {
  const fr = useCurrentFrame();
  const o = interpolate(fr, [0, 4, len - 4, len], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{opacity: o}}>{children}</AbsoluteFill>;
};

const EndCard: React.FC = () => {
  const fr = useCurrentFrame();
  const o = interpolate(fr, [0, 8], [0, 1], {extrapolateRight: 'clamp'});
  const s = interpolate(fr, [0, ENDCARD], [1.0, 1.06]);
  return (
    <AbsoluteFill style={{backgroundColor: '#F3EDE4', opacity: o, justifyContent: 'center', alignItems: 'center'}}>
      <Img src={staticFile('images/duo.png')} style={{width: 1080, height: 1080, objectFit: 'cover', transform: `scale(${s})`}} />
    </AbsoluteFill>
  );
};

export const Assembly: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    {ORDER.map((k) => (
      <Sequence key={k} from={starts[k]} durationInFrames={f((ENDS as Record<string, number>)[k])}>
        <OffthreadVideo src={staticFile(`clips/${k}.mp4`)} style={fill} />
      </Sequence>
    ))}
    {BROLL.map((b) => (
      <Sequence key={b.src} from={starts[b.scene] + f(b.at)} durationInFrames={f(b.dur)}>
        <Fade len={f(b.dur)}><OffthreadVideo src={staticFile(b.src)} startFrom={f(b.from)} muted style={fill} /></Fade>
      </Sequence>
    ))}
    <Sequence from={SCENES_END} durationInFrames={ENDCARD}><EndCard /></Sequence>
    {SFX.map((s, i) => (
      <Sequence key={i} from={s.at()} durationInFrames={f(s.dur)}>
        <Audio src={staticFile(`audio/KREIZI-2026-10-HONEST_${s.file}_v1.mp3`)} volume={s.vol} />
      </Sequence>
    ))}
  </AbsoluteFill>
);
