import json,re,csv,collections
d=json.load(open('harvest.json')); R=d['records']
PROTO=re.compile(r'\b(MCP|Model Context Protocol|A2A|Agent2Agent|ANP|Agora|protocols?|interoperab\w*|agentic web|internet of agents|agentic commerce|agent payments?|AP2|x402)\b',re.I)
CAT=[('security',r'attack|poison|inject|vulnerab|threat|secur|malicious|adversar|exploit|privacy|trust'),
     ('measurement',r'empirical|measurement|ecosystem|large-scale|we (collect|analy[sz]e|stud)|mining|in the wild'),
     ('benchmark',r'benchmark'),
     ('design',r'we (propose|present|introduce|design)\b.{0,80}(protocol|extension|framework|architecture|layer|registry|standard)'),]
rows=[]; stage=collections.Counter()
for r in R:
    t=r['title']; a=r['abstract']
    central=bool(PROTO.search(t))  # protocol named in title => protocol-centric candidate
    cat='application/other'
    for c,p in CAT:
        if re.search(p,t+' '+a,re.I): cat=c; break
    if not central: cat='excluded:not protocol-centric (title)'
    rows.append({**r,'queries':';'.join(r['queries']),'protocol_centric':central,'category':cat})
    stage[cat]+=1
with open('screening.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','published','title','queries','protocol_centric','category','abstract']); w.writeheader(); w.writerows(rows)
print('records',len(rows)); [print(f'  {k}: {v}') for k,v in stage.most_common()]
print('protocol-centric:',sum(r['protocol_centric'] for r in rows))
# quarterly trend
q=collections.Counter(); q2=collections.Counter()
for r in rows:
    y,m=int(r['published'][:4]),int(r['published'][5:7]); key=f"{y}Q{(m-1)//3+1}"
    if 'Q1' in r['queries']: q[key]+=1
    if 'Q2' in r['queries'] or 'Q3' in r['queries'] or 'Q5' in r['queries']: q2[key]+=1
for k in sorted(set(q)|set(q2)): print(k, q[k], q2[k])
