# _brand/ — Context theo từng brand

> Project này phục vụ **nhiều brand**. Mỗi brand một folder con. Làm campaign của brand nào thì **chỉ đọc folder của brand đó** — không đọc chéo.

## Brand đang có

| Folder | Brand | Ngành | Tệp chính | Trạng thái context |
|---|---|---|---|---|
| `kreizi-beauty/` | Kreizi Beauty | Clean beauty — makeup + skincare | Nữ 18–40 (Lips/Makeup) · 45–65 (Skincare, chưa research) | Đầy đủ: brand-brief + target-audience + brand-assets |
| `kolor-acrylic/` | Kolor Acrylic | Nail supply — acrylic powder, gel polish, tools | Nail tech US + DIY | Sơ bộ: brand-brief (dựng từ website). **Thiếu** target-audience + brand-assets |

## Cấu trúc mỗi brand

```
_brand/[brand]/
├── brand-brief.md      ← Positioning, tone, USP, dòng sản phẩm
├── target-audience.md  ← ICP, pain points, ngôn ngữ khách hàng
└── brand-assets/       ← Logo, badge, font, palette (người dùng cung cấp)
```

## Brand nào thuộc sản phẩm nào

Xem trường **Brand** ở đầu `_products/<brand>/<sku>/product-brief.md`. Không chắc thì hỏi, không đoán.

| Sản phẩm | Brand |
|---|---|
| `glass-skin-duo` | Kreizi Beauty |
| `collagen-peptide-moisture-treatment` | Kreizi Beauty |
| `kolor-blooming-gel` | Kolor Acrylic |
| `kolor-glossy-top-coat` | Kolor Acrylic |
| `kolor-topcoat-gel-combo` | Kolor Acrylic |
| `kolor-acrylic-cover-powder` | Kolor Acrylic |

## Thêm brand mới

1. Tạo `_brand/[tên-brand]/`, copy cấu trúc trên
2. Thêm dòng vào 2 bảng ở file này
3. Ghi trường **Brand** vào `product-brief.md` của mọi SKU thuộc brand đó
4. Campaign code của brand đó dùng mã riêng (xem `CLAUDE.md` → Naming convention)

## Dùng chung được giữa các brand

`_skills/` · `_workflows/` · `_prompts/` · `_tools/` · `_assets/broll-library/generic/` (clip không gắn brand)

**KHÔNG dùng chung:** `_characters/` của brand này cho brand khác · `_assets/broll-library/character-product/` · badge/logo/font.
