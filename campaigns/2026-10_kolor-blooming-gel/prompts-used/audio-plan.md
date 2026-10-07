# Audio Plan — Kolor Blooming Gel "One Dot" · lượt 4D

Campaign `KOLOR-2026-10-BLOOM` · 20.0s · 9:16
Lưu tất cả file âm thanh vào: `outputs/audio/`

> ⚠️ **Đổi so với storyboard:** storyboard ghi VO là **1 file liền 20s**. Đổi thành **5 file theo scene**.
> Lý do: thời lượng mỗi clip đã cố định sau render — cắt VO theo scene thì khớp chính xác, không bị trôi dồn.
> Khoảng lặng ở giây 3 nằm **trong** file `vo-S01` nên nhịp đọc vẫn liền mạch như ý định ban đầu.

---

## Bảng âm thanh

| Mốc | Scene | Lời đọc | Cách đọc · nhấn · nghỉ | Nhạc nền | SFX | Đồng bộ với hình | Chuyển âm sang cảnh sau | Tạo cùng clip / riêng |
|---|---|---|---|---|---|---|---|---|
| 0.0–6.0 | S01 | "One dot. That's the whole flower." … "You didn't paint that. It bloomed." | Đều, khô, tự tin. Nhấn nhẹ *dot* và *paint*. **Nghỉ 1.0–1.2s** sau câu 1 | Vào ngay 0.0s, rất nhẹ, 1 lớp | `sfx-01` giọt rơi ~0.4s | Câu 1 xong trước khi màu bắt đầu nở; câu 2 vào đúng lúc hoa mở rộng | Nhạc giữ nguyên, không ngắt | **Riêng** — clip mute |
| 6.0–11.0 | S02 | "Clear blooming gel over your cured base. Drop your color in." | Nhịp dạy nghề, rõ từng từ. Nghỉ ngắn sau *base* | Giữ nền | `sfx-02` cọ lướt ~6.8s | *"Drop your color in"* kết đúng lúc giọt đỏ chạm móng (~10.5s) | Nhạc giữ nguyên | **Riêng** |
| 11.0–14.0 | S03 | "It spreads itself. In seconds." | **Nghỉ 0.4s** sau *itself*, để *In seconds* đứng riêng | Giữ nền | — | *"spreads itself"* vào lúc màu bắt đầu loang | Nhạc nhích lên nhẹ | **Riêng** |
| 14.0–17.0 | S04 | "Florals, marble, croc, ombre. One bottle." | 4 từ đọc tách nhịp đều nhau | Giữ nền | `sfx-03` 4 tiếng cut nhẹ, khớp 4 nhát cắt | Mỗi từ khớp 1 nhát cắt hình | Nhạc bắt đầu thưa dần | **Riêng** |
| 17.0–20.0 | S05 | "Crystal clear, never yellows. Kolor Acrylic." | Chậm lại, hạ giọng. Tên brand đọc bình thường, **không nhấn** | Thưa dần rồi tắt | — | Chữ end card hiện cùng lúc đọc tên brand | Kết | **Riêng** |

---

## A. Voice-over

### 1. Chỉ dẫn giọng (không đọc ra)

- **Ngôn ngữ / vùng:** English, American, giọng trung tính không vùng miền rõ
- **Đặc tính + cảm xúc:** nữ 25–35, ấm vừa, hơi khô, điềm tĩnh và chắc. Không phấn khích, không "bán hàng"
- **Phong cách đọc:** như thợ nail chỉ một mẹo cho đồng nghiệp — nói với người trong nghề, không giải thích thừa
- **Tốc độ:** ~2.0–2.2 từ/giây (chậm hơn mặc định). Không tăng tốc để nhét chữ
- **Ngữ điệu:** câu kết đi xuống, **không lên giọng cuối câu**
- **Phát âm:** `Kolor` đọc đúng như chữ *color* — ⚠️ KHÔNG đọc rời từng chữ cái hay thành "ko-lor"
- **Cấm:** tự thêm lời, "um/uh", hơi thở giả, cười trong giọng

**Voice ElevenLabs đề xuất:** `Lyan – Clean Natural Explainer Female` (`OHbs18UsFunlwffsTLNn`) — UGC/explainer giọng Mỹ, không bóng bẩy. Model `eleven_v3`.

### 2. Lời đọc sạch

| File | Text | Ước tính (s) | Slot scene (s) | Vừa? |
|---|---|---|---|---|
| `KOLOR-2026-10-BLOOM_vo-S01_v1.mp3` | One dot. That's the whole flower. *(nghỉ)* You didn't paint that. It bloomed. | ~5.8 (12 từ + nghỉ 1.1s) | 6.0 | ✅ vừa |
| `KOLOR-2026-10-BLOOM_vo-S02_v1.mp3` | Clear blooming gel over your cured base. Drop your color in. | ~5.0 (11 từ) | 5.0 | ⚠️ sát — phải đọc đúng 2.2 từ/s |
| `KOLOR-2026-10-BLOOM_vo-S03_v1.mp3` | It spreads itself. In seconds. | ~2.9 (5 từ + nghỉ 0.4s) | 3.0 | ✅ vừa |
| `KOLOR-2026-10-BLOOM_vo-S04_v1.mp3` | Florals, marble, croc, ombre. One bottle. | ~3.0 (6 từ) | 3.0 | ⚠️ sát |
| `KOLOR-2026-10-BLOOM_vo-S05_v1.mp3` | Crystal clear, never yellows. Kolor Acrylic. | ~3.0 (6 từ) | 3.0 | ⚠️ sát |

**Tổng 40 từ / 20.0s.** Ba slot sát nhịp — nếu bản gen nào tràn, **không rút lời** (lời đã khoá ở cổng B); cách xử lý theo thứ tự: (1) gen lại với pace chậm hơn một chút, (2) cho phép tràn tối đa 0.3s và bù bằng cách kéo dài giữ hình cuối cảnh ở `/edit`, (3) nếu vẫn không được thì mới xin sửa lời và ghi vào `status.md`.

---

## B. Nhạc nền — 1 bản xuyên suốt

```
Duration: 22 seconds (20s video + 2s đuôi)
Mood/style/tempo: minimal, clean, modern beauty-ad bed. Calm and confident,
  not hyped. ~90 BPM felt, no drop, no build-up cliché.
Instruments: soft analog synth pad, muted plucked synth notes, light shaker or
  finger-snap texture for pulse, subtle low sine for warmth. No drums kit.
Timeline:
  0–6s    one sparse pad + a few plucked notes, lots of space
  6–11s   add light rhythmic pulse, stays underneath
  11–14s  tiny lift — one extra plucked layer
  14–17s  pulse becomes slightly more present for the four quick cuts
  17–20s  thin out to pad only, settle
  20–22s  ring out and fade
Accent points: 11.0s (nhấc nhẹ khi màu bắt đầu loang) · 14.0s (vào loạt cắt nhanh)
VO space: giữ dải mid ~1–4kHz thoáng, không melody chính đè lời
Tail: ring-out 2s
Instrumental only, no vocals.
```

Người dùng tự gen/chọn → `outputs/audio/KOLOR-2026-10-BLOOM_music_v1.mp3`
Nếu lấy nhạc royalty-free: **kiểm license cho phép dùng trong paid ads**.

---

## C. SFX

| Mã | Scene | Prompt (EN) | Nguồn âm · chất · cường độ | Dài | Mốc dự kiến | Đuôi · tránh |
|---|---|---|---|---|---|---|
| `sfx-01` | S01 | A single small droplet of thick liquid landing on a smooth glossy surface, close-mic, soft and rounded, no splash | Rất khẽ, gần như dưới ngưỡng. Không vang | ~0.4s | ~0.4s | Không "plop" kiểu cartoon, không echo |
| `sfx-02` | S02 | A soft fine brush gliding once across a smooth wet surface, very quiet, close-mic | Khẽ, mượt, 1 nhát duy nhất | ~0.8s | ~6.8s | Không tiếng cọ khô, không sột soạt |
| `sfx-03` | S04 | Four short clean transition ticks, soft and dry, evenly spaced | Gọn, khô, không âm vang | 4 × ~0.1s | 14.0 / 14.7 / 15.4 / 16.1s | Không whoosh, không riser |

Người dùng tự gen/chọn → `outputs/audio/`
Mốc SFX là **dự kiến** — chốt lại theo hành động thật của clip ở `/edit`.

---

## D. Phối âm

- VO rõ nhất. Tổng ~−14 LUFS, VO trội hơn nhạc ~10–12 dB khi có lời
- Nhạc duck dưới lời, nâng nhẹ ở khoảng lặng giây 3 và giây 11
- SFX rất khẽ — đây là video đẹp mắt, không phải video ASMR; âm thanh chỉ để đỡ hình
- **Clip Veo mute toàn bộ** — mọi âm đều thêm khi dựng, không để trùng
- Không để mỗi cảnh tự sinh nhạc riêng
- Peak không vượt −1 dBTP

---

## Sau khi duyệt 4D

Claude gen 5 file VO qua ElevenLabs → `outputs/audio/`.
Nhạc và 3 SFX do người dùng gen/chọn.

---

# KẾT QUẢ GEN VO — 2026-10-01

**Flow ElevenLabs:** https://elevenlabs.io/app/flows/JhefK85zKFVRTei6EY4y
Voice: `Lyan - Beauty, Lifestyle` (`OHbs18UsFunlwffsTLNn`) · model `eleven_v3` · 2 bản mỗi câu.

> ⚠️ **Claude không tải được file về.** Egress của cả máy lẫn cloud đều chặn `storage.googleapis.com`.
> Người dùng mở flow, tải bản được chọn, đổi tên theo cột "Lưu" rồi thả vào `outputs/audio/`.

## Bản được chọn

| Scene | Bản chọn | Dài thực tế | Lưu |
|---|---|---|---|
| S01 | Take 1 | **6.24s** | `KOLOR-2026-10-BLOOM_vo-S01_v1.mp3` |
| S02 | Take 1 | **3.68s** | `KOLOR-2026-10-BLOOM_vo-S02_v1.mp3` |
| S03 | Take 2 (bản ngắn hơn) | **2.88s** | `KOLOR-2026-10-BLOOM_vo-S03_v1.mp3` |
| S04 | Take 2 (bản ngắn hơn) | **3.84s** | `KOLOR-2026-10-BLOOM_vo-S04_v1.mp3` |
| S05 | Take 2 (bản ngắn hơn) | **3.20s** | `KOLOR-2026-10-BLOOM_vo-S05_v1.mp3` |

**Tổng VO thực tế: 19.84s** — khớp gần như chính xác 20s của brief.

## Phân bổ lại mốc thời gian

Tổng thì vừa, nhưng **phân bổ giữa các scene lệch so với dự kiến**: S02 ngắn hơn ước tính 1.3s, còn S04 và S05 dài hơn. Chỗ dư của S02 vừa đủ bù cho hai cảnh sau.

| Scene | Slot cũ | **Slot mới** | VO | Ghi chú |
|---|---|---|---|---|
| S01 | 0.0–6.0 | **0.00–6.24** | 6.24 | Clip dài 6.016s → giữ khung cuối thêm ~0.25s |
| S02 | 6.0–11.0 | **6.24–10.60** | 3.68 | Dư 0.68s im lặng — đặt ở đầu, để cọ bắt đầu hạ xuống trước khi có lời |
| S03 | 11.0–14.0 | **10.60–13.60** | 2.88 | Dư 0.12s |
| S04 | 14.0–17.0 | **13.60–17.50** | 3.84 | Nhịp 4 nhát cắt giãn ra ~0.96s/nhát |
| S05 | 17.0–20.0 | **17.50–20.80** | 3.20 | End card |

**Tổng: 20.80s.** Rút về đúng 20.0s bằng cách **cắt khoảng lặng đầu/cuối của 5 file VO** ở `/edit` (thường mỗi file dư 0.1–0.3s) — không đụng vào lời.

## Ghi chú kỹ thuật

⚠️ **Prompt S05 viết "Color Acrylic" thay vì "Kolor Acrylic"** — cố ý, để TTS phát âm đúng. Âm thanh nghe ra đúng *"Kolor Acrylic"*. Lời trong script **không đổi**.

⚠️ **Cần nghe kiểm trước khi dựng:** S01 dùng tag `[pause]` giữa 2 câu — kiểm tra model có nghỉ thật không, hay đọc luôn "pause".

---

# ĐO FILE VO THẬT — 2026-10-01 (sau khi tải về)

5 file đã đổi tên đúng quy ước, nằm ở `outputs/audio/`.

| File | Dài thật | Ghi chú |
|---|---|---|
| `vo-S01` | 6.27s | Bản dài hơn trong 2 take |
| `vo-S02` | 3.71s | |
| `vo-S03` | 3.16s | Bản dài hơn (take đã chọn là 2.88s) |
| `vo-S04` | 3.97s | Bản dài hơn (take đã chọn là 3.84s) |
| `vo-S05` | 3.40s | Bản dài hơn (take đã chọn là 3.20s) |

**Tổng: 20.51s.**

## ⚠️ Phát hiện: khoảng nghỉ trong S01 dài gấp đôi dự kiến

Đo bằng `silencedetect`: `vo-S01` có **2.15 giây im lặng** từ 2.09s đến 4.24s.
Tag `[pause]` có tác dụng — model nghỉ thật, **không đọc ra chữ "pause"** — nhưng nghỉ quá dài. Bảng âm thanh dự kiến 1.0–1.2s.

Cấu trúc file:
```
0.00 – 2.09   "One dot. That's the whole flower."
2.09 – 4.24   im lặng 2.15s   ← quá dài
4.24 – 6.27   "You didn't paint that. It bloomed."
```

**Xử lý ở `/edit`:** cắt khoảng im lặng giữa xuống còn ~1.1s → `vo-S01` còn ~5.2s, vừa khít clip S01 (6.016s) và còn dư chỗ thở. Không cần gen lại.

## Khoảng lặng đầu/cuối

Mỗi file có ~0.15–0.28s im lặng ở cuối, đầu file gần như không có. Cắt đuôi 5 file được thêm ~1.0s.

**Tổng sau khi cắt: ≈ 19.4s** — nằm trong khung 15–20s của brief.
