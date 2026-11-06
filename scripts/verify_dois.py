#!/usr/bin/env python3
"""Resolve every DOI in a references.bib through Crossref and confirm title + first-author surname.
Also prints the Crossref container title next to any 'Published in ...' note so venue notes can be audited.
usage: verify_dois.py <references.bib> [out.tsv]   -- polite: 1 s between requests."""
import re, sys, time, json, html, difflib, unicodedata, urllib.request, urllib.parse
bib = open(sys.argv[1]).read(); out = sys.argv[2] if len(sys.argv) > 2 else None
H = {'User-Agent': 'survey-bib-check/1.0'}
ACC = {r"\'": '\u0301', r'\`': '\u0300', r'\^': '\u0302', r'\"': '\u0308', r'\~': '\u0303', r'\v': '\u030c', r'\c': '\u0327'}
def norm(t):
    t = re.sub(r'\\([\'`^"~vc])\{?(\w)\}?', lambda m: m.group(2), t)
    t = unicodedata.normalize('NFKD', html.unescape(t)).encode('ascii', 'ignore').decode()
    t = re.sub(r'<[^>]+>', '', t); t = re.sub(r'\\[a-zA-Z]+|[{}$\\"\'`^~]', '', t)
    return re.sub(r'[^a-z0-9]', '', t.lower())
def field(body, name):
    m = re.search(r'\b' + name + r'\s*=\s*\{(.*)\},?\s*$', body, re.M); return m.group(1) if m else ''
rows = []
for m in re.finditer(r'@(\w+)\{([^,]+),(.*?)\n\}', bib, re.S):
    typ, key, body = m.groups(); doi = field(body, 'doi')
    if doi: rows.append((key, doi, field(body, 'title'), field(body, 'author'), field(body, 'note'), field(body, 'booktitle') or field(body, 'journal'), field(body, 'year')))
res = []
for key, doi, title, auth, note, venue, year in rows:
    msg = None
    for attempt in range(3):
        try:
            msg = json.load(urllib.request.urlopen(urllib.request.Request('https://api.crossref.org/works/' + urllib.parse.quote(doi), headers=H), timeout=60))['message']; break
        except urllib.error.HTTPError as ex:
            if ex.code == 404: break
            time.sleep(5 * (attempt + 1))
        except Exception:
            time.sleep(5 * (attempt + 1))
    if not msg:
        res.append((key, doi, 'NOT_FOUND', '', '', '', '')); print(key, doi, 'NOT_FOUND', flush=True); time.sleep(1); continue
    ctitle = (msg.get('title') or [''])[0]; cont = (msg.get('container-title') or [''])[0]
    cau = (msg.get('author') or [{}])[0]; cfam = cau.get('family', '') or cau.get('name', '')
    cyear = ((msg.get('published-print') or msg.get('published-online') or msg.get('issued') or {}).get('date-parts') or [['']])[0][0]
    sim = difflib.SequenceMatcher(None, norm(title), norm(ctitle)).ratio()
    first = re.split(r'\s+and\s+', auth.strip())[0].strip(' {}')
    sur = norm(first.split(',')[0] if ',' in first else (first.split()[-1] if first.split() else ''))
    aok = (not auth) or (not cfam) or sur == norm(cfam) or norm(cfam) in norm(first) or sur in norm(cfam)
    status = []
    if sim < 0.85: status.append(f'TITLE_MISMATCH({sim:.2f})')
    if not aok: status.append('AUTHOR_MISMATCH')
    if year and str(cyear) and str(cyear) != year: status.append(f'YEAR({year}->{cyear})')
    st = ' '.join(status) or 'OK'
    res.append((key, doi, st, ctitle, cfam, cont, str(cyear)))
    print(key, doi, st, '|', ctitle[:90], '|', cfam, '|', cont, '|', cyear, '| note:', note[:80], flush=True)
    time.sleep(1)
if out:
    with open(out, 'w') as f:
        f.write('key\tdoi\tstatus\tcrossref_title\tcrossref_first_author\tcontainer\tyear\n')
        for r in res: f.write('\t'.join(r) + '\n')
bad = [r for r in res if r[2] != 'OK']
print(f'checked {len(res)} DOIs; {len(res) - len(bad)} OK; {len(bad)} flagged')
