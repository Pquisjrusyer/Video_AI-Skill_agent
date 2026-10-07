# Remotion — Scene Templates (đã test, sẵn dùng)

Khác với `_skills/motion-graphic/references/animation-patterns.md` (pattern atomic — 1 hiệu ứng), file này là TEMPLATE SCENE HOÀN CHỈNH — ghép nhiều pattern lại thành 1 scene sẵn dùng cho các loại scene phổ biến trong ad. Copy, đổi asset/text, dùng ngay.

Component dùng chung dạng file `.tsx` (không phải template trong file này): `components/VisualsOverlay.tsx`, b-roll cutaway + card minh hoạ chạy theo `visuals.json` (xem `_workflows/ugc-workflow.md` Bước 7).

---

## Template 1 — Hero Product Reveal (Ken Burns + text entrance)

Dùng cho: scene mở đầu hoặc scene giới thiệu sản phẩm, ảnh tĩnh hero shot.

```tsx
import { Img, interpolate, spring, useCurrentFrame, useVideoConfig, staticFile } from 'remotion';

export const HeroProductReveal: React.FC<{imgSrc: string; headline: string}> = ({imgSrc, headline}) => {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();

  const scale = interpolate(frame, [0, durationInFrames], [1, 1.12]);
  const textScale = spring({frame: frame - 10, fps, config: {damping: 12}});

  return (
    <div style={{width: '100%', height: '100%', position: 'relative'}}>
      <Img src={staticFile(imgSrc)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${scale})`}} />
      <div style={{
        position: 'absolute', bottom: '12%', left: 0, right: 0, textAlign: 'center',
        transform: `scale(${textScale})`, opacity: textScale,
      }}>
        <span style={{color: 'white', fontSize: 56, fontWeight: 700, textShadow: '0 2px 8px rgba(0,0,0,0.5)'}}>
          {headline}
        </span>
      </div>
    </div>
  );
};
```

## Template 2 — Quote / Testimonial Card (không phải video người thật)

Dùng cho: khi muốn dẫn 1 câu quote khách hàng dạng graphic thay vì quay video người nói.

```tsx
import { useCurrentFrame } from 'remotion';

export const QuoteCard: React.FC<{quote: string; author: string}> = ({quote, author}) => {
  const frame = useCurrentFrame();
  const visibleChars = Math.floor(frame * 0.9);
  const displayText = quote.slice(0, visibleChars);

  return (
    <div style={{
      width: '100%', height: '100%', display: 'flex', flexDirection: 'column',
      justifyContent: 'center', alignItems: 'center', padding: '10%',
      background: '#faf7f2', // đổi theo brand-brief.md
    }}>
      <span style={{fontSize: 44, fontStyle: 'italic', textAlign: 'center', lineHeight: 1.4}}>
        "{displayText}"
      </span>
      {visibleChars >= quote.length && (
        <span style={{marginTop: 24, fontSize: 28, fontWeight: 600, opacity: 0.7}}>— {author}</span>
      )}
    </div>
  );
};
```

## Template 3 — Before / After Compare

Dùng cho: scene so sánh kết quả, dùng 2 ảnh tĩnh.

```tsx
import { Img, interpolate, useCurrentFrame, staticFile } from 'remotion';

export const BeforeAfter: React.FC<{beforeSrc: string; afterSrc: string}> = ({beforeSrc, afterSrc}) => {
  const frame = useCurrentFrame();
  const wipeX = interpolate(frame, [30, 90], [0, 100], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

  return (
    <div style={{width: '100%', height: '100%', position: 'relative'}}>
      <Img src={staticFile(beforeSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      <div style={{position: 'absolute', top: 0, left: 0, width: `${wipeX}%`, height: '100%', overflow: 'hidden'}}>
        <Img src={staticFile(afterSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      </div>
      <div style={{position: 'absolute', top: 20, left: 20, color: 'white', fontWeight: 700, fontSize: 32}}>BEFORE</div>
      <div style={{position: 'absolute', top: 20, right: 20, color: 'white', fontWeight: 700, fontSize: 32}}>AFTER</div>
    </div>
  );
};
```

## Template 4 — CTA End Card

Dùng cho: scene cuối cùng của mọi video (đóng ad).

```tsx
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const CTAEndCard: React.FC<{ctaText: string; logoSrc: string}> = ({ctaText, logoSrc}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pulse = spring({frame, fps, config: {damping: 8, stiffness: 100}});

  return (
    <div style={{
      width: '100%', height: '100%', display: 'flex', flexDirection: 'column',
      justifyContent: 'center', alignItems: 'center', gap: 32,
    }}>
      <img src={logoSrc} style={{width: 120}} />
      <div style={{
        padding: '16px 48px', background: '#000', borderRadius: 999,
        transform: `scale(${1 + Math.sin(frame / 10) * 0.03 * pulse})`,
      }}>
        <span style={{color: 'white', fontSize: 36, fontWeight: 700}}>{ctaText}</span>
      </div>
    </div>
  );
};
```

---

## Ghi chú khi dùng lại

- Đổi màu/font trong mọi template theo `_brand/<brand>/brand-assets/` — không giữ giá trị mặc định (`#faf7f2`, `#000`...) nếu brand có palette riêng
- Log lại version đã dùng + kết quả (worked/needs adjustment) vào `campaigns/[campaign]/prompts-used/` sau mỗi lần dùng, giống quy tắc với prompt Veo3/Nano Banana
