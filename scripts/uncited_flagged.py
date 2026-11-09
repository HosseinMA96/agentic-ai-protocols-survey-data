#!/usr/bin/env python3
"""List the protocol-centric pool records that the title retrieval flagged but the survey does not cite (Section II-E).
usage: python3 scripts/uncited_flagged.py [out.tsv]   (run from the data repository root, or from literature/)
Default output: data/coverage/uncited_flagged_pool.tsv (repository) or ../data_release/data/coverage/... (literature/).
Matches cited works to records the same way as
provenance.py (arXiv ID, else normalized title), so works cited in their peer-reviewed version count as cited."""
import csv, collections, os, re, sys
REPO = os.path.exists('data/harvest/screening.csv')  # data repository layout vs. the survey's literature/ folder
P = (dict(scr='data/harvest/screening.csv', wd='data/verification/withdrawn_check.tsv',
          tr='data/coverage/rerun_2026-11-05/title_retrieval.tsv', out='data/coverage/uncited_flagged_pool.tsv') if REPO else
     dict(scr='screening.csv', wd='verification/withdrawn_check.tsv',
          tr='coverage/rerun_2026-11-05/title_retrieval.tsv', out='../data_release/data/coverage/uncited_flagged_pool.tsv'))
src = open('scripts/provenance.py').read()
src = src.replace("for c, v in sorted(cat.items()): print(len(v), c)\nprint(sum(map(len, cat.values())), 'cited')", '')
src = src.replace("    cat.setdefault(c, []).append(k)", "    cat.setdefault(c, []).append(k); REC[k] = r['id'] if r else None")
g = {}; exec(compile('REC = {}\n' + src, 'provenance.py', 'exec'), g)
cited_ids = {v for v in g['REC'].values() if v}
WITHDRAWN = {r.split('\t')[1] for r in open(P['wd']) if '\tWITHDRAWN' in r}
scr = {r['id']: r for r in csv.DictReader(open(P['scr']))}
flagged = [r for r in csv.DictReader(open(P['tr']), delimiter='\t')
           if r['harvest_protocol_centric'] == 'True']
rows = [r for r in flagged if r['id'] not in cited_ids]
out = sys.argv[1] if len(sys.argv) > 1 else P['out']
with open(out, 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(['id', 'published', 'keyword_category', 'note', 'title'])
    for r in sorted(rows, key=lambda r: (scr[r['id']]['category'], r['id'])):
        w.writerow([r['id'], r['published'], scr[r['id']]['category'],
                    'withdrawn by its authors' if r['id'] in WITHDRAWN else '', r['title']])
print(f'{len(flagged)} flagged pool records; {len(flagged) - len(rows)} cited; {len(rows)} uncited ->', out)
print('uncited by keyword category:', dict(collections.Counter(scr[r['id']]['category'] for r in rows).most_common()))
print('withdrawn among uncited:', sum(r['id'] in WITHDRAWN for r in rows))
