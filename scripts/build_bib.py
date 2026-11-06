#!/usr/bin/env python3
"""Assemble references.bib for a paper.
usage: build_bib.py <paper_dir> <manual.bib> <venues.txt|-> <arxiv1.bib> [arxiv2.bib ...] [--with-year] [--rename old=new ...]
 --with-year: append the venue year to the note. Use only with a venue file whose years were checked against
              official proceedings (e.g. Paper 1's venues_verified.txt); Semantic Scholar years are unreliable.
 - keeps only entries cited in the manuscript (plus IEEEtran control entry)
 - upgrades arXiv entries to DBLP-verified peer-reviewed venue (keeps eprint/url)"""
import sys,re,glob,os
args=sys.argv[1:]; ren={}
WITH_YEAR='--with-year' in args; args=[a for a in args if a!='--with-year']
if '--rename' in args:
    i=args.index('--rename'); ren=dict(a.split('=') for a in args[i+1:]); args=args[:i]
paper,manual,venues,*arx=args
VEN={'NeurIPS D&B':'Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track','Findings ACL':'Findings of the Assoc. Computational Linguistics: ACL','Findings EMNLP':'Findings of the Assoc. Computational Linguistics: EMNLP','Findings NAACL':'Findings of the Assoc. Computational Linguistics: NAACL','Neural Information Processing Systems':'Advances in Neural Information Processing Systems (NeurIPS)','International Conference on Learning Representations':'Proc. Int. Conf. Learning Representations (ICLR)','International Conference on Machine Learning':'Proc. Int. Conf. Machine Learning (ICML)','Annual Meeting of the Association for Computational Linguistics':'Proc. Annu. Meeting Assoc. Computational Linguistics (ACL)','Conference on Empirical Methods in Natural Language Processing':'Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP)','North American Chapter of the Association for Computational Linguistics':'Proc. NAACL','Conference on Robot Learning':'Proc. Conf. Robot Learning (CoRL)','Computer Vision and Pattern Recognition':'Proc. IEEE/CVF CVPR','Conference on Fairness, Accountability and Transparency':'Proc. ACM FAccT','ACM Symposium on User Interface Software and Technology':'Proc. ACM UIST','International Joint Conference on Artificial Intelligence':'Proc. IJCAI','AAAI Conference on Artificial Intelligence':'Proc. AAAI Conf. Artificial Intelligence','ICLR':'Proc. Int. Conf. Learning Representations (ICLR)','NeurIPS':'Advances in Neural Information Processing Systems (NeurIPS)',
 'ICML':'Proc. Int. Conf. Machine Learning (ICML)','ACL':'Proc. Annu. Meeting Assoc. Computational Linguistics (ACL)',
 'EMNLP':'Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP)','NAACL-HLT':'Proc. NAACL-HLT','COLM':'Proc. Conf. Language Modeling (COLM)',
 'CoRL':'Proc. Conf. Robot Learning (CoRL)','UIST':'Proc. ACM Symp. User Interface Software and Technology (UIST)','CVPR':'Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition (CVPR)',
 'Trans. Mach. Learn. Res.':'Transactions on Machine Learning Research','Journal of machine learning research':'Journal of Machine Learning Research','J. Mach. Learn. Res.':'Journal of Machine Learning Research','Nat.':'Nature','Nat. Mac. Intell.':'Nature Machine Intelligence','Frontiers Comput. Sci.':'Frontiers of Computer Science',
 'Sci. China Inf. Sci.':'Science China Information Sciences','FAccT':'Proc. ACM Conf. Fairness, Accountability, and Transparency (FAccT)','AAAI':'Proc. AAAI Conf. Artificial Intelligence','KDD':'Proc. ACM SIGKDD Conf. Knowledge Discovery and Data Mining (KDD)','WWW':'Proc. ACM Web Conf. (WWW)','CHI':'Proc. CHI Conf. Human Factors in Computing Systems','IJCAI':'Proc. Int. Joint Conf. Artificial Intelligence (IJCAI)','SIGIR':'Proc. Int. ACM SIGIR Conf. Research and Development in Information Retrieval','CIKM':'Proc. ACM Int. Conf. Information and Knowledge Management (CIKM)','COLING':'Proc. Int. Conf. Computational Linguistics (COLING)'}
venue={}
if venues!='-' and os.path.exists(venues):
    for l in open(venues):
        m=re.match(r'(\S+): (.+?) (\d{4}) \| (\S+.*?) \| doi=(.*)$',l.strip())
        if m: venue[m.group(1)]=(m.group(2),m.group(3),m.group(4),m.group(5))
def entries(txt):
    out=[]; 
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,',txt):
        d,i=1,m.end()
        while i<len(txt) and d: d+={'{':1,'}':-1}.get(txt[i],0); i+=1
        out.append((m.group(1),m.group(2),txt[m.start():i]))
    return out
tex=''
for f in [f'{paper}/main.tex']+sorted(glob.glob(f'{paper}/sections/*.tex')): tex+=open(f).read()
cited=set()
for g in re.findall(r'\\cite[tp]?\*?(?:\[[^\]]*\])?\{([^}]+)\}',tex): cited|={k.strip() for k in g.split(',')}
allents={}
for typ,k,body in entries(open(manual).read()): allents[k]=body
for f in arx:
    for typ,k,body in entries(open(f).read()):
        nk=ren.get(k,k); body=body.replace('{'+k+',','{'+nk+',',1)
        if nk in venue:
            v,y,t,doi=venue[nk]; full=re.sub(r'(?<!\\)([&%#])',r'\\\1',VEN.get(v,v))
            # Keep the verified arXiv entry and year; add the peer-reviewed venue as a note (no guessed years).
            fm=re.search(r'\.findings-(acl|emnlp|naacl|eacl)', doi or '', re.I)
            if fm and not full.startswith('Findings'): full=f'Findings of the Assoc. Computational Linguistics: {fm.group(1).upper()}'  # S2 labels Findings papers with the main venue
            if WITH_YEAR: full+=(f' {y}' if full.startswith('Findings') else f', {y}')
            note=f'Published in {full}'
            body=body.rstrip()
            assert body.endswith('}')
            body=body[:-1].rstrip()+(',' if not body[:-1].rstrip().endswith(',') else '')
            if doi and doi!='None' and 'doi =' not in body: body+=f'\n  doi = {{{doi}}},'
            body+=f'\n  note = {{{note}}}\n}}'
        if nk not in allents: allents[nk]=body
# ---- Normalization (all papers): non-ASCII to LaTeX, corporate "X Team" authors, per-paper fixes ----
UNI={'τ':r'\tau','π':r'\pi','α':r'\alpha','β':r'\beta','γ':r'\gamma','λ':r'\lambda','μ':r'\mu','δ':r'\delta',
     'ć':r"{\'c}",'č':r'{\v{c}}','š':r'{\v{s}}','ž':r'{\v{z}}','ř':r'{\v{r}}','ł':r'{\l}','ø':r'{\o}','ß':r'{\ss}',
     'é':r"{\'e}",'è':r'{\`e}','ê':r'{\^e}','ë':r'{\"e}','á':r"{\'a}",'à':r'{\`a}','â':r'{\^a}','ä':r'{\"a}','ã':r'{\~a}','å':r'{\aa}',
     'í':r"{\'i}",'ï':r'{\"i}','ó':r"{\'o}",'ò':r'{\`o}','ô':r'{\^o}','ö':r'{\"o}','õ':r'{\~o}','ú':r"{\'u}",'ü':r'{\"u}','ñ':r'{\~n}',
     'ç':r'{\c{c}}','ı':r'{\i}','É':r"{\'E}",'Ö':r'{\"O}','Ü':r'{\"U}','Ł':r'{\L}','Š':r'{\v{S}}','–':'--','—':'---','’':"'",'‘':'`','“':'``','”':"''"}
GREEK=set('τπαβγλμδ')
def norm(body):
    def fix_field(m):
        val=m.group(2); out=''; inmath=False
        for ch in val:
            if ch=='$': inmath=not inmath
            if ch in UNI:
                r=UNI[ch]; out+= (r if inmath else ('{$'+r+'$}')) if ch in GREEK else r
            else: out+=ch
        return m.group(1)+out
    body=re.sub(r'(\b(?:author|title)\s*=\s*\{)(.*)',fix_field,body)
    body=re.sub(r'(author\s*=\s*\{)\s*([A-Z][\w.-]*(?: [\w.-]+)?) Team and',r'\1{\2 Team} and',body)  # "Kimi Team" -> corporate
    body=re.sub(r'(title\s*=\s*\{[^\n]*?) :',r'\1:',body)  # "GUI-R1 : A" -> "GUI-R1: A"
    # "Agents:Mechanisms" -> "Agents: Mechanisms" (arXiv titles sometimes omit the space after a colon)
    body=re.sub(r'(\btitle\s*=\s*\{.*)',lambda m: re.sub(r'(?<=[A-Za-z0-9)]):(?=[A-Za-z])',': ',m.group(1)),body)
    # Capitalize the first word of a subtitle ("memories: separating" -> "memories: Separating")
    body=re.sub(r'(\btitle\s*=\s*\{.*)',lambda m: re.sub(r'(: )([a-z])',lambda n: n.group(1)+n.group(2).upper(),m.group(1)),body)
    # IEEEtran lowercases the word after "? " (subtitle after a question): protect its capital ("? {E}valuating")
    body=re.sub(r'(\btitle\s*=\s*\{.*)',lambda m: re.sub(r'(\? )([A-Z])(?=[a-z])',r'\1{\2}',m.group(1)),body)
    # Hyphenated given names with a lowercase second part (Tzu-iunn, Hung-yi): brace them so BibTeX
    # does not read the second part as a "von" particle ("K. T. iunn Ong").
    body=re.sub(r'(\bauthor\s*=\s*\{.*)',lambda m: re.sub(r'(?<![{\w-])([A-Z][a-z]+-[a-z]+)(?=[\s,}])',r'{\1}',m.group(1)),body)
    # Protect name-like tokens that the bibliography style would lowercase (R1-Searcher, Memory-R1, K2, v3).
    def protect(m):
        head, val = m.group(1), m.group(2)
        def tok(t):
            core = t.rstrip(':,;?!.)"\''); tail = t[len(core):]
            lead = core[:len(core) - len(core.lstrip('("`\''))]; core = core[len(lead):]
            if not core or any(c in core for c in '{}\\$'): return t
            parts = core.split('-')
            if (any(re.search(r'[A-Z]', q[1:]) for q in parts) or (re.search(r'\d', core) and re.search(r'[A-Z]', core))
                    or (tail.startswith(':') and len(parts) > 1 and sum(q[:1].isupper() for q in parts) >= 2)):  # system names before the colon (O-Mem:, Mem-Gallery:)
                return lead + '{' + core + '}' + tail
            return t
        return head + ' '.join(tok(t) for t in val.split(' '))
    body=re.sub(r'(\btitle\s*=\s*\{)(.*)(?=\},\s*$)',protect,body,flags=re.M)
    return body
fixfile=os.path.join(os.path.dirname(manual),'bib_fixes.tsv')
FIX=[l.rstrip('\n').split('\t') for l in open(fixfile) if l.strip() and not l.startswith('#')] if os.path.exists(fixfile) else []
for k in list(allents):
    b=norm(allents[k])
    for fk,old,new in FIX:
        old,new=old.replace("\\n","\n"),new.replace("\\n","\n")
        if fk==k:
            if old not in b: print(f'WARNING bib_fixes: {k}: {old!r} not found')
            b=b.replace(old,new)
    allents[k]=b
out=[allents['IEEEexample:BSTcontrol']] if 'IEEEexample:BSTcontrol' in allents else []
missing=sorted(cited-set(allents))
for k in sorted(cited&set(allents)): out.append(allents[k])
open(f'{paper}/references.bib','w').write('\n\n'.join(out)+'\n')
print(f'wrote {len(out)-1} entries; upgraded to venue: {sum(1 for k in cited if k in venue)}; MISSING: {missing}')
