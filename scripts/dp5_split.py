"""Coverage with and without DP5, and DP5 split into its two parts (survey Section IX-B, Table VI).

    python3 scripts/dp5_split.py

DP5 ("smaller core, extensions, and rigor") bundles two kinds of change named in its codebook definition:
'core'       makes the core smaller or modular (moves a feature into an extension, adds an extension point,
             deprecates or removes a feature);
'tightening' tightens what remains (schemas, names, error models, normative definitions).
The split (data/coding/dp5_split.tsv) was proposed after adjudication by the first author with an AI assistant and
reviewed by the second author; it was not coded independently by two coders.
"""
import csv, pathlib
from collections import Counter

D = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'coding'
rows = list(csv.DictReader(open(D / 'dp_coding.tsv', encoding='utf-8'), delimiter='\t'))
split = {r['item']: r['dp5_part'] for r in csv.DictReader(open(D / 'dp5_split.tsv', encoding='utf-8'), delimiter='\t')}
assert set(split) == {r['item'] for r in rows if r['primary_dp'] == 'DP5'}

def period(r):
    if r['protocol'] == 'MCP':
        return 'MCP ' + r['revision'][:7]
    return 'A2A 0.3->1.0' if r['item'].startswith('1.0') else 'A2A 0.2.1-0.3.0'

cols = ['MCP 2025-03', 'MCP 2025-06', 'MCP 2025-11', 'MCP 2026-07', 'MCP', 'A2A 0.2.1-0.3.0', 'A2A 0.3->1.0', 'A2A', 'All']
def members(c):
    return [r for r in rows if c == 'All' or r['protocol'] == c or period(r) == c]
DPS = {'DP1', 'DP2', 'DP3', 'DP4', 'DP5', 'DP6'}
print(f"{'':28s}" + ''.join(f'{c:>16s}' for c in cols))
lines = [
    ('DP5 total', lambda r: r['primary_dp'] == 'DP5'),
    ('  DP5 core (smaller/modular)', lambda r: split.get(r['item']) == 'core'),
    ('  DP5 tightening', lambda r: split.get(r['item']) == 'tightening'),
    ('Fit by DP1-DP6', lambda r: r['primary_dp'] in DPS),
    ('Fit without DP5', lambda r: r['primary_dp'] in DPS - {'DP5'}),
    ('Fit without DP5 tightening', lambda r: r['primary_dp'] in DPS and split.get(r['item']) != 'tightening'),
]
for name, test in lines:
    cells = []
    for c in cols:
        m = members(c); k = sum(test(r) for r in m)
        cells.append(f'{k}/{len(m)} ({100 * k / len(m):.0f}%)' if name.startswith('Fit') else str(k))
    print(f'{name:28s}' + ''.join(f'{x:>16s}' for x in cells))
