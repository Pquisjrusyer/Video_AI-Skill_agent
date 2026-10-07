// Render 1 lần đóng gói (bundle) → nhiều khung xem trước / video. Gọi qua `python3 _tools/remotion.py`, không gọi tay.
//   node render.mjs --entry <src/index.ts> --public <campaign/outputs> --props <timeline.json> --mode stills|video --out <file|dir>
//                   [--size 1080x1350] (bản phụ khác tỷ lệ)
import {bundle} from '@remotion/bundler';
import {renderMedia, renderStill, selectComposition} from '@remotion/renderer';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const arg = (k, d) => { const i = process.argv.indexOf(`--${k}`); return i > 0 ? process.argv[i + 1] : d; };
const entry = arg('entry'), publicDir = arg('public'), propsFile = arg('props'), mode = arg('mode', 'video'), out = arg('out');
const props = JSON.parse(fs.readFileSync(propsFile, 'utf8'));
const size = arg('size');
if (size) { const [w, h] = size.split('x').map(Number); props.width = w; props.height = h; }
const t0 = Date.now(); const log = (m) => console.log(`[${((Date.now() - t0) / 1000).toFixed(1)}s] ${m}`);

const RX = /^remotion-(v[\d.]+-assets|webpack-bundle-)/;
const before = new Set(fs.readdirSync(os.tmpdir()).filter((n) => RX.test(n)));   // rác có sẵn trước lần render này
let last = -1;
const serveUrl = await bundle({entryPoint: entry, publicDir, onProgress: (p) => { if (p - last >= 25) { last = p; log(`đóng gói ${p}%`); } }});
try {
  const composition = await selectComposition({serveUrl, id: 'Main', inputProps: props});
  log(`khung ${composition.width}×${composition.height} · ${composition.fps}fps · ${(composition.durationInFrames / composition.fps).toFixed(2)}s`);
  if (mode === 'stills') {
    fs.mkdirSync(out, {recursive: true});
    let cursor = 0; const done = [];
    for (const s of props.scenes) {                       // 1 khung giữa mỗi cảnh — dùng chung 1 bundle
      const frame = Math.min(composition.durationInFrames - 1, Math.round((cursor + s.duration / 2) * composition.fps));
      cursor += s.duration;
      const file = path.join(out, `${s.id}.png`);
      await renderStill({composition, serveUrl, output: file, frame, inputProps: props});
      done.push({id: s.id, frame, file});
    }
    fs.writeFileSync(path.join(out, 'stills.json'), JSON.stringify(done, null, 2));
    log(`xong ${done.length} khung xem trước → ${out}`);
  } else {
    let pct = -1;
    await renderMedia({composition, serveUrl, codec: 'h264', outputLocation: out, inputProps: props, crf: 18,
      onProgress: ({progress}) => { const p = Math.floor(progress * 10) * 10; if (p > pct) { pct = p; log(`render ${p}%`); } }});
    log(`xong video → ${out}`);
  }
} finally {
  fs.rmSync(serveUrl.replace(/^file:\/\//, ''), {recursive: true, force: true});
  // Dọn rác Remotion trong Temp: thư mục do CHÍNH lần render này tạo + thư mục cũ hơn 1 giờ (không đụng lần render khác đang chạy)
  const tmp = os.tmpdir(); const old = Date.now() - 3600e3;
  for (const n of fs.readdirSync(tmp)) {
    if (!RX.test(n)) continue;
    const p = path.join(tmp, n);
    try { if (!before.has(n) || fs.statSync(p).mtimeMs < old) fs.rmSync(p, {recursive: true, force: true}); } catch {}
  }
}
