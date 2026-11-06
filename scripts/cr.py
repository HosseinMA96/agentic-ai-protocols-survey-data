import sys,json,urllib.request,urllib.parse
H={'User-Agent':'survey-bib-check/1.0'}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=60))
for a in sys.argv[1:]:
    try:
        if a.startswith('10.'):
            m=get('https://api.crossref.org/works/'+urllib.parse.quote(a))['message']
        else:
            m=get('https://api.crossref.org/works?rows=1&query.bibliographic='+urllib.parse.quote(a))['message']['items'][0]
        au='; '.join(f"{x.get('family','')}, {x.get('given','')}" for x in m.get('author',[])[:8])
        y=(m.get('published-print') or m.get('published-online') or m.get('issued'))['date-parts'][0]
        print(f"[{a[:40]}] DOI {m['DOI']} | {m.get('title',[''])[0]} | {au} | {(m.get('container-title') or [''])[0]} | {y} | vol {m.get('volume','')} no {m.get('issue','')} pp {m.get('page','')}")
    except Exception as e: print(f"[{a}] ERROR {e}")
