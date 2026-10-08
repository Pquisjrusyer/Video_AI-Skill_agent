# Bước 0 — Nhận brief (đầu cổng 1, mọi video mới)

> Chạy **trước** khi hỏi format / viết script. Mục tiêu: có brief để bám theo — brief của user nếu có, không thì Claude gợi ý từ link sản phẩm cho user chọn.
> Báo user theo kiểu ngắn: `✅ Xong` · `⛔ Cần duyệt` · `📁 File` (`production-steps.md`).

> ⛔ **Thời lượng video là câu BẮT BUỘC.** Brief / tin nhắn chưa có số giây → **hỏi ngay** (10 / 15 / 20 / 30s / khác), không tự đặt, không ghi "(giả định)", không viết script khi chưa có. Có rồi → mọi bước sau bám đúng số đó: tổng thời gian các cảnh = đúng thời lượng, lời đọc không vượt (VO ≈ 2.4 từ/giây · UGC Flow ≤ 20 từ / 8s).

## 1. Hỏi 1 câu (AskUserQuestion)

"Bạn đã có brief cho video này chưa?"
- **Có — tôi gửi brief** (dán vào chat, kéo file vào chat, hoặc file trong thư mục dự án: .md / .docx / .pdf / ảnh chụp)
- **Chưa — gợi ý brief từ link sản phẩm** (Recommended khi chỉ có link)
- **Chỉ có ý tưởng ngắn** — user gõ 1–2 câu, Claude dựng thành brief
- **Brainstorm giúp tôi** — user chỉ nói *"Hãy tạo cho tôi video [thời lượng] về [tên sản phẩm / link sản phẩm]"*, Claude tự lên ý tưởng (Nhánh D)

User đã gửi brief / ý tưởng / link ngay trong tin nhắn đầu → bỏ qua câu hỏi, đi thẳng nhánh tương ứng. Tin nhắn kiểu "tạo cho tôi video 20s về [sản phẩm / link]" (chỉ có thời lượng + sản phẩm, không có ý tưởng) → Nhánh D.

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
   - Trường còn thiếu (format, ratio, tệp khách, CTA…) → hỏi gom 1 lần, hoặc ghi "(giả định)" nếu user muốn chạy luôn. **Riêng thời lượng: luôn hỏi, không giả định.**
   - Câu nào **không có trong claim APPROVED** của `product-brief.md` → ⚠️ + đề xuất câu thay, không tự xoá.
   - Thời lượng không khớp số lời (VO ≈ 2.4 từ/giây · UGC Flow ≤ 20 từ / 8s) → ⚠️ + đề xuất rút.
   - Brief có ref hình / video mẫu → thả vào `refs/`, ghi style cần bám vào `brief.md` mục Creative Direction.
5. Brief đã ghi rõ format → **không hỏi lại format**.
6. Sản phẩm chưa có `_products/<brand>/<sku>/` → tạo product-brief từ link sản phẩm (hỏi link nếu brief không có) + tải ảnh official. Claim lấy từ brief của user **và** từ trang sản phẩm → ghi vào mục APPROVED dạng **chờ duyệt**, user duyệt cùng cổng 1. Claim pháp lý (Non-toxic, Made in USA, HEMA-free…) luôn treo tới khi có xác nhận văn bản.

## 3. Nhánh B — Chưa có brief → gợi ý từ link sản phẩm

1. Đọc trang sản phẩm (Shopify: thêm `.json` vào link → title, mô tả, variant, ảnh). Sản phẩm chưa có `_products/<brand>/<sku>/` → tạo product-brief + tải ảnh official (như mục "Thêm mới" trong `CLAUDE.md`).
2. Đọc `_brand/<brand>/brand-brief.md` + `target-audience.md` (tone, tệp khách, điều không nên nói).
3. **Hỏi thời lượng** nếu user chưa nói (10 / 15 / 20 / 30s) — bắt buộc, trước khi gợi ý brief.
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

Chưa có thời lượng → hỏi trước. Dựng 1 brief theo khung ở Nhánh B mục 4 từ đúng ý tưởng đó (không đổi ý), bổ sung phần thiếu từ trang sản phẩm + brand → ⛔ user xác nhận → `brief.md`.

## 5. Nhánh D — Brainstorm: "Hãy tạo cho tôi video [thời lượng] về [sản phẩm / link]"

1. Thiếu thời lượng hoặc sản phẩm → hỏi đúng thứ còn thiếu (1 câu) — **không brainstorm khi chưa có số giây**; 5 ý tưởng đều phải vừa đúng thời lượng đó. Có link → đọc trang sản phẩm như Nhánh B mục 1; chỉ có tên → tìm trong `_products/`, không thấy thì hỏi link.
2. Đọc brand (`brand-brief.md`, `target-audience.md`), claim APPROVED, ảnh official, campaign cũ cùng brand (tránh lặp ý đã làm, ghi rõ "đã có campaign X dùng góc này").
3. Brainstorm **5 ý tưởng khác hẳn nhau về góc** — ví dụ: nỗi đau của khách · demo quy trình thật · trước / sau · UGC người dùng nói · so sánh / "1 sản phẩm 2 cách dùng" · trend / hook gây tò mò. Có skill `hook-writing` / `creative-strategy-engine` thì dùng để ra hook. Mỗi ý tưởng dạng thẻ ngắn:
   ```
   💡 [số]. [Tên ý tưởng 3–6 chữ]
   Hook 3s: "…"                     (câu mở + hình mở)
   Diễn biến: cảnh 1 → cảnh 2 → … → packshot / CTA
   Format: Voiceover / UGC / Product demo · hợp nền tảng: …
   Vì sao hợp: [tệp khách / điểm bán nổi bật của sản phẩm]
   Độ khó làm bằng AI: thấp / vừa / cao (lý do 1 câu)
   ```
4. Đánh dấu **⭐ 1 ý tưởng Claude khuyên chọn** + 1 câu lý do. ⛔ User chọn (hoặc ghép 2 ý, hoặc bảo "brainstorm thêm") → Claude dựng ý được chọn thành brief đầy đủ (khung Nhánh B mục 4) → `brief.md`, **Nguồn brief** = "Claude brainstorm — ý tưởng [số], user chọn [ngày]".
5. Sau đó hỏi nền tảng / khung hình / template như mục 1 (nếu user chưa nói) rồi đi tiếp.

## 6. Hỏi làm clip + âm thanh bằng gì (ngay sau khi chốt brief — 1 lượt AskUserQuestion, tối đa 3 câu)

Đọc `prefs.env` (hook đầu session đã in). Lựa chọn ở setup là mặc định → câu hỏi đặt lựa chọn đó lên đầu kèm "(đang dùng)". User chọn khác → chỉ đổi cho campaign này (ghi vào `status.md` dòng **Công cụ**), muốn đổi luôn → `set-prefs.sh`.

| Câu | Lựa chọn (mô tả ngắn, dễ hiểu) |
|---|---|
| "Clip video làm bằng gì?" | **Qua API — Claude gen tự động** (fal.ai Kling v3 / Replicate: có credit dùng thử khi đăng ký · Google Veo: trả phí, thật nhất) → `api` · TopView / Higgsfield (MCP / API) · Google Flow — chỉ để test, bạn tự render |
| "Giọng đọc (VO)?" (bỏ qua nếu video không có VO) | ElevenLabs (connector — **không có connector thì Claude dùng API key**, popup) · **Miễn phí qua API: Gemini TTS / Cloudflare** · OpenAI TTS · Tôi tự gen |
| "Nhạc nền?" | **Miễn phí: Freesound CC0** (Claude tự tìm nhạc có sẵn, dùng ads được, cắt đúng độ dài) · ElevenLabs Music (connector hoặc API key — gói trả phí) · Google Lyria 3 (AI gen, trả phí, key Gemini) · Tôi tự chọn (YouTube Audio Library / Pixabay Music) |

Chọn API mà máy chưa có key → mở popup `sh _tools/pick-provider.sh video|voice|music "..."` (popup có **hướng dẫn lấy key từng bước + nút mở trang**). Key đã có (`key-status.py`) → không hỏi lại.
Nói thật 1 dòng khi user hỏi "miễn phí": giọng đọc có nhà free thật; nhạc free = **thư viện CC0 có sẵn** (không phải AI gen); **video chỉ có credit dùng thử**; ElevenLabs free không được dùng thương mại.
Claude chỉ gen clip ở **cổng 2b**, sau khi user duyệt ảnh khung đầu + danh sách clip (cổng 2a) — câu hỏi này chỉ để chuẩn bị key sớm.

## Sau Bước 0

Video có người → `character-intake.md` (bước nhân vật). Format đã rõ → đi tiếp cổng 1 (script → storyboard có ảnh…). Chưa rõ → hỏi chốt format kèm 1 câu recommend (`CLAUDE.md` → Chọn format).
