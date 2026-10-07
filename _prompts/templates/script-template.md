# Script — [TÊN SCRIPT]

> Lưu tại `campaigns/[campaign]/scripts/script.md` (luôn tên này). Viết/kiểm ở `/script`, dừng cổng B.

---

## Metadata

| Field | Thông tin |
|-------|-----------|
| **Campaign** | [Campaign code] |
| **Format** | [UGC / Voiceover / Product demo / Motion graphic] |
| **Character** | [Tên nhân vật] |
| **Product** | [Tên sản phẩm] |
| **Duration** | [15s / 20s / 30s] |
| **Ratio** | [9:16 / 4:5] |
| **Audience stage** | [Cold / Warm / Retargeting] |
| **Status** | [Draft / Approved / Used] |

---

## Script

```
[0–3s — HOOK]
"[Câu mở đầu — xong trong 3 giây]"

[3–8s — PROBLEM]
"[Mô tả pain point bằng ngôn ngữ khách hàng thực sự dùng]"

[8–18s — DISCOVERY + PRODUCT]
"[Kể về việc tìm ra sản phẩm — tự nhiên, không over-hype]"
[ACTION: e.g., holds up product]
"[Key benefit — chỉ dùng approved claims]"

[18–[X]s — RESULT]
"[Kết quả cụ thể, có thể relate — không quá dramatic]"

[Last 3s — CTA]
"[Soft CTA: VD: 'Link is in the comments', 'Worth trying']"
```

## Lời theo cảnh (EN + dịch VI — bắt buộc)

| Cảnh | Thời gian | Lời thoại / VO (EN, nguyên văn) | Dịch (VI) | Chữ trên màn hình |
|---|---|---|---|---|
| S01 | 0.0–3.5s | | | |

> Bảng này là nguồn cho `line_en` / `line_vi` trong `storyboard.json` và `clips.json` — chép nguyên văn, không viết lại.

**Word count:** [XX] từ / [XX] giây — VO/ElevenLabs ≈ 2.4 từ/giây (30s ≈ 70 từ) · UGC/Google Flow ≤ 20 từ/take (8s) · UGC/TopView ≈ 3.5 từ/giây, mỗi take < 40 từ

---

## Claim check

| Câu trong script (nói về sản phẩm) | Claim APPROVED tương ứng (`product-brief.md`) | OK / ⚠️ |
|---|---|---|
| | | |

> Không map được claim approved → ⚠️, đề xuất bản sửa.

---

## TAKE (UGC)

> Chỉ cho UGC. Mỗi trạng thái ảnh (tay trống / cầm sản phẩm A…) = 1 take (`_workflows/ugc-workflow.md` Bước 2). Mỗi take < 40 từ, bỏ em dash (—).

| Take | Trạng thái ảnh | Lời (nguyên văn) | Số từ |
|---|---|---|---|
| take-A | | | |

---

## VO / TTS direction

> Hướng dẫn giọng đọc cho ElevenLabs (Voiceover) hoặc mô tả giọng trong thẻ take UGC (Flow) / TopView TTS — giọng, pace, chỗ nghỉ

**Delivery style:** [VD: Calm, genuine — NOT excited. Natural pauses before key benefit lines.]

**Key moments:**
- [Second X]: [VD: Slight smile khi mention kết quả]
- [Second X]: [VD: Hold product up naturally — không như infomercial]
- [Second X]: [VD: Look slightly off-camera sau CTA — like talking to a friend]

**Avoid:** [VD: Do not perform lines — should feel like she's remembering the experience]

---

## On-Screen Text (tùy chọn)

```
[Second X–Y]: "[TEXT]" — [position: center / lower third / top]
[Second X–Y]: "[TEXT]" — [position]
```

---

## Alternative Hooks

1. "[Hook option 2]"
2. "[Hook option 3]"
3. "[Hook option 4]"

---

## Review Log

| Version | Reviewed by | Date | Notes |
|---------|-------------|------|-------|
| v1 Draft | | | |
| v1 Approved | | | |

---

## Performance (điền sau khi ad chạy 7+ ngày)

- Hook rate (3s view / impressions): ___%
- Ad ID trong Ads Manager: ___
- Notes: ___
