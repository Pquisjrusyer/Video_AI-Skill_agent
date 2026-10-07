# Campaign Brief — Kolor Blooming Gel — Cold Traffic TikTok

> ⚠️ **TRẠNG THÁI: DRAFT, CHỜ DUYỆT CỔNG A.** Claude soạn 2026-10-01.
> Field chưa có dữ liệu thật được đánh dấu **(giả định)** hoặc **(CHƯA CÓ)** — không bịa số liệu.

---

## Campaign Overview

| Field | Thông tin |
|-------|-----------|
| **Campaign name** | Oct Launch — Kolor Blooming Gel — Cold Traffic |
| **Brand** | **Kolor Acrylic** → context: `_brand/kolor-acrylic/` |
| **Campaign code** | `KOLOR-2026-10-BLOOM` ← dùng cho naming files |
| **Ngày bắt đầu** | 2026-10-01 |
| **Ngày kết thúc (dự kiến)** | (chưa có) |
| **Format** | **Voiceover** ✅ *đã chốt 2026-10-01 bởi Tịnh* |
| **Duration** | 15–20s |
| **Ratio** | 9:16 |
| **Voice (VO)** | Chốt ở 4D trong `prompts-used/audio-plan.md`. Hướng: nữ Mỹ trẻ, UGC/explainer, không giọng quảng cáo |

---

## Chọn format — ✅ ĐÃ CHỐT: **Voiceover** (Tịnh, 2026-10-01)

Theo bảng routing trong `CLAUDE.md`:

| Tín hiệu | Kết quả |
|---|---|
| Giọng kể | Ngôi thứ 3, VO dẫn dắt → **Voiceover** |
| Cấu trúc | Chia scene rõ (hook → demo → kết quả → packshot) → **Voiceover** |
| Vai trò b-roll | **Chính** — gần như toàn bộ video là macro móng tay → **Voiceover** |
| Nhân vật | Không cần gương mặt cố định → **Voiceover** |

> ✅ **Chốt Voiceover.** Pipeline: Veo 3.1 (scene `AI-VIDEO`, người dùng tự render) + Remotion (scene `MOTION-GRAPHIC`, Claude code). Chi tiết: `_workflows/voiceover-video-workflow.md`.
>
> Hướng UGC (TopView, nail tech thật kể chuyện) **không dùng cho campaign này** — nếu muốn test sau thì mở campaign riêng, không đổi giữa chừng.

---

## Objective

**Business goal:**
> (giả định) Cold traffic — kéo nail tech US biết tới sản phẩm và click vào product page. Chưa có target ROAS / ngân sách từ client.

**Ad objective trong Meta Ads Manager:**
- [x] Traffic *(giả định — đổi sang Sales nếu đã có pixel + dữ liệu chuyển đổi)*
- [ ] Sales (Conversions — Purchase)
- [ ] Add to Cart
- [ ] Awareness

---

## Creative Scope

| Deliverable | Format | Ratio | Ghi chú |
|-------------|--------|-------|---------|
| Video 15–20s | Voiceover | 9:16 | Bản 4:5 cắt lại khi dựng nếu cần chạy Feed |

---

## Targeting & Audience

**Cold audience:** *(giả định — chưa có input từ client)*
- [x] Interest targeting: Nail salon, Nail technician, Gel nails, Nail art, Beauty professionals
- [ ] Lookalike — (CHƯA CÓ dữ liệu nguồn)
- [x] Broad / Advantage+

**Warm audience (retargeting):** chưa dùng ở campaign này

---

## Products Featured

| Product | Angle chính | Approved claims dùng |
|---------|------------|---------------------|
| Kolor Blooming Gel 15ml | Hiệu ứng tự loang — nail art phức tạp mà không cần vẽ tay | `Time-Saving Art` · `Effortless Blending` · `Versatile Looks` · `No-Yellowing Crystal Clarity` *(4 claim in trên bao bì official — an toàn nhất)* |

⚠️ `product-brief.md` của sản phẩm này đang ở trạng thái **DRAFT**. Cổng B không qua được cho tới khi claim được duyệt.

---

## Creative Direction

**Audience stage:** `Cold`

**Key message (1 câu):**
> Chấm màu lên, màu tự loang thành hoạ tiết — nail art không cần vẽ.

**Primary pain point muốn address:**
> (giả định) Nail art vẽ tay tốn thời gian và phụ thuộc tay nghề — thợ mới không dám nhận, thợ giỏi thì kẹt lịch.
> ⚠️ Pain point này **chưa được verify**: `_brand/kolor-acrylic/target-audience.md` hiện là **placeholder chưa research** — mọi pain point ở đây là giả định. (Không dùng `_brand/kreizi-beauty/target-audience.md` thay thế: khác brand, khác ngành.)

**Hook direction:**
> 3 giây đầu là *hiệu ứng*, không phải lời. Cận cảnh một chấm màu rơi xuống móng rồi tự nở ra. Không mở bằng tên brand.

**Tone:**
> Theo `_brand/kolor-acrylic/brand-brief.md`: thân thiện nhưng có nghề, nói với người trong nghề, không giải thích thừa. Thực tế không hype ("truly work", "confident control"). Inclusive — không gatekeep, không hạ thấp tay nghề. Không giọng quảng cáo, không đánh premium.

**Aesthetic:**
> Theo Visual Identity trong `_products/kolor-blooming-gel/product-brief.md`: nền trắng/xám nhạt trơn, ánh sáng studio khuếch tán, macro cạn DOF, bề mặt gel bóng gương. Chai đen bóng chữ trắng.

**Character(s) dùng:**
> Không có. Chỉ bàn tay (hand model), không lộ mặt.

**KHÔNG làm trong campaign này:**
> - Không nhắc giá (giá $11.99 là giá sale, chưa rõ còn hiệu lực khi ad chạy)
> - Không dùng rating / review / quote khách (CHƯA CÓ proof xác thực)
> - Không dùng claim ngoài danh sách trong `product-brief.md`
> - Không nói "no skill needed" — hạ thấp nghề, trái tone brand ("every skill, every style")
> - Không đánh premium/luxury — lệch định vị giá của Kolor
> - Không nêu số phút tiết kiệm cụ thể (chưa đo)
> - Không gọi tên đối thủ
> - ⚠️ Demo phải đúng 5 bước official — **Step 2 phủ Blooming Gel KHÔNG cure**

---

## Production Timeline

| Mốc | Deadline |
|-----|----------|
| Video final (cổng E) | (chưa có) |
| Campaign live | (chưa có) |

---

## Performance Tracking

**URL campaign trong Ads Manager:** (chưa có)

| Metric | Target | Actual (7 ngày) | Actual (30 ngày) |
|--------|--------|-----------------|------------------|
| ROAS | (chưa có) | | |
| CPA / CPO | (chưa có) | | |
| CTR (link) | (chưa có) | | |
| Hook rate (3s) | >30% *(benchmark chung)* | | |
| CPM | (chưa có) | | |

---

## Gap cần lấp (ghi rõ theo yêu cầu của CLAUDE.md)

1. ~~Không có brand context cho Kolor~~ → **ĐÃ LẤP SƠ BỘ 2026-10-01**: `_brand/kolor-acrylic/brand-brief.md` (dựng từ website; chưa có xác nhận client, brand guideline, logo/font/palette).
2. **Không có audience research cho nail tech US.** `_brand/kolor-acrylic/target-audience.md` là placeholder. Pain point đang là giả định. Lấp bằng skill `anthropic-skills:audience-research`.
3. **Không có social proof.** Chưa có review nào.
4. **`product-brief.md` chưa duyệt claim**, trong đó "Made in USA" cần xác nhận pháp lý.
5. **Không có competitor research.** Ngách blooming gel đông (Beetles, Modelones, Makartt). Lấp bằng skill `imp-meta-ads-research`.

---

## Post-Campaign Notes

> Điền sau khi kết thúc campaign
