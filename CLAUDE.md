# CLAUDE.md — AI Video Project

> Meta Ads DTC — AI Video · Nano Banana / GPT Image (ảnh) · Veo 3.1 (video) · TopView (UGC) · ElevenLabs (VO) · Remotion (dựng)
> Owner: Phạm Ngọc Tịnh. Hướng dẫn người dùng: `HUONG-DAN-SU-DUNG.md` (cập nhật khi đổi quy trình). `HUONG-DAN-NGUOI-MOI.pdf` là bản cũ (quy trình 14 cổng).

## Quy trình — 3 cổng (chi tiết + quy tắc tiết kiệm token: `_workflows/production-steps.md`)

```
1. Kế hoạch (brief + script + storyboard + thẻ ảnh) ⛔ → user duyệt kế hoạch (chưa gen ảnh)
2. Ảnh (Claude gen GPT Image → QC → thẻ video + âm thanh + VO + bàn giao) ⛔ → user render video, chọn nhạc/SFX
3. Final (kiểm file → dựng Remotion → review → final) ⛔
```

- Trong 1 cổng Claude **chạy liền**, chỉ dừng ở cuối cổng (hoặc khi user dặn dừng). "ok cổng N" → ghi ✅ + người duyệt vào `status.md`, cập nhật **Tiếp theo**.
- Mở việc → đọc `campaigns/[campaign]/status.md` trước để biết đang ở đâu.
- Tên cổng cũ (A–E, 4A–4E, `/start`, `/assets`…) trong file khác → quy đổi theo bảng trong `production-steps.md`.

| Ai làm gì | |
|---|---|
| Ảnh (mặc định GPT Image 2) | Claude gen qua `_tools/gen-image.py` ở đầu cổng 2 — quy trình: `_skills/image/SKILL.md` → Gen GPT Image. Báo danh sách ảnh trước khi gen. **Mỗi ảnh tối đa 1 gen + 1 sửa**, vẫn lỗi → note user tự sửa tay. Thiếu key / hết credit → thẻ tự gen. |
| Video · SFX · ảnh Nano Banana (chỉ khi user yêu cầu) | **Người dùng tự gen/chọn** theo thẻ Claude viết. Claude không gọi API/MCP gen video. |
| Nhạc nền | Claude gen qua **connector ElevenLabs (MCP)** (`creative_generate_in_flow`, node `music`, `eleven_music_v2_5`) theo prompt trong `audio-plan.md`. Claude chọn bản (kiểm không vocal bằng faster-whisper + beat theo RMS) và tự tải về, trừ khi user muốn tự chọn. |
| VO (ElevenLabs) | Claude gen qua **connector ElevenLabs (MCP)**, không dùng API key, sau khi ảnh pass ở cổng 2. Connector lỗi → thẻ để user tự gen. File: Claude tự tải về — lấy `media[].url` qua `creative_get_flow_run_status` → `curl` về `outputs/audio/` đúng tên (link hết hạn sau 2 giờ). Tải lỗi → user tải tay từ elevenlabs.io. |
| Script, storyboard, prompt, QC, dựng Remotion | Claude |

Không báo giá / ước tính chi phí.

## Đọc gì khi nào (chỉ đọc đúng dòng cần — không đọc cả chuỗi)

| Việc | Đọc |
|---|---|
| Mọi việc creative | `_brand/README.md` → xác định brand (không đoán, không đọc chéo brand) → `_brand/<brand>/brand-brief.md` + `target-audience.md` · `_products/<sku>/product-brief.md` (claim APPROVED, Visual Identity) · nhân vật → `_characters/<tên>/profile.md` |
| Chọn format | Bảng "Chọn format" bên dưới → 1 file `_workflows/<format>-workflow.md` (file lớn → grep đúng bước) |
| Storyboard ≥2 scene | `_skills/scene-routing/SKILL.md` (route AI-VIDEO / MOTION-GRAPHIC) · reuse: grep `_assets/broll-library/keywords.json` |
| Thẻ ảnh | `_prompts/nano-banana/image-prompt-card.md` + **1** file model: `_skills/image/references/nano-banana.md` HOẶC `gpt-image.md`. Chưa rõ model → `models.md`. Giữ identity → `characters.md` |
| Thẻ video (Veo) | `_prompts/veo3/video-prompt-card.md` + `_skills/video/references/veo.md` (`universal-rules.md` khi lần đầu trong session) |
| Âm thanh / bàn giao | `_prompts/audio/audio-plan-template.md` · `_prompts/handoff-template.md` |
| Dựng Remotion | `_skills/motion-graphic/SKILL.md` → chỉ reference cần: `remotion-setup.md` · `animation-patterns.md` · `render-pipeline.md` · `audio-and-voice.md` · `caption-effects.md` |
| B-roll theo lời nói, loudness | `_tools/post-edit/post_edit.py` + `_prompts/remotion/components/VisualsOverlay.tsx` |

`_prompts/` ngoài các thẻ trên = thư viện ý tưởng, chỉ mở khi cần.

## Quy tắc nội dung

- Script: ngôn ngữ từ `target-audience.md`/review thật (brand chưa research → ghi rõ "giả định"). Label `[FORMAT] [NHÂN VẬT] [SẢN PHẨM] [DURATION] [RATIO]`. Hook trong 3s, không mở bằng tên brand. **Chỉ claim APPROVED.**
- **Chữ trên màn hình / caption: không dùng em dash (—)** — tách câu, dùng dấu chấm hoặc xuống dòng.
- Visual Identity của product-brief + profile nhân vật ưu tiên hơn "Notes cho AI Tools" trong brand-brief.
- Không viết prompt video trước khi ảnh đầu vào pass. Mỗi scene render riêng. Clip lỗi → phản hồi theo mẫu `handoff-template.md`, không làm lại cảnh đã đạt.
- Ghi kết quả prompt: worked / needs adjustment / failed. Clip sạch + generic → copy vào `_assets/broll-library/` + thêm dòng `index.md`.
- Deliverable xong cổng → lưu campaign folder (bản gốc) + gửi vào chat 1 lần.

## Chọn format

User đưa script/ý tưởng → **luôn hỏi chốt format, kèm 1 câu recommend** (trừ khi user đã nói rõ). UGC và Voiceover không đổi qua lại giữa chừng được.

| Tín hiệu | UGC (`ugc-workflow.md`) | Voiceover (`voiceover-video-workflow.md`) |
|---|---|---|
| Giọng kể | Ngôi 1, testimonial | Ngôi 3, VO dẫn dắt |
| Cấu trúc | 1 khối thoại liên tục | Chia scene, mỗi scene 1 hình |
| B-roll | Phụ, 1–2 điểm chèn | Chính |
| Clip | TopView Avatar4, không Veo | Veo + Remotion |

Khác: Product demo → `product-demo-workflow.md` · Static+video → `static-video-combo-workflow.md` · Motion graphic → `motion-graphic-workflow.md`.

## Cấu trúc & lưu file

```
_brand/<brand>/  _products/<sku>/  _characters/<tên>/  _assets/broll-library/
_skills/  _prompts/  _workflows/  _tools/
campaigns/_template/  → copy khi tạo campaign mới
campaigns/[YYYY-MM]_[tên]/
  brief.md · status.md · performance-notes.md
  scripts/ (script.md, storyboard.md) · prompts-used/ (prompt-pack, audio-plan, handoff)
  remotion-project/ · outputs/ images · videos · audio · review · final
```

Seed nhân vật pass → copy thêm vào `_characters/<tên>/reference-images/<tên>-face-ref-01.png`. Chỉ upload Meta từ `outputs/final/`. Campaign xong → `_archive/`.

**Campaign code:** `[BRAND]-[YYYY-MM]-[TÊN]` (mã brand: `KREIZI` · `KOLOR`).
```
Asset thô:  [code]_[asset-id]_[mô-tả]_v[n].[ext]
            A-01 ảnh tham chiếu · B-01 khung video · S01 scene
            KOLOR-2026-10-BLOOM_B-01_S01-dot_v1.png · …_S01_dot-to-bloom_v1.mp4 · …_vo-S01_v1.mp3 · …_music_v1.mp3 · …_sfx-01_click_v1.mp3 · …_take-A_v1.mp4
Final:      [code]_[format]_[character]_[product]_[ratio]_v[n].[ext]
            KOLOR-2026-10-BLOOM_voiceover_nochar_blooming-gel_9x16_v1.mp4
```

## Setup máy

Người mới: nói **"set up dự án"** → skill `.claude/skills/setup/` cài giúp. Hướng dẫn người: `_workflows/setup-guide.md` Phần 1. Hook `.claude/settings.json` → `_tools/setup-check.sh` tự kiểm mỗi session.
Cần: `OPENAI_API_KEY` (gen ảnh — nhập/đổi bằng `sh _tools/set-key.sh OPENAI_API_KEY`, hộp thoại ẩn, không qua chat), Node.js (Remotion — có sẵn ffmpeg qua `npx remotion ffmpeg`), faster-whisper (transcript), connector ElevenLabs bật trong claude.ai → Settings → Connectors. Key khác (Pexels/Pixabay, tuỳ chọn) ở `~/.config/ai-studio/.env` — **không bao giờ** tạo `.env` trong project (folder share qua Drive). Thiếu → nhắc 1 lần theo `_workflows/setup-guide.md`, chỉ chặn ở bước thật sự cần.

## Thêm mới

- Brand: `_brand/<brand>/` theo `_brand/README.md` + cập nhật 2 bảng trong đó + chọn mã brand.
- Sản phẩm: copy `_products/_template/` (bắt buộc trường **Brand** + claim APPROVED), hoặc đưa link sản phẩm ở cổng 1.
- Nhân vật: copy `_characters/_template/`; thẻ seed ở cổng 1, gen ở cổng 2.
- Campaign: copy `campaigns/_template/`. **1 script = 1 campaign**, tái dùng nhân vật/seed thoải mái.

## Meta compliance trước publish

AI disclosure bật · lip sync xem 1.5x · logo/màu/chữ label đúng · chỉ claim APPROVED · file ở `outputs/final/` đúng ratio.
