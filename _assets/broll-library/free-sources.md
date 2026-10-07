# Nguồn B-roll miễn phí — Reference

Nguồn footage thật (không phải AI-gen) để bổ sung vào `generic/`. Dùng khi cần cảnh thật mà AI gen hay fail: texture nước, chất lỏng, ánh sáng phòng tắm, cảnh sinh hoạt, thiên nhiên, lab/khoa học.

**Cập nhật:** 2026-09-20

---

## ⚠️ Đọc trước: model release — rủi ro thật với paid ads

Tất cả nguồn dưới đây đều "free for commercial use, no attribution". **Nhưng license đó chỉ nói về bản quyền video, không phải quyền hình ảnh của người trong video.**

Cả Pexels lẫn Pixabay đều **không đảm bảo có model release**. Dùng clip có mặt người nhận diện được trong ads bán hàng = rủi ro pháp lý (right of publicity), và Meta có thể reject nếu bị report.

**Quy tắc cho pack này:**

| Loại clip | Dùng trong ad được? |
|---|---|
| Không có người (texture, nước, thiên nhiên, lab, object) | ✅ Thoải mái |
| Có người nhưng **không nhận diện được** (chỉ tay, gáy, bóng, crop dưới cằm) | ✅ OK |
| Có mặt người nhận diện được — làm b-roll ambient, không hàm ý endorse | ⚠️ Tránh. Dùng AI-gen hoặc nhân vật của mình |
| Có mặt người + ghép với claim/testimonial/trước-sau | ❌ Không bao giờ |

Luôn tránh gợi ý người trong clip endorse sản phẩm, và không dùng trong ngữ cảnh tiêu cực (VD: "da xấu", "lão hoá") — Pixabay cấm explicit, Pexels cấm defamatory context.

---

## Xếp hạng nguồn

### Tier 1 — dùng chính, có API

**1. Pexels** — [pexels.com/videos](https://www.pexels.com/videos/) · [API](https://www.pexels.com/api/)
- Thư viện người + lifestyle tốt nhất. Có filter **portrait** → hợp 9:16.
- 4K nhiều, không watermark, không cần account để tải thủ công.
- API free: key lấy ngay, 200 req/giờ · 20.000 req/tháng.
- Cấm: bán lại clip nguyên bản, dựng platform stock cạnh tranh.
- **Dùng cho:** hand interaction, bathroom/vanity setting, morning routine, lifestyle ambient.

**2. Pixabay** — [pixabay.com/videos](https://pixabay.com/videos/) · [API](https://pixabay.com/api/docs/)
- Phủ rộng: abstract, macro, science/lab, nature, texture. Có cả mục AI-generated video riêng.
- API free, 100 req/phút.
- **Dùng cho:** macro chất lỏng, texture, lab/khoa học, abstract background cho stat overlay.

### Tier 2 — tải thủ công, chất lượng cao

**3. Mixkit** — [mixkit.co/free-stock-video](https://mixkit.co/free-stock-video/) · [license](https://mixkit.co/license/)
- ~3.000 clip nhưng **đã screen chất lượng** — không có footage nghiệp dư. Hit rate cao nhất.
- Không API. Tải thủ công, không watermark, không attribution.
- Cấm: dùng clip làm nội dung chính của sản phẩm bán ra.
- **Dùng cho:** khi cần 1-2 clip "nhìn đắt tiền" cho hero shot / opening.

**4. Coverr** — [coverr.co](https://coverr.co/) · [license](https://coverr.co/license) · [API](https://api.coverr.co/docs)
- Thiên về loop ngắn, ambient, background. Có API.
- **Dùng cho:** background loop dưới text overlay, transition filler.

**5. Videvo** — [videvo.net](https://www.videvo.net/)
- Kho lớn, 4K, **license trộn lẫn** — có clip đòi attribution, có clip không.
- ⚠️ Phải check license từng clip. Chỉ dùng khi 2 nguồn trên không có.

### Tier 3 — nguồn đặc thù

- **NASA / Internet Archive** — public domain, dùng thương mại được.
- ⚠️ **NIH NIGMS** có ảnh hiển vi fibroblast thật nhưng license **NonCommercial** — không dùng cho ads. Xem mục "Nguồn khoa học" cuối file.
- **Life of Vids, Dareful, Mazwai** — kho nhỏ, thỉnh thoảng có gem về texture/nature.

---

## Query list cho ngành beauty/skincare

Chạy các query này trên Pexels (orientation=portrait) và Pixabay:

**Không người — an toàn tuyệt đối cho ads:**
```
serum drop macro          water droplet skin        cream texture macro
cosmetic bottle light     glass dropper             bathroom marble counter
morning light window      silk fabric slow motion   white clean background
liquid swirl macro        glowing particles black   abstract cells
```

**Có người nhưng crop an toàn (tay/vai/gáy):**
```
hands applying cream      woman hands face          skincare routine hands
applying serum close up   washing face hands        towel face
```

**Lifestyle ambient (check kỹ có lộ mặt không):**
```
morning routine bathroom  woman mirror silhouette   getting ready morning
```

---

## Quy trình đưa clip vào thư viện

1. Tải về → `_assets/broll-library/generic/stock/`
2. Đặt tên: `stock-[nguồn]-[mô-tả-ngắn].mp4` — VD `stock-pexels-serum-drop-macro.mp4`
3. Thêm 1 dòng vào bảng Generic trong [index.md](index.md), cột `Campaign gốc` ghi `stock-import`, `Trạng thái` ghi `worked`
4. Ghi nguồn + link gốc vào `stock/CREDITS.md` — không phải để attribution, mà để truy vết license khi cần chứng minh
5. Clip có mặt người nhận diện được → **không import**, trừ khi chỉ định rõ dùng làm reference cho AI gen

---

## Script tải tự động

`_tools/fetch-stock-broll.py` — tải batch từ Pexels + Pixabay bằng API.

```bash
# Key để trong ~/.config/ai-studio/.env (KHÔNG để trong project):
#   PEXELS_API_KEY=...     # https://www.pexels.com/api/
#   PIXABAY_API_KEY=...    # https://pixabay.com/api/docs/
set -a; . ~/.config/ai-studio/.env; set +a
python3 "_tools/fetch-stock-broll.py" "serum drop macro" "cream texture macro" --limit 5
```

Mặc định lọc portrait/vertical, tải vào `_assets/broll-library/generic/stock/`, và append log thô vào `_download-log.md`. Clip giữ lại: đổi tên `stock-[nguồn]-[mô-tả-ngắn].mp4`, thêm vào bảng giữ lại của `CREDITS.md` + `index.md` + `keywords.json`.

---

## Nguồn khoa học (collagen / tế bào / hiển vi) — kết quả research 2026-09-20

**Kết luận: không có footage collagen/fibroblast thật nào miễn phí mà dùng được cho ads.**

Probe thẳng Pexels API: query `collagen` và `fibroblast` trả về spa/facial treatment, không phải khoa học — search engine map 2 từ đó sang ngành beauty.

| Nguồn | Có gì | Dùng cho ad? |
|---|---|---|
| [NIH NIGMS Image Gallery](https://nigms.nih.gov/image-gallery) | Fibroblast chụp hiển vi thật — đúng thứ cần | ❌ CC BY-**NC**-SA 3.0, cấm thương mại |
| [Vecteezy](https://www.vecteezy.com/free-videos/collagen-3d) | ~104 clip "collagen 3d" | ❌ Free license bắt buộc attribution + trần budget $1.000/dự án |
| [CDC PHIL](https://phil.cdc.gov/FAQ.aspx) | Phần lớn public domain | ⚠️ Được, nhưng kho thiên về bệnh truyền nhiễm, không có da |
| Pexels/Pixabay | 3D render abstract: cell, molecule, DNA, particle | ✅ Dùng được — nhưng generic, không nói gì về collagen |
| Getty / iStock / Envato | Collagen 3D thật, nhiều | 💰 Trả tiền |

### Hai quy tắc rút ra

1. **Visual cơ chế collagen → AI-gen, không phải stock.** Các file `aivideo-peptide-reaching-fibroblast`, `aivideo-collagen-fibers-dissolving`, `illustration-fibroblast-cell-glow` trong thư viện là cách duy nhất có visual đúng cơ chế. Stock chỉ bổ sung lớp nền.

2. **Không dùng footage phòng lab thật trong ad skincare.** Ghép cảnh lab/hiển vi thật = hàm ý đã có kiểm chứng lâm sàng. FTC soi claim substantiation ở đúng chỗ này, độc lập với chuyện license. Nếu `product-brief.md` không có nghiên cứu thật đứng sau thì cảnh lab làm tăng rủi ro, không tăng chuyển đổi.

### Query hiệu quả (thay cho "collagen")

```
cells microscope      microscopic particles     molecule animation
abstract cells        dna helix                 glowing particles black
```
