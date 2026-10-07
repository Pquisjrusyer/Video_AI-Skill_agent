// Khung dựng dùng chung — mọi campaign chỉ thay timeline.json (schema: _skills/motion-graphic/references/remotion-setup.md).
// File media đọc từ thư mục outputs/ của campaign (publicDir) → src trong timeline viết dạng "videos/x.mp4", "audio/vo-S01.mp3".
import React from 'react';
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {loadFont as loadMontserrat} from '@remotion/google-fonts/Montserrat';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';
import {loadFont as loadBeVietnamPro} from '@remotion/google-fonts/BeVietnamPro';

export type TextItem = {
  text: string; from?: number; to?: number;                 // giây, tính từ đầu cảnh
  pos?: 'top' | 'center' | 'bottom' | 'lowerThird';
  size?: number; weight?: number; color?: string; bg?: string; align?: 'left' | 'center' | 'right';
};
export type Scene = {
  id: string; type: 'clip' | 'image' | 'endcard'; duration: number;
  src?: string; trimStart?: number; keepAudio?: boolean;    // clip: bỏ qua bao nhiêu giây đầu, giữ tiếng gốc (UGC)
  zoom?: [number, number]; scale?: number; position?: string; // scale > 1 để cắt bớt mép (VD giấu watermark)
  bg?: string; logo?: string; logoWidth?: number;            // endcard
  texts?: TextItem[]; transition?: 'cut' | 'fade';
};
export type Timeline = {
  fps?: number; width?: number; height?: number;
  safe?: {top: number; bottom: number; left: number; right: number};   // % — lấy từ _tools/platforms.json
  font?: 'Montserrat' | 'Inter' | 'BeVietnamPro'; accent?: string; textColor?: string;
  scenes: Scene[];
  audio?: {
    vo?: {src: string; at: number; dur?: number; volume?: number}[];
    music?: {src: string; volume?: number; duck?: number; fadeOut?: number};
    sfx?: {src: string; at: number; volume?: number}[];
  };
};

const FONTS = {Montserrat: loadMontserrat, Inter: loadInter, BeVietnamPro: loadBeVietnamPro};
// Chỉ tải độ đậm + bộ chữ cần (có tiếng Việt) — tải đủ mọi weight làm mỗi khung chờ 45–90 request.
const loaded: Record<string, string> = {};
const familyOf = (name?: Timeline['font']) => {
  if (!name || !FONTS[name]) return 'system-ui, sans-serif';
  if (!loaded[name]) loaded[name] = FONTS[name]('normal', {weights: ['600', '700', '800'], subsets: ['latin', 'latin-ext', 'vietnamese'],
    ignoreTooManyRequestsWarning: true} as never).fontFamily;
  return loaded[name];
};
export const totalSeconds = (t: Timeline) => (t.scenes || []).reduce((s, x) => s + (x.duration || 0), 0);

const Txt: React.FC<{t: TextItem; tl: Timeline; family: string}> = ({t, tl, family}) => {
  const frame = useCurrentFrame(); const {fps, height} = useVideoConfig();
  const safe = tl.safe || {top: 14, bottom: 35, left: 6, right: 6};
  const a = Math.round((t.from || 0) * fps);
  const op = interpolate(frame, [a, a + 6], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const y = interpolate(frame, [a, a + 8], [18, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const pos = t.pos || 'top';
  const v: React.CSSProperties = pos === 'top' ? {top: `${safe.top + 2}%`} : pos === 'bottom' ? {bottom: `${safe.bottom + 2}%`}
    : pos === 'lowerThird' ? {top: '58%'} : {top: '50%', transform: `translateY(-50%) translateY(${y}px)`};
  return (
    <div style={{position: 'absolute', left: `${safe.left + 2}%`, right: `${safe.right + 2}%`, ...v, opacity: op,
      transform: v.transform || `translateY(${y}px)`, textAlign: t.align || 'center'}}>
      <span style={{fontFamily: family, fontSize: t.size || Math.round(height * 0.042), fontWeight: t.weight || 800,
        color: t.color || tl.textColor || '#fff', lineHeight: 1.15, letterSpacing: '-0.01em', whiteSpace: 'pre-wrap',
        background: t.bg, padding: t.bg ? '0.15em 0.45em' : 0, borderRadius: 14,
        textShadow: t.bg ? 'none' : '0 1px 3px rgba(0,0,0,.55), 0 4px 22px rgba(0,0,0,.5)', boxDecorationBreak: 'clone', WebkitBoxDecorationBreak: 'clone'}}>
        {t.text}
      </span>
    </div>
  );
};

const SceneView: React.FC<{s: Scene; tl: Timeline; family: string}> = ({s, tl, family}) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const dur = Math.round(s.duration * fps);
  const [z0, z1] = s.zoom || (s.type === 'image' ? [1, 1.06] : [1, 1]);
  const z = interpolate(frame, [0, dur], [z0, z1], {extrapolateRight: 'clamp'}) * (s.scale || 1);
  const fade = s.transition === 'fade' ? interpolate(frame, [0, 8], [0, 1], {extrapolateRight: 'clamp'}) : 1;
  const media: React.CSSProperties = {width: '100%', height: '100%', objectFit: 'cover', objectPosition: s.position || '50% 50%',
    transform: `scale(${z})`};
  return (
    <AbsoluteFill style={{backgroundColor: s.bg || '#000', opacity: fade}}>
      {s.type === 'clip' && s.src && (
        <OffthreadVideo src={staticFile(s.src)} startFrom={Math.round((s.trimStart || 0) * fps)} muted={!s.keepAudio} style={media} />
      )}
      {s.type === 'image' && s.src && <Img src={staticFile(s.src)} style={media} />}
      {s.type === 'endcard' && (
        <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
          {s.src && <Img src={staticFile(s.src)} style={{...media, objectFit: 'contain'}} />}
          {s.logo && <Img src={staticFile(s.logo)} style={{position: 'absolute', top: `${(tl.safe?.top ?? 14) + 2}%`, width: s.logoWidth || '38%'}} />}
        </AbsoluteFill>
      )}
      {(s.texts || []).map((t, i) => {
        const from = Math.round((t.from || 0) * fps); const to = t.to != null ? Math.round(t.to * fps) : dur;
        return <Sequence key={i} from={from} durationInFrames={Math.max(1, to - from)} layout="none"><Txt t={{...t, from: 0}} tl={tl} family={family} /></Sequence>;
      })}
    </AbsoluteFill>
  );
};

export const Main: React.FC<Timeline> = (tl) => {
  const {fps, durationInFrames} = useVideoConfig();
  const family = familyOf(tl.font);
  let cursor = 0;
  const vo = tl.audio?.vo || [];
  const music = tl.audio?.music;
  const musicVol = (f: number) => {
    const t = f / fps; const base = music?.volume ?? 0.25;
    const talking = vo.some((v) => t >= v.at - 0.15 && t <= v.at + (v.dur ?? 3) + 0.15);
    const fadeOut = music?.fadeOut ?? 1;
    const tail = interpolate(f, [durationInFrames - fadeOut * fps, durationInFrames], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
    return (talking ? music?.duck ?? 0.1 : base) * tail;
  };
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {tl.scenes.map((s) => {
        const from = Math.round(cursor * fps); cursor += s.duration;
        return <Sequence key={s.id} from={from} durationInFrames={Math.max(1, Math.round(s.duration * fps))}><SceneView s={s} tl={tl} family={family} /></Sequence>;
      })}
      {music && <Audio src={staticFile(music.src)} volume={musicVol} />}
      {vo.map((v, i) => <Sequence key={`vo${i}`} from={Math.round(v.at * fps)} layout="none"><Audio src={staticFile(v.src)} volume={v.volume ?? 1} /></Sequence>)}
      {(tl.audio?.sfx || []).map((x, i) => <Sequence key={`sfx${i}`} from={Math.round(x.at * fps)} layout="none"><Audio src={staticFile(x.src)} volume={x.volume ?? 0.7} /></Sequence>)}
    </AbsoluteFill>
  );
};
