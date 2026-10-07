> **Khi dùng:** video voiceover ngôi thứ 3 (VO dẫn dắt/giải thích + b-roll/illustration/packshot), nhiều scene — đã xác định KHÔNG phải UGC ở Bước 0 trong `CLAUDE.md`.
> **Skills dùng:** `_skills/scene-routing/` → `_skills/video/` (scene AI-VIDEO) + `_skills/image/` (keyframe) → `_skills/motion-graphic/` (scene MOTION-GRAPHIC + assembly)
> **Cổng dùng chung của 6 lệnh** (`_workflows/production-steps.md`) — tới cổng là dừng, đợi user duyệt mới đi tiếp. File này là chi tiết kỹ thuật cho các lệnh, không có cổng đánh số riêng.

# Workflow SOP — Voiceover Video

| Step | Lệnh | Cổng |
|---|---|---|
| Trước khi bắt đầu | `/start` | ⛔A brief |
| 1 Script VO | `/script` | ⛔B script + claim |
| 2 Storyboard | `/storyboard` | ⛔C storyboard + danh sách asset |
| 3 Ảnh + prompt video | `/assets` | ⛔4A prompt ảnh → ⛔4B duyệt ảnh → ⛔4C prompt video |
| 4 Âm thanh + VO | `/assets` | ⛔4D bảng âm thanh → Claude gen VO |
| 4E Bàn giao | `/assets` | ⛔4E bảng clip (`clip-board.html`) → tạo clip · `handoff.md` (âm thanh, dựng) |
| (kiểm asset) | `/check` | ⛔D |
| 5–6 Dựng + export | `/edit` | ⛔E |

---

## Trước khi bắt đầu

1. Campaign folder + `brief.md` + `status.md` do `/start` tạo (không copy `_template` bằng tay). Brief phải có key message DUY NHẤT, audience stage, duration, ratio
2. Xác định brand từ `_products/<brand>/<sku>/product-brief.md` (trường **Brand**) → đọc `_brand/<brand>/brand-brief.md`, `_brand/<brand>/target-audience.md`, và phần APPROVED của product-brief
3. Có nhân vật xuất hiện → đọc `_characters/[nhân-vật]/profile.md` + list `reference-images/`

---

## Step 1: Viết script VO

Dùng **Voiceover Script Prompt** trong `_prompts/gemini-omni/script-generation.md` (ngôi thứ 3 — KHÔNG dùng Master Script Prompt, cái đó dành cho UGC ngôi thứ nhất).

- Tốc độ đọc ~2.4 từ/giây: 15s ≈ 35 từ · 20s ≈ 48 từ · 30s ≈ 70 từ. Vượt → cắt câu, không đọc nhanh hơn.
- Mỗi câu VO = 1 beat hình ảnh (sẽ thành 1 scene ở Step 2).
- Lập bảng claim check: mỗi câu nói về sản phẩm ↔ claim approved tương ứng. Câu nào không map được → sửa hoặc đánh dấu ⚠️ cần brand duyệt.
- Lưu `scripts/script.md` (template: `_prompts/templates/script-template.md`), kèm VO direction (giới tính, tuổi giọng, accent, nhịp) + 3 hook thay thế.

### ⛔ Cổng B — duyệt script + claim check

---

## Step 2: Storyboard

Chạy `_skills/scene-routing/SKILL.md`: chia scene theo từng câu VO, gắn route tag, check `_assets/broll-library/index.md` để reuse.

- Ưu tiên **ảnh sản phẩm thật** (`_products/.../reference-images/`) cho packshot/callout/end card (MOTION-GRAPHIC) — packaging đúng 100%.
- Scene cần chứng minh claim (VD: "không vón dưới makeup") → phải có hành động chứng minh trong hình, không chỉ minh hoạ chung chung.
- Mặc định 1 scene = 1 clip render (chỉ gộp khi user yêu cầu).
- Ghi cuối storyboard (template `_prompts/templates/storyboard-template.md`): danh sách asset — keyframe cần gen, clip Veo cần gen (kèm duration 4/6/8s), clip reuse, audio (VO/nhạc/SFX).

### ⛔ Cổng C — duyệt storyboard + danh sách asset

---

## Step 3: Ảnh + prompt video (scene AI-VIDEO) — `/assets` 4A → 4B → 4C

Cho mỗi scene AI-VIDEO không reuse được. (Tuỳ chọn: phác shot card `_prompts/veo3/shot-card-template.md` làm công cụ suy nghĩ — không phải deliverable.)

**4A — thẻ prompt ảnh:** keyframe (first frame) mỗi scene viết theo `_prompts/nano-banana/image-prompt-card.md` + `_skills/image/SKILL.md` — ref ảnh nhân vật + ảnh sản phẩm thật, tên file `[code]_B-01_S01-[mô-tả]_v1.png`. Seed/ảnh nền tảng trước. Gen ở đầu cổng 2: `_skills/image/SKILL.md` → Gen GPT Image.

### ⛔ Cổng 4B — Claude QC ảnh
Check: identity nhân vật khớp ref · packaging/label đúng product brief · không tay/ngón biến dạng · đúng ratio. Fail → sửa prompt theo edit logic (đổi đúng 1 thứ), không re-roll toàn bộ.

**4C — thẻ prompt video:** chỉ viết SAU khi ảnh đã duyệt ở 4B, theo `_prompts/veo3/video-prompt-card.md` + `_skills/video/references/veo.md` §7: Veo 3.1 image-to-video, "Maintain the subject from the first frame", chỉ tả chuyển động/camera/ánh sáng, không tả lại phần tĩnh. Dòng audio mặc định: **"No dialogue, no music, no sound effects; quiet natural ambience only."** (VO làm riêng ở Step 4). Render 4/6/8s — độ dài render ≠ độ dài dùng.

Lưu mọi thẻ vào `prompts-used/`. **Chưa render video ở đây** — render chỉ bắt đầu sau 4E.

---

## Step 4: Bảng âm thanh + VO — `/assets` 4D

**4D.1 — Bảng âm thanh trước:** lập `prompts-used/audio-plan.md` theo `_prompts/audio/audio-plan-template.md` (VO từng scene + giọng, nhạc nền, SFX, clip nào giữ audio "tạo cùng clip"). Đây là chỗ DUY NHẤT ghi `voice_id` + voice settings.

### ⛔ Cổng 4D — duyệt bảng âm thanh
Chỉ sau khi user "ok 4D" Claude mới gen VO. Nhạc nền + SFX: người dùng tự tạo/chọn theo prompt trong `audio-plan.md`, lưu `outputs/audio/`.

VO tạo bằng **connector ElevenLabs (MCP)** — không dùng API key. Tool: `creative_list_voices` · `creative_generate_speech` (load qua ToolSearch nếu đang deferred). Connector chưa kết nối → nhắc user bật trong claude.ai → Settings → Connectors → ElevenLabs.

**4D.2 Chọn giọng** (lần đầu mỗi campaign — đề xuất trong bảng âm thanh): gọi `creative_list_voices` → đề xuất 2–3 giọng khớp VO direction (giới tính, tuổi, accent) → user chọn (widget có nút đổi giọng, đọc widget context thay vì hỏi lại) → ghi `voice_id` vào `prompts-used/audio-plan.md`. `voice_id` chỉ lấy từ tool hoặc user, không lấy từ trí nhớ.

**4D.3 Gen VO — mỗi câu script = 1 lần `creative_generate_speech`** (khớp cut chính xác), cùng `voice_id` + settings trong `audio-plan.md`.
- Kết quả hiện ngay trong chat. Claude tự tải: lấy `media[].url` qua `creative_get_flow_run_status` → `curl` về `outputs/audio/` đúng tên (link hết hạn sau 2 giờ). Tải lỗi → user tải tay từ elevenlabs.io. Tên file `<campaign-code>_vo-S01_v1.mp3`… thả vào `outputs/audio/`.
- Đọc đều quá/robot → giảm stability; lệch giọng → tăng similarity. Mỗi lần đổi 1 tham số.
- Nhịp/ngắt: thêm dấu phẩy, dấu chấm, hoặc `...` trong text — không nhồi câu để "đọc nhanh hơn".
- File đã về: đo duration `afinfo <file> | grep duration` → duration scene lấy theo audio (không hardcode) — `_skills/motion-graphic/references/audio-and-voice.md` §2.
- Ghi text + voice_id + settings đã dùng vào `prompts-used/audio-plan.md`.
- Copy VO vào `/tmp/<campaign>-remotion/public/audio/` làm ở bước dựng, không làm ở bước này.

Connector lỗi / hết credit → xuất thẻ để user tự gen trên elevenlabs.io (cùng giọng, cùng settings), tải mp3 về `outputs/audio/` đúng tên file như trên.

---

## Step 4E: Bộ bàn giao — `/assets` 4E

Thẻ video đã duyệt (4C) → `prompts-used/clips.json` → `python3 _tools/clip-board.py campaigns/[campaign]` → **bảng clip** gửi user (đây là chỗ user nhận prompt video). Audio (4D) + hướng dẫn dựng → `prompts-used/handoff.md`. Theo `_prompts/handoff-template.md`.

### ⛔ Cổng 4E — duyệt bộ bàn giao
Sau 4E: tạo clip theo bảng clip — Claude gen nếu `VIDEO_TOOL` = `higgsfield`/`topview` (MCP/API, 1 gen + 1 sửa/clip); `flow`/`other` → **người dùng tự render** theo bảng. File vào `outputs/videos/` đúng tên ở cột "Lưu về". Xong → chạy lại `clip-board.py` để duyệt (khung hình thật, lời, độ dài) → cổng 3.

---

## Step 5: Build scene MOTION-GRAPHIC + Assembly — `/edit`

`_skills/motion-graphic/SKILL.md`:
- **Mode A:** build từng scene MOTION-GRAPHIC (packshot + callout, end card + CTA)
- **Mode B:** ráp tất cả scene theo thứ tự storyboard, transition theo Assembly notes
- Copy VO/nhạc/SFX từ `outputs/audio/` + clip từ `outputs/videos/` vào `/tmp/<campaign>-remotion/public/`; frame count clip lấy bằng `npx remotion ffprobe` (không dùng `mdls`)
- Clip audio mute trừ khi `audio-plan.md` đánh dấu "tạo cùng clip"
- Nhạc nền duck dưới VO (`audio-and-voice.md` §3) · sub text word-by-word theo `caption-effects.md` · loudnorm -14 LUFS (`_tools/post-edit/`)

### ⛔ Cổng E — QC video final (bản review ở `outputs/review/`)
Xem 1x và 1.5x: VO khớp hình từng scene · text overlay không đè caption · claim trên màn hình = claim trong script · CTA mềm, không FOMO · có before/after thì có "Actual results may vary".

---

## Step 6: Export, compliance, log

- Render → `outputs/final/` theo naming convention trong `CLAUDE.md`
- Chạy checklist **Meta Ads compliance** trong `CLAUDE.md` (AI disclosure, claim, ratio)
- Clip AI-VIDEO sạch, dùng lại được → copy vào `_assets/broll-library/` + thêm dòng `index.md`
- Ghi `performance-notes.md` sau khi chạy ads
