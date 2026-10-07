// Copy file này vào src/ của bản build Remotion, `import visuals from './visuals.json'`
// (file do `post_edit.py plan --public` sinh ra). Thứ tự lớp trong Assembly để caption
// luôn nằm TRÊN b-roll: (1) map take chỉ render video, (2) <VisualsOverlay visuals={visuals} />,
// (3) map take lần nữa chỉ render CaptionOverlay/TitleCard. Xem ugc-workflow.md Bước 7.
import React from 'react';
import { AbsoluteFill, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

type Broll = { src: string; isImage: boolean; from: number; durationInFrames: number };
type Illustration = { icon: string; label: string; from: number; durationInFrames: number };
export type Visuals = { brolls: Broll[]; illustrations: Illustration[] };

// Fade 7 frame vào/ra: style đã chốt trong ugc-workflow.md Bước 7, không cắt cứng.
const FADE_FRAMES = 7;

const BrollCutaway: React.FC<{ b: Broll }> = ({ b }) => {
  const frame = useCurrentFrame();
  const d = b.durationInFrames;
  const opacity = interpolate(frame, [0, FADE_FRAMES, d - FADE_FRAMES, d], [0, 1, 1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const style = { width: '100%', height: '100%', objectFit: 'cover' as const };
  return (
    <AbsoluteFill style={{ opacity }}>
      {b.isImage ? (
        // Ảnh tĩnh zoom chậm 1.0 -> 1.08 để không bị "đứng hình"
        <Img src={staticFile(b.src)} style={{ ...style, transform: `scale(${interpolate(frame, [0, d], [1, 1.08])})` }} />
      ) : (
        <OffthreadVideo src={staticFile(b.src)} muted style={style} />
      )}
    </AbsoluteFill>
  );
};

const IllustrationPop: React.FC<{ il: Illustration }> = ({ il }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const d = il.durationInFrames;
  const pop = spring({ frame, fps, config: { damping: 12, stiffness: 180 } });
  const exit = interpolate(frame, [d - 6, d], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ alignItems: 'center', top: 380 }}>
      <div
        style={{
          transform: `scale(${pop * exit})`,
          opacity: exit,
          display: 'flex',
          alignItems: 'center',
          gap: 28,
          padding: '28px 48px',
          borderRadius: 40,
          background: 'rgba(255,255,255,0.95)',
          boxShadow: '0 16px 48px rgba(0,0,0,0.35)',
        }}
      >
        <span style={{ fontSize: 110, lineHeight: 1 }}>{il.icon}</span>
        <span style={{ fontSize: 64, fontWeight: 800, color: '#111', fontFamily: 'Arial, sans-serif' }}>{il.label}</span>
      </div>
    </AbsoluteFill>
  );
};

export const VisualsOverlay: React.FC<{ visuals: Visuals }> = ({ visuals }) => (
  <>
    {visuals.brolls.map((b) => (
      <Sequence key={`b-${b.from}`} from={b.from} durationInFrames={b.durationInFrames}>
        <BrollCutaway b={b} />
      </Sequence>
    ))}
    {visuals.illustrations.map((il) => (
      <Sequence key={`i-${il.from}`} from={il.from} durationInFrames={il.durationInFrames}>
        <IllustrationPop il={il} />
      </Sequence>
    ))}
  </>
);
