#!/usr/bin/env python3
"""Update search (run 2026-11-17). The main harvest (harvest.json, window 2024-11-01..2026-10-31) stays frozen.
This script re-runs the same six arXiv abstract queries and the title retrieval of the coverage check over the extended
window 2024-11-01..END, and the OpenAlex supplementary search for publication dates after the original window, then
reports every record that is not in the frozen harvest, screened with the same title rule as screen.py.
usage: update_search.py <harvest.json> <references.bib> <out_dir> [END=20261117]"""
import csv, json, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
NS = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
END = sys.argv[4] if len(sys.argv) > 4 else '20261117'
DATE = f'submittedDate:[202411010000 TO {END}2359]'
QUERIES = {  # identical to harvest.py
 'Q1': 'abs:"Model Context Protocol"',
 'Q2': 'abs:"Agent2Agent" OR abs:"A2A protocol"',
 'Q3': 'abs:"agent communication protocol" OR abs:"agent communication protocols"',
 'Q4': 'abs:"agent interoperability" OR abs:"agent protocol" OR abs:"agent protocols"',
 'Q5': 'abs:"Agent Network Protocol" OR abs:"agentic web" OR abs:"internet of agents"',
 'Q6': 'abs:"agentic commerce" OR abs:"agent payments" OR abs:"Agent Payments Protocol"',
 'T': '(ti:"Model Context Protocol" OR ti:MCP OR ti:A2A OR ti:Agent2Agent OR ti:"agent protocol" OR ti:"agent protocols" '
      'OR ti:"agent communication protocol" OR ti:"agent communication protocols")',  # = title_retrieval.py
}
PROTO = re.compile(r'\b(MCP|Model Context Protocol|A2A|Agent2Agent|ANP|Agora|protocols?|interoperab\w*|agentic web|internet of agents|agentic commerce|agent payments?|AP2|x402)\b', re.I)  # = screen.py
NOT_PROTO_MCP = re.compile(r'microchannel|multi-?channel plate|monte carlo', re.I)  # = title_retrieval.py

def arxiv(q):
    recs, start = {}, 0
    while True:
        url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': f'({q}) AND {DATE}', 'start': start, 'max_results': 500, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
        root = None
        for t in range(5):
            try: root = ET.fromstring(urllib.request.urlopen(url, timeout=120).read()); break
            except Exception: time.sleep(10 * (t + 1))
        if root is None: sys.exit('arXiv API unavailable')
        total = int(root.find('o:totalResults', NS).text); es = root.findall('a:entry', NS)
        for e in es:
            i = re.sub(r'v\d+$', '', e.find('a:id', NS).text.split('/abs/')[-1])
            recs[i] = dict(id=i, published=e.find('a:published', NS).text[:10], title=' '.join(e.find('a:title', NS).text.split()),
                           abstract=' '.join(e.find('a:summary', NS).text.split()))
        start += 500; time.sleep(3.5)
        if start >= total or not es: return recs, total

harvest = {r['id']: r for r in json.load(open(sys.argv[1]))['records']}
bib = open(sys.argv[2]).read(); cited = set(re.findall(r'eprint\s*=\s*\{([^}]+)\}', bib))
out = sys.argv[3]
allr, counts = {}, {}
for qid, q in QUERIES.items():
    recs, counts[qid] = arxiv(q)
    for i, r in recs.items():
        if qid == 'T' and NOT_PROTO_MCP.search(r['title']): continue
        allr.setdefault(i, {**r, 'queries': set()})['queries'].add(qid)
    print(qid, counts[qid], file=sys.stderr)
rows = []
for i, r in sorted(allr.items(), key=lambda x: x[1]['published']):
    if i in harvest: continue
    rows.append(dict(id=i, published=r['published'], queries=';'.join(sorted(r['queries'])),
                     window='original (late-indexed)' if r['published'] <= '2026-10-31' else 'extension',
                     protocol_centric=bool(PROTO.search(r['title'])), cited=i in cited, title=r['title'], abstract=r['abstract']))
gone = sorted(set(harvest) - set(allr))
with open(f'{out}/update_search_arxiv.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
with open(f'{out}/update_search_not_returned.tsv', 'w') as f:  # frozen-harvest records the re-run no longer returns
    f.write('id\ttitle\n'); [f.write(f"{i}\t{harvest[i]['title']}\n") for i in gone]
Q6only = [r for r in rows if r['queries'] != 'T']
print('arXiv query counts (extended window):', counts)
print(f'not in frozen harvest: {len(rows)} (abstract queries {len(Q6only)}, title retrieval only {len(rows) - len(Q6only)}); '
      f'original window {sum(r["window"].startswith("orig") for r in rows)}, extension {sum(r["window"] == "extension" for r in rows)}; '
      f'protocol-centric by title rule {sum(r["protocol_centric"] for r in rows)}; frozen records no longer returned {len(gone)}')

# OpenAlex, publication dates after the original window (same query families as openalex_supplement.py)
OQ = ['"Model Context Protocol"', '"Agent2Agent"', '"A2A protocol"', '"agent communication protocol"', '"agent communication protocols"',
      '"agent interoperability"', '"agent protocol"', '"agent protocols"', '"Agent Network Protocol"', '"agentic web"', '"internet of agents"',
      '"agentic commerce"', '"agent payments"', '"Agent Payments Protocol"']
PC = re.compile(r'model context protocol|\bmcp\b|\ba2a\b|agent2agent|agent network protocol|\banp\b|interoperab|agentic web|internet of agents|agent payment|agentic commerce|agent protocol|agent communication protocol', re.I)
endd = f'{END[:4]}-{END[4:6]}-{END[6:]}'; got = {}
for t in OQ:
    cursor = '*'
    while cursor:
        url = 'https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': f'title_and_abstract.search:{t},from_publication_date:2026-11-01,to_publication_date:{endd}', 'per-page': 200, 'cursor': cursor, 'select': 'id,doi,title,publication_date,type,primary_location,locations'})
        d = None
        for a in range(5):
            try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'survey-harvest/1.0'}), timeout=90)); break
            except Exception: time.sleep(10 * (a + 1))
        if not d: print('OpenAlex unavailable for', t, file=sys.stderr); break
        for w in d['results']: got[w['id']] = w
        cursor = d['meta'].get('next_cursor') if d['results'] else None
        time.sleep(0.5)
orows = []
for w in got.values():
    s = [((l.get('source') or {}).get('display_name') or '') for l in (w.get('locations') or [])]
    t = w.get('title') or ''
    orows.append(dict(id=w['id'], doi=(w.get('doi') or '').replace('https://doi.org/', ''), date=w.get('publication_date'), type=w.get('type'),
                      venue=((w.get('primary_location') or {}).get('source') or {}).get('display_name') or '',
                      arxiv_only=all('arxiv' in x.lower() or not x for x in s), protocol_centric=bool(PC.search(t)), title=t))
if orows:
    with open(f'{out}/update_search_openalex.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(orows[0]), delimiter='\t'); w.writeheader(); w.writerows(sorted(orows, key=lambda r: r['date'] or ''))
nonarx = [r for r in orows if not r['arxiv_only']]
print(f'OpenAlex {endd[:8]}01..{endd}: {len(orows)} unique, {len(nonarx)} not arXiv-only, protocol-centric {sum(r["protocol_centric"] for r in nonarx)}')
