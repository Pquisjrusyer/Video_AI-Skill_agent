# Dựng S01/S02 bằng code từ ảnh đã duyệt (không có API video). Chạy từ thư mục campaign: python prompts-used/render-clips.py [s01] [s02]
import sys
import numpy as np, av
from PIL import Image
from scipy import ndimage as ndi
FPS, W, H, DUR = 30, 1080, 1920, 4.0
I = "outputs/images/KOLOR-2026-10-TOPCOAT_"
A = np.asarray(Image.open(I+"A-01_nail-base-satin_v1.png").convert("RGB")).astype(np.float32)/255
B = np.asarray(Image.open(I+"B-02_S02-glossy_v1.png").convert("RGB")).astype(np.float32)/255
h0, w0 = A.shape[:2]

def redmask(X):
    hsv = np.asarray(Image.fromarray((X*255).astype(np.uint8)).convert("HSV")).astype(np.float32)
    h, s, v = hsv[...,0]*360/255, hsv[...,1]/255, hsv[...,2]/255
    return ((h < 12) | (h > 340)) & (s > 0.5) & (v > 0.15)
m = redmask(A) | redmask(B)
m = ndi.binary_closing(m, iterations=4); m = ndi.binary_fill_holes(m); m = ndi.binary_opening(m, iterations=3)
lab, n = ndi.label(m); sizes = ndi.sum(m, lab, range(1, n+1))
keep = [i+1 for i, s in enumerate(sizes) if s > 4000]
m = np.isin(lab, keep); lab = np.where(m, lab, 0)
soft = ndi.gaussian_filter(ndi.binary_dilation(m, iterations=2).astype(np.float32), 2.0)

yy, xx = np.mgrid[0:h0, 0:w0].astype(np.float32)
d = np.array([0.6, -0.8], np.float32)                       # gốc móng (dưới-trái) → đầu móng (trên-phải)
proj = xx*d[0] + yy*d[1]
local = np.zeros_like(proj); start = np.zeros_like(proj)   # toạ độ 0..1 trong từng móng + độ trễ theo vị trí ngang
dist = ndi.distance_transform_edt(m); dn = np.zeros_like(dist)
cx_all = []
for k in keep:
    sel = lab == k; p = proj[sel]; local[sel] = (p - p.min())/(p.max() - p.min())
    dn[sel] = dist[sel]/dist[sel].max()                      # 0 ở viền → 1 ở giữa móng: giả độ cong mặt móng
    cx_all.append((k, xx[sel].mean()))
for rank, (k, _) in enumerate(sorted(cx_all, key=lambda t: t[1])):
    start[lab == k] = rank*0.12                              # móng trái trước, lệch 0.12s
local = ndi.gaussian_filter(local, 1.5)
curv = ndi.gaussian_filter(np.clip(dn*1.6, 0, 1)**0.8, 1.5)

def ss(e0, e1, x): t = np.clip((x-e0)/(e1-e0), 0, 1); return t*t*(3-2*t)
def frame(img, scale, cx=0.6, cy=0.52):
    cw, ch = w0/scale, h0/scale; x0 = np.clip(cx*w0 - cw/2, 0, w0-cw); y0 = np.clip(cy*h0 - ch/2, 0, h0-ch)
    im = Image.fromarray((np.clip(img, 0, 1)*255).astype(np.uint8))
    return np.asarray(im.resize((W, H), Image.LANCZOS, box=(x0, y0, x0+cw, y0+ch)))
def write(path, render):
    c = av.open(path, "w"); s = c.add_stream("libx264", rate=FPS); s.width, s.height, s.pix_fmt = W, H, "yuv420p"
    s.options = {"crf": "16", "preset": "slow"}
    for i in range(int(DUR*FPS)):
        for p in s.encode(av.VideoFrame.from_ndarray(render(i/FPS), format="rgb24")): c.mux(p)
    for p in s.encode(): c.mux(p)
    c.close(); print("saved", path)

# S01: satin → bóng gương chạy dọc từng móng (0.5–2.3s), vệt sáng ở mép chuyển; push-in 1.00→1.05
def s01(t):
    front = (t - 0.5 - start)/1.4
    rev = ss(-0.08, 0.08, front*1.16 - local) * soft
    glint = np.exp(-((front*1.16 - local)/0.035)**2) * soft * (front > 0) * (front < 1.15)
    img = A*(1-rev[...,None]) + B*rev[...,None]
    img = 1 - (1-img)*(1 - 0.45*glint[...,None])             # screen
    return frame(img, 1.0 + 0.05*ss(0, DUR, t))

# S02: vệt phản chiếu sắc lướt trái → phải qua móng (0.5–3.2s), đậm giữa móng, nhạt ra viền; push-in 1.05→1.10
bp = (xx*1.0 + yy*0.25)/w0
def s02(t):
    pos = 0.35 + 0.9*ss(0.5, 3.2, t)
    band = np.exp(-((bp - pos)/0.012)**2) * curv
    halo = np.exp(-((bp - pos)/0.04)**2) * curv * 0.25
    g = np.clip(0.85*band + halo, 0, 1)[..., None]
    img = 1 - (1-B)*(1 - g*np.array([1, 0.98, 0.94], np.float32))
    return frame(img, 1.05 + 0.05*ss(0, DUR, t))

args = sys.argv[1:] or ["s01", "s02"]
if "s01" in args: write("outputs/videos/KOLOR-2026-10-TOPCOAT_S01_one-coat_v1.mp4", s01)
if "s02" in args: write("outputs/videos/KOLOR-2026-10-TOPCOAT_S02_shine-sweep_v1.mp4", s02)
