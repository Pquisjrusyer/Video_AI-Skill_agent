"""Hậu kỳ tự động cho video nhiều take (UGC): timing theo transcript thật,
chọn slot b-roll/minh hoạ theo rule, loudnorm. Port từ project AI Clipping.

  python3 _tools/post-edit/post_edit.py transcribe outputs/videos/take-A1.mp4 ...
  python3 _tools/post-edit/post_edit.py plan campaigns/X take-A1.mp4 take-A2.mp4 ... [--public /tmp/X-remotion/public]
  python3 _tools/post-edit/post_edit.py loudnorm /tmp/X-remotion in.mp4 out.mp4
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIBRARY = ROOT / "_assets" / "broll-library"
FPS = 30

# ponytail: editing-craft defaults port nguyên từ AI Clipping, chưa đo trên
# ads UGC; chỉnh nếu ở E-2 plan b-roll (duyệt trong /edit) thường xuyên thấy quá thưa/dày.
EDGE_GUARD_SECONDS = 2.0   # không chèn trong 2s đầu (hook) và 2s cuối (CTA) của cả video
MIN_GAP_SECONDS = 2.5
MAX_PER_MINUTE = 5
CUTAWAY_SECONDS = 2.0
MAX_CUTAWAY_SECONDS = 3.0
LOUDNORM_FILTER = "loudnorm=I=-14:TP=-1.5:LRA=11"
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def normalize(word: str) -> str:
    return re.sub(r"[^\w]", "", word.lower())


def select_slots(candidates: list, duration_seconds: float) -> list:
    """Giữ candidate (đã sort theo start) không đè 2s đầu/cuối, cách nhau đủ
    xa, không vượt trần mỗi phút. Mỗi beat chỉ 1 visual."""
    accepted = []
    last_end = None
    used = set()
    for c in candidates:
        key = c.get("dedupe")
        if key is not None and key in used:
            continue
        start = c["start"]
        end = min(c["end"], start + MAX_CUTAWAY_SECONDS)
        if start < EDGE_GUARD_SECONDS or end > duration_seconds - EDGE_GUARD_SECONDS:
            continue
        if last_end is not None and start - last_end < MIN_GAP_SECONDS:
            continue
        if sum(1 for a in accepted if a["start"] >= start - 60.0) >= MAX_PER_MINUTE:
            continue
        accepted.append({**c, "end": end})
        last_end = end
        used.add(key)
    return accepted


def match_candidates(timeline_words: list, broll_map: dict, illustration_map: dict) -> list:
    """timeline_words: [{word, start, end, take}] với start/end tính trên cả video."""
    broll_map = {normalize(k): v for k, v in broll_map.items()}
    illustration_map = {normalize(k): v for k, v in illustration_map.items()}
    candidates = []
    for w in timeline_words:
        key = normalize(w["word"])
        base = {"start": w["start"], "end": w["start"] + CUTAWAY_SECONDS, "take": w["take"], "word": w["word"]}
        # giữ mọi lần xuất hiện; select_slots mới loại trùng theo "dedupe", để lần đầu
        # bị loại (vd rơi vào 2s đầu) không chặn các lần sau
        if key in illustration_map:
            candidates.append({**base, "kind": "illustration", "dedupe": ("i", key), **illustration_map[key]})
        elif key in broll_map:
            candidates.append({**base, "kind": "broll", "dedupe": ("b", broll_map[key]), "asset": broll_map[key]})
    return candidates


def build_timeline(takes: list) -> tuple:
    """takes: [{src, durationInFrames, words}] theo thứ tự ghép hard cut."""
    words, offset_frames = [], 0
    for t in takes:
        offset = offset_frames / FPS
        for w in t["words"]:
            words.append({**w, "start": w["start"] + offset, "end": w["end"] + offset, "take": t["src"]})
        offset_frames += t["durationInFrames"]
    return words, offset_frames / FPS


def to_visuals(slots: list) -> dict:
    brolls, illustrations = [], []
    for s in slots:
        frame = {"from": round(s["start"] * FPS), "durationInFrames": round((s["end"] - s["start"]) * FPS)}
        if s["kind"] == "broll":
            name = Path(s["asset"]).name
            brolls.append({"src": f"broll/{name}", "isImage": Path(name).suffix.lower() in IMAGE_EXTS, **frame})
        else:
            illustrations.append({"icon": s["icon"], "label": s["label"], **frame})
    return {"brolls": brolls, "illustrations": illustrations}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text()) if path.exists() else {}


def media_duration_seconds(path: str) -> float:
    import av
    with av.open(path) as container:
        return container.duration / 1_000_000


def cmd_transcribe(paths: list) -> None:
    from faster_whisper import WhisperModel
    model = WhisperModel("base", device="cpu", compute_type="int8")
    for p in paths:
        segments, _ = model.transcribe(p, word_timestamps=True)
        words = [{"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)} for s in segments for w in s.words]
        out = Path(p).with_suffix(".words.json")
        out.write_text(json.dumps(words, indent=2, ensure_ascii=False))
        print(f"{out}  ({len(words)} từ)")


def cmd_plan(campaign: str, take_names: list, public: str = None) -> None:
    campaign_dir = Path(campaign)
    videos = campaign_dir / "outputs" / "videos"
    takes = []
    for name in take_names:
        mp4 = videos / name
        words_path = mp4.with_suffix(".words.json")
        if not words_path.exists():
            sys.exit(f"Thiếu {words_path}, chạy `transcribe` trước.")
        takes.append({
            "src": name,
            "durationInFrames": round(media_duration_seconds(str(mp4)) * FPS),
            "words": json.loads(words_path.read_text()),
        })

    library_map = {k: str(LIBRARY / v) for k, v in load_json(LIBRARY / "keywords.json").items()}
    campaign_kw = load_json(campaign_dir / "scripts" / "visuals-keywords.json")
    broll_map = {**library_map, **{k: str(LIBRARY / v) for k, v in campaign_kw.get("broll", {}).items()}}
    illustration_map = campaign_kw.get("illustrations", {})
    for word in campaign_kw.get("skip", []):  # beat cảm xúc chính: không che, bất kể map chung
        broll_map.pop(word, None)
        illustration_map.pop(word, None)

    timeline, total_seconds = build_timeline(takes)
    slots = select_slots(sorted(match_candidates(timeline, broll_map, illustration_map), key=lambda c: c["start"]), total_seconds)
    for s in slots:
        if s["kind"] == "broll" and not Path(s["asset"]).exists():
            sys.exit(f"Asset không tồn tại: {s['asset']}")

    visuals = {"fps": FPS, "takes": [{"src": t["src"], "durationInFrames": t["durationInFrames"]} for t in takes], **to_visuals(slots)}
    json_path = campaign_dir / "scripts" / "visuals.json"
    json_path.write_text(json.dumps(visuals, indent=2, ensure_ascii=False))

    rows = [f"| {s['start']:.1f}s | {s['take']} | \"{s['word']}\" | "
            + (f"B-roll | `{Path(s['asset']).relative_to(LIBRARY)}`" if s["kind"] == "broll" else f"Minh hoạ | {s['icon']} {s['label']}")
            + f" | {s['end'] - s['start']:.1f}s |" for s in slots]
    plan = ["# Visuals plan — E-2 plan b-roll (duyệt trong /edit) — tự sinh bởi post_edit.py", "",
            f"Tổng {total_seconds:.1f}s, {len(slots)} visual. Giờ tính trên cả video đã ghép.", "",
            "| Lúc | Take | Từ khoá | Loại | Asset / nội dung | Dài |", "|---|---|---|---|---|---|", *rows, "",
            "Kiểm tra: không che beat cảm xúc chính, không trùng lúc title card đang hiện.", ""]
    (campaign_dir / "scripts" / "visuals-plan.md").write_text("\n".join(plan))

    if public:
        dest = Path(public) / "broll"
        dest.mkdir(parents=True, exist_ok=True)
        for s in slots:
            if s["kind"] == "broll":
                shutil.copyfile(s["asset"], dest / Path(s["asset"]).name)
        shutil.copyfile(json_path, Path(public).parent / "src" / "visuals.json")

    print("\n".join(plan))


def cmd_loudnorm(build_dir: str, src: str, out: str) -> None:
    subprocess.run(
        ["npx", "remotion", "ffmpeg", "-y", "-i", str(Path(src).resolve()), "-af", LOUDNORM_FILTER,
         # -ar 48000: loudnorm upsample nội bộ (ra 96 kHz nếu không ép lại)
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(Path(out).resolve())],
        cwd=build_dir, check=True,
    )
    print(f"Đã loudnorm -14 LUFS: {out}")


def main(argv: list) -> None:
    if len(argv) < 2:
        sys.exit(__doc__)
    cmd, args = argv[1], argv[2:]
    if cmd == "transcribe" and args:
        cmd_transcribe(args)
    elif cmd == "plan" and len(args) >= 2:
        public = None
        if "--public" in args:
            i = args.index("--public")
            public = args[i + 1]
            args = args[:i] + args[i + 2:]
        cmd_plan(args[0], args[1:], public)
    elif cmd == "loudnorm" and len(args) == 3:
        cmd_loudnorm(*args)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
