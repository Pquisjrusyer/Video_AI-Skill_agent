# Status — Glass Skin Serum — "Four Actives" 10s

> Quy trình 3 cổng: `_workflows/production-steps.md`. Duyệt: "ok cổng 1/2/3".
> Brand: **Kreizi Beauty** · Code: `KREIZI-2026-10-ACTIVES` · Format: **Voiceover** (chốt 2026-10-02) · Ratio: 9:16 · Duration: 10s · Nhân vật: không

| Cổng | Gồm | Trạng thái | Duyệt bởi | Ngày |
|---|---|---|---|---|
| 1. Kế hoạch | `brief.md` · `scripts/script.md` · `scripts/storyboard.md` · thẻ ảnh trong `prompts-used/prompt-pack.md` | ✅ | jason.do | 2026-10-02 |
| 2. Ảnh | QC ảnh · thẻ video · `audio-plan.md` · VO · `handoff.md` | ✅ | jason.do | 2026-10-02 |
| 3. Final | kiểm file · review · `outputs/final/` | ◐ | | |

☐ chưa làm · ◐ đang làm · ☑ xong, chờ duyệt · ✅ đã duyệt

**Tiếp theo:** User xem `outputs/review/KREIZI-2026-10-ACTIVES_review_v4_notext.mp4` → "ok cổng 3" → Claude xuất vào `outputs/final/`.

## Asset
| Tên file | Loại | Ai gen | Xong | QC |
|---|---|---|---|---|
| `KREIZI-2026-10-ACTIVES_A-01_ref-skin-cross-section_v1.png` | ảnh ref | user gửi | ✅ | ref |
| `KREIZI-2026-10-ACTIVES_A-02_serum-underwater_v1.png` | first frame S03 | user gửi | ✅ | label đúng. Ảnh 941×1672, đủ cho Veo |
| `KREIZI-2026-10-ACTIVES_B-01_S01-actives-above-skin_v1.png` | first frame S01 | Claude GPT Image | ✅ | worked |
| `KREIZI-2026-10-ACTIVES_B-02_S01-glass-surface_v1.png` | last frame S01 | Claude GPT Image | ✅ | worked |
| `KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v3.png` | first frame S02 | v1–v2 Claude, v3 user sửa tay | ✅ | v3 texture đúng ref A-04, worked |
| `KREIZI-2026-10-ACTIVES_vo-S01/S02/S03_v1.mp3` | VO | Claude ElevenLabs | ✅ | 2.1 / 1.9 / 4.3s |
| `KREIZI-2026-10-ACTIVES_music_v1.mp3` | nhạc | Claude ElevenLabs | ✅ | không vocal, đỉnh ~6.5s |
| `KREIZI-2026-10-ACTIVES_S01_actives-to-glass_v1.mp4` | clip | User Veo | ✅ | đạt, dùng nguồn 1.0–5.9s @1.4x |
| `KREIZI-2026-10-ACTIVES_S02_hand-gel-spread_v1.mp4` | clip | User Veo | ✅ | dùng 3.0–5.5s (đầu clip serum đục xanh, không khớp v3) |
| `KREIZI-2026-10-ACTIVES_S03_serum-underwater_v1.mp4` | clip | User Veo | ❌ | label sai chữ, đã thay bằng v2 |
| `KREIZI-2026-10-ACTIVES_S03_serum-underwater_v2.mov` | clip | User sửa label | ✅ | label đúng đầu/giữa/cuối clip |
| `KREIZI-2026-10-ACTIVES_review_v1.mp4` | review | Claude Remotion | ✅ | 10s, -14 LUFS, chưa SFX |
| `KREIZI-2026-10-ACTIVES_sfx-01/02/03_*_v1.mp3` | SFX | User | ✅ | sfx-01 lặp 4 lần 1.05–1.5s · sfx-02 cắt từ 1.4s, đặt 3.45s · sfx-03 đặt 5.95s |

## Vấn đề (mỗi ý 1 dòng)
- 2026-10-02 — ✅ Đã xác nhận qua INCI: serum có tảo xanh, tảo đỏ, Niacinamide, HA. Giữ 4 hoạt chất như script. INCI đã ghi vào product-brief.
- 2026-10-02 — Ảnh tham chiếu user gửi cho hoạt chất xuống tới nang lông/lớp mỡ. Đã đổi: hoạt chất chỉ dừng ở lớp trên cùng, vì claim thẩm thấu sâu là NOT APPROVED.
- 2026-10-02 — Product page đang Sold Out nên video không có giá/offer.
- 2026-10-02 — `brand-assets/` Kreizi trống, end card dùng chữ serif "KREIZI BEAUTY" thay cho logo.
- 2026-10-02 — Không reuse `aivideo-peptide-absorbing-skin-layers.mp4` vì clip đó thấm sâu, sai claim.
- 2026-10-02 — Timeline chỉnh theo VO thật (S03 VO 3.7s không vừa slot 3s): S01 0–3.5s · S02 3.5–6s · S03 6–10s. Script/storyboard/thẻ video đã cập nhật.
- 2026-10-02 — Giọng Meshell (library) cần gói Creator ElevenLabs → dùng giọng premade Matilda.
- 2026-10-02 — User góp ý: (1) tên 4 hoạt chất hiện trên màn hình (không đọc VO, vì ngân sách 10s) → nhãn to hơn, hiện lần lượt; (2) B-03 gel trông 3D → sửa v2 theo ref texture A-03. Đã dùng hết lượt sửa của B-03.
- 2026-10-02 — User gửi ref texture serum thật (A-04: trong + vệt trắng sữa). B-03 hết lượt gen → user tự sửa tay ra v3 theo prompt-pack §B-03 v3. Prompt video S02 đã đổi mô tả texture.
- 2026-10-02 — Clip S03 Veo sai label (INPUSED, ALGAIE, 50 mL) → dựng bằng ảnh A-02 tĩnh. Muốn chuyển động nước thật → render lại S03 với camera tĩnh.
- 2026-10-02 — Clip S01 + S02 có dấu ✦ của Veo ở góc phải dưới. Chưa xử lý, chờ user quyết.
- 2026-10-02 — Chưa có SFX → bản review chỉ có VO + nhạc.
- 2026-10-02 — User muốn tự chèn chữ → xuất bản không chữ (render với `REMOTION_TEXT=0`) + spec chữ ở `prompts-used/text-overlay-spec.md`. Bản có chữ vẫn là `review_v1`.
- 2026-10-02 — Review v3 (không chữ): S03 đổi sang clip Veo theo yêu cầu user + thêm 3 SFX. ⚠️ Label trong clip S03 sai chữ, cần user xác nhận chấp nhận hoặc render lại trước khi chạy ad (Meta compliance: chữ label đúng).
- 2026-10-02 — Label S03 đã sửa (clip v2 .mov). Review v4 không chữ, có SFX. Còn mở: dấu ✦ Veo ở S01/S02.
- 2026-10-05 — User đề xuất thay S03 bằng cảnh người mẫu cầm chai (A-05). Thẻ video ở prompt-pack §S03-alt. Ảnh gốc: chai ngả mint, dòng chữ nhỏ hơi nhoè.
