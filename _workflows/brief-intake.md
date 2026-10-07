# Bước 0 — Nhận brief (đầu cổng 1, mọi video mới)

> Chạy **trước** khi hỏi format / viết script. Mục tiêu: có brief để bám theo — brief của user nếu có, không thì Claude gợi ý từ link sản phẩm cho user chọn.
> Báo user theo kiểu ngắn: `✅ Xong` · `⛔ Cần duyệt` · `📁 File` (`production-steps.md`).

## 1. Hỏi 1 câu (AskUserQuestion)

"Bạn đã có brief cho video này chưa?"
- **Có — tôi gửi brief** (dán vào chat, kéo file vào chat, hoặc file trong thư mục dự án: .md / .docx / .pdf / ảnh chụp)
- **Chưa — gợi ý brief từ link sản phẩm** (Recommended khi chỉ có link)
- **Chỉ có ý tưởng ngắn** — user gõ 1–2 câu, Claude dựng thành brief

User đã gửi brief / ý tưởng / link ngay trong tin nhắn đầu → bỏ qua câu hỏi, đi thẳng nhánh tương ứng.

**Cùng lượt hỏi (hoặc ngay sau, nếu brief chưa ghi) — nền tảng, khung hình, template:**
- "Video đăng lên đâu?" (chọn nhiều): Meta Reels · Meta Stories · Meta Feed · TikTok · YouTube Shorts → id trong `_tools/platforms.json`.
- "Khung hình?": tự suy từ nền tảng — chỉ Feed → 4:5; có Reels / Stories / TikTok / Shorts → **9:16 làm bản chính**, Feed đi kèm → thêm bản phụ 4:5 (cắt lại khi dựng, nên giữ chủ thể ở giữa khung). Chỉ hỏi khi user muốn khác.
- "Có template / khung mẫu không?": **Dùng vùng an toàn chuẩn của nền tảng (Recommended)** · **Tôi có template riêng** (ảnh overlay PNG, video mẫu, layout end card, khung chữ của brand → kéo vào chat; lưu `refs/template/`, Claude bám đúng bố cục: vị trí logo, chữ, CTA, font, màu) · Không cần.
Ghi vào `brief.md` (Nền tảng · Ratio chính / bản phụ · Vùng an toàn · Template) và `storyboard.json` → `platform`.

## 2. Nhánh A — User có brief → import và bám theo

1. Đọc brief (file `.docx` → skill docx · `.pdf` → Read theo trang · link Google Doc → nhờ user dán nội dung hoặc tải file về, Claude không tự mở link cần đăng nhập).
2. Lưu bản gốc vào `campaigns/[campaign]/refs/brief-goc.[ext]` (dán chat → `brief-goc.md`, nguyên văn).
3. Điền `brief.md` theo `campaigns/_template/brief.md`, **giữ nguyên ý của user**: ý tưởng, cấu trúc, lời thoại, CTA, ref hình. Không tự đổi concept. Dòng **Nguồn brief** = "User import — `refs/brief-goc.*`".
4. Đối chiếu, báo trong 1 lần (gom thành danh sách ngắn):
   - Trường còn thiếu (format, duration, ratio, tệp khách, CTA…) → hỏi gom 1 lần, hoặc ghi "(giả định)" nếu user muốn chạy luôn.
   - Câu nào **không có trong claim APPROVED** của `product-brief.md` → ⚠️ + đề xuất câu thay, không tự xoá.
   - Thời lượng không khớp số lời (VO ≈ 2.4 từ/giây · UGC Flow ≤ 20 từ / 8s) → ⚠️ + đề xuất rút.
   - Brief có ref hình / video mẫu → thả vào `refs/`, ghi style cần bám vào `brief.md` mục Creative Direction.
5. Brief đã ghi rõ format → **không hỏi lại format**.
6. Sản phẩm chưa có `_products/<brand>/<sku>/` → tạo product-brief từ link sản phẩm (hỏi link nếu brief không có) + tải ảnh official. Claim lấy từ brief của user **và** từ trang sản phẩm → ghi vào mục APPROVED dạng **chờ duyệt**, user duyệt cùng cổng 1. Claim pháp lý (Non-toxic, Made in USA, HEMA-free…) luôn treo tới khi có xác nhận văn bản.

## 3. Nhánh B — Chưa có brief → gợi ý từ link sản phẩm

1. Đọc trang sản phẩm (Shopify: thêm `.json` vào link → title, mô tả, variant, ảnh). Sản phẩm chưa có `_products/<brand>/<sku>/` → tạo product-brief + tải ảnh official (như mục "Thêm mới" trong `CLAUDE.md`).
2. Đọc `_brand/<brand>/brand-brief.md` + `target-audience.md` (tone, tệp khách, điều không nên nói).
3. Hỏi duration nếu user chưa nói (10 / 15 / 20 / 30s).
4. Gợi ý **2–3 brief khác góc**, mỗi brief ≤ 6 dòng, dạng copy được:

   ```
   Brief [A] — [Format] [duration] · 9:16
   Ý tưởng 1 câu: …
   Cấu trúc: cảnh 1 … → cảnh 2 … → … → packshot
   Hook 3s đầu: …
   Claim dùng (APPROVED): …
   Hợp khi: [mục tiêu / tệp khách]
   ```
   Các góc nên khác nhau: VD 1 Voiceover quy trình thật, 1 UGC người dùng nói, 1 Product demo / so sánh trước-sau. Dựa vào điểm bán nổi bật nhất của sản phẩm (VD combo glossy + matte → "1 màu, 2 kiểu hoàn thiện").
5. ⛔ User chọn 1 brief (hoặc sửa) → điền `brief.md`, **Nguồn brief** = "Claude gợi ý — Brief [A], user chọn [ngày]".

## 4. Nhánh C — Chỉ có ý tưởng ngắn

Dựng 1 brief theo khung ở Nhánh B mục 4 từ đúng ý tưởng đó (không đổi ý), bổ sung phần thiếu từ trang sản phẩm + brand → ⛔ user xác nhận → `brief.md`.

## Sau Bước 0

Video có người → `character-intake.md` (bước nhân vật). Format đã rõ → đi tiếp cổng 1 (script → storyboard có ảnh…). Chưa rõ → hỏi chốt format kèm 1 câu recommend (`CLAUDE.md` → Chọn format).
