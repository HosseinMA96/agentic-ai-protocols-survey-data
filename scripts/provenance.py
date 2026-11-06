#!/usr/bin/env python3
"""Provenance of cited works (Table II). usage: python3 scripts/provenance.py  (run from the repository root)"""
import re, csv, glob
n = lambda s: re.sub(r'[^a-z0-9]', '', re.sub(r'\\[a-z]+|[{}$]', '', s.lower()))[:50]
bib = open('data/bib/references.bib').read(); cited = {l.strip() for l in open('data/bib/cited_keys.txt') if l.strip()}
scr = {r['id']: r for r in csv.DictReader(open('data/harvest/screening.csv'))}; ti = {n(r['title']): r for r in scr.values()}
k5 = {l.split()[0] for l in open('data/coverage/coverage_check_added_keys.txt') if l.strip()}
OA = {'li2026confused', 'park2026token', 'deshmukh2026agentcard', 'he2026bugs', 'debi2026whispers'}
GREY_EXTRA = {'google2025a2a'}; POOL_EXTRA = {'habler2025a2a'}
STD = r'^(rfc|w3c|oasis|fipa|jsonrpc|openapi|erc8004|cimddraft|oauth21draft|lsp|ecma|webbotauthdraft|txntokensdraft)'
tr = {r['id']: r for r in csv.DictReader(open('data/coverage/rerun_2026-11-05/title_retrieval.tsv'), delimiter='\t')}
cat = {}
for m in re.finditer(r'@(\w+)\{([^,]+),(.*?)\n\}', bib, re.S):
    t, k, b = m.groups()
    if k not in cited: continue
    e = re.search(r'eprint = \{([^}]*)', b); y = re.search(r'year = \{(\d+)', b); y = int(y.group(1)) if y else 0
    tt = re.search(r'title = \{(.*)\},?\n', b).group(1); ax = e.group(1) if e else None; doi = 'doi =' in b
    r = (scr.get(ax) if ax else None) or ti.get(n(tt))
    if k in OA: c = '4 OpenAlex only'
    elif k in POOL_EXTRA or (r and r['protocol_centric'] == 'True'): c = '2 pool, added by coverage check' if k in k5 else '1 pool, initial synthesis'
    elif k in GREY_EXTRA: c = '8 grey'
    elif k in k5: c = '3a coverage only: title retrieval' if ax in tr and tr[ax]['in_harvest'] == 'False' else '3b coverage only: survey bibliographies (first run)'
    elif re.search(STD, k): c = '7 standards'
    elif not ax and not doi: c = '8 grey'
    elif y and y < 2024: c = '6 foundations'
    else: c = '5 snowball 2024+'
    cat.setdefault(c, []).append(k)
for c, v in sorted(cat.items()): print(len(v), c)
print(sum(map(len, cat.values())), 'cited')
