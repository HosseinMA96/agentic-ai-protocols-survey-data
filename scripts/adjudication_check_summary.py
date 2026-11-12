"""Summarize the second author's blind check of the adjudication (survey Appendix A).

    python3 scripts/adjudication_check_summary.py

Reads data/coding/adjudication_check_scored.tsv: for each of the 31 disagreeing codes, the option the second author
chose (shown as two unlabeled options in random order, without the resolution), the adjudicated code, and the
second author's own earlier code.
"""
import csv, pathlib
from collections import Counter

p = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'coding' / 'adjudication_check_scored.tsv'
rows = list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
yes = lambda r, k: r[k] == 'True'
n = len(rows)
print(f"blind choice = adjudicated code: {sum(yes(r, 'agrees') for r in rows)} of {n}")
for way in ('second adopted', 'first kept'):
    s = [r for r in rows if r['adjudication'] == way]
    print(f"  adjudication {way:15s}: {sum(yes(r, 'agrees') for r in s)} of {len(s)}")
for dim in ('Primary pressure', 'Plane'):
    s = [r for r in rows if r['dimension'] == dim]
    print(f"  {dim:16s}: {sum(yes(r, 'agrees') for r in s)} of {len(s)}")
print(f"blind choice = own earlier code: {sum(yes(r, 'own_earlier') for r in rows)} of {n}")
s = [r for r in rows if r['adjudication'] == 'second adopted' and not yes(r, 'own_earlier')]
print(f"resolved to the second code but first code now preferred: {len(s)}")
print(f"confidence: {dict(Counter(r['confidence'] for r in rows))}")
