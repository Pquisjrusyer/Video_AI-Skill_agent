import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from post_edit import build_timeline, match_candidates, select_slots, to_visuals


def test_timeline_offsets_words_by_previous_takes():
    takes = [
        {"src": "take-A.mp4", "durationInFrames": 300, "words": [{"word": "hi", "start": 1.0, "end": 1.2}]},
        {"src": "take-B.mp4", "durationInFrames": 150, "words": [{"word": "money", "start": 0.5, "end": 0.8}]},
    ]
    words, total = build_timeline(takes)
    assert total == 15.0
    assert words[1] == {"word": "money", "start": 10.5, "end": 10.8, "take": "take-B.mp4"}


def test_illustration_wins_over_broll_and_each_visual_used_once():
    words = [
        {"word": "Hollow,", "start": 5.0, "end": 5.3, "take": "B"},
        {"word": "hollow", "start": 9.0, "end": 9.3, "take": "B"},
        {"word": "money", "start": 12.0, "end": 12.3, "take": "C"},
    ]
    cands = match_candidates(words, {"hollow": "/lib/a.jpg", "money": "/lib/cash.mp4"}, {"hollow": {"icon": "🕳️", "label": "Hollow"}})
    result = select_slots(cands, duration_seconds=60.0)
    assert [(c["kind"], c["start"]) for c in result] == [("illustration", 5.0), ("broll", 12.0)]


def test_asset_blocked_early_is_still_used_later():
    # "mattress" rơi vào 2s đầu nên bị loại, "pillow" cùng clip vẫn phải được chèn
    words = [
        {"word": "mattress", "start": 1.2, "end": 1.5, "take": "A"},
        {"word": "pillow,", "start": 4.7, "end": 5.0, "take": "A"},
    ]
    cands = match_candidates(words, {"mattress": "/lib/bed.mp4", "pillow": "/lib/bed.mp4"}, {})
    assert [c["start"] for c in select_slots(cands, duration_seconds=30.0)] == [4.7]


def test_select_slots_respects_edges_gap_and_rate():
    cands = [{"start": s, "end": s + 2.0} for s in (1.0, 5.0, 6.0, 10.0, 15.0, 20.0, 25.0, 30.0, 58.0)]
    result = select_slots(cands, duration_seconds=60.0)
    # 1.0 = 2s đầu, 6.0 = nghỉ < 2.5s, 30.0 = vượt trần 5/phút, 58.0 = 2s cuối
    assert [c["start"] for c in result] == [5.0, 10.0, 15.0, 20.0, 25.0]


def test_to_visuals_converts_to_frames_and_flags_images():
    slots = [
        {"kind": "broll", "asset": "/lib/generic/macro-bw-eye-hollow.jpg", "start": 4.0, "end": 6.0},
        {"kind": "illustration", "icon": "💧", "label": "Collagen", "start": 10.0, "end": 12.0},
    ]
    v = to_visuals(slots)
    assert v["brolls"] == [{"src": "broll/macro-bw-eye-hollow.jpg", "isImage": True, "from": 120, "durationInFrames": 60}]
    assert v["illustrations"] == [{"icon": "💧", "label": "Collagen", "from": 300, "durationInFrames": 60}]
