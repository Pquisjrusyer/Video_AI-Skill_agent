# remotion-project/

Source code Remotion của campaign — **luôn có sau `/edit`** (mọi format đều dựng bằng Remotion, kể cả UGC).

Đây là project code, không phải "output". Build + render thật diễn ra ở thư mục tạm `/tmp/[campaign]-remotion` (không `npm install` ở đây — folder sync Drive). Sau khi render, chỉ sync `src/` + `package.json` + `package-lock.json` về đây (không `node_modules/`), giữ qua các version để sửa / render lại.

Setup + cấu trúc chi tiết: `_skills/motion-graphic/references/remotion-setup.md`.

File render: bản review → `../outputs/review/` · bản final → `../outputs/final/`. Không lưu file render trong folder này.
