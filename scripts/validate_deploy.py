"""validate_deploy.py - sanity-check the data blobs in deploy/index.html."""
import json, re
from pathlib import Path

text = Path("deploy/index.html").read_text(encoding="utf-8")

def extract(name):
    m = re.search(rf"  const {name} = ", text)
    if not m:
        return None
    i = m.end()
    depth = 0
    in_str = False
    esc = False
    while i < len(text):
        c = text[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{" or c == "[":
                depth += 1
            elif c == "}" or c == "]":
                depth -= 1
                if depth == 0:
                    return text[m.end(): i + 1]
        i += 1
    return None

for name in ("DATA", "RECORD_COORDS", "PATTERN_FEATURES"):
    blob = extract(name)
    if blob is None:
        print(f"{name}: NOT FOUND")
        continue
    try:
        obj = json.loads(blob)
        if name == "DATA":
            print(f"{name}: OK, records={len(obj['records'])} edges={len(obj['edges'])}")
            # Release split
            r1 = sum(1 for r in obj["records"] if r.get("release") == "R1")
            r2 = sum(1 for r in obj["records"] if r.get("release") == "R2")
            print(f"  release split: R1={r1}  R2={r2}")
            agencies = {}
            for r in obj["records"]:
                agencies[r["agency"]] = agencies.get(r["agency"], 0) + 1
            print(f"  by agency: {agencies}")
            types = {}
            for r in obj["records"]:
                types[r["type"]] = types.get(r["type"], 0) + 1
            print(f"  by type: {types}")
        elif name == "RECORD_COORDS":
            print(f"{name}: OK, {len(obj)} keys")
            # Sample
            sample = list(obj.items())[:3]
            for k, v in sample:
                print(f"  {k[:50]}: [{v[0]:.2f}, {v[1]:.2f}]")
        else:
            print(f"{name}: OK, {len(obj)} keys")
    except json.JSONDecodeError as e:
        print(f"{name}: JSON ERROR: {e}")
        print(f"  span len: {len(blob)}")
        print(f"  first 300 chars: {blob[:300]}")
