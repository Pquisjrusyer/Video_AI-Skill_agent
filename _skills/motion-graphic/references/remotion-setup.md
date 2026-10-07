# Remotion — Setup & dựng (bộ dùng chung cả máy)

## What Remotion is

Remotion (remotion.dev) renders video from React code, frame by frame. It does not animate still images like an AI video model.

## ⚡ Cách dựng chuẩn — KHÔNG `npm install` mỗi campaign

Bộ Remotion **dùng chung cả máy**, cài 1 lần ở `~/.config/ai-studio/remotion-base/` (ngoài dự án / Drive / git; phiên bản khoá ở `_tools/remotion-base/package.json` + `package-lock.json`). Khung dựng sẵn `_tools/remotion-base/src/` đọc **dữ liệu** `timeline.json` — Claude **chỉ viết timeline.json**, không viết lại Root / Assembly / scenes.

```bash
python3 _tools/remotion.py check   campaigns/<c>     # kiểm timeline + đủ file trong outputs/ (vài giây, không render)
python3 _tools/remotion.py stills  campaigns/<c>     # 1 khung giữa mỗi cảnh + ảnh ghép outputs/review/<code>_stills.jpg — 1 lần đóng gói
python3 _tools/remotion.py review  campaigns/<c>     # outputs/review/<code>_review_vN.mp4
python3 _tools/remotion.py final   campaigns/<c> --name <tên chuẩn CLAUDE.md>.mp4 [--extra 4:5]   # + -14 LUFS, bản phụ
```
- Máy chưa có bộ dùng chung / repo đổi phiên bản → lệnh tự cài trước (vài phút, **1 lần / máy**). Cài tay: `python3 _tools/remotion.py ensure`. Trạng thái: `status`.
- Media đọc **thẳng** từ `campaigns/<c>/outputs/` (không copy vào public/): `src` viết `"videos/x.mp4"`, `"audio/vo-S01.mp3"`, `"images/logo.png"`.
- Thứ tự gọn: `check` → `stills` (soi bố cục, vùng an toàn) → `review` → góp ý → sửa timeline → `review` → `final`. **Không render từng khung bằng lệnh riêng** (mỗi lệnh đóng gói lại từ đầu, rất chậm).
- Rác Remotion trong Temp được tự dọn sau mỗi lần render.

### `campaigns/<c>/remotion-project/timeline.json`

```json
{
  "campaign": "KOLOR-2026-10-TOPCOAT",
  "fps": 30, "width": 1080, "height": 1920,
  "safe": {"top": 14, "bottom": 35, "left": 6, "right": 12},
  "font": "Montserrat",
  "accent": "#9e1b2c", "textColor": "#ffffff",
  "scenes": [
    {"id": "S01", "type": "clip", "src": "videos/KOLOR-…_S01_one-coat_v1.mp4", "duration": 3.5, "trimStart": 0.2,
     "scale": 1.06, "texts": [{"text": "ONE COAT", "pos": "top", "from": 0.3}]},
    {"id": "S02", "type": "clip", "src": "videos/…_S02_v1.mp4", "duration": 3.0, "transition": "fade", "keepAudio": false,
     "texts": [{"text": "NO-WIPE", "pos": "lowerThird", "bg": "#9e1b2c", "from": 0.6, "to": 2.8}]},
    {"id": "S03", "type": "image", "src": "images/…_B-03_v1.png", "duration": 3.0, "zoom": [1, 1.08]},
    {"id": "S04", "type": "endcard", "src": "images/packshot.png", "logo": "images/logo.png", "bg": "#debdb8", "duration": 3.5,
     "texts": [{"text": "Shop now", "pos": "bottom", "bg": "#1c1b19", "from": 0.5}]}
  ],
  "audio": {
    "vo": [{"src": "audio/…_vo-S01_v1.mp3", "at": 0.4, "dur": 2.2}],
    "music": {"src": "audio/…_music_v1.mp3", "volume": 0.25, "duck": 0.08, "fadeOut": 1.5},
    "sfx": [{"src": "audio/…_sfx-01_v1.mp3", "at": 1.0, "volume": 0.7}]
  }
}
```

| Trường | Ý nghĩa |
|---|---|
| `safe` | % vùng an toàn — lấy từ `_tools/platforms.json` theo nền tảng trong brief (gộp nhiều nền tảng = lề lớn nhất). Chữ `top` / `bottom` / logo tự đặt trong vùng an toàn |
| `font` | `Montserrat` · `Inter` · `BeVietnamPro` (Google Fonts, có dấu tiếng Việt) |
| scene `type` | `clip` (video) · `image` (ảnh tĩnh, Ken Burns `zoom`) · `endcard` (packshot `src` contain + `logo` + nền `bg`) |
| `duration` | giây — **chốt theo VO thật** (đo file audio), tổng = đúng thời lượng brief |
| `trimStart` · `scale` · `position` | clip: bỏ bao nhiêu giây đầu · phóng to để cắt mép (giấu watermark) · tâm khung (`"50% 40%"`) |
| `keepAudio` | giữ tiếng gốc clip (UGC có lời, Flow có thoại). Mặc định tắt |
| `texts[]` | `text` (không em dash) · `pos` `top` / `center` / `bottom` / `lowerThird` · `from` / `to` giây trong cảnh · `size` px · `bg` = viên nền chữ |
| `audio.vo[]` | `at` = giây trên toàn video · `dur` = độ dài thật (để nhạc tự hạ khi có lời) |
| `audio.music` | `volume` nền · `duck` khi có lời · `fadeOut` giây cuối |

### Cần hiệu ứng khung chung chưa có
Đặt file `.tsx` vào `campaigns/<c>/remotion-project/src/` — lệnh tự chép **đè** lên khung chung khi dựng campaign đó (VD `Main.tsx` riêng). Hiệu ứng dùng lại được nhiều campaign → thêm vào `_tools/remotion-base/src/Main.tsx` (khung chung), ghi vào bảng trên.

## Quy tắc cũ vẫn giữ

- **Không** `npm install` trong `campaigns/<c>/remotion-project/` (thư mục đồng bộ Drive — `node_modules` hàng nghìn file nhỏ, xoá không được). `remotion-project/` chỉ chứa `timeline.json` (+ `src/` riêng nếu có).
- Render review → `outputs/review/`, final → `outputs/final/` đúng tên chuẩn `CLAUDE.md`.
- Composition id duy nhất: `Main`. Kích thước theo `width` / `height` trong timeline (bản phụ: `--extra 4:5`).

## Kiến thức React / Remotion tối thiểu (khi phải viết `.tsx` riêng)

- `useCurrentFrame()` · `useVideoConfig()` · `interpolate(frame, [in], [out])` · `spring({frame, fps})`
- `<Sequence from durationInFrames>` · `<OffthreadVideo src>` · `<Img>` · `<Audio>` · `staticFile('videos/x.mp4')` (gốc = `outputs/` của campaign)
