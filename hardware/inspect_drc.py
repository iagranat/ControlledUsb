import json
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "drc_final2.json"
data = json.load(open(filename))
violations = data.get("violations", [])
print(f"Total violations in {filename}: {len(violations)}")
for i, v in enumerate(violations):
    print(f"#{i+1}: {v['type']} - {v['description']}")
    for it in v.get("items", []):
        print(f"  {it.get('description')} @ {it.get('pos')}")
