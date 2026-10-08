# Audio Plan — VO · nhạc nền · SFX · phối âm (lượt 4D)

> Dùng ở `/assets` lượt 4D, sau khi prompt video đã duyệt. Lưu `prompts-used/audio-plan.md`.
> Nếu cần đổi AUDIO CUES trong prompt video → chỉ sửa phần audio, ghi rõ thay đổi, giữ nguyên chuyển động đã duyệt.

## Bảng âm thanh

| Mốc | Scene | Lời đọc | Cách đọc · từ nhấn · nghỉ | Nhạc nền | SFX | Đồng bộ với hình | Chuyển âm sang cảnh sau | Tạo cùng clip / riêng |
|---|---|---|---|---|---|---|---|---|

## A. Voice-over

**1. Prompt chỉ dẫn giọng** (cho ElevenLabs voice design / chọn giọng — không đọc ra):
- Ngôn ngữ + giọng vùng: ...
- Đặc tính giọng + cảm xúc: ...
- Phong cách đọc: ...
- Tốc độ (~từ/giây), khoảng nghỉ, từ nhấn: ...
- Phát âm brand/tên sản phẩm: ... (chưa rõ → hỏi user, đánh dấu ⚠️)
- Không tự thêm lời, không âm đệm ("um", hơi thở giả).

**2. Lời đọc sạch** — chỉ nội dung đọc, mỗi câu 1 file. Claude gen ở cổng 2b theo `VO_TOOL` (connector ElevenLabs; không có connector hoặc `VO_TOOL=api` → `python3 _tools/gen-voice.py --text "…" --style "[tóm mục 1]" --out …`) → `outputs/audio/`, tên file `[campaign-code]_vo-[scene-id]_v[n].mp3` (VD 2026-06-LAUNCH_vo-S01_v1.mp3):
| File | Text | Ước tính (s) | Slot scene (s) | Vừa? |
|---|---|---|---|---|

Ước tính ~2.4 từ/s cho giọng chậm. Không vừa → đề xuất rút gọn, chờ user duyệt (script đã khoá ở cổng B — mọi sửa lời phải ghi vào `status.md` mục Vấn đề).

## B. Nhạc nền — 1 bản xuyên suốt

```
Duration: [tổng video + 2s đuôi]
Mood/style/tempo: ...
Instruments: ...
Timeline: 0–3s ... | 3–17s ... | 17–22s ... | 22–30s ...
Accent points: [mốc + lý do — VD 22.0s nhạc mở ra khi ra ngoài nắng]
VO space: giữ dải mid (~1–4kHz) thoáng; không melody chính đè lời
Tail: [fade/ring-out x s]
Instrumental only, no vocals.
```
Nguồn: `MUSIC_TOOL=elevenlabs` → connector, không có connector thì `python3 _tools/gen-music.py --provider elevenlabs_music` · `MUSIC_TOOL=api` → `gen-music.py` (nhà theo `MUSIC_PROVIDER`) — dùng khối trên làm `--prompt`, `--seconds` = Duration; `freesound_cc0` (miễn phí) cần thêm `--query` 2–4 từ khoá tiếng Anh từ Mood/style (VD "bright pop loop"), nghe 5 ứng viên, `--pick N` đổi bài · `MUSIC_TOOL=self` → prompt cho tool gen nhạc, HOẶC tiêu chí chọn bài royalty-free (kiểm license dùng cho ads), **người dùng tự gen/chọn → `outputs/audio/`** (VD 2026-06-LAUNCH_music_v1.mp3). Thêm vào Danh sách asset (Loại = nhạc).

## C. SFX

| Mã | Scene | Prompt (EN) | Nguồn âm · chất · cường độ · vang | Dài | Kích hoạt / mốc | Đuôi · tránh |
|---|---|---|---|---|---|---|

**Người dùng tự gen/chọn → `outputs/audio/`** (VD 2026-06-LAUNCH_sfx-01_pump-click_v1.mp3). Thêm từng SFX vào Danh sách asset (Loại = SFX).

Mốc SFX là **dự kiến** — chốt lại theo hành động thật của clip sau render (ở `/edit`).

## D. Phối âm
- VO rõ nhất (~-14 LUFS tổng, VO trội hơn nhạc ~10–12dB khi có lời).
- Nhạc duck dưới lời, nâng nhẹ ở khoảng không lời.
- SFX khớp hành động thực tế của clip.
- **Không tạo trùng**: âm nào thêm khi dựng thì clip không được tự sinh (mute hoặc prompt "no sound effects").
- Không để mỗi cảnh tự sinh nhạc riêng.
- Tránh chồng quá nhiều lớp, peak > -1 dBTP, vỡ âm, cắt đuôi đột ngột.
