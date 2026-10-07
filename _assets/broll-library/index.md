# B-roll Library Index

Thư viện video/image clip tái sử dụng được giữa các campaign. **Check bảng dưới TRƯỚC KHI viết prompt gen mới** (Veo/Kling/Seedance/Nano Banana/GPT Image) — có clip phù hợp thì reuse, không có mới tạo mới.

Sau khi tạo clip mới đủ tốt để tái dùng cho campaign khác trong tương lai → copy file vào `generic/` hoặc `character-product/[nhân-vật]_[sản-phẩm]/` và thêm 1 dòng vào bảng tương ứng bên dưới.

**`keywords.json`:** map từ khoá lời thoại → clip `generic/`, dùng để `_tools/post-edit/post_edit.py plan` tự chèn b-roll đúng lúc nói. Thêm clip generic mới thì thêm luôn vài từ khoá khớp nội dung clip (cả số ít/số nhiều). Clip `character-product/` không đưa vào đây, khai báo ở `visuals-keywords.json` của campaign dùng đúng nhân vật+sản phẩm đó.

---

## Generic (không gắn nhân vật/sản phẩm cụ thể)

Reuse được cho mọi campaign — texture, ambient, background, hand-only interaction không gắn brand.

Cột File: đường dẫn tính từ `generic/` (VD `stock/...` = `generic/stock/...`).

| File | Mô tả | Mood/Setting | Ratio | Campaign gốc | Ngày tạo | Trạng thái |
|---|---|---|---|---|---|---|
| `hand-touch-face-mirror-natural-light.mp4` | Tay chạm gò má/hàm trước gương phòng tắm, ánh sáng cửa sổ tự nhiên. ⚠️ LỘ MẶT trong gương (nữ da sáng, tóc xám, KHÔNG phải Grace), không ghép chung video có nhân vật khác (sửa 2026-09-29). Có watermark ✦ góc dưới. Không map trong `keywords.json` | Bathroom mirror, natural light, face visible in reflection | 9:16 | collagen-cliff-barrier-education | 2026-09-13 | needs-adjustment |
| `hand-pat-product-dry-skin-macro.mp4` | Macro da khô, tay vỗ nhẹ moisturizer nhưng sản phẩm nổi trên bề mặt không thấm | Macro, anonymous, no product branding visible | 9:16 | collagen-cliff-barrier-education | 2026-09-13 | worked |
| `hand-apply-product-jawline-neck.mp4` | Tay thoa sản phẩm lên jawline/cổ, da lên hình mềm dưới ánh sáng dịu | Soft light, anonymous | 9:16 | collagen-cliff-barrier-education | 2026-09-13 | worked |
| `illustration-muscle-fascia-collagen-fiber.jpg` | Illustration lớp cơ/fascia mặt, sợi collagen mờ dần (profile view) | Medical illustration, blue bg | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-skin-texture-soft-bg.jpg` | Macro da tay, bokeh mờ nền | Macro, soft focus | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-bw-jowl-skin.jpg` | Macro đen trắng vùng jowl | B&W macro | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-bw-eye-hollow.jpg` | Macro đen trắng hốc mắt | B&W macro | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-bw-neck-crepey.jpg` | Macro đen trắng da cổ nhăn | B&W macro | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `illustration-droplet-on-skin-surface.jpg` | Giọt tinh chất nổi trên bề mặt da, chưa thấm | Product-agnostic illustration | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `illustration-droplet-absorbing-layers.jpg` | Giọt thấm xuống các lớp da, mũi tên minh hoạ đường đi | Medical illustration, cross-section | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `illustration-skin-cross-section-nerve-zoom.jpg` | Cross-section khối da, zoom vào tế bào/dây thần kinh | Medical illustration, glow highlight | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `illustration-fibroblast-cell-glow.jpg` | Tế bào fibroblast phát sáng, cận cảnh | Medical illustration, warm glow | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-recovery-jowl.jpg` | Macro vùng jowl "phục hồi", da căng mịn | Macro, warm light | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-recovery-cheek.jpg` | Macro vùng má "phục hồi" | Macro, warm light | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `macro-recovery-eye.jpg` | Macro vùng mắt "phục hồi" | Macro, warm light | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `aivideo-collagen-fibers-dissolving.mp4` | Sợi collagen mờ dần trong lớp cơ/fascia mặt, medical illustration animation | Medical illustration, blue tones | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-skin-macro-texture-bg.mp4` | Macro da texture real motion, dùng làm nền cho stat overlay | Macro, neutral | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-skin-macro-3zone-bw-pan.mp4` | Macro đen trắng 3 vùng da (jowl/mắt/cổ), continuous pan | B&W macro, continuous pan | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-botox-villain-frozen-face.mp4` | Cận mặt biểu cảm "đơ cứng" kiểu Botox villain | Villain beat, clinical | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-droplet-on-skin-not-absorbing.mp4` | Giọt collagen nổi trên bề mặt da, wobble nhưng không thấm | Macro droplet, real motion | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-peptide-absorbing-skin-layers.mp4` | Match cut: giọt peptide thấm sâu vào cross-section da, mũi tên minh hoạ | Medical illustration, cross-section | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-peptide-reaching-fibroblast.mp4` | Illustration cắt lớp da: hạt peptide thấm tới fibroblast, particle docking | Medical illustration, warm glow | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-fibroblast-activation-glow.mp4` | Fibroblast "thức dậy", phát sáng, particle collagen/elastin mới hình thành | Medical illustration, activation glow | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `aivideo-skin-recovery-montage-warm.mp4` | Macro da 3 vùng phục hồi, warm golden light, pan nhẹ | Macro, warm golden light | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-15 | worked |
| `hand-hover-skincare-counter.mp4` | Tay hover trên 5 sản phẩm skincare trên marble counter, biểu cảm do dự, không chạm | Bathroom counter, cool neutral light, morning | 9:16 | collagen-routine-stopped-working | 2026-09-16 | worked |
| `hand-browse-skincare-counter-frustrated.mp4` | Bathroom counter đầy sản phẩm skincare (serums, creams, bottles), tay lướt qua nhưng không chọn, biểu cảm frustration nhẹ | Bathroom counter, anonymous, frustrated | 9:16 | collagen-routine-stopped-working | 2026-09-16 | worked |
| `hand-scoop-collagen-powder-kitchen.mp4` | UGC morning kitchen: tay múc bột collagen bằng scoop, đổ vào ly nước/smoothie | Kitchen, anonymous, morning | 9:16 | collagen-supplement-myth | 2026-09-16 | worked |
| `illustration-oral-collagen-digestion-scatter.mp4` | Illustration: collagen uống vào → dạ dày → enzyme cắt nhỏ thành amino acid → particles phân tán toàn thân (joints, cơ, xương, nội tạng) | Medical illustration, body map | 9:16 | collagen-supplement-myth | 2026-09-16 | worked |
| `illustration-body-map-face-ignored.mp4` | Illustration tiếp nối: toàn thân highlight nơi amino acid tới, da mặt bị bỏ qua/tối mờ | Medical illustration, body map | 9:16 | collagen-supplement-myth | 2026-09-16 | worked |
| `hand-apply-highlighter-conceal-dullness.mp4` | Tay lấy highlighter/concealer, dặm lên má — "che tạm" dullness, không lộ mặt rõ | Anonymous, makeup routine | 9:16 | collagen-tired-face | 2026-09-16 | worked |
| `stock/stock-pexels-serum-droplet-dropper-tip-black.mp4` | Stock thật: giọt serum ở đầu ống nhỏ giọt, nền đen macro | Macro, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-hand-hold-amber-dropper-curtain.mp4` | Stock thật: tay cầm ống nhỏ giọt màu hổ phách, rèm cửa nền | Hand only, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-hands-dropper-to-palm.mp4` | Stock thật: nhỏ tinh dầu từ ống nhỏ giọt vào lòng bàn tay | Hand only, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-pink-surface-droplets-macro.mp4` | Stock thật: bong bóng nước macro trên bề mặt hồng | Macro, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-bw-condensation-texture.mp4` | Stock thật: texture hơi nước ngưng tụ đen trắng | Macro, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-white-bottle-green-botanical.mp4` | Stock thật: đặt chai skincare trắng, prop thực vật xanh | Product ambient, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-hand-hold-white-bottle-curtain.mp4` | Stock thật: tay cầm chai lotion trắng, rèm cửa nền | Hand only, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-hand-place-jar-pedestal.mp4` | Stock thật: tay đặt jar/chai nhỏ giọt lên bệ | Hand only, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-honey-dropper-bowl-ambient.mp4` | Stock thật: ống nhỏ giọt thuỷ tinh, chất lỏng sánh như mật ong | Macro ambient, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-pump-bottles-dark-marble-moody.mp4` | Stock thật: chai pump trên mặt đá marble tối, moody light | Product ambient, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-pump-bottles-marble-lineup.mp4` | Stock thật: dãy chai pump trên mặt đá marble sáng | Product ambient, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-luxury-bathroom-interior-wide.mp4` | Stock thật: toàn cảnh phòng tắm sang trọng | Bathroom wide, no face | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-sci-purple-cells-bg.mp4` | Stock thật: animation tế bào tím trừu tượng — nền cho stat/mechanism overlay | Abstract science bg | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-sci-blue-particles-black.mp4` | Stock thật: hạt particle xanh trôi nổi nền đen — nền cho stat/mechanism overlay | Abstract science bg | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-sci-molecular-structure.mp4` | Stock thật: animation cấu trúc phân tử — nền cho mechanism overlay | Abstract science bg | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-hands-counting-cash-clean-bg.mp4` | Stock thật: tay đếm tiền mặt, nền sạch — hợp cho beat "tốn tiền/đổ tiền vào giải pháp sai" | Hand only, no face | 9:16 | stock-import | 2026-09-23 | unused — đã tải + ghi CREDITS.md nhưng chưa dùng campaign nào, sót khỏi bảng này tới giờ mới bổ sung |
| `stock/stock-pexels-sci-dna-helix-glow.mp4` | Stock thật: DNA helix phát sáng xoay — nền cho mechanism overlay | Abstract science bg | 9:16 | stock-import | 2026-09-23 | worked |
| `stock/stock-pexels-bedroom-pillow-blackout-curtains.mp4` | Stock thật: tracking shot phòng ngủ, gối + rèm cửa blackout, không có người | Bedroom, morning, no face | 9:16 | collagen-hollow-not-tired | 2026-09-24 | worked |

> ⚠️ Clip khoa học (`sci-*`) là abstract/generic — KHÔNG hàm ý đã có nghiên cứu lâm sàng cụ thể cho sản phẩm. Không ghép với footage lab thật (xem `free-sources.md` mục "Nguồn khoa học"). Toàn bộ clip `stock/` đã lọc thủ công: không có mặt người nhận diện được — an toàn dùng trong ad, xem điều kiện đầy đủ ở `free-sources.md`.

## Character + Product (gắn nhân vật/sản phẩm cụ thể)

Chỉ reuse được cho campaign dùng đúng combo nhân vật + sản phẩm này. Đặt file trong subfolder `character-product/[nhân-vật]_[sản-phẩm]/`.

Cột File: đường dẫn tính từ `character-product/`.

| File | Nhân vật | Sản phẩm | Mô tả | Ratio | Campaign gốc | Ngày tạo | Trạng thái |
|---|---|---|---|---|---|---|---|
| `grace_collagen-peptide-moisture-treatment/hook-face-closeup-ugc.mp4` | grace | collagen-peptide-moisture-treatment | Cận mặt UGC, biểu cảm mở đầu | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `grace_collagen-peptide-moisture-treatment/mirror-shock-touch-jaw.mp4` | grace | collagen-peptide-moisture-treatment | Soi gương, chạm hàm, biểu cảm hoang mang | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `grace_collagen-peptide-moisture-treatment/product-texture-scoop.mp4` | grace | collagen-peptide-moisture-treatment | Tay múc kết cấu treatment lên đầu ngón tay | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `grace_collagen-peptide-moisture-treatment/proof-smile-touch-cheek.mp4` | grace | collagen-peptide-moisture-treatment | Cười nhẹ, chạm má, ánh sáng tự nhiên (proof beat) | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `grace_collagen-peptide-moisture-treatment/product-reveal-hold-jar.mp4` | grace | collagen-peptide-moisture-treatment | Hero shot: tay cầm jar, xoay nhẹ, mở nắp | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `grace_collagen-peptide-moisture-treatment/apply-product-face-neck.mp4` | grace | collagen-peptide-moisture-treatment | Thoa sản phẩm lên mặt/cổ, ánh mắt tự tin | 9:16 | collagen-peptide-mechanism-reveal | 2026-09-10 | worked |
| `grace_collagen-peptide-moisture-treatment/mirror-disappointed-touch-jaw.mp4` | grace | collagen-peptide-moisture-treatment | Soi gương, chạm hàm, biểu cảm thất vọng nhẹ (khác mirror-shock: resignation, không shock) | 9:16 | collagen-routine-stopped-working | 2026-09-16 | worked |
| `grace_collagen-peptide-moisture-treatment/grace-drink-oral-collagen-mirror-disappointed.mp4` | grace | collagen-peptide-moisture-treatment | Khuấy ly collagen uống, uống, soi gương — biểu cảm "hm, vẫn vậy" (setup "myth" — chưa cầm sản phẩm S100 trong clip này) | 9:16 | collagen-supplement-myth | 2026-09-16 | worked |
| `grace_collagen-peptide-moisture-treatment/grace-harsh-light-are-you-tired.mp4` | grace | collagen-peptide-moisture-treatment | Nhìn thẳng camera, biểu cảm bình thường, ánh sáng bathroom fluorescent harsh/flat (khác các clip Grace khác đều soft/warm) | 9:16 | collagen-tired-face | 2026-09-16 | worked |
| `grace_collagen-peptide-moisture-treatment/grace-harsh-light-im-fine.mp4` | grace | collagen-peptide-moisture-treatment | Nối tiếp scene harsh-light: nhìn xuống rồi nhìn lại camera, biểu cảm "tôi biết, nhưng tôi không mệt", cùng setting ánh sáng harsh | 9:16 | collagen-tired-face | 2026-09-16 | worked |

---

## Quy tắc

- Trạng thái ghi: `worked` (dùng được, chưa qua feedback) / `validated` (đã chạy ads, performance tốt) / `needs-adjustment` (dùng được nhưng có lỗi nhỏ đã biết)
- Không thêm clip vào đây nếu nó gắn quá chặt vào 1 campaign cụ thể (VD: có text overlay campaign-specific burn sẵn vào hình) — chỉ thêm clip "sạch" (chưa overlay text/CTA) để tái dùng linh hoạt
- Xoá dòng khỏi bảng nếu file gốc đã bị xoá khỏi thư mục
