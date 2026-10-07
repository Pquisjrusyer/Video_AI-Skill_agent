#!/usr/bin/env python3
"""Đọc providers.json + nhà tự thêm (~/.config/ai-studio/providers-custom.json) cho pick-provider.sh (nhánh Mac) và gen-image.py.

  python3 _tools/providers_cli.py list image [exclude,csv]   → "id<TAB>label" mỗi dòng
  python3 _tools/providers_cli.py get image <id> guide|url|keys
  python3 _tools/providers_cli.py add-custom '<json>'        → lưu nhà tự thêm (không chứa key)
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CUSTOM = os.path.expanduser("~/.config/ai-studio/providers-custom.json")


def load(task="image"):
    items = json.load(open(os.path.join(HERE, "providers.json"), encoding="utf-8"))[task]
    if os.path.exists(CUSTOM):
        for name, c in json.load(open(CUSTOM, encoding="utf-8")).items():
            items.insert(0, {"id": f"custom:{name}", "label": f"{name} — nhà tự thêm ({c['model']})", "free": False,
                             "refs": bool(c.get("refs")), "url": "", "custom": c,
                             "keys": [{"env": c["key_env"], "label": "API key", "hidden": True}],
                             "guide": [f"Nhà tự thêm: {c['base_url']}", "Lấy key mới ở trang quản lý API của nhà đó."]})
    return items


def get(task, pid):
    return next((p for p in load(task) if p["id"] == pid), None)


if __name__ == "__main__":
    for _s in (sys.stdout,):
        if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "list":
        skip = set((sys.argv[3] if len(sys.argv) > 3 else "").split(","))
        for p in load(sys.argv[2]):
            if p["id"] not in skip: print(f"{p['id']}\t{p['label']}")
    elif cmd == "get":
        p = get(sys.argv[2], sys.argv[3]) or {}
        what = sys.argv[4]
        if what == "guide": print("\n".join(f"{i}. {s}" for i, s in enumerate(p.get("guide", []), 1)))
        elif what == "url": print(p.get("url", ""))
        elif what == "keys": print("\n".join(f"{k['env']}\t{k['label']}\t{int(k['hidden'])}" for k in p.get("keys", [])))
    elif cmd == "add-custom":
        c = json.loads(sys.argv[2]); os.makedirs(os.path.dirname(CUSTOM), exist_ok=True)
        cur = json.load(open(CUSTOM, encoding="utf-8")) if os.path.exists(CUSTOM) else {}
        cur[c.pop("name")] = c
        json.dump(cur, open(CUSTOM, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    else:
        sys.exit(__doc__)
