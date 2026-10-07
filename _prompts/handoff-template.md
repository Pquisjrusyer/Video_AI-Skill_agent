# Handoff Pack — bàn giao render & dựng (cổng 2)

> 2 phần:
> - **Bảng clip** (mục 0) — làm **ngay khi ảnh thật pass, TRƯỚC khi tạo clip**: đây là chỗ user nhận prompt video để render (hoặc theo dõi khi Claude gen qua TopView/Higgsfield). Sau khi có clip → chạy lại để duyệt.
> - **`prompts-used/handoff.md`** (mục B–D) — âm thanh, hướng dẫn dựng, tiêu chí duyệt. Không chép prompt video vào đây.
> **Chỉ tổng hợp nội dung ĐÃ DUYỆT.** Thứ gì chưa duyệt → ghi ⚠️ và dừng hỏi.


## 0. Bảng clip — bàn giao + duyệt (bắt buộc khi có clip video)

Claude ghi `prompts-used/clips.json` → chạy `python3 _tools/clip-board.py campaigns/[campaign]` → `outputs/review/clip-board.html` → hỏi user **Xem tại đây** (file card `display: render`) hay **Mở trên trình duyệt** (`sh _tools/open-browser.sh outputs/review/clip-board.html`).
- **Trước khi render:** bảng bàn giao — mỗi cảnh: mã · thời gian · mục đích · công cụ + cài đặt · render/dùng (s) · ảnh khung đầu · prompt EN (nút Copy) + dịch VI · lời thoại EN + VI · file lưu về · ô "Xong".
- **Sau khi có clip** (Claude gen xong hoặc user thả vào `outputs/videos/`): chạy lại đúng lệnh → mỗi cảnh thêm 3 khung hình cắt từ clip thật, **lời nghe được trong clip** (faster-whisper) so với lời script (chữ thiếu gạch đỏ, chữ thừa tô vàng, % khớp) và kiểm tra: 9:16 · đủ độ dài · lời không vượt đoạn dùng · tốc độ nói ≤ 3.2 từ/giây. Báo user lỗi theo từng cảnh, chỉ làm lại cảnh lỗi.

```json
{
  "campaign": "KREIZI-2026-10-HONEST",
  "title": "Flow có lời",
  "wps": 2.4,
  "ratio": "9:16",
  "duration": "20s",
  "platform": {"ids": ["meta_reels", "tiktok"], "extra_ratios": ["4:5"]},
  "character": {"name": "dana", "images": ["../../_characters/dana/reference-images/dana-face-ref-01.png"], "identity_lock_en": "…", "identity_vi": "…"},
  "howto": "1 dòng thao tác cho người render (chỉ cần khi user tự render, VD Flow: Veo 3.1 → Frames to Video → upload ảnh → 9:16 → dán prompt → tải 1080p)",
  "clips": [
    {
      "id": "S1", "time": "0.0–7.5s", "purpose": "Hook",
      "tool": "Flow · Veo 3.1 · Frames to Video · 9:16",
      "tool_id": "flow | higgsfield | topview — chọn khối '⚙️ Hướng dẫn setting' (`_tools/video-tools.json`); bỏ trống → tự đoán từ `tool`",
      "render_s": 8, "use_s": 7.5,
      "first_frame": "outputs/images/[code]_A-02_take-A-talk_v1.png",
      "prompt_en": "Prompt nguyên văn (EN)",
      "prompt_vi": "Dịch prompt (VI)",
      "line_en": "Lời thoại / VO của cảnh này — để trống nếu cảnh không có lời",
      "line_vi": "Dịch lời thoại (VI)",
      "audio": "in-clip | vo:outputs/audio/[code]_vo-S01_v1.mp3 | none",
      "notes_vi": "Kiểm khung cuối, âm thêm sau khi dựng (vo/sfx/nhạc)…",
      "out": "outputs/videos/[code]_S1_hook_v1.mp4"
    }
  ]
}
```
- `audio`: `in-clip` = lời nằm trong clip (Flow có lời, TopView, Higgsfield) · `vo:…` = lời là file VO riêng → kiểm VO đó có vừa đoạn dùng của cảnh không · `none` = cảnh không lời.
- `wps`: tốc độ đọc để ước tính độ dài lời (VO ElevenLabs/OpenAI ≈ 2.4 · UGC Flow có lời ≈ 2.7 — đã test 20 từ / 7.4s). Bảng hiện "N từ ≈ Xs · cảnh dùng Ys ✅/⚠️" ngay cả khi chưa có âm thanh.
- `render_s` và `use_s` chỉ ghi ở đây — mọi chỗ khác dẫn chiếu, không gõ lại (tránh lệch kiểu cột ghi 6s nhưng prompt ghi 8s).

## A. Prompt render — KHÔNG ghi ở đây

Prompt video, ảnh khung đầu, cài đặt công cụ, render/dùng (s), âm tạo cùng clip, kiểm khung cuối → **chỉ nằm trong bảng clip** (mục 0, `clips.json` → `clip-board.html`). `handoff.md` không chép lại prompt — 1 nguồn duy nhất, tránh lệch số giữa 2 nơi.
Cảnh MOTION-GRAPHIC: vẫn có 1 dòng trong `clips.json` với `tool: "Remotion"`, `prompt_en` để trống, `notes_vi` ghi asset nguồn.

## B. Bộ âm thanh
- **VO:** prompt chỉ dẫn giọng + bảng lời đọc sạch (file · text · ước tính s) — copy từ `audio-plan.md`. Ghi voice_id/settings nếu Claude đã gen.
- **Nhạc nền:** prompt 1 bản xuyên suốt — người dùng tự gen/chọn → `outputs/audio/` (VD 2026-06-LAUNCH_music_v1.mp3).
- **SFX:** từng mã · prompt EN · mốc dự kiến — người dùng tự gen/chọn → `outputs/audio/` (VD 2026-06-LAUNCH_sfx-01_pump-click_v1.mp3).
- **Timeline phối âm:**

| Mốc | VO | Nhạc (mức) | SFX | Ghi chú |
|---|---|---|---|---|

## C. Hướng dẫn dựng
| # | Cảnh | In–out trên timeline | Cắt / nối | Chữ hiển thị · thời điểm · vị trí | Âm đồng bộ |
|---|---|---|---|---|---|

- Logo / CTA: [vị trí, thời điểm, nội dung nút]
- Cân màu & độ sáng: [nhiệt màu chung, khớp các clip, không đẩy saturation da]
- Xuất: [ratio · độ phân giải · fps · codec · loudness -14 LUFS · tên file theo naming convention] — theo brief + khả năng tool dựng (mặc định Remotion ở `/edit`)

## D. Tiêu chí duyệt video
- ☐ Đúng thời lượng + tỷ lệ brief
- ☐ Thông điệp rõ, CTA dễ hiểu
- ☐ Nhân vật + sản phẩm nhất quán mọi cảnh
- ☐ Không méo tay, lỗi phản chiếu, sai bao bì, chuyển động bất thường
- ☐ Khung cuối đạt trạng thái yêu cầu
- ☐ Lời quảng cáo đúng claim APPROVED / thông tin được cung cấp
- ☐ Chữ đọc được trên điện thoại (xem ở kích thước thật)
- ☐ VO không gấp, không bị cắt
- ☐ Nhạc không lấn lời; SFX khớp hình
- ☐ Không khung đen, nhấp nháy, âm đứt đoạn
- ☐ + checklist Meta Ads compliance trong `CLAUDE.md`

---

# Mẫu phản hồi SAU KHI NHẬN RENDER (dùng ở `/check` cho clip, `/edit` cho bản dựng)

| Cảnh / mốc | Lỗi quan sát được | Nguyên nhân có thể | Prompt sửa / cách chỉnh khi dựng | Giữ nguyên |
|---|---|---|---|---|
| S03 · 2.1–2.8s | VD: ngón tay nhân đôi khi chạm má | (suy đoán) rack focus + tay sát mặt | Prompt: bỏ rack focus, "static macro" · hoặc dựng: cắt out ở 2.0s | Giọt gel 0.5–1.8s, label rõ |

Quy tắc: nguyên nhân chưa chắc → ghi "(suy đoán)". Chỉ sửa đúng chỗ lỗi — **không đổi concept, không làm lại cảnh đã đạt.** Chờ user duyệt thay đổi trước khi gửi prompt sửa / dựng lại.
