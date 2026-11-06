import sys, urllib.request, urllib.parse, xml.etree.ElementTree as ET, time
NS={'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom'}
def q(params):
    url='http://export.arxiv.org/api/query?'+urllib.parse.urlencode(params)
    for i in range(3):
        try: return ET.fromstring(urllib.request.urlopen(url,timeout=60).read())
        except Exception as e: time.sleep(3)
def show(root):
    for e in root.findall('a:entry',NS):
        i=e.find('a:id',NS).text.split('/abs/')[-1]
        t=' '.join(e.find('a:title',NS).text.split())
        au=[a.find('a:name',NS).text for a in e.findall('a:author',NS)]
        d=e.find('a:published',NS).text[:10]
        doi=e.find('x:doi',NS); jr=e.find('x:journal_ref',NS)
        print(f"{i} | {d} | {t} | {', '.join(au[:6])}{' et al.' if len(au)>6 else ''} ({len(au)})"+(f" | DOI {doi.text}" if doi is not None else "")+(f" | JR {jr.text}" if jr is not None else ""))
mode=sys.argv[1]
if mode=='id': show(q({'id_list':','.join(sys.argv[2:]),'max_results':50}))
else:
    for s in sys.argv[2:]:
        print('##',s); show(q({'search_query':s,'max_results':12,'sortBy':'relevance'})); time.sleep(3)
