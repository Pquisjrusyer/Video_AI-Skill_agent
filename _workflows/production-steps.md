# Quy trình sản xuất — 3 cổng

> Trạng thái campaign: `campaigns/[campaign]/status.md` (dòng **Tiếp theo** = việc kế + ai làm).
> Không có slash command — nói bằng lời thường ("làm video cho sp X", "ảnh xong rồi", "clip đã thả vào"). Claude tự biết đang ở bước nào nhờ `status.md`.
> Chi tiết theo format: `voiceover-video-workflow.md`, `ugc-workflow.md`, `product-demo-workflow.md`, `static-video-combo-workflow.md`, `motion-graphic-workflow.md`.

---

## 3 cổng (cổng 2 có 2 điểm dừng: 2a ảnh · 2b clip)

| Cổng | Claude làm (chạy liền trong cổng) | User duyệt / làm | File |
|---|---|---|---|
| **1. Kế hoạch** | ① **Tạo campaign**: copy `campaigns/_template/` → `campaigns/[YYYY-MM]_[tên]/`, đặt mã `[BRAND]-[YYYY-MM]-[TÊN]`, mở `status.md` · ② **Nhận brief** (`brief-intake.md`: có brief → import, bám theo · chưa → gợi ý 2–3 brief từ link) + **nền tảng · khung hình · template** (Reels / Stories / Feed / TikTok / Shorts → ratio chính + bản phụ, vùng an toàn, template riêng nếu có) · ③ Sản phẩm mới → `product-brief.md` + ảnh official + **danh sách claim chờ duyệt** · ④ Chốt format (nếu brief chưa ghi) → `brief.md` · ⑤ **Nhân vật** (nếu có người — `character-intake.md`: hỏi dùng nhân vật thế nào, có sẵn / import ảnh / tạo mới → thẻ nhân vật 3 ảnh + mô tả chi tiết) · ⑥ Script (đếm từ, bảng lời theo cảnh EN + VI, đối chiếu claim) · ⑦ Ảnh minh hoạ chất lượng thấp mỗi cảnh (`IMAGE_TOOL=self` → bỏ ảnh, storyboard ghi "chưa có ảnh" + prompt để user tự gen) · ⑧ Storyboard có ảnh (`_tools/storyboard.py`: thẻ nhân vật ở đầu, prompt ảnh + video nháp có Copy + dịch VI, ước tính độ dài lời) · ⑨ Thẻ prompt ảnh thật | Duyệt cả gói 1 lần trên `storyboard.html`: brief · claim (sản phẩm mới) · **đúng nhân vật** · script · cảnh. Sửa cảnh nào nói cảnh đó → **"ok cổng 1"** | `status.md` · `brief.md` · `refs/` · `scripts/script.md` · `scripts/storyboard.json/.md/.html` · `prompts-used/prompt-pack.md` |
| **2a. Ảnh** | Gen ảnh thật theo đợt phụ thuộc (ảnh có nhân vật / label: `--require-ref`, Image 1 = face-ref) → QC (có mục ☐ **đúng nhân vật**; lỗi → sửa 1 lần, vẫn lỗi → note user sửa tay) → prompt video chốt theo ảnh thật → **bảng clip** (`clips.json` → `clip-board.html`: ảnh khung đầu + prompt + lời + file lưu về) | **Duyệt ảnh + danh sách clip trên bảng clip** trước khi tốn credit video → **"ok 2a"** (hoặc "S03 sửa tay") | `outputs/images/` · `prompts-used/clips.json` · `outputs/review/clip-board.html` |
| **2b. Clip + âm thanh** | Tạo clip (Claude qua TopView/Higgsfield MCP/API, 1 gen + 1 sửa/clip · Flow / nền tảng khác → user tự render theo bảng clip) → `audio-plan.md` → gen VO (theo `VO_TOOL`) + gen nhạc (theo `MUSIC_TOOL`) → **chạy lại bảng clip**: khung hình thật, lời nghe được so với script, tỷ lệ, độ dài → `handoff.md` (âm thanh, dựng) | Render clip khi dùng Flow (test). Chọn SFX (+ nhạc nếu `MUSIC_TOOL=self`) → thả vào `outputs/`. Duyệt bảng clip → **"ok cổng 2"** | `outputs/videos/` · `outputs/audio/` · `prompts-used/audio-plan.md` · `handoff.md` |
| **3. Final** | **Kiểm đủ file** (mỗi cảnh có clip / ảnh MG, VO, nhạc, SFX; đúng tên; đúng 9:16) → dựng Remotion (chữ, logo, CTA trong vùng an toàn; xuất thêm bản phụ 4:5 nếu có) → bản review `outputs/review/` → **bảng review có transcript** (`_tools/review-board.py`: 2 khung hình tiêu biểu / cảnh + lời nghe được đúng đoạn đó so với script + dịch VI, lời tràn cảnh, lặng dài, nói nhanh) → sửa theo góp ý → final + loudness + compliance | Xem video + `review-board.html`, góp ý theo mã cảnh → duyệt final → **"ok cổng 3"** | `outputs/review/` · `outputs/final/` |

### Cách báo cho user (mọi lần dừng)

Ngắn, chỉ 3 phần, tối đa ~10 dòng. Không giải thích quy trình, không kể lại đã đọc gì, trừ khi user hỏi.

```
✅ Xong: [1 dòng — làm được gì]
⛔ Cần duyệt: [đúng câu hỏi / lựa chọn user phải trả lời]
📁 File: [file chính — gửi kèm file card]
```

- Ảnh, storyboard, video: **gửi file card hiển thị trực tiếp** (`display: render`), không dán link đường dẫn (link có dấu cách / ngoài thư mục đang mở thường không mở được). Nhiều ảnh → gom vào `storyboard.html` hoặc 1 ảnh ghép.
- Vấn đề phát sinh → 1 dòng mỗi vấn đề, kèm lựa chọn để user chọn.

**Duyệt:** "ok cổng 1" · "ok 2a" · "ok cổng 2" · "ok cổng 3" → Claude ghi ✅ + tên người duyệt vào `status.md`.
**Muốn dừng giữa chừng:** nói trước, VD "dừng cho mình xem script" → Claude dừng đúng chỗ đó. Không nói → chạy liền.
**Cổng trước chưa ✅ → không làm việc của cổng sau.** Ngoại lệ duy nhất: user yêu cầu rõ.

### Không đổi
- Công cụ cho từng việc (ảnh, video, UGC, giọng đọc, nhạc) = **lựa chọn của user ở bước setup** (`~/.config/ai-studio/prefs.env`, hook báo mỗi session). Chưa chọn → hỏi 1 lần theo skill setup bước 1.
- Ảnh thật: gen ở cổng 2a, tối đa 1 gen + 1 sửa/ảnh. Clip: chỉ gen sau "ok 2a". Ảnh minh hoạ storyboard ở cổng 1 (`--quality low`) không tính lượt.
- Prompt video ở cổng 1 chỉ là **nháp** trong storyboard (copy thử được). Bản chốt viết sau khi ảnh thật đã pass. Mỗi scene = 1 clip render riêng.
- Lỗi thuộc chặng trước (VD script dài lúc dựng) → sửa ở file của chặng đó, ghi 1 dòng vào `status.md` mục Vấn đề.
- 1 campaign = 1 script. Không báo giá.

---

## Quy đổi tên cổng cũ

Các file trong `_workflows/`, `_skills/`, `_prompts/` còn ghi tên cổng cũ. Đọc theo bảng này — **tên cũ chỉ là tên bước bên trong, không phải điểm dừng**:

| Tên cũ | Thuộc cổng mới | Dừng chờ duyệt? |
|---|---|---|
| A (brief) · B (script) · C (storyboard) · 4A (thẻ ảnh — chỉ viết, chưa gen) | 1 | Chỉ dừng ở cuối, sau thẻ ảnh |
| gen ảnh · 4B (QC ảnh) · 4C (thẻ video) · 4D (âm thanh + gen VO) · 4E (bàn giao) | 2 | Chỉ dừng ở cuối, sau bộ bàn giao |
| D (kiểm asset) · E (final) | 3 | Dừng ở bản review + final |
| `/start` `/brief` `/script` `/storyboard` | việc của cổng 1 | — |
| `/assets` | cuối cổng 1 + cổng 2 | — |
| `/check` `/edit` | cổng 3 | — |

---

## Tiết kiệm token — Claude làm theo

1. **1 cổng ≈ 1 session.** Xong cổng → user mở session mới. `status.md` giữ trạng thái, không cần chat cũ. Session dài là nguồn tốn token lớn nhất.
2. **Đọc đúng file cần, không đọc cả chuỗi.** Xem bảng "Đọc gì khi nào" trong `CLAUDE.md`. Đã đọc trong session → không đọc lại.
3. **File lớn → grep, không đọc hết.** `ugc-workflow.md`, `_assets/broll-library/index.md` (dò `keywords.json` trước), product-brief cũ.
4. **Xem ảnh bản thu nhỏ:** `python3 _tools/thumb.py in.png outputs/review/_qc/in.jpg 768` rồi mới Read. Chỉ xem bản gốc khi cần soi chữ label.
5. **Xem clip bằng 3 khung** (đầu/giữa/cuối, rộng 480px) qua `ffmpeg`, không trích nhiều khung.
6. **Không chép lại nội dung** của file trước sang file sau — dẫn chiếu (`xem script.md §S02`).
7. **Gửi file vào chat 1 lần ở cuối cổng**, không gửi mỗi lần sửa nhỏ.
8. **Việc máy móc → lệnh bash** (đối tên file, đo duration), không suy luận từng file.
9. `status.md`: sửa đúng dòng thay đổi; mục Vấn đề mỗi ý 1 dòng.
