#!/usr/bin/env python3
"""Flag cited arXiv preprints whose latest version is withdrawn. usage: check_withdrawn.py <references.bib> [out.tsv]"""
import re, sys, time, urllib.request
bib = open(sys.argv[1]).read(); ids = re.findall(r'@\w+\{([^,]+),[^@]*?(?:eprint = \{|arXiv:)([0-9]{4}\.[0-9]{4,5})', bib)
seen = {}; out = []
for k, a in ids:
    if a in seen: continue
    seen[a] = 1
    for t in range(4):
        try: p = urllib.request.urlopen(urllib.request.Request(f'https://arxiv.org/abs/{a}', headers={'User-Agent': 'survey-bib-check/1.0'}), timeout=60).read().decode('utf8', 'ignore'); break
        except Exception: p = ''; time.sleep(10 * (t + 1))
    st = 'FETCH_FAIL' if not p else ('WITHDRAWN' if re.search(r'This paper has been withdrawn|\(withdrawn\)|withdrawn by', p, re.I) else 'OK')
    out.append((k, a, st)); print(k, a, st, flush=True) if st != 'OK' else None; time.sleep(1.5)
if len(sys.argv) > 2: open(sys.argv[2], 'w').write(''.join(f'{k}\t{a}\t{s}\n' for k, a, s in out))
print(f'checked {len(out)}; withdrawn {sum(s=="WITHDRAWN" for *_, s in out)}; fail {sum(s=="FETCH_FAIL" for *_, s in out)}')
