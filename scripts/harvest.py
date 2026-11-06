import urllib.request, urllib.parse, xml.etree.ElementTree as ET, time, json, csv, sys
NS={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
DATE='submittedDate:[202411010000 TO 202610312359]'
QUERIES={
 'Q1':'abs:"Model Context Protocol"',
 'Q2':'abs:"Agent2Agent" OR abs:"A2A protocol"',
 'Q3':'abs:"agent communication protocol" OR abs:"agent communication protocols"',
 'Q4':'abs:"agent interoperability" OR abs:"agent protocol" OR abs:"agent protocols"',
 'Q5':'abs:"Agent Network Protocol" OR abs:"agentic web" OR abs:"internet of agents"',
 'Q6':'abs:"agentic commerce" OR abs:"agent payments" OR abs:"Agent Payments Protocol"',
}
recs={}; counts={}
for qid,q in QUERIES.items():
    start=0; total=None; got=0
    while True:
        url='http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':f'({q}) AND {DATE}','start':start,'max_results':500,'sortBy':'submittedDate','sortOrder':'ascending'})
        for t in range(4):
            try: root=ET.fromstring(urllib.request.urlopen(url,timeout=120).read()); break
            except Exception as e: time.sleep(5)
        total=int(root.find('o:totalResults',NS).text)
        es=root.findall('a:entry',NS)
        for e in es:
            i=e.find('a:id',NS).text.split('/abs/')[-1].split('v')[0]
            r=recs.setdefault(i,{'id':i,'title':' '.join(e.find('a:title',NS).text.split()),'published':e.find('a:published',NS).text[:10],'abstract':' '.join(e.find('a:summary',NS).text.split()),'queries':set()})
            r['queries'].add(qid)
        got+=len(es); start+=500
        if got>=total or not es: break
        time.sleep(3.5)
    counts[qid]=total; print(qid,total,file=sys.stderr); time.sleep(3.5)
json.dump({'counts':counts,'records':[{**r,'queries':sorted(r['queries'])} for r in recs.values()]},open('harvest.json','w'))
print('identified (sum)',sum(counts.values()),'unique',len(recs))
