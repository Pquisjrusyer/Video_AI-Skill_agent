import React from 'react';
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {loadFont} from '@remotion/google-fonts/CormorantGaramond';

const {fontFamily} = loadFont('normal', {weights: ['500', '600'], subsets: ['latin']});
const CODE = 'KREIZI-2026-10-ACTIVES';
const f = (s: number) => Math.round(s * 30);

// Timeline (storyboard.md): S01 0–3.5s · S02 3.5–6.0s · S03 6.0–10.0s
export const TOTAL = f(10);
const S01 = {from: 0, dur: f(3.5)};
const XF = 6; // crossfade S01→S02
const S02 = {from: f(3.5), dur: f(2.5)};
const S03 = {from: f(6), dur: f(4)};
const VO = [
  {file: 'vo-S01', at: 0.3, end: 1.9},
  {file: 'vo-S02', at: 3.8, end: 5.2},
  {file: 'vo-S03', at: 6.2, end: 9.9},
];

const BROWN = '#4A2E22';
// TEXT=false → bản không chữ để user tự chèn chữ (spec: prompts-used/text-overlay-spec.md)
const TEXT = process.env.REMOTION_TEXT !== '0';
// AUDIO=false → bản hình trơn để user tự ghép VO/SFX/nhạc
const AUDIO = process.env.REMOTION_AUDIO !== '0';
const fade = (frame: number, a: number, b: number, c: number, d: number) =>
  interpolate(frame, [a, b, c, d], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

const Rise: React.FC<{delay: number; out?: number; children: React.ReactNode; style?: React.CSSProperties}> = ({delay, out = 9999, children, style}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame: frame - delay, fps, config: {damping: 200}, durationInFrames: 14});
  const o = Math.min(s, interpolate(frame, [out, out + 8], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  return <div style={{opacity: o, transform: `translateY(${(1 - s) * 18}px)`, ...style}}>{children}</div>;
};

// Nhãn tên hiện lần lượt, ngay trên từng quả cầu (vị trí đo từ B-01)
const LABELS = [
  {t: ['Green', 'Seaweed'], x: 155, at: 0.3},
  {t: ['Red', 'Algae'], x: 408, at: 0.7},
  {t: ['Niacinamide'], x: 663, at: 1.1},
  {t: ['Hyaluronic', 'Acid'], x: 925, at: 1.5},
];

const SceneS01: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: '#F4F1EC'}}>
      {/* nguồn 1.0–5.9s, tăng tốc 1.4x để vừa 3.5s */}
      <OffthreadVideo src={staticFile(`clips/${CODE}_S01_actives-to-glass_v1.mp4`)} startFrom={f(1)} playbackRate={1.4} muted
        style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${interpolate(frame, [0, S01.dur + XF], [1, 1.05])})`}} />
      {TEXT && LABELS.map((l) => (
        <Rise key={l.x} delay={f(l.at)} out={f(2.6)}
          style={{position: 'absolute', left: l.x - 135, width: 270, top: 790, textAlign: "center", fontFamily, fontWeight: 600, fontSize: 48, lineHeight: 1.05, color: BROWN}}>
          {l.t.map((w) => <div key={w}>{w}</div>)}
        </Rise>
      ))}
      {TEXT && <Rise delay={f(2.0)} style={{position: 'absolute', top: 250, width: '100%', textAlign: 'center', fontFamily, fontWeight: 500, fontSize: 92, lineHeight: 1.05, color: BROWN}}>
        <div>Four actives.</div>
        <div>One glow.</div>
      </Rise>}
    </AbsoluteFill>
  );
};

const SceneS02: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity: interpolate(frame, [0, XF], [0, 1], {extrapolateRight: 'clamp'})}}>
      {/* nguồn 3.0–5.5s: đầu clip serum đục xanh, không khớp B-03 v3 → bỏ */}
      <OffthreadVideo src={staticFile(`clips/${CODE}_S02_hand-gel-spread_v1.mp4`)} startFrom={f(3)} muted
        style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      {TEXT && <Rise delay={f(0.3)} style={{position: 'absolute', bottom: 230, left: 90, right: 90, padding: '30px 36px', borderRadius: 28,
        backgroundColor: 'rgba(250,246,240,0.86)', textAlign: 'center', fontFamily, color: BROWN}}>
        <div style={{fontSize: 40, fontWeight: 600, letterSpacing: 2, textTransform: 'uppercase'}}>Hyaluronic Acid</div>
        <div style={{fontSize: 54, fontWeight: 500, lineHeight: 1.1, marginTop: 8}}>Holds up to 1,000x its weight in water</div>
      </Rise>}
    </AbsoluteFill>
  );
};

const SceneS03: React.FC = () => {
  const frame = useCurrentFrame();
  const shadow = '0 2px 18px rgba(0,30,40,0.55)';
  return (
    <AbsoluteFill style={{backgroundColor: '#0B2B30'}}>
      {/* Clip Veo S03 v2: user sửa label (v1 sai INPUSED / ALGAIE / 50 mL), QC chữ đúng 2026-10-02 */}
      <OffthreadVideo src={staticFile(`clips/${CODE}_S03_serum-underwater_v2.mov`)} muted
        style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      {TEXT && <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(5,30,36,0.55) 0%, rgba(5,30,36,0) 28%)'}} />}
      {TEXT && <div style={{position: 'absolute', top: 120, width: '100%', textAlign: 'center', fontFamily, color: '#FFFFFF', textShadow: shadow}}>
        <Rise delay={f(0.6)}><div style={{fontSize: 74, fontWeight: 600, lineHeight: 1.05}}>Luminous Glass Skin Serum</div></Rise>
        <Rise delay={f(1.2)}><div style={{fontSize: 48, fontWeight: 500, marginTop: 14}}>Designed for skin 40+</div></Rise>
        <Rise delay={f(2.0)}><div style={{fontSize: 34, fontWeight: 600, letterSpacing: 12, marginTop: 26}}>KREIZI BEAUTY</div></Rise>
      </div>}
    </AbsoluteFill>
  );
};

export const Assembly: React.FC = () => {
  const frame = useCurrentFrame();
  // Nhạc duck dưới VO, fade cuối video
  let music = 0.42;
  for (const v of VO) {
    music = Math.min(music, interpolate(frame, [f(v.at) - 8, f(v.at), f(v.end), f(v.end) + 10], [0.42, 0.13, 0.13, 0.42], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  }
  music *= interpolate(frame, [f(9.5), TOTAL], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <Sequence from={S01.from} durationInFrames={S01.dur + XF}><SceneS01 /></Sequence>
      <Sequence from={S02.from} durationInFrames={S02.dur}><SceneS02 /></Sequence>
      <Sequence from={S03.from} durationInFrames={S03.dur}><SceneS03 /></Sequence>
      {AUDIO && <>
      <Audio src={staticFile(`audio/${CODE}_music_v1.mp3`)} volume={music} />
      {/* SFX: 4 tiếng pop khi quả cầu chạm da · giọt serum đầu S02 · whoosh lúc cut S03 */}
      {[1.05, 1.2, 1.35, 1.5].map((t, i) => (
        <Sequence key={t} from={f(t)} durationInFrames={f(0.5)}><Audio src={staticFile(`audio/${CODE}_sfx-01_bubble-pop_v1.mp3`)} volume={[0.55, 0.45, 0.5, 0.42][i]} /></Sequence>
      ))}
      <Sequence from={f(3.45)} durationInFrames={f(0.8)}><Audio src={staticFile(`audio/${CODE}_sfx-02_droplet_v1.mp3`)} startFrom={f(1.4)} volume={0.9} /></Sequence>
      <Sequence from={f(5.95)} durationInFrames={f(0.5)}><Audio src={staticFile(`audio/${CODE}_sfx-03_underwater-whoosh_v1.mp3`)} volume={0.6} /></Sequence>
      {VO.map((v) => (
        <Sequence key={v.file} from={f(v.at)}><Audio src={staticFile(`audio/${CODE}_${v.file}_v1.mp3`)} /></Sequence>
      ))}
      </>}
    </AbsoluteFill>
  );
};
