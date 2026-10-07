# CLAUDE.md — AI Video Project

> Meta Ads DTC — AI Video · GPT Image / Nano Banana (ảnh) · TopView / Higgsfield qua MCP hoặc API (video + UGC; Google Flow chỉ để test) · ElevenLabs / OpenAI TTS (VO) · Remotion (dựng)
> Công cụ cụ thể cho từng việc = **lựa chọn của user ở bước setup** (`~/.config/ai-studio/prefs.env`, hook báo đầu mỗi session).
> Owner: Phạm Ngọc Tịnh. Hướng dẫn người dùng: `HUONG-DAN-SU-DUNG.md` (cập nhật khi đổi quy trình). `HUONG-DAN-NGUOI-MOI.pdf` là bản cũ (quy trình 14 cổng).

## Quy trình — 3 cổng (chi tiết + quy tắc tiết kiệm token: `_workflows/production-steps.md`)

```
1. Kế hoạch (tạo campaign → nhận brief + nền tảng / khung hình / template → claim SP mới → nhân vật có ảnh → script → storyboard CÓ ẢNH, có vùng an toàn) ⛔ user duyệt trên storyboard.html
2a. Ảnh (ảnh thật + QC đúng nhân vật → bảng clip) ⛔ user duyệt ảnh + danh sách clip TRƯỚC khi tốn credit video
2b. Clip + âm thanh (gen clip qua TopView/Higgsfield — hoặc user render Flow khi test → VO, nhạc → bảng clip chạy lại) ⛔
3. Final (kiểm đủ file → dựng Remotion → bảng review có transcript → final) ⛔
```

- Trong 1 cổng Claude **chạy liền**, chỉ dừng ở cuối cổng (hoặc khi user dặn dừng). "ok cổng N" → ghi ✅ + người duyệt vào `status.md`, cập nhật **Tiếp theo**.
- Mở việc → đọc `campaigns/[campaign]/status.md` trước để biết đang ở đâu.
- Tên cổng cũ (A–E, 4A–4E, `/start`, `/assets`…) trong file khác → quy đổi theo bảng trong `production-steps.md`.
- **Trang HTML cho user duyệt chỉ sinh bằng tool** — `_tools/storyboard.py` (cổng 1) · `clip-board.py` (cổng 2) · `review-board.py` (cổng 3), cùng khung `_tools/_board.py`. Không tự viết HTML riêng; cần thêm loại trang mới → thêm tool dùng `_board.py`.
- **Gửi trang HTML → hỏi "Xem tại đây" hay "Mở trên trình duyệt"** (trình duyệt: `sh _tools/open-browser.sh <file.html>` — chỉ ở đó Copy ảnh / Mở thư mục mới chạy). Chi tiết: `production-steps.md` → "Cách báo cho user".
- **Báo cho user ngắn gọn:** mỗi lần dừng chỉ `✅ Xong` · `⛔ Cần duyệt` · `📁 File` (tối đa ~10 dòng, không giải thích trừ khi được hỏi). Ảnh / storyboard / video → **gửi file card hiển thị trực tiếp**, không dán link đường dẫn. Chi tiết: `production-steps.md` → "Cách báo cho user".

| Ai làm gì (theo lựa chọn ở setup — `prefs.env`) | |
|---|---|
| Ảnh — `IMAGE_TOOL` | `claude` (mặc định): Claude gen qua `_tools/gen-image.py` — nhà cung cấp `IMAGE_PROVIDER` (openai mặc định; có cloudflare / pollinations / huggingface **miễn phí**, gemini / fal / replicate). **Lỗi key / hết credit / timeout → in câu thần chú 🔮 (chép nguyên cho user) + popup tự hỏi đổi nhà + dán key**, chạy lại đúng ảnh đó. User tự đọc thần chú ("gọi hồn đứa khác", "cháy credit", "đổi provider/key") → skill `goi-hon` mở popup ngay — `_skills/image/SKILL.md` → Gen GPT Image. Báo danh sách ảnh trước khi gen. **Mỗi ảnh thật tối đa 1 gen + 1 sửa**, vẫn lỗi → note user tự sửa tay. Thiếu key / hết credit → thẻ tự gen. · `self`: chỉ xuất thẻ, user tự gen (ChatGPT / Gemini). Ảnh minh hoạ storyboard cổng 1 luôn do Claude gen nếu có key. |
| Video (b-roll, demo) — `VIDEO_TOOL` | `higgsfield` / `topview`: **Claude gen** qua MCP hoặc API (theo `HIGGSFIELD_CONN` / `TOPVIEW_CONN`), từ thẻ video + ảnh khung đầu đã pass. **Mỗi clip tối đa 1 gen + 1 sửa**, báo danh sách clip trước khi gen. Kết nối chưa sẵn sàng / chưa có tool gọi API → xuất thẻ cho user tự render · `api`: **Claude gen** bằng `_tools/gen-video.py` (nhà `VIDEO_PROVIDER`: fal_video / replicate_video / gemini_veo — chỉ credit dùng thử, không free lâu dài), cùng quy tắc 1 gen + 1 sửa · `flow`: **chỉ để test** — user tự render trên Google Flow (Veo 3.1) theo thẻ · `other`: thẻ dạng chung. |
| UGC (người nói) — `UGC_TOOL` | `topview` / `higgsfield`: **Claude gen** take qua MCP hoặc API (ảnh take + lời thoại + giọng — `ugc-workflow.md` Bước 4B), cùng quy tắc 1 gen + 1 sửa · `flow`: **chỉ để test** — Veo 3.1 tạo thoại + khẩu hình trong clip, mỗi take ≤ 8s, user tự render (Bước 4A). |
| VO — `VO_TOOL` | `elevenlabs`: Claude gen qua **connector ElevenLabs (MCP)**, tự tải file (`media[].url` qua `creative_get_flow_run_status` → `curl` về `outputs/audio/`, link hết hạn 2 giờ) **Không có connector → dùng API key ElevenLabs** qua `_tools/gen-voice.py --provider elevenlabs` (popup key nếu chưa có) · `api`: `gen-voice.py` theo `VO_PROVIDER` (**miễn phí**: gemini_tts, cloudflare_aura / cloudflare_melo · elevenlabs free không dùng thương mại · openai_tts) · `openai`: = `api` + openai_tts · `self`: thẻ cho user tự gen. Lựa chọn không dùng được → thử lựa chọn kế, rồi tới thẻ. Giọng mặc định theo brand: mục "Brand voice" trong `brand-brief.md` (nếu có — chưa có thì giữ giọng campaign trước của brand). |
| Nhạc nền · SFX — `MUSIC_TOOL` | `elevenlabs`: Claude gen nhạc qua connector (`creative_generate_in_flow`, node `music`, `eleven_music_v2_5`) theo `audio-plan.md`, chọn bản (không vocal — kiểm faster-whisper, beat theo RMS), tự tải về; **không có connector → `_tools/gen-music.py --provider elevenlabs_music`** (API key) · `api`: `gen-music.py` theo `MUSIC_PROVIDER` (replicate_music) · `self`: user tự chọn theo prompt. SFX: user tự chọn. Không tự tổng hợp nhạc bằng code cho bản thật. |
| Script, storyboard (kèm ảnh minh hoạ), prompt, QC, dựng Remotion | Claude |

Không báo giá / ước tính chi phí.

## Đọc gì khi nào (chỉ đọc đúng dòng cần — không đọc cả chuỗi)

| Việc | Đọc |
|---|---|
| Nhân vật (video có người) | `_workflows/character-intake.md` — hỏi dùng nhân vật thế nào (có sẵn / import ảnh / tạo mới), thẻ nhân vật 3 ảnh + IDENTITY LOCK, mọi ảnh có người `--require-ref` |
| Mở file / thư mục cho user | User nói "mở thư mục S01 / videos / ảnh…" → `sh _tools/open-path.sh <đường dẫn>` (Explorer / Finder, chọn sẵn file, chỉ mở không chạy). Nút 📂 trên bảng HTML cần cài 1 lần (Windows, user tự chạy): `powershell -ExecutionPolicy Bypass -File _tools\install-open-handler.ps1` |
| Review bản dựng | `python3 _tools/review-board.py campaigns/[campaign]` → `outputs/review/review-board.html` (khung hình từng cảnh + transcript đúng đoạn so với script) |
| Bắt đầu video mới | `_workflows/brief-intake.md` — hỏi user có brief chưa: có → import, bám theo · chưa → gợi ý 2–3 brief từ link sản phẩm |
| Mọi việc creative | `_brand/README.md` → xác định brand (không đoán, không đọc chéo brand) → `_brand/<brand>/brand-brief.md` + `target-audience.md` · `_products/<brand>/<sku>/product-brief.md` (claim APPROVED, Visual Identity) · nhân vật → `_characters/<tên>/profile.md` |
| Chọn format | Bảng "Chọn format" bên dưới → 1 file `_workflows/<format>-workflow.md` (file lớn → grep đúng bước) |
| Storyboard ≥2 scene | `_skills/scene-routing/SKILL.md` (route AI-VIDEO / MOTION-GRAPHIC) + `_prompts/templates/storyboard-template.md` (JSON → `_tools/storyboard.py`) · reuse: grep `_assets/broll-library/keywords.json` |
| Thẻ ảnh | `_prompts/nano-banana/image-prompt-card.md` + **1** file model: `_skills/image/references/nano-banana.md` HOẶC `gpt-image.md`. Chưa rõ model → `models.md`. Giữ identity → `characters.md` |
| Thẻ video | `_prompts/veo3/video-prompt-card.md` + `_skills/video/references/veo.md` (`universal-rules.md` khi lần đầu trong session) — dùng chung cho Higgsfield / TopView / Flow |
| Âm thanh / bàn giao | `_prompts/audio/audio-plan-template.md` · `_prompts/handoff-template.md` |
| Gen giọng / nhạc / video qua API | `_tools/gen-voice.py` · `gen-music.py` · `gen-video.py` (`--list-providers`; lỗi key/credit → thần chú 🔮 + popup `pick-provider.sh voice\|music\|video` có hướng dẫn lấy key). Nhà + hướng dẫn: `_tools/providers.json` |
| Bàn giao + duyệt clip | `prompts-used/clips.json` → `python3 _tools/clip-board.py campaigns/[campaign]` → `outputs/review/clip-board.html` (khung hình thật, lời nghe được so với script + dịch VI). Chạy lại mỗi khi có clip mới (`_prompts/handoff-template.md` mục 0) |
| Dựng Remotion | **Bộ dùng chung cả máy**: viết `remotion-project/timeline.json` → `python3 _tools/remotion.py check / stills / review / final campaigns/[c]` (tự cài 1 lần / máy, không `npm install` mỗi campaign) · chi tiết `_skills/motion-graphic/SKILL.md` → chỉ reference cần: `remotion-setup.md` · `animation-patterns.md` · `render-pipeline.md` · `audio-and-voice.md` · `caption-effects.md` |
| B-roll theo lời nói, loudness | `_tools/post-edit/post_edit.py` + `_prompts/remotion/components/VisualsOverlay.tsx` |

`_prompts/` ngoài các thẻ trên = thư viện ý tưởng, chỉ mở khi cần.

## Quy tắc nội dung

- **Thời lượng video phải hỏi user** (Bước 0) — không tự đặt, không giả định. Mọi cảnh + lời đọc vừa đúng số giây đó; `storyboard.py` báo ⚠️ LỐ thì sửa trước khi trình.
- Script: ngôn ngữ từ `target-audience.md`/review thật (brand chưa research → ghi rõ "giả định"). Label `[FORMAT] [NHÂN VẬT] [SẢN PHẨM] [DURATION] [RATIO]`. Hook trong 3s, không mở bằng tên brand. **Chỉ claim APPROVED.**
- **Chữ trên màn hình / caption: không dùng em dash (—)** — tách câu, dùng dấu chấm hoặc xuống dòng.
- Visual Identity của product-brief + profile nhân vật ưu tiên hơn "Notes cho AI Tools" trong brand-brief.
- Prompt video ở cổng 1 = **nháp** (trong storyboard, để user hình dung / copy thử). Bản chốt chỉ viết sau khi ảnh khung đầu thật pass. Mỗi scene render riêng. Clip lỗi → phản hồi theo mẫu `handoff-template.md`, không làm lại cảnh đã đạt.
- Ghi kết quả prompt: worked / needs adjustment / failed. Clip sạch + generic → copy vào `_assets/broll-library/` + thêm dòng `index.md`.
- Deliverable xong cổng → lưu campaign folder (bản gốc) + gửi vào chat 1 lần.

## Chọn format

Sau Bước 0 nhận brief (`brief-intake.md`). Brief chưa ghi format → **hỏi chốt format, kèm 1 câu recommend**. UGC và Voiceover không đổi qua lại giữa chừng được.

| Tín hiệu | UGC (`ugc-workflow.md`) | Voiceover (`voiceover-video-workflow.md`) |
|---|---|---|
| Giọng kể | Ngôi 1, testimonial | Ngôi 3, VO dẫn dắt |
| Cấu trúc | 1 khối thoại liên tục | Chia scene, mỗi scene 1 hình |
| B-roll | Phụ, 1–2 điểm chèn | Chính |
| Clip | TopView / Higgsfield (Claude gen qua MCP/API) — Google Flow khi test | Higgsfield / TopView (hoặc Flow khi test) + Remotion |

Khác: Product demo → `product-demo-workflow.md` · Static+video → `static-video-combo-workflow.md` · Motion graphic → `motion-graphic-workflow.md`.

## Cấu trúc & lưu file

```
_brand/<brand>/  _products/<brand>/<sku>/  _characters/<tên>/  _assets/broll-library/
_skills/  _prompts/  _workflows/  _tools/
campaigns/_template/  → copy khi tạo campaign mới
campaigns/[YYYY-MM]_[tên]/
  brief.md · status.md · performance-notes.md
  scripts/ (script.md, storyboard.json → .md + .html) · prompts-used/ (prompt-pack, audio-plan, handoff)
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

Người mới: nói **"set up dự án"** → skill `.claude/skills/setup/` **hỏi user chọn công cụ** (ảnh / video / UGC / giọng đọc / nhạc) rồi cài đúng thứ cần, chạy được trên Mac và Windows. Hướng dẫn người: `_workflows/setup-guide.md` Phần 1. Hook `.claude/settings.json` → `_tools/setup-check.sh` tự kiểm mỗi session.
**Key + lựa chọn công cụ lưu chung cả máy** (`~/.config/ai-studio/`) → dự án mới trên cùng máy **không hỏi lại**: luôn chạy `python3 _tools/key-status.py` trước (có + còn dùng được → bỏ qua; chỉ popup key thiếu / lỗi).
Cần (tuỳ lựa chọn): TopView / Higgsfield — connector MCP (`mcp.topview.ai/mcp`, `mcp.higgsfield.ai/mcp`, đăng nhập, không key) hoặc API key (`TOPVIEW_API_KEY` + `TOPVIEW_UID` / `HIGGSFIELD_API_KEY` + `HIGGSFIELD_API_SECRET`) — **mọi key nhập qua popup `set-key.sh`**, Python 3 (Windows: lệnh `python3` phải chạy được — setup tạo alias), `OPENAI_API_KEY` (gen ảnh / OpenAI TTS — nhập/đổi bằng `sh _tools/set-key.sh OPENAI_API_KEY`, hộp thoại ẩn, không qua chat), Node.js (Remotion), ffmpeg (xem/cắt khung clip — Windows `winget install Gyan.FFmpeg`, Mac `brew install ffmpeg`; `npx remotion ffmpeg` chỉ chạy trong dự án Remotion đã `npm install`), faster-whisper (transcript; máy không GPU → `device="cpu"`), connector ElevenLabs (nếu chọn) bật trong claude.ai → Settings → Connectors. Key khác (Pexels/Pixabay, tuỳ chọn) ở `~/.config/ai-studio/.env` — **không bao giờ** tạo `.env` trong project (folder share qua Drive). Thiếu → nhắc 1 lần theo `_workflows/setup-guide.md`, chỉ chặn ở bước thật sự cần.

## Thêm mới

- Brand: `_brand/<brand>/` theo `_brand/README.md` + cập nhật 2 bảng trong đó + chọn mã brand.
- Sản phẩm: copy `_products/_template/` vào `_products/<brand>/<sku>/` (bắt buộc trường **Brand** + claim APPROVED), hoặc đưa link sản phẩm ở cổng 1.
- Nhân vật: theo `_workflows/character-intake.md` ở cổng 1 (có ảnh + mô tả chi tiết, import được ảnh có sẵn); lưu `_characters/<tên>/`.
- Campaign: copy `campaigns/_template/`. **1 script = 1 campaign**, tái dùng nhân vật/seed thoải mái.

## Meta compliance trước publish

AI disclosure bật · lip sync xem 1.5x · logo/màu/chữ label đúng · chỉ claim APPROVED · file ở `outputs/final/` đúng ratio từng nền tảng (bản chính + bản phụ) · chữ / logo / CTA nằm trong vùng an toàn (`_tools/platforms.json`).
