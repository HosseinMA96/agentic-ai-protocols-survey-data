#!/usr/bin/env python3
"""Learning-centric screen of the protocol-centric pool (Methodology, "Learning-centric screen").

Flags every protocol-centric record whose title or abstract describes training, fine-tuning, reinforcement
learning, distillation, or training-data synthesis. The manual decision for every flagged record that was not
already cited is in learning_screen_decisions.tsv; records included there are treated as not yet cited, so the
output reproduces the candidate list as it stood before the screen (37 flagged, 7 already cited).

usage (data repository root):  python3 scripts/learning_screen.py
usage (survey literature/):    python3 scripts/learning_screen.py screening.csv ../paper/references.bib \\
                                   learning_screen_decisions.tsv learning_screen.tsv
"""
import csv, re, sys

args = sys.argv[1:] or ['data/harvest/screening.csv', 'data/bib/references.bib',
                        'data/harvest/learning_screen_decisions.tsv', 'data/harvest/learning_screen.tsv']
SCREENING, BIB, DECISIONS, OUT = args

LEARN = re.compile(
    r'fine-tun\w*|post-train\w*|reinforcement learning|\bRL\b|\bGRPO\b|\bPPO\b|\bDPO\b|'
    r'preference (?:alignment|optimi[sz]ation)|training (?:data|set|corpus|corpora|trajector\w*|environment\w*)|'
    r'synthesi[sz]\w*(?:\W+\w+){0,3}?\W+(?:data|trajector\w*|tasks)|distill\w*|reward\w*|'
    r'\bwe train\b|\btrained (?:on|with|using)\b|imitation learning|curricul\w*|self-evolv\w*|self-improv\w*',
    re.I)

bib = open(BIB, encoding='utf-8').read()
added = {r['id'] for r in csv.DictReader(open(DECISIONS, encoding='utf-8'), delimiter='\t') if r['decision'] == 'include'}
cited = set(re.findall(r'eprint\s*=\s*\{([^}]+)\}', bib)) - added
rows = [r for r in csv.DictReader(open(SCREENING, encoding='utf-8')) if r['protocol_centric'] == 'True']
out = []
for r in rows:
    hits = sorted({m.group(0).lower() for m in LEARN.finditer(r['title'] + ' ' + r['abstract'])})
    if hits:
        out.append({'id': r['id'], 'published': r['published'][:10], 'cited': r['id'] in cited,
                    'matched': '; '.join(hits), 'title': r['title']})
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'published', 'cited', 'matched', 'title'], delimiter='\t', lineterminator='\n')
    w.writeheader(); w.writerows(out)
print(f'{len(rows)} protocol-centric records; {len(out)} match the learning rule '
      f'({sum(o["cited"] for o in out)} cited before the screen; {len(added)} added by it)')
