#!/usr/bin/env python3
"""Coverage check, part 2: every arXiv paper whose TITLE names MCP, A2A, or an agent protocol (Nov 2024 - Oct 2026),
compared with the protocol-centric pool of the main harvest (screening.csv) and with references.bib.
usage: title_retrieval.py <screening.csv> <references.bib> <out.tsv>"""
import csv, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
NS = {'a': 'http://www.w3.org/2005/Atom'}
Q = ('(ti:"Model Context Protocol" OR ti:MCP OR ti:A2A OR ti:Agent2Agent OR ti:"agent protocol" OR ti:"agent protocols" '
     'OR ti:"agent communication protocol" OR ti:"agent communication protocols") AND submittedDate:[202411010000 TO 202610312359]')
scr = {r['id']: r for r in csv.DictReader(open(sys.argv[1]))}
bib = open(sys.argv[2]).read(); cited = set(re.findall(r'eprint\s*=\s*\{([^}]+)\}', bib))
got = {}
for start in range(0, 3000, 200):
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': Q, 'start': start, 'max_results': 200, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
    for _ in range(5):
        try: root = ET.fromstring(urllib.request.urlopen(url, timeout=120).read()); break
        except Exception: root = None; time.sleep(60)
    if root is None: sys.exit('arXiv API unavailable')
    es = root.findall('a:entry', NS)
    for e in es:
        aid = re.sub(r'v\d+$', '', e.find('a:id', NS).text.split('/abs/')[-1])
        got[aid] = (e.find('a:published', NS).text[:10], ' '.join(e.find('a:title', NS).text.split()))
    time.sleep(3.5)
    if len(es) < 200: break
# MCP also abbreviates unrelated things (e.g. microchannel plates); keep titles where MCP is plausibly the protocol
keep = {k: v for k, v in got.items() if not re.search(r'microchannel|multi-?channel plate|monte carlo', v[1], re.I)}
with open(sys.argv[3], 'w') as f:
    f.write('id\tpublished\tin_harvest\tharvest_protocol_centric\tcited\ttitle\n')
    for k, (d, t) in sorted(keep.items(), key=lambda x: x[1][0]):
        f.write(f"{k}\t{d}\t{k in scr}\t{scr[k]['protocol_centric'] if k in scr else ''}\t{k in cited}\t{t}\n")
pc = {k for k, r in scr.items() if r['protocol_centric'] == 'True'}
K = set(keep)
print(f'title-retrieved: {len(K)} (raw {len(got)}); also protocol-centric in harvest: {len(K & pc)}; in harvest but not protocol-centric: {len(K & (set(scr) - pc))}; not in harvest: {len(K - set(scr))}')
print(f'protocol-centric harvest records not title-retrieved: {len(pc - K)}; cited among title-retrieved: {len(K & cited)}; cited among new-only: {len((K - set(scr)) & cited)}')
