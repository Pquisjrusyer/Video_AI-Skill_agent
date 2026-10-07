"""Hàm dùng chung cho clip-board.py + review-board.py: đọc video (ffprobe/ffmpeg), transcript (faster-whisper, CPU), so lời với script."""
import difflib, html, io, json, re, subprocess
from PIL import Image

MAX_WPS = 3.2          # nói nhanh hơn mức này → nghe rít
MIN_MATCH = 0.90       # % chữ khớp script tối thiểu
_whisper = None


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate:format=duration", "-of", "json", path],
                         capture_output=True, text=True).stdout
    j = json.loads(out or "{}"); st = (j.get("streams") or [{}])[0]
    num, den = (st.get("r_frame_rate", "0/1").split("/") + ["1"])[:2]
    return {"w": st.get("width", 0), "h": st.get("height", 0),
            "fps": round(float(num) / float(den or 1), 2) if float(den or 1) else 0,
            "dur": float(j.get("format", {}).get("duration", 0) or 0)}
def frame_at(path, t):
    png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", path, "-frames:v", "1",
                          "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(png)) if png else None
def transcribe(path):
    global _whisper
    if _whisper is None:
        from faster_whisper import WhisperModel   # máy không GPU → CPU
        _whisper = WhisperModel("base", device="cpu", compute_type="int8")
    segs, _ = _whisper.transcribe(path, word_timestamps=True, language="en")
    return [w for s in segs for w in (s.words or [])]
# Chuẩn hoá để "won't" = "will not", "I'm" = "I am", "fifty-two" = "52" không bị tính là sai lời.
CONTR = {"won't": "will not", "can't": "can not", "cannot": "can not", "shan't": "shall not", "let's": "let us",
         "it's": "it is", "that's": "that is", "there's": "there is", "what's": "what is", "here's": "here is",
         "he's": "he is", "she's": "she is"}
SUFFIX = [("n't", " not"), ("'m", " am"), ("'ll", " will"), ("'re", " are"), ("'ve", " have"), ("'d", " would")]
ONES = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * i for i, w in enumerate("_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
def norm(s):
    toks = re.sub(r"[^a-z0-9' ]", " ", s.lower().replace("’", "'").replace("-", " ")).split()
    out = []
    for t in toks:
        t = CONTR.get(t, t)
        for suf, rep in SUFFIX:
            if t.endswith(suf) and " " not in t: t = t[: -len(suf)] + rep; break
        out += t.replace("'", "").split()
    res, i = [], 0                                   # số chữ → số: "fifty two" → "52"
    while i < len(out):
        t = out[i]
        if t in TENS:
            n = TENS[t]
            if i + 1 < len(out) and out[i + 1] in ONES and ONES[out[i + 1]] < 10: n += ONES[out[i + 1]]; i += 1
            res.append(str(n))
        elif t in ONES: res.append(str(ONES[t]))
        else: res.append(t)
        i += 1
    return res

def same(x, y): return x == y or difflib.SequenceMatcher(a=x, b=y).ratio() >= 0.8   # lỗi chính tả nhỏ của whisper
def diff_html(script, heard):
    a, b = norm(script), norm(heard)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False); out = []; ok = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "replace" and i2 - i1 == j2 - j1 and all(same(x, y) for x, y in zip(a[i1:i2], b[j1:j2])):
            op = "equal"
        if op == "equal": out.append(html.escape(" ".join(b[j1:j2]))); ok += i2 - i1
        if op in ("delete", "replace"): out.append(f'<del title="thiếu so với script">{html.escape(" ".join(a[i1:i2]))}</del>')
        if op in ("insert", "replace"): out.append(f'<ins title="thừa / nghe khác script">{html.escape(" ".join(b[j1:j2]))}</ins>')
    score = ok / max(len(a), len(b)) if a else 1.0      # % chữ trong script được nói đúng
    return " ".join(out), score

