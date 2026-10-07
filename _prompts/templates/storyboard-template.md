# Storyboard — template (có ảnh minh hoạ từng cảnh)

> Claude viết `campaigns/[campaign]/scripts/storyboard.json` → chạy `python3 _tools/storyboard.py campaigns/[campaign]` → sinh:
> - `scripts/storyboard.md` — bảng gọn + ảnh + prompt EN kèm dịch VI (các bước sau đọc file này)
> - `scripts/storyboard.html` — **cùng khung với bảng clip** (`_tools/clip-board.py`): mỗi cảnh có mã · thời gian · mục đích · công cụ · render/dùng · ảnh · prompt ảnh + prompt video nháp (nút Copy + dịch VI) · lời thoại EN + VI · chữ trên màn hình · file lưu về. Copy prompt sang nền tảng nào cũng đủ thông tin. **Gửi vào chat bằng file card `display: render`**, không gửi link ảnh rời.
> Sửa storyboard = sửa JSON rồi chạy lại tool. Không sửa tay `storyboard.md`.

## Ảnh minh hoạ (bắt buộc, mỗi cảnh 1 ảnh)

- Gen ở cổng 1 bằng `gen-image.py --quality low`, đúng tỷ lệ, đúng bố cục / cỡ cảnh / hướng sáng dự kiến.
- Lưu `outputs/review/storyboard/[code]_P-S01_v1.png` (P = preview). **Chỉ để duyệt ý** — không dùng làm khung video, không tính vào lượt 1 gen + 1 sửa của ảnh thật.
- Cảnh dùng ảnh thật (packshot, logo) → trỏ thẳng tới ảnh thật, không gen.
- Cảnh có thay đổi lớn (trước → sau) → thêm ảnh cuối cảnh vào `notes_vi` hoặc tách 2 cảnh.

## Cấu trúc `storyboard.json`

```json
{
  "campaign": "KOLOR-2026-10-TOPCOAT",
  "duration": "10s",
  "ratio": "9:16",
  "format": "Voiceover",
  "platform": {"ids": ["meta_reels", "tiktok"], "extra_ratios": ["4:5"], "template": "chuẩn nền tảng | refs/template/<file>"},
  "look": "Look chung 1–2 câu (VI): nền, ánh sáng, tông màu, cỡ cảnh",
  "character": {
    "name": "dana", "source": "Import ảnh user / có sẵn / tạo mới",
    "images": ["../../_characters/dana/reference-images/dana-face-ref-01.png", "...half-body-01.png", "...in-scene-01.png"],
    "identity_lock_en": "Khối mô tả EN chi tiết — chép nguyên văn vào mọi prompt có nhân vật (character-intake.md mục 2)",
    "identity_vi": "Dịch VI để user duyệt",
    "voice_en": "Mô tả giọng 1 câu (UGC)"
  },
  "scenes": [
    {
      "id": "S01",
      "time": "0.0–3.5s",
      "purpose": "Hook / Proof / CTA…",
      "route": "AI-VIDEO | MOTION-GRAPHIC",
      "tool": "Công cụ + cài đặt theo prefs — VD Higgsfield · image-to-video · 9:16 / Remotion",
      "render_s": 5,
      "use_s": 3.5,
      "image": "outputs/review/storyboard/KOLOR-2026-10-TOPCOAT_P-S01_v1.png",
      "visual_vi": "Mô tả hình bằng tiếng Việt: ai làm gì, từ đầu cảnh tới cuối cảnh",
      "line_en": "Lời thoại / VO nguyên văn (EN) — trống nếu cảnh không lời",
      "line_vi": "Dịch lời thoại (VI)",
      "onscreen": "Chữ trên màn hình (không em dash)",
      "prompt_en": "Prompt ảnh khung đầu (EN)",
      "prompt_vi": "Dịch prompt ảnh (VI)",
      "video_prompt_en": "Prompt video NHÁP (EN) — đủ để copy sang nền tảng khác thử; chốt lại ở cổng 2 theo ảnh thật",
      "video_prompt_vi": "Dịch prompt video (VI)",
      "notes_vi": "Tuỳ chọn: camera 1 chuyển động, nối cảnh, rủi ro AI + cách đơn giản hoá",
      "out": "outputs/videos/[code]_S01_[mô-tả]_v1.mp4"
    }
  ],
  "images": [
    {"Mã": "B-01", "Nội dung": "...", "Vai trò": "first frame", "Cảnh": "S01", "Nguồn": "tạo mới / ảnh thật / chỉnh sửa", "Ref": "..."}
  ],
  "assets": [
    {"Asset": "S01", "Loại": "clip", "Nguồn": "gen mới", "Tên file": "[code]_S01_[mô-tả]_v1.mp4", "Ai làm": "User (Flow)", "Render (s)": "4", "Dùng (s)": "3.5"}
  ]
}
```

## Quy tắc

- `platform.ids` theo `_tools/platforms.json` → trang storyboard / bảng clip / bảng review vẽ **vùng an toàn** đè lên ảnh (dải đỏ = bị app che). Chữ trên màn hình, logo, CTA, mặt nhân vật, label sản phẩm phải nằm trong khung nét đứt. Có bản phụ 4:5 → chủ thể ở giữa khung để cắt được.

- Tổng thời lượng các cảnh = **đúng** duration brief.
- Mỗi cảnh = 1 hành động chính, 1 chuyển động máy (hoặc đứng yên). Hành động phức tạp → tách cảnh.
- Sản phẩm dùng theo bước (nail, skincare, makeup) → cảnh đi theo **đúng các bước thật** (thao tác → xử lý → thành phẩm). Muốn giảm rủi ro AI thì làm động tác đơn giản đi, không cắt mất hành động cốt lõi.
- Route mập mờ → `_skills/scene-routing/references/scene-routing-rules.md`.
- Mỗi cảnh = 1 clip render riêng. Gộp cảnh chỉ khi user yêu cầu.
- `images` + `assets`: tên file theo naming convention trong `CLAUDE.md`. Clip render 4/6/8s; "Dùng" = đoạn cắt theo VO thật ở cổng 3.
- VO có thật → duration cảnh chốt theo file audio thật ở cổng 3 (`_skills/motion-graphic/references/audio-and-voice.md`).
