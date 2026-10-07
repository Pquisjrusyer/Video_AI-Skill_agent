> **Trước khi bắt đầu:** Workflow này build video UGC testimonial bằng **TopView Avatar4** (avatar ảnh tĩnh + TTS — người dùng tự gen trên web, Claude chỉ xuất thẻ take), KHÔNG dùng Veo/Kling như `_skills/video/`. Vẫn cần đọc `_skills/scene-routing/` trước khi mở phần assembly, và `_skills/motion-graphic/SKILL.md` khi tới bước ghép (Remotion) — 2 skill đó dùng nguyên bản, không có version riêng cho UGC.
> **Đúc kết từ:** 1 campaign UGC thật — mọi lỗi/fix trong workflow này đã dính thật, không phải lý thuyết.

# Workflow SOP — UGC Video (TopView Avatar4)

> **Output cuối:** 1 video testimonial 9:16 Meta-ready trong `outputs/final/`, avatar AI nói theo script, có broll cutaway minh hoạ theo từ khoá
> **Tools:** GPT Image 2 (seed + ảnh take — Claude gen qua `_tools/gen-image.py`) → TopView web (avatar4/avatar4Fast, avatar nói — người dùng tự gen) → Remotion (ghép + broll + text overlay)
> **Không dùng route AI-VIDEO/MOTION-GRAPHIC chuẩn của `_skills/scene-routing/`** — video này đi qua route riêng: `TOPVIEW` (avatar nói) + `BROLL-CUTAWAY` (chèn ở bước ghép) + `TEXT-ONLY`.

## Bước ↔ lệnh / cổng (cổng dùng chung của 6 lệnh — không có cổng đánh số riêng)

Campaign folder + `brief.md` + `status.md` do `/start` tạo (⛔A). Thứ tự chạy theo lệnh, KHÔNG theo số bước:

| Bước trong file này | Lệnh | Cổng |
|---|---|---|
| Bước 2 — script + chia take | `/script` | ⛔B |
| Bước 3 — storyboard + map b-roll + danh sách asset | `/storyboard` | ⛔C |
| Bước 1 — thẻ seed + ảnh take (sau storyboard) | `/assets` | ⛔4A thẻ ảnh (cổng 1) → Claude gen (cổng 2) → ⛔4B QC ảnh |
| Bước 4 — thẻ take TopView | `/assets` (thay 4C) | ⛔4C |
| Âm thanh | `/assets` | ⛔4D: N/A — âm thanh là TTS TopView trong take; ghi rõ không VO/nhạc riêng (trừ khi plan có nhạc) |
| Bàn giao | `/assets` | ⛔4E: bảng take + plan ghép (`handoff.md`) → người dùng gen take |
| Bước 5 — QC take | `/check` | ⛔D |
| Bước 6–8 — ghép, b-roll, sub, final | `/edit` | ⛔ trong /edit: E-1 plan dựng, E-2 plan b-roll → ⛔E |

---

## Trước khi bắt đầu — đọc

- [ ] `_brand/<brand>/brand-brief.md`, `_brand/<brand>/target-audience.md` (brand lấy từ trường **Brand** trong product-brief)
- [ ] `_characters/[nhân-vật]/profile.md` + `voice-profile.md`
- [ ] `_products/[sản-phẩm]/product-brief.md` — **đặc biệt mục `✅ APPROVED claims`/ingredient**. Lỗi thật đã gặp: viết "collagen peptide" vào script vì nhớ nhầm, trong khi brief chỉ approve Marine Extracts/Niacinamide/HA/Ceramide — soát lại field ingredient TRƯỚC khi viết script, không tin trí nhớ.
- [ ] `_assets/broll-library/index.md` — check trước khi tính gen/tải broll mới

---

## Bước 1 — Seed ảnh nhân vật (Nano Banana Pro)

> Làm ở `/assets` 4A, SAU khi script (B) + storyboard (C) đã duyệt — không gen seed trước script. Claude viết thẻ theo `_prompts/nano-banana/image-prompt-card.md` + `_skills/image/SKILL.md` (kèm file ref + tên file lưu), rồi gen ở cổng 2 theo mục Gen GPT Image của skill đó. Seed trước, ảnh take sau.

1. Thẻ gen 1 ảnh chân dung mặt trơn làm identity-anchor (physical description theo `profile.md`) → lưu `outputs/images/[code]_A-01_seed-face_v1.png`. Duyệt ở 4B → copy sang `_characters/[nhân-vật]/reference-images/[nhân-vật]-face-ref-01.png`.
2. Từ seed đó, thẻ gen thêm **1 ảnh riêng cho mỗi trạng thái tay/sản phẩm sẽ xuất hiện trong video** (xem Bước 2 vì sao) — đính kèm ref 1 = seed để giữ identity, ref 2 = ảnh sản phẩm thật (`_products/.../reference-images/`) để giữ đúng label/màu/logo. Lưu `outputs/images/[code]_A-02_take-B-[mô-tả]_v1.png`…

⚠️ **Lỗi thật đã gặp — label sai khi 1 ảnh chứa 2+ sản phẩm cùng lúc:** gen ảnh nhân vật cầm 2 sản phẩm 1 lúc bị model tự bịa màu chữ/text label (chữ trắng bị đổi thành cam, "GLASS" bị viết nhầm "CLASS"). Nếu cần nhiều sản phẩm xuất hiện, **gen riêng từng ảnh 1-sản-phẩm** thay vì nhồi chung — an toàn hơn cho compliance (label phải đúng thật).

---

## Bước 2 — Script + xác định số TAKE (⚠️ bước hay bị bỏ qua)

TopView Avatar4 chỉ animate từ **1 ảnh tĩnh / 1 lần submit**, và mỗi lần submit đọc đúng **1 đoạn ttsText liên tục** — không đổi ảnh/pose giữa chừng 1 take.

Trước khi viết script, liệt kê **mỗi trạng thái hình ảnh khác nhau sẽ cần** (tay trống mở đầu, cầm sản phẩm A, cầm sản phẩm B, quay lại tay trống cho CTA...) — mỗi trạng thái = 1 TAKE = 1 ảnh riêng (Bước 1, gen ở `/assets`) = 1 lần submit riêng (Bước 4) = 1 điểm hard-cut khi ghép (Bước 6).

**Nguyên tắc viết ttsText mỗi take — tránh rít/khó nghe:**
- Giọng TopView (đã test: elevenlabs-v3 và minimax-v2.5) pace ổn định **~0.28s/từ** (~3.5 từ/giây) khi đọc tự nhiên.
- Nếu 1 take cần nói nhiều nhưng bạn set kỳ vọng duration ngắn, TTS sẽ nói nhanh/rít để kịp → **không set duration cứng, để TTS tự pace theo độ dài câu**, và **giữ mỗi take dưới ~40 từ** nếu muốn nghe rõ từng chữ — chia nhỏ thành nhiều câu ngắn thay vì 1 câu dài nhồi nhiều mệnh đề.
- ✅ Đã verify: câu 46 từ nén trong ý định 12s → nghe rít không rõ. Rút còn 30 từ, để TTS tự nói hết ~9.3s → rõ hẳn.

**Output:** `campaigns/[campaign]/scripts/[tên-script].md` — mỗi TAKE đánh dấu rõ `[ẢNH: ...]` dùng ảnh nào, ghi chú lý do tách take.

**⛔ Cổng B — dừng, trình script cho user duyệt trước khi qua storyboard.** Chưa xuất thẻ ảnh/take khi script chưa được xác nhận.

---

## Bước 3 — Storyboard (kèm map broll chi tiết từ script)

Follow `_skills/scene-routing/SKILL.md`. Bảng thời gian ghi rõ: file take nào ↔ ảnh nào ↔ nội dung thoại nào ↔ có broll cutaway ở đâu.

**Duration ở storyboard chỉ là ước lượng** (~3.5 từ/giây), duration thật chỉ biết sau khi take gen xong, vì TTS tự pace. Frame count thật lấy từ `scripts/visuals.json` (trường `takes`, đo theo stream video) — file này do `post_edit.py transcribe` + `plan` (Bước 7 mục 1–2) sinh ra, nên ở `/edit` phải chạy Bước 7 mục 1–2 TRƯỚC khi build assembly Bước 6. **Không dùng `mdls`**: đã đo thật, `mdls` báo dư (take A1 campaign hollow-not-tired: `mdls` 12.12s, thật 12.04s), làm vài frame cuối mỗi take bị đứng hình khi ghép.

### 3.1 — Map script → broll, câu theo câu (làm ngay ở bước này, không để tới lúc ghép mới nghĩ)

Đọc lại toàn bộ script (Bước 2) từ đầu tới cuối, với MỖI câu/mệnh đề hỏi: *"câu này có nhắc tới 1 thứ cụ thể hình dung được không (tiền, da khô, chất lỏng thấm, kem, texture...)?"* Ghi thành bảng — đây là output bắt buộc của Bước 3, không phải optional:

| Take | Câu thoại (trích) | Concept hình ảnh | Có broll không | Asset (có sẵn / cần tìm-gen) |
|---|---|---|---|---|
| VD: A | "I spent SO much money..." | Tiền/tốn tiền | Có | Cần tìm — không có sẵn trong `broll-library` |
| VD: B | "marine extracts and hyaluronic acid... pulls water into your skin" | Chất lỏng thấm vào da | Có | Có sẵn: `stock-pexels-hands-dropper-to-palm.mp4` |
| VD: D | "my husband looked at me and asked..." | — (beat cảm xúc chính) | **Không** | — giữ mặt, không chèn gì |

Nguyên tắc lọc:
- Câu chỉ mang tính chuyển ý, xây dựng bối cảnh, hoặc **là beat cảm xúc chính (hook/turning point)** → đánh dấu "Không" — không phải câu nào cũng cần broll, chèn dày quá cũng rối
- Câu có danh từ cụ thể hình dung được (tiền, sản phẩm, ingredient, triệu chứng da...) → ứng viên chèn broll
- Với mỗi ứng viên: check `_assets/broll-library/index.md` ngay tại bước này — thứ còn thiếu ghi vào danh sách asset của storyboard (⛔C), tránh phát hiện thiếu asset muộn ở Bước 7 rồi phải quay lại

### 3.2: Chuyển bảng 3.1 thành file keyword (timing tự tính ở Bước 7)

Không ước lượng timing bằng công thức vị trí từ nữa. Đã đo thật: công thức cũ đặt b-roll "New pillow" ở 5.08s, transcript thật là 4.5s, trễ ~0.6s. Timing giờ lấy từ transcript word-level (Bước 7).

Từ bảng 3.1, ghi `campaigns/[campaign]/scripts/visuals-keywords.json`:

```json
{
  "skip": ["hollow", "tired"],
  "broll": {"jar": "character-product/grace_collagen-peptide-moisture-treatment/product-reveal-hold-jar.mp4"},
  "illustrations": {"volume": {"icon": "📉", "label": "Lost volume"}}
}
```

- `skip`: từ là beat cảm xúc chính/hook/turning point (dòng "Không" ở 3.1). Không bao giờ chèn gì lúc nói từ này, kể cả khi map chung có.
- `broll`: chỉ cần ghi từ nào map chung `_assets/broll-library/keywords.json` chưa có, hoặc clip `character-product/` (map chung chỉ chứa clip `generic/`). Path tính từ `_assets/broll-library/`.
- `illustrations`: card icon + chữ ngắn bật lên đè cảnh nhân vật (không thay cảnh). Hợp với khái niệm trừu tượng, con số, cảm xúc. Label phải khớp lời thoại/claim approved, không tự thêm claim, không em dash.
- Keyword khớp từng từ (bỏ dấu câu, không phân biệt hoa thường). Cần cả số ít/số nhiều thì ghi cả 2.

Thiếu asset cho dòng "Có" nào ở 3.1 → ghi vào danh sách asset ở ⛔C. Thẻ gen viết ở `/assets`, Claude gen ảnh (video vẫn người dùng tự gen); stock tải bằng `_tools/fetch-stock-broll.py`. Asset mới dùng lại được → thêm vào library + `keywords.json` chung.

---

## Bước 4 — Gói thẻ TAKE → người dùng tự gen trên TopView (web) — `/assets` (thay 4C)

> **Claude KHÔNG gọi API/MCP gen video.** Output của bước này là thẻ cho từng take — người dùng tự gen trên https://www.topview.ai (Avatar 4 / Photo Avatar), rồi thả file về đúng chỗ. Thẻ chỉ viết khi ảnh take đã duyệt ở 4B.

### 4.1 — Mode mặc định

Thẻ take ghi sẵn **avatar4** · offPeak: off. Người gen tự đổi sang avatar4Fast / offPeak nếu muốn — không dừng hỏi.

### 4.2 — Xuất thẻ take vào `prompts-used/topview-takes.md`

Mỗi take 1 thẻ, người gen không cần hỏi lại gì:

```
### TAKE A — [mô tả ngắn]
Ảnh upload:   campaigns/[campaign]/outputs/images/[ảnh take A đã duyệt 4B].png
Mode:         avatar4 · offPeak: off (người gen tự đổi nếu muốn)
Voice:        [tên voice] — lọc English · American · Female · Middle Age · style UGC
Script (dán nguyên văn vào ô text):
[ttsText — đã bỏ em dash, < 40 từ]
Lưu về:       campaigns/[campaign]/outputs/videos/[code]_take-A_v1.mp4
QC nhanh:     ☐ nghe rõ từng chữ, không rít ☐ khẩu hình khớp ☐ claim đúng APPROVED ☐ tay/mặt không biến dạng
```

Quy tắc khi viết thẻ:
- **Voice:** chọn voice style **UGC** (casual), không lấy style **Advertisement** (tone đọc quảng cáo). Mọi take trong campaign dùng CÙNG 1 voice — ghi đúng tên voice ở mọi thẻ.
- **Script:** thay em dash (—) bằng dấu phẩy/chấm — em dash làm TopView fail TTS. Giữ < 40 từ/take, không ép duration.
- **Ảnh:** mỗi take đúng 1 ảnh trạng thái từ Bước 1 (tay trống / cầm sản phẩm A...), mỗi ảnh chỉ 1 sản phẩm.
- Gen tất cả take trong **cùng 1 board/project** của campaign trên TopView, tránh chạm giới hạn task đồng thời.
- Avatar4 chuẩn có thể mất ~1 giờ/take — theo dõi % trên dashboard TopView, không phải lỗi.

Sau đó: 4D ghi N/A (âm thanh = TTS TopView trong take, không VO/nhạc riêng — trừ khi plan có nhạc) → 4E gom bảng take + plan ghép vào `prompts-used/handoff.md`. **Chỉ sau ⛔4E** người dùng mới gen take, tải file về (nút Download trên TopView), đặt đúng tên ở dòng "Lưu về", tick vào `status.md`.

---

## Bước 5 — QC từng take trước khi ghép — `/check`

- [ ] Nghe rõ từng từ, không rít (nếu rít → quay lại Bước 2, rút ngắn câu, gen lại — chỉ gen lại đúng take đó)
- [ ] Claim/ingredient nhắc trong audio khớp `✅ APPROVED` trong product-brief
- [ ] Duration thật lấy ở Bước 7 (`visuals.json`), không dùng `mdls` (báo dư, xem Bước 3)

**⛔ Cổng D — nếu bất kỳ mục nào ở trên fail, dừng và sửa/gen lại take đó NGAY, không mang lỗi qua Bước 6.** Chỉ đi tiếp khi mọi take pass hết.

---

## Bước 6 — Ghép bằng Remotion (theo `_skills/motion-graphic/SKILL.md` Mode B) — `/edit`

> Chạy Bước 7 mục 1–2 (`transcribe` + `plan`) trước để có `visuals.json` — assembly Bước 6 cần file này.


- Build ở `/tmp/[campaign-slug]-remotion` (không `npm install` trong `remotion-project/` — xem `remotion-setup.md`)
- Mỗi take = 1 `<Sequence from={} durationInFrames={}>` chứa `<OffthreadVideo>`, nối **hard cut** (không crossfade, trừ khi nghe thử thấy nối bị khựng). `durationInFrames` mỗi take lấy từ `visuals.json` (`import visuals from './visuals.json'`), không gõ cứng số đo tay, không bao giờ dùng `mdls`
- Audio: giữ nguyên audio TTS embedded trong từng clip take — không thêm nhạc nền đè lời
- **⛔ E-1 plan dựng (trong /edit, trước E) — trình bày plan (thứ tự take, tổng duration, vị trí overlay/broll) và chờ user xác nhận trước khi render bản final** — đúng ràng buộc trong `motion-graphic/SKILL.md`, không tự ý ghi đè file đã có trong `outputs/final/`

---

## Bước 7: B-roll + minh hoạ tự động theo transcript (⛔ E-2 plan b-roll)

Tool: `_tools/post-edit/post_edit.py` (Python, cần `faster-whisper`, không cần ffmpeg hệ thống). Component: `_prompts/remotion/components/VisualsOverlay.tsx`.

1. **Transcribe từng take** (word-level, ghi `[code]_take-X_v1.words.json` cạnh file take):
   ```bash
   python3 _tools/post-edit/post_edit.py transcribe campaigns/[campaign]/outputs/videos/*_take-*.mp4
   ```
   Đọc lại transcript, sửa `visuals-keywords.json` (Bước 3.2) nếu từ trong audio khác script.
2. **Lập plan** (đúng thứ tự ghép take):
   ```bash
   python3 _tools/post-edit/post_edit.py plan campaigns/[campaign] [code]_take-A_v1.mp4 [code]_take-B_v1.mp4 [code]_take-C_v1.mp4 ... --public /tmp/[campaign-slug]-remotion/public
   ```
   Sinh `scripts/visuals-plan.md` (bảng duyệt), `scripts/visuals.json` (cho Remotion, copy luôn vào `src/`), copy asset cần dùng vào `public/broll/`.
3. **⛔ E-2 plan b-roll: trình `visuals-plan.md` cho user.** Sửa bằng cách chỉnh `visuals-keywords.json` (thêm `skip`, đổi asset, đổi label) rồi chạy lại bước 2, không sửa tay `visuals.json`.
4. **Build:** copy `VisualsOverlay.tsx` vào `src/`. Assembly render 3 lớp để caption luôn nằm trên b-roll:
   ```tsx
   {items.map(t => <Sequence ...><OffthreadVideo src={...} /></Sequence>)}        {/* 1. video take */}
   <VisualsOverlay visuals={visuals} />                                              {/* 2. b-roll + minh hoạ */}
   {items.map(t => <Sequence ...><CaptionOverlay .../>{titleCard}</Sequence>)}     {/* 3. caption + title card */}
   ```
   Assembly cũ đặt b-roll ở cấp gốc sau các take nên **b-roll che mất caption**, đừng lặp lại.

**Rule chọn slot (tự áp, hằng số đầu `post_edit.py`):** không chèn trong 2s đầu (hook) và 2s cuối (CTA) của cả video; nghỉ tối thiểu 2.5s giữa 2 visual; tối đa 5 visual/phút; mỗi visual 2s. B-roll và minh hoạ dùng chung ngân sách, không bao giờ 2 visual cùng lúc. Mỗi asset/minh hoạ dùng 1 lần; lần xuất hiện đầu bị loại (vd rơi vào 2s đầu) thì lần sau vẫn được xét.

**Kỹ thuật chèn (giữ nguyên nguyên tắc cũ, component đã làm sẵn):** b-roll fullbleed, mute, fade 7 frame vào/ra; ảnh tĩnh tự zoom chậm 1.0 → 1.08. Card minh hoạ bật lò xo, đặt `top: 380` (có thể đè tóc nhân vật ở khung cận, chỉnh trong `VisualsOverlay.tsx` nếu che mặt).

Asset stock mới tải thêm (`_tools/fetch-stock-broll.py`) → thêm dòng vào `_assets/broll-library/index.md` (+ `CREDITS.md` nếu Pexels/Pixabay) **và** thêm keyword vào `_assets/broll-library/keywords.json` nếu là clip `generic/` đáng dùng lại. Xoá bản download thừa, chỉ giữ 1 bản tốt nhất, không lộ mặt người nhận diện được.

---

## Bước 7.5 — Sub text + title card (mặc định làm cho mọi video UGC, trừ khi user nói không cần)

Đọc `_skills/motion-graphic/references/caption-effects.md` — có sẵn code component `CaptionOverlay.tsx` (sub text word-highlight kiểu TikTok) và `TitleCard.tsx` (chữ to kinetic cho câu hook/reveal), copy-paste rồi chỉnh màu/size theo brand.

1. **Sub text:** dùng duration thật từng take (từ `visuals.json`, Bước 7), timing ước lượng đều theo pace (công thức trong `caption-effects.md`) — không cần whisper trừ khi lệch nhịp rõ khi nghe lại.
   Transcript thật đã có sẵn ở `[code]_take-X_v1.words.json` (Bước 7). Đã thấy caption ước lượng lệch ~0.5s so với lời ở hollow-not-tired; nếu nghe thấy lệch thì chuyển `CaptionOverlay` sang dùng timestamp trong file này.
2. **Title card:** nếu script gốc có cột "TEXT overlay"/"Visual overlay" ghi câu chữ riêng (không phải lời thoại) → LUÔN build title card cho đúng câu đó ở đúng take — đây là tín hiệu rõ nhất cho biết đâu là điểm nổi bật trong video.
3. **Emphasis words:** những từ khoá quan trọng (số tiền, tên triệu chứng, tên ingredient...) truyền vào prop `emphasisWords` để phóng to + glow khi được nói tới.
4. Render preview, nghe/xem lại → chỉnh màu/size theo phản hồi (đã verify thực tế: size mặc định 72px/màu trắng bị chê "nhỏ, chưa nổi bật" — tăng lên ~104px + màu vàng gold rực mới đạt) → mới coi là bản để trình user.

---

## Bước 8 — Render final + checklist trước upload Meta (⛔E)

Theo `render-pipeline.md`, render ra `/tmp/[campaign-slug]-remotion/out/`, rồi **chuẩn hoá loudness về -14 LUFS** (dùng ffmpeg đi kèm Remotion, không cần cài gì) ghi thẳng vào `outputs/final/`, naming `[campaign-code]_[format]_[character]_[product]_[ratio]_v[version].mp4`:

```bash
python3 _tools/post-edit/post_edit.py loudnorm /tmp/[campaign-slug]-remotion /tmp/[campaign-slug]-remotion/out/final.mp4 campaigns/[campaign]/outputs/final/[tên-chuẩn].mp4
```

Đã đo thật: bản chưa chuẩn hoá của hollow-not-tired ra -21.4 LUFS, nhỏ hơn hẳn video khác trên feed; sau loudnorm -14.5 LUFS.

- [ ] AI disclosure toggle bật trong Ads Manager
- [ ] Lip sync kiểm tra kỹ (xem ở 1.5x speed)
- [ ] Product label/logo/màu đúng thật — không có gì tự bịa
- [ ] Không có claim ngoài `✅ APPROVED` trong product-brief
- [ ] Nghe hết video ở loa ngoài — không có đoạn rít/khó nghe, điểm nối giữa các take không bị khựng audio
- [ ] Đã chạy `post_edit.py loudnorm` (file trong `final/` là bản đã chuẩn hoá -14 LUFS)
- [ ] Xem từng b-roll/minh hoạ theo `visuals-plan.md`: đúng lúc nói, không lạc đề, caption vẫn đọc được
- [ ] Sub text/title card (Bước 7.5) không che sản phẩm/mặt ở khoảnh khắc quan trọng, không có lỗi chính tả, đúng claim approved

---

## Tóm tắt lỗi hay gặp (đọc nhanh trước khi bắt đầu campaign UGC mới)

| Lỗi | Nguyên nhân | Cách tránh |
|---|---|---|
| Audio rít, khó nghe 1 đoạn | Câu quá dài nhồi trong ý định duration ngắn | Giữ mỗi take <40 từ, để TTS tự pace |
| Label sản phẩm sai màu/chữ | Gen 1 ảnh có 2+ sản phẩm cùng lúc | Gen riêng từng ảnh 1-sản-phẩm |
| Claim ingredient sai | Viết theo trí nhớ, không check lại brief | Luôn đối chiếu `✅ APPROVED` trước khi chốt script |
| Broll nhìn chán/amateur | Card ảnh nổi cố định, không liên quan lời đang nói | Fullbleed cutaway bám từ khoá, audio giữ nguyên giọng creator |
| B-roll lệch lời nói ~0.5s | Timing ước lượng theo vị trí từ | Transcript word-level qua `post_edit.py transcribe` + `plan` (Bước 7) |
| Caption biến mất lúc chèn b-roll | B-roll đặt ở cấp gốc sau các take, đè lên caption nằm trong take | Assembly 3 lớp: video → `VisualsOverlay` → caption (Bước 7) |
| Vài frame cuối mỗi take bị đứng hình | Duration đo bằng `mdls` bị dư | Lấy `durationInFrames` từ `visuals.json` |
| TopView báo lỗi TTS ngay khi bấm gen | Em dash (—) trong script | Đổi em dash thành dấu phẩy/dấu chấm trong thẻ take |
