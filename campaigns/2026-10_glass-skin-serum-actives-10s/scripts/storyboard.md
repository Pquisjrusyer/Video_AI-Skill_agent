# Storyboard — Glass Skin Serum — "Four Actives" 10s

> Viết 2026-10-02 (cổng 1). Script: `script.md`. Route theo `_skills/scene-routing/`.

## Metadata

| Field | Thông tin |
|-------|-----------|
| **Campaign** | `KREIZI-2026-10-ACTIVES` |
| **Duration tổng** | 10.0s |
| **Ratio** | 9:16 |
| **Format** | Voiceover · Mixed (3 clip AI-VIDEO + chữ overlay Remotion) |

---

## Scene breakdown

| Mã | Bắt đầu–Kết thúc | Dài | Mục đích | Hình đầu cảnh | 1 hành động chính | Cỡ cảnh · góc | Camera | Hình cuối cảnh | Nối sang cảnh sau | Chữ hiển thị | Lời đọc | Nhạc · SFX | Route | Rủi ro AI → đơn giản hoá |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 0.0–3.5s | 3.5s | Hook: 4 hoạt chất chạm da, da ngậm nước | **B-01**: 3D mặt cắt da (style A-01), 4 quả cầu lơ lửng phía trên mặt da | 4 quả cầu chậm rãi trôi xuống, chạm mặt da rồi tan thành nước trong, lan ra **chỉ trên lớp trên cùng**; mặt da phẳng lại và bóng như kính | Medium, mặt cắt nhìn ngang, hơi chếch từ trên | Push-in chậm về mặt da | **B-02**: cùng mặt cắt, quả cầu đã tan, lớp trên cùng căng mọng, phản sáng bóng | Match cut "bề mặt bóng" sang S02, crossfade 6 frame | 4 nhãn tên hiện lần lượt theo từng quả cầu chạm da · "Four actives. One glow." | "Four actives. One glow." | Nhạc vào từ 0s · SFX bong bóng vỡ nhẹ ×4 | AI-VIDEO (first + last frame) | Veo có thể kéo quả cầu xuống sâu tới nang lông/lớp mỡ (sai claim) → khoá last frame B-02, prompt "stays on the outermost layer". Giải phẫu biến dạng → camera chỉ push-in, không orbit |
| S02 | 3.5–6.0s | 2.5s | Proof cảm quan: gel tan trên da thật, để lại lớp bóng ẩm | **B-03**: macro mu bàn tay phụ nữ ~58, 1 giọt gel trong hơi xanh có bọt khí nằm trên da, đầu ngón trỏ tay kia ngay phía trên | Đầu ngón ấn rồi tán giọt gel thành vệt mỏng, da để lại ánh bóng ẩm | Macro, nhìn xuống ~30° | Static | Vệt gel mỏng đã tán, da bóng ẩm, ngón tay rời khỏi khung | Hard cut theo tiếng nước sang S03 | "Hyaluronic Acid" / "Holds up to 1,000x its weight in water" | "Serum floods deep hydration." | SFX giọt nước chạm da | AI-VIDEO | Ngón/tay biến dạng → chỉ 1 đầu ngón vào khung, hành động ngắn, camera đứng yên. Gel chảy sai vật lý → giọt nhỏ, độ nhớt cao |
| S03 | 6.0–10.0s | 4.0s | Packshot + end card | **A-02**: chai serum giữa tảo xanh + tảo đỏ dưới nước, tia nắng (ảnh user gửi, dùng trực tiếp) | Nước lay nhẹ, bọt khí bay lên, tia nắng lung linh, tảo đung đưa. Chai đứng yên | Medium close, chính diện | Push-in rất chậm | Như đầu cảnh, gần hơn chút | Hết video. Chữ end card vào từ 6.6s | "Luminous Glass Skin Serum" / "Designed for skin 40+" / "KREIZI BEAUTY" | "Luminous Glass Skin Serum. Designed for skin forty plus." | SFX whoosh dưới nước nhẹ khi cut vào · nhạc fade out 9.5–10s · nhạc lên đỉnh ~6.5s | AI-VIDEO + chữ overlay MOTION-GRAPHIC | Label chai méo khi chuyển động → chai đứng yên, camera gần như tĩnh. Vẫn méo → Remotion giữ ảnh tĩnh A-02 + Ken Burns cho 1.5s cuối |

---

## Assembly notes

- S01→S02: match cut bề mặt bóng (lớp da 3D → da thật), crossfade 6 frame.
- S02→S03: hard cut theo SFX nước.
- Chữ: serif kiểu Cormorant/Playfair (không có font brand), nâu đậm trên S01–S02, trắng trên S03.

### Audio

| Loại | Có dùng? | Nguồn file | Scene áp dụng |
|------|----------|------------|----------------|
| Nhạc nền | Có | Claude gen qua ElevenLabs (ambient, không vocal) → `KREIZI-2026-10-ACTIVES_music_v1.mp3` | Toàn video, duck dưới VO |
| Voiceover | Có | Claude gen qua ElevenLabs, mỗi câu 1 file → `KREIZI-2026-10-ACTIVES_vo-S01_v1.mp3` … `vo-S03` | S01, S02, S03 |
| SFX | Có | User chọn theo prompt ở `audio-plan.md` → `_sfx-01_bubble-pop`, `_sfx-02_droplet`, `_sfx-03_underwater-whoosh` | S01, S02, S03 |
| Audio gốc clip | Không | Mute khi dựng | — |

> Duration scene lấy theo VO thật ở cổng 3. Nhạc duck dưới VO.

---

## Hand-off checklist

- [ ] S01–S03 có danh sách ảnh. Thẻ ảnh ở `prompts-used/prompt-pack.md`, thẻ video viết sau khi ảnh pass (cổng 2)
- [ ] Chữ overlay + end card dựng ở cổng 3
- [ ] VO có trong `outputs/audio/` trước khi dựng

---

## Danh sách ảnh

### A. Ảnh tham chiếu
| Mã | Nội dung | Vai trò | Dùng cho cảnh | Dùng trực tiếp / chỉnh sửa / tạo mới | Ref cần + vai trò | Bắt buộc giữ | Prompt nháp |
|---|---|---|---|---|---|---|---|
| A-01 | 3D mặt cắt da + 4 quả cầu (user gửi) | Phong cách minh hoạ, bố cục, dáng 4 quả cầu | S01 (ref cho B-01, B-02) | Tham chiếu, không làm khung video | — | Tông kem/hồng đào, nền trắng, 4 quả cầu | — |
| A-02 | Chai serum dưới nước giữa tảo (user gửi) | Bao bì chai + khung đầu S03 | S03 | **Dùng trực tiếp** làm first frame S03 | — | Label đúng, chai kính mờ xanh nhạt | — |

### B. Ảnh dùng trực tiếp cho video
| Mã | Nội dung | Vai trò | Dùng cho cảnh | Dùng trực tiếp / chỉnh sửa / tạo mới | Ref cần + vai trò | Bắt buộc giữ | Prompt nháp |
|---|---|---|---|---|---|---|---|
| B-01 | 3D mặt cắt, khung gần hơn A-01, lớp trên cùng chiếm nửa dưới, 4 quả cầu lơ lửng | First frame | S01 | Tạo mới (từ A-01) | A-01 = style + quả cầu | Style minh hoạ, 4 quả cầu đúng nội dung | Xem prompt-pack |
| B-02 | Như B-01 nhưng quả cầu đã tan, lớp trên cùng căng mọng + bóng như kính | Last frame | S01 | Chỉnh sửa B-01 | B-01 = toàn bộ | Bố cục, góc, giải phẫu y hệt B-01 | Xem prompt-pack |
| B-03 | Macro mu bàn tay nữ ~58 + 1 giọt gel serum + đầu ngón trỏ phía trên | First frame | S02 | Tạo mới | `serum-texture-callout-01.png` = chất gel | Da có texture thật, 5 ngón, gel trong hơi xanh | Xem prompt-pack |

---

## Danh sách asset

| Asset | Loại | Nguồn | Tên file | Ai gen | Render (s) | Dùng (s) |
|---|---|---|---|---|---|---|
| A-01 | ảnh ref | user gửi | `KREIZI-2026-10-ACTIVES_A-01_ref-skin-cross-section_v1.png` | — | | |
| A-02 | ảnh | user gửi, dùng trực tiếp | `KREIZI-2026-10-ACTIVES_A-02_serum-underwater_v1.png` | — | | |
| B-01 | ảnh | gen mới | `KREIZI-2026-10-ACTIVES_B-01_S01-actives-above-skin_v1.png` | Claude (GPT Image) | | |
| B-02 | ảnh | edit B-01 | `KREIZI-2026-10-ACTIVES_B-02_S01-glass-surface_v1.png` | Claude (GPT Image) | | |
| B-03 | ảnh | gen mới | `KREIZI-2026-10-ACTIVES_B-03_S02-hand-gel-drop_v1.png` | Claude (GPT Image) | | |
| S01 | clip | Veo 3.1 first+last frame | `KREIZI-2026-10-ACTIVES_S01_actives-to-glass_v1.mp4` | User | 6 | 3.5 |
| S02 | clip | Veo 3.1 image-to-video | `KREIZI-2026-10-ACTIVES_S02_hand-gel-spread_v1.mp4` | User | 4 | 2.5 |
| S03 | clip | Veo 3.1 image-to-video | `KREIZI-2026-10-ACTIVES_S03_serum-underwater_v1.mp4` | User | 4 | 4.0 |
| VO | VO ×3 | ElevenLabs | `KREIZI-2026-10-ACTIVES_vo-S01_v1.mp3` … `vo-S03` | Claude | | |
| Nhạc | nhạc | ElevenLabs | `KREIZI-2026-10-ACTIVES_music_v1.mp3` | Claude | | 10 |
| SFX ×3 | SFX | user chọn | `KREIZI-2026-10-ACTIVES_sfx-01_bubble-pop_v1.mp3` · `sfx-02_droplet` · `sfx-03_underwater-whoosh` | User | | |

> Reuse đã kiểm: `_assets/broll-library` có `aivideo-peptide-absorbing-skin-layers.mp4` nhưng clip đó thấm sâu + mũi tên (sai claim cho serum này) nên không dùng.
