"""Agreement between the original audit verdicts (S2-audit-evidence.json)
and the blind second coding (blind_recode_verdicts.json).
Reports raw agreement, Cohen's kappa, linearly weighted kappa, and the
disagreeing cells. Categories: satisfied, partial, absent."""
import json, collections, sys

orig_path = sys.argv[1] if len(sys.argv) > 1 else "S2-audit-evidence.json"
blind_path = sys.argv[2] if len(sys.argv) > 2 else "blind_recode_verdicts.json"
names = ["MCP", "A2A", "LangGraph", "AutoGen", "OpenAI"]
O = {}
for a in json.load(open(orig_path))["artifacts"]:
    key = next(k for k in names if k.lower() in a["artifact"].lower())
    for c in a["conditions"]:
        O[(key, c["id"])] = c["verdict"]
B = {}
for r in json.load(open(blind_path)):
    key = next(k for k in names if k.lower() in r["artifact"].lower().replace("-", ""))
    B[(key, r["condition"])] = r["verdict"]
assert len(O) == len(B) == 25
cells = sorted(O)
cats = ["satisfied", "partial", "absent"]
agree = [c for c in cells if O[c] == B[c]]
po = len(agree) / 25
mo, mb = collections.Counter(O.values()), collections.Counter(B.values())
pe = sum((mo[c] / 25) * (mb[c] / 25) for c in cats)
kappa = (po - pe) / (1 - pe)
w = lambda a, b: 1 - abs(cats.index(a) - cats.index(b)) / 2
pow_ = sum(w(O[c], B[c]) for c in cells) / 25
pew = sum((mo[a] / 25) * (mb[b] / 25) * w(a, b) for a in cats for b in cats)
kw = (pow_ - pew) / (1 - pew)
print(f"raw agreement: {len(agree)}/25 ({100*po:.0f}%)")
print(f"Cohen's kappa: {kappa:.3f}")
print(f"linearly weighted kappa: {kw:.3f}")
for c in cells:
    if O[c] != B[c]:
        print(f"disagree {c[0]}-{c[1]}: original={O[c]} blind={B[c]}")
