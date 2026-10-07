# Shot Card Template — 14 Fields

> **Thư viện tham khảo — không bắt buộc, không phải deliverable.** Output chuẩn ở `/assets` lượt 4C là thẻ `_prompts/veo3/video-prompt-card.md` (Veo 3.1 image-to-video, render 4/6/8s; độ dài render ≠ độ dài dùng). Dùng 14 field này để nghĩ kỹ direction khi cần; nếu mâu thuẫn với thẻ → theo thẻ.

> Fill tất cả 14 fields trước khi viết prompt. Field trống = direction còn thiếu → điền hoặc bỏ shot.

---

## Template (copy cho mỗi shot)

```
Shot ID:          [01, 02, 03...]
Beat:             [Điều gì thay đổi trong story ở shot này]
Emotion:          [Fear / Shame / Anger / Guilt / Resolve / Relief / Joy / Tension...]
Frame:            [Wide / Medium / Close-up / Macro insert]
Composition:      [Center / Edge / Negative space / Reflection / Silhouette / Foreground obstruction]
Camera:           [Static / Push-in / Handheld / Tracking / Whip-pan / Rack focus]
Movement reason:  [Tại sao camera di chuyển ở đây — "what changed?"]
Action:           [Sự kiện vật lý cụ thể đang xảy ra]
Eye trace:        [Mắt người xem nhìn vào đâu trong 0.3s đầu]
Duration:         [0.5s / 1s / 2s / 3s... — độ dài DÙNG khi dựng; render Veo vẫn 4/6/8s]
Cut type:         [Match cut / Smash cut / Cut on action / J-cut / L-cut]
Sound:            [Breath / Bass hit / Street noise / Silence / Specific sound cue]
Light / Color:    [Cold / Warm / High contrast / Flicker / Shadow / Specific palette]
Production note:  [Prop, location, actor direction, wardrobe detail]
```

---

## Three-detail check (bắt buộc trước khi submit)

Mỗi shot phải có cả 3:

- [ ] **Environmental pressure** — sự thật vật lý về không gian mang cảm xúc *(VD: ánh đèn huỳnh quang nhấp nháy, kính ướt, hơi nước từ ấm đun)*
- [ ] **Physical micro-action** — cảm xúc dịch thành cơ thể *(VD: hàm răng siết lại, ngón tay cong vào khung cửa, mắt rơi xuống một phần tư inch)*
- [ ] **Sound anchor / visual motif** — hook cảm giác lặp lại *(VD: tiếng dạ dày 3 lần, phản chiếu trong kính tối ở mỗi transition)*

---

## Dramaturgy check (chạy trước khi gửi prompt)

- [ ] Scene formula đủ? *(desire + obstacle + geometry + gaze + rhythm)*
- [ ] Mỗi shot pass three-detail check?
- [ ] Mỗi shot làm ít nhất 1 trong 3 jobs? *(change emotion / advance action / increase pressure)*
- [ ] Camera movement có motivated reason?
- [ ] Spatial geometry đọc được?
- [ ] Five anchors đã đặt tên? *(emotion / motif / object / break / final image)*

---

## Worked example — Testimonial DTC (15s, Veo 3)

**Five anchors:**
- Emotion: Relief / Discovery
- Motif: Ánh sáng tự nhiên tăng dần qua các shot
- Anchor object: Lọ serum trên bàn trang điểm
- Break: Cô ấy nhìn vào gương lần đầu sau khi dùng
- Final image: Nụ cười phản chiếu trong gương, tay chạm nhẹ vào má

> Cột Duration (0.3–3s) = **nhịp cắt khi dựng ở /edit, không phải đơn vị render.** Mỗi scene vẫn render 1 clip 4/6/8s rồi cắt.

| Shot | Beat | Emotion | Frame | Duration | Three details |
|------|------|---------|-------|----------|---------------|
| 01 | Hook — tay cầm lọ serum | Curiosity | Close-up | 2s | Ánh sáng sớm mờ / ngón tay xoay nắp chậm / tiếng nắp click |
| 02 | Nhỏ serum ra tay | Anticipation | Macro | 1s | Giọt trong suốt / ngón trỏ chạm lòng bàn tay / tiếng nhỏ giọt |
| 03 | Thoa lên mặt, mắt nhắm | Sensation | Medium | 2s | Ánh sáng cửa sổ bên trái / môi hé / im lặng |
| 04 | Mở mắt nhìn gương | Discovery | Close-up | 1.5s | Gương phản ánh cửa sổ / lông mày nhích lên / hơi thở ra |
| 05 | Nụ cười, chạm má | Relief | Medium | 3s | Ánh sáng ấm đầy gương / bàn tay chạm nhẹ / nhạc nền fade in |

---

## Rhythm ladders tham khảo

> Nhịp cắt khi dựng ở /edit, không phải đơn vị render.

**Testimonial DTC (15s):**
3s → 2s → 1.5s → 1s → 0.5s (product macro) → 2.5s (hero smile)

**Product demo (30s):**
4s → 2s → 2s → 1s → 1s → 0.5s → pause → 3s → 2s → 1s → 5s (lifestyle)

**Anxiety/problem → solution (15s):**
2s → 1s → 0.5s → 0.3s → pause → 3s → 2s → 4s
