import { AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { loadFont } from '@remotion/google-fonts/Montserrat';

const { fontFamily } = loadFont('normal', { weights: ['600', '800'], subsets: ['latin'] });
const INK = '#151515';
const s = (sec: number) => Math.round(sec * 30);

// Timeline theo storyboard.md (giây)
const T = { s01: [0, 3.0], s02: [3.0, 6.5], s03: [6.5, 8.5], s04: [8.5, 10.0] } as const;
export const TOTAL = s(10.0);

// Mọi chữ hiện bằng fade + trượt nhẹ lên
const Rise: React.FC<{ at: number; children: React.ReactNode; style?: React.CSSProperties }> = ({ at, children, style }) => {
  const f = useCurrentFrame() - at;
  const o = interpolate(f, [0, 6], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const y = interpolate(f, [0, 8], [24, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return <div style={{ width: '100%', opacity: o, transform: `translateY(${y}px)`, ...style }}>{children}</div>;
};

const text = (size: number, color: string, weight = 800): React.CSSProperties => ({
  fontFamily, fontSize: size, fontWeight: weight, color, textAlign: 'center', lineHeight: 1.15, letterSpacing: -0.5,
});

// Clip Veo 720p + watermark ✦ góc dưới phải → phóng 1.18 neo mép trên (cắt ~15% đáy)
const VeoClip: React.FC<{ file: string; startFromSec?: number; originX?: string }> = ({ file, startFromSec = 0, originX = '50%' }) => (
  <AbsoluteFill style={{ transform: 'scale(1.18)', transformOrigin: `${originX} 0%` }}>
    <OffthreadVideo src={staticFile(`clips/${file}`)} startFrom={s(startFromSec)} muted style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
  </AbsoluteFill>
);

const S01: React.FC = () => (
  <AbsoluteFill>
    <VeoClip file="KOLOR-2026-10-STUDIO_S01_dot-bloom_v1.mp4" />
    <AbsoluteFill style={{ top: 200, height: 260 }}>
      <Sequence durationInFrames={s(1.2)}><Rise at={0} style={text(110, INK)}>One dot.</Rise></Sequence>
      <Sequence from={s(1.2)}><Rise at={0} style={text(110, INK)}>Watch it bloom.</Rise></Sequence>
    </AbsoluteFill>
  </AbsoluteFill>
);

const S02: React.FC = () => (
  <AbsoluteFill>
    <VeoClip file="KOLOR-2026-10-STUDIO_S02_nia-bottle_v1.mp4" startFromSec={0.3} originX="15%" />
    <AbsoluteFill style={{ top: 1560, padding: '0 90px' }}>
      <Rise at={4} style={{ ...text(60, '#FFFFFF'), textShadow: '0 2px 18px rgba(0,0,0,0.45)' }}>
        Colors disperse into organic patterns in seconds.
      </Rise>
    </AbsoluteFill>
  </AbsoluteFill>
);

// Ảnh tĩnh: móng nằm ở ~20–44% chiều cao ảnh → phóng neo vào vùng móng, push-in chậm
const S03: React.FC = () => {
  const f = useCurrentFrame();
  const z = interpolate(f, [0, s(2)], [1.18, 1.26]);
  const words = ['Florals', 'Marble', 'Snake print', 'Watercolor'];
  return (
    <AbsoluteFill style={{ backgroundColor: '#E9E9EB' }}>
      <AbsoluteFill style={{ transform: `scale(${z})`, transformOrigin: '45% 25%' }}>
        <Img src={staticFile('images/b03.png')} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
      </AbsoluteFill>
      <AbsoluteFill style={{ top: 1330, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
        {words.map((w, i) => (
          <Rise key={w} at={i * s(0.4)} style={{ ...text(78, '#FFFFFF'), textShadow: '0 2px 16px rgba(0,0,0,0.4)' }}>{w}</Rise>
        ))}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const S04: React.FC = () => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const k = spring({ frame: f, fps, config: { damping: 200 } });
  return (
    <AbsoluteFill style={{ backgroundColor: '#F5F5F5', alignItems: 'center' }}>
      <Img src={staticFile('images/packshot.jpg')} style={{ width: 1080, marginTop: 120, transform: `scale(${0.96 + 0.04 * k})` }} />
      <div style={{ position: 'absolute', top: 1230, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 22 }}>
        <Rise at={2} style={text(84, INK)}>Kolor Blooming Gel</Rise>
        <Rise at={6} style={{ ...text(40, '#5A5A5A', 600), letterSpacing: 2 }}>EVEN BLOOMING · LONG LASTING</Rise>
        <Rise at={10} style={{ marginTop: 26, display: 'flex', justifyContent: 'center' }}>
          <span style={{ background: INK, color: '#fff', fontFamily, fontWeight: 800, fontSize: 46, padding: '24px 74px', borderRadius: 999 }}>Shop now</span>
        </Rise>
      </div>
    </AbsoluteFill>
  );
};

const scenes = [[S01, T.s01], [S02, T.s02], [S03, T.s03], [S04, T.s04]] as const;

// Nhạc m1 (ElevenLabs): beat vào ở 3.5s của track → bắt đầu từ 0.5s để rơi đúng cut S02 (3.0s)
const MUSIC_OFFSET = s(0.5);
const musicVolume = (f: number) => interpolate(f, [0, 4, TOTAL - 9, TOTAL], [0, 1, 1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

// SFX (ElevenLabs, đã chọn take b): at = mốc trên timeline, from = điểm bắt đầu trong file, len = độ dài dùng
const SFX = [
  { file: 'bloom_b.mp3', at: 0.4, from: 0, len: 1.6, vol: 0.9 },   // peak 0.7s trong file → ~1.1s, lúc màu nở
  { file: 'click_b.mp3', at: 4.8, from: 1.25, len: 0.3, vol: 0.6 }, // Nia nghiêng chai
  ...[0, 1, 2, 3].map((i) => ({ file: 'tick_b.mp3', at: 6.5 + i * 0.4, from: 0, len: 0.25, vol: 0.5 })), // 4 chữ S03
  { file: 'pop_b.mp3', at: 8.5, from: 0, len: 0.4, vol: 0.6 },     // end card
];

export const Assembly: React.FC = () => (
  <AbsoluteFill style={{ backgroundColor: '#000' }}>
    <Audio src={staticFile('audio/music.mp3')} startFrom={MUSIC_OFFSET} volume={musicVolume} />
    {SFX.map((x) => (
      <Sequence key={x.file + x.at} from={s(x.at)} durationInFrames={s(x.len)}>
        <Audio src={staticFile(`audio/${x.file}`)} startFrom={s(x.from)} volume={(f) => x.vol * interpolate(f, [s(x.len) - 3, s(x.len)], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })} />
      </Sequence>
    ))}
    {scenes.map(([C, [a, b]], i) => (
      <Sequence key={i} from={s(a)} durationInFrames={s(b) - s(a)}><C /></Sequence>
    ))}
  </AbsoluteFill>
);
