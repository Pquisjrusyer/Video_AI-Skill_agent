# Character Profile — [TÊN NHÂN VẬT]

> **Hướng dẫn:** Copy folder `_template` → đổi tên thành tên nhân vật → điền thông tin bên dưới. Mỗi nhân vật dùng nhất quán xuyên suốt các campaign để build brand familiarity.

---

## Identity

| Field | Thông tin |
|-------|-----------|
| **Tên (fictional)** | [VD: Sarah] |
| **Tuổi** | [VD: 34] |
| **Giới tính** | [VD: Female] |
| **Ethnicity** | [VD: White American / Asian American / Latina — chọn phù hợp với ICP] |
| **Nghề nghiệp (trong video)** | [VD: Freelance designer, work from home] |
| **Location feel** | [VD: US Pacific Northwest — Seattle/Portland vibes] |

---

## Physical Description (dùng cho thẻ prompt ảnh Nano Banana Pro + Veo 3 — người dùng tự gen theo thẻ)

> **Quan trọng:** Mô tả càng cụ thể càng giúp AI generate nhất quán. Không dùng tên người thật.

```
Age appearance: [VD: Early-to-mid 30s]
Hair: [VD: Dark brown shoulder-length hair, slight wave, natural texture]
Eyes: [VD: Brown eyes, minimal makeup]
Skin: [VD: Light olive skin, natural glow, no heavy foundation look]
Build: [VD: Average build, relatable — not model-thin]
Style: [VD: Casual but put-together — linen tops, minimal jewelry]
Distinguishing features: [VD: Small freckles across nose, warm smile]
```

---

## Personality & Backstory

**Backstory ngắn (dùng khi viết script ở `/script`):**
> [VD: "Sarah là freelance graphic designer, mẹ của 1 đứa con 5 tuổi. Bận rộn nhưng luôn cố maintain self-care routine. Đã thử nhiều sản phẩm skincare, hay skeptical với quảng cáo. Khi tìm ra thứ work, cô nói thật và thẳng thắn với bạn bè — không over-hype."]

**Tính cách thể hiện trong video:**
- Relatable, not perfect
- Nói tự nhiên — có pause, có filler words nhẹ ("you know", "honestly", "like")
- Không đọc script — nói như đang kể với bạn
- Genuine emotion — không quá excited kiểu infomercial

**Điều cô ấy KHÔNG làm trong video:**
- Không nói "This product is amazing!" một cách vô hồn
- Không nhìn camera 100% thời gian (thỉnh thoảng look away tự nhiên)
- Không gesticulate quá nhiều

---

## Voice Profile (dùng cho ElevenLabs / OpenAI TTS VO, mô tả giọng trong thẻ take Google Flow, TopView TTS)

```
Accent: American English, neutral / slight Pacific Northwest
Pace: Moderate — không quá nhanh, không quá chậm. ~140 wpm
Pitch: Mid-range, warm
Energy: Calm enthusiasm — excited nhưng không hype
Filler words OK: "honestly", "like", "you know", "I mean"
Pause style: Natural pauses trước key points
```

---

## Setting thường xuất hiện

| Setting | Khi nào dùng | Veo 3 / Nano Banana direction |
|---------|-------------|-------------------------------|
| **Home bathroom** | Morning routine, skincare video | Warm lighting, white/beige tiles, products visible on shelf |
| **Kitchen counter** | Supplement, food product | Natural light from window, marble or wood counter |
| **Living room couch** | Casual testimonial | Soft afternoon light, neutral couch, plants in background |
| **Outdoor — backyard/patio** | Lifestyle, feel-good content | Dappled sunlight, green background, casual setting |

---

## Prompt Snippet (paste vào Veo 3 / Nano Banana prompts)

```
[CHARACTER PROMPT BLOCK — copy-paste vào prompt khi cần nhân vật này]

A woman in her early-to-mid 30s with dark brown shoulder-length wavy hair, 
light olive skin with natural freckles, brown eyes, minimal makeup. 
Wearing casual linen clothing. Warm, relatable appearance — 
not a model, a real person. Calm, genuine expression.
```

---

## Consistency Notes

- **Đã dùng trong campaigns:** [Liệt kê campaign IDs đã generate nhân vật này]
- **Seed image:** `reference-images/[name]-face-ref-01.png` — người dùng tự gen theo thẻ ở `/assets` 4A, duyệt ở 4B rồi copy vào đây.
- **Reference images:** Lưu vào `reference-images/` folder — đính kèm làm ref 1 (nhận diện) khi người dùng tự gen theo thẻ prompt để giữ consistency
- **Không mix** nhân vật này với character khác trong cùng 1 video (tránh audience confusion)
