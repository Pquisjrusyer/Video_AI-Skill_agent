import numpy as np, av, sys, os
SR = 44100
rng = np.random.default_rng(7)
def t_(d): return np.arange(int(d*SR))/SR
def env_ad(n, a, d):  # attack s, exp decay tau s
    t = np.arange(n)/SR; return np.minimum(t/max(a,1e-4), 1) * np.exp(-t/d)
def bandnoise(n, lo, hi):
    x = rng.standard_normal(n); X = np.fft.rfft(x); f = np.fft.rfftfreq(n, 1/SR)
    X[(f < lo) | (f > hi)] = 0; y = np.fft.irfft(X, n); return y/np.max(np.abs(y))
def save(x, path, stereo_w=0.0):
    x = x/np.max(np.abs(x))*0.89  # ~ -1 dBFS peak
    L = x; R = np.roll(x, int(stereo_w*SR)) if stereo_w else x
    st = np.stack([L, R]).astype(np.float32)
    c = av.open(path, "w"); s = c.add_stream("mp3", rate=SR); s.layout = "stereo"
    fr = av.AudioFrame.from_ndarray(st, format="fltp", layout="stereo"); fr.sample_rate = SR
    for p in s.encode(fr): c.mux(p)
    for p in s.encode(None): c.mux(p)
    c.close(); print("saved", path, f"{x.size/SR:.2f}s")
def mtof(m): return 440*2**((m-69)/12)

out = sys.argv[1]; code = "KOLOR-2026-10-TOPCOAT"

# ---- SFX-02: glass shine ting ----
n = int(1.2*SR); t = np.arange(n)/SR; f0 = 2093
ting = sum(a*np.sin(2*np.pi*f0*r*t)*np.exp(-t/d) for r,a,d in [(1,1,.45),(2.76,.45,.22),(5.4,.25,.1),(8.93,.12,.05)])
ting *= np.minimum(t/0.002, 1)
sp = bandnoise(n, 6000, 14000)*np.exp(-t/.08)*0.15
save(ting+sp, f"{out}/{code}_sfx-02_shine-ting_v1.mp3", 0.004)

# ---- SFX-01: soft brush swipe ----
n = int(2.0*SR); t = np.arange(n)/SR
e = np.sin(np.pi*np.clip((t-0.05)/1.85, 0, 1))**1.5
grain = 1 + 0.35*np.sin(2*np.pi*23*t + 3*np.sin(2*np.pi*1.3*t))
sw = bandnoise(n, 1800, 7000)*e*grain + 0.4*bandnoise(n, 400, 1500)*e
save(sw, f"{out}/{code}_sfx-01_brush-swipe_v1.mp3", 0.006)

# ---- Music: 12s, 100 BPM ----
D = 12.0; N = int(D*SR); mix = np.zeros(N); beat = 0.6
def add(sig, at, g=1.0):
    i = int(at*SR); j = min(N, i+sig.size); mix[i:j] += g*sig[:j-i]
def epiano(m, dur, vel=1.0):
    n = int(dur*SR); t = np.arange(n)/SR; f = mtof(m)
    x = np.sin(2*np.pi*f*t + 0.9*np.exp(-t/0.25)*np.sin(2*np.pi*f*t)) + 0.25*np.sin(2*np.pi*2*f*t)*np.exp(-t/.3)
    return vel*x*env_ad(n, 0.004, 1.1)*(1+0.12*np.sin(2*np.pi*4.5*t))
chords = [[53,57,60,64],[52,55,59,62],[50,53,57,60],[55,59,62,65],[48,52,55,59,62]]  # Fmaj7 Em7 Dm7 G7 Cmaj9
bar = 4*beat
for b, ch in enumerate(chords):
    t0 = b*bar
    hits = [0, 1.5*beat, 2.5*beat] if b < 4 else [0]
    for h in hits:
        for m in ch: add(epiano(m+12, 2.4 if b==4 else 1.0, 0.9 if h==0 else 0.55), t0+h, 0.10)
    # sub bass from 3.5s
    if t0+bar > 3.5 and b < 5:
        n = int(bar*SR); tt = np.arange(n)/SR
        bass = np.sin(2*np.pi*mtof(ch[0]-12)*tt)*env_ad(n, .01, 1.2)
        if t0 < 3.5: bass[:int((3.5-t0)*SR)] = 0
        add(bass, t0, 0.32 if b < 4 else 0.28)
# snaps on 2 & 4 (beats 1,3 zero-based) until 10s
k = 0
while k*beat < 10.0:
    if k % 2 == 1:
        n = int(.12*SR); tt = np.arange(n)/SR
        add(bandnoise(n, 1200, 5000)*np.exp(-tt/.025), k*beat, 0.30)
    # soft hats from 6.5s on offbeats
    if k*beat >= 6.5:
        n = int(.05*SR); tt = np.arange(n)/SR
        add(bandnoise(n, 8000, 15000)*np.exp(-tt/.012), k*beat+beat/2, 0.08)
    k += 1
# shimmer pad 3.5–10s
n = int(6.5*SR); tt = np.arange(n)/SR
pad = sum(np.sin(2*np.pi*mtof(m)*tt*(1+d)) for m in [72,76,79] for d in (-0.002, 0.002))
pad *= np.minimum(tt/1.5, 1)*np.minimum((6.5-tt)/1.0, 1)
add(pad, 3.5, 0.018)
# accents: bell at 5.0s, lift (reverse swell) into 6.5s
add(ting, 5.0, 0.12)
n = int(0.8*SR); tt = np.arange(n)/SR
add(bandnoise(n, 3000, 12000)*(tt/0.8)**3, 5.7, 0.10)
# master: fade tail 10–12s, gentle soft clip
tt = np.arange(N)/SR; mix *= np.where(tt > 10.0, np.clip(1-(tt-10.0)/2.0, 0, 1)**1.5, 1)
mix = np.tanh(mix*1.4)
save(mix, f"{out}/{code}_music_v1.mp3", 0.008)
