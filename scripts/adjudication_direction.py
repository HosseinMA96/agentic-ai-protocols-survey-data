"""Direction of adjudication (Appendix A, table "Outcome of Adjudication for Each Disagreeing Code").

For every double-coded item and each dimension (primary pressure, plane) on which the two coders disagreed,
report whether the adjudicated code is the second coder's code, the first (pre-adjudication) code, or a third code.
Also checks that no code on which the coders agreed was changed.
Run from the repository root:  python3 scripts/adjudication_direction.py
"""
import csv, collections, sys
from pathlib import Path

D = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('data/coding')


def load(name):
    with open(D / name, encoding='utf-8') as f:
        return {r['item']: r for r in csv.DictReader(f, delimiter='\t')}


first, final, second = load('dp_coding_pre_adjudication.tsv'), load('dp_coding.tsv'), load('second_coder_all_filled.tsv')
round1 = set(load('second_coder_sample_filled.tsv'))
count, changed_agreed, items = collections.Counter(), [], collections.defaultdict(set)
for item, s in second.items():
    for dim, k1, k2 in (('pressure', 'primary_dp', 'primary_dp_coder2'), ('plane', 'plane', 'plane_coder2')):
        a, b, z = first[item][k1].strip(), s[k2].strip(), final[item][k1].strip()
        if a == b:
            if z != a:
                changed_agreed.append((item, dim))
            continue
        out = 'second' if z == b else ('first' if z == a else 'third')
        rnd = 'round 1' if item in round1 else 'round 2'
        count[(rnd, dim, out)] += 1
        count[('all', dim, out)] += 1
        items[item].add(out)
print(f'{"":10s} {"pressure: second/first/third":>30s} {"plane: second/first/third":>28s}')
for rnd in ('round 1', 'round 2', 'all'):
    cells = ['/'.join(str(count[(rnd, dim, o)]) for o in ('second', 'first', 'third')) for dim in ('pressure', 'plane')]
    print(f'{rnd:10s} {cells[0]:>30s} {cells[1]:>28s}')
print(f'disagreeing items: {len(items)}; items with a changed code: {sum(1 for v in items.values() if v - {"first"})}')
print(f'codes changed although the coders agreed: {len(changed_agreed)} {changed_agreed}')
