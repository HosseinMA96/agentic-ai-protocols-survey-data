#!/usr/bin/env python3
"""Supplementary database search (M5): OpenAlex, which indexes ACM, IEEE, Springer, Elsevier, and other publishers.
Same six query families as the arXiv harvest, title+abstract field, publication dates 2024-11-01..2026-10-31.
Reports records that are NOT arXiv-only and have no counterpart (DOI-free title match) in the arXiv harvest, and
applies the same title rule for protocol-centric screening.
usage: openalex_supplement.py <screening.csv> <references.bib> <out.tsv>"""
import csv, json, re, sys, time, urllib.parse, urllib.request
Q = {'Q1': ['"Model Context Protocol"'], 'Q2': ['"Agent2Agent"', '"A2A protocol"'], 'Q3': ['"agent communication protocol"', '"agent communication protocols"'],
     'Q4': ['"agent interoperability"', '"agent protocol"', '"agent protocols"'], 'Q5': ['"Agent Network Protocol"', '"agentic web"', '"internet of agents"'],
     'Q6': ['"agentic commerce"', '"agent payments"', '"Agent Payments Protocol"']}
n = lambda s: re.sub(r'[^a-z0-9]', '', (s or '').lower())[:60]
scr = list(csv.DictReader(open(sys.argv[1]))); harvest_t = {n(r['title']) for r in scr}
bib = open(sys.argv[2]).read(); cited_t = {n(re.sub(r'[{}\\$]', '', t)) for t in re.findall(r'\btitle = \{(.*)\},?\n', bib)}
cited_doi = {d.lower() for d in re.findall(r'doi = \{([^}]*)\}', bib)}
PC = re.compile(r'model context protocol|\bmcp\b|\ba2a\b|agent2agent|agent network protocol|\banp\b|interoperab|agentic web|internet of agents|agent payment|agentic commerce|agent protocol|agent communication protocol', re.I)
got = {}; per_q = {}
for q, terms in Q.items():
    ids = set()
    for t in terms:
        cursor = '*'
        while cursor:
            url = 'https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': f'title_and_abstract.search:{t},from_publication_date:2024-11-01,to_publication_date:2026-10-31', 'per-page': 200, 'cursor': cursor, 'select': 'id,doi,title,publication_date,type,primary_location,locations'})
            for a in range(5):
                try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'survey-harvest/1.0'}), timeout=90)); break
                except Exception: d = None; time.sleep(10 * (a + 1))
            if not d: break
            for w in d['results']:
                ids.add(w['id']); got[w['id']] = w
            cursor = d['meta'].get('next_cursor') if d['results'] else None
            time.sleep(0.5)
    per_q[q] = len(ids)
def src(w):
    return [((l.get('source') or {}).get('display_name') or '') for l in (w.get('locations') or [])]
rows = []
for w in got.values():
    s = src(w); arxiv_only = all('arxiv' in x.lower() or not x for x in s)
    t = w.get('title') or ''; doi = (w.get('doi') or '').replace('https://doi.org/', '').lower()
    rows.append(dict(id=w['id'], doi=doi, date=w.get('publication_date'), type=w.get('type'), venue=((w.get('primary_location') or {}).get('source') or {}).get('display_name') or '',
                     arxiv_only=arxiv_only, in_harvest=n(t) in harvest_t, protocol_centric=bool(PC.search(t)), cited=(n(t) in cited_t or doi in cited_doi), title=t))
with open(sys.argv[3], 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(sorted(rows, key=lambda r: r['date'] or ''))
new = [r for r in rows if not r['arxiv_only'] and not r['in_harvest']]
print('per query:', per_q, '| unique:', len(rows))
print('not arXiv-only:', sum(not r['arxiv_only'] for r in rows), '| of which absent from arXiv harvest:', len(new))
print('delta, protocol-centric by title rule:', sum(r['protocol_centric'] for r in new), '| already cited:', sum(r['cited'] for r in new))
print('delta by type:', {t: sum(r['type'] == t for r in new) for t in {r['type'] for r in new}})
