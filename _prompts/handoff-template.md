# Handoff Pack — bàn giao render & dựng (lượt 4E)

> Dùng ở `/assets` lượt 4E, sau khi 4A–4D đã ✅. Lưu `prompts-used/handoff.md`. **Chỉ tổng hợp nội dung ĐÃ DUYỆT** — không viết mới, không đổi chuyển động/lời. Thứ gì chưa duyệt → ghi ⚠️ và dừng hỏi.
> Không render tại đây. Mục tiêu: người render / người dựng copy được ngay, không phải mở file khác.

## A. Bảng render (mỗi cảnh 1 khối)

```
### [SCENE ID] · [tên file clip — `[campaign-code]_[scene-id]_[mô-tả-ngắn]_v[n].mp4`, VD 2026-06-LAUNCH_S01_mirror_v1.mp4 → outputs/videos/]
Tool / model:            Veo 3.1 · image-to-video · 9:16 · 1080p
Ảnh đầu vào + vai trò:   First frame = [file] · (last frame / ref nếu tool hỗ trợ)
Render:                  [4/6/8]s        Dùng khi dựng: [in–out, VD 0.4–3.4s = 3.0s]
Âm tạo cùng clip:        [VD: không — mute khi dựng]
Âm thêm sau:             [vo-S01 · sfx-02 · music — file trong outputs/audio/, VD 2026-06-LAUNCH_vo-S01_v1.mp3]
PROMPT (đã gộp AUDIO CUES đã duyệt — copy nguyên văn):
...
Kiểm khung đầu:          ☐ khớp ảnh đầu vào (mặt, sản phẩm, ánh sáng)
Kiểm khung cuối:         ☐ [trạng thái cuối yêu cầu] ☐ giữ yên đủ [x]s để nối
```
Cảnh MOTION-GRAPHIC: ghi "Dựng bằng Remotion ở /edit — không render ở tool ngoài" + asset nguồn.

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
