#!/usr/bin/env python3
"""Reference-integrity fixes after the Nov. 5, 2026 review (Paper 4).
Applies (1) the shared title/author normalization of shared/tools/build_bib.py (acronym bracing, accents),
(2) Crossref-derived venue notes with years for every entry that has a DOI, and (3) hand-verified fixes listed
in FIXES below (each backed by literature/verification/doi_check.tsv or a Crossref lookup).
usage: fix_bib_round1.py <references.bib> <doi_check.tsv>"""
import re, sys, os
bibf, doitsv = sys.argv[1], sys.argv[2]
src = open(os.path.join(os.path.dirname(__file__), 'build_bib.py')).read()
seg = src[src.index('UNI={'):src.index('fixfile=')]
ns = {'re': re}; exec(seg, ns); ns['UNI']['ń'] = r"{\'n}"; norm = ns['norm']
bib = open(bibf).read()
ents = {m.group(2): m.group(0) for m in re.finditer(r'@(\w+)\{([^,]+),(.*?)\n\}', bib, re.S)}
order = list(ents)
def setf(k, f, v):
    e = ents[k]
    if re.search(r'\n  ' + f + r' = \{', e): e = re.sub(r'\n  ' + f + r' = \{.*\}(,?)(?=\n)', lambda m: '\n  ' + f + ' = {' + v + '}' + m.group(1), e)
    else: e = e[:-2] + ',\n  ' + f + ' = {' + v + '}\n}'
    ents[k] = e
def delf(k, f): ents[k] = re.sub(r',?\n  ' + f + r' = \{.*\}(?=,?\n)', '', ents[k]).replace('{,\n', '{\n')
# (2) Crossref venue + year for DOI-backed entries that carry a "Published in" note
cr = {r[0]: r for r in (l.rstrip('\n').split('\t') for l in open(doitsv)) if r[0] != 'key'}
for k, r in cr.items():
    if k in ents and 'note = {Published in' in ents[k] and r[5]:
        setf(k, 'note', f'Published in {r[5]}, {r[6]}')
# (3) hand-verified fixes
setf('bhatt2025etdi', 'note', 'Published in 2025 Cyber Awareness and Research Symposium (CARS), 2025')
for k in ('huang2025ans', 'narajala2025enterprise'):
    setf(k, 'note', 'Published in 2026 IEEE 5th International Conference on AI in Cybersecurity (ICAIC), 2026')
delf('maloyan2026breaking', 'note')
ents['gaire2026sok'] = ents.pop('gaire2027sok').replace('{gaire2027sok,', '{gaire2026sok,'); order[order.index('gaire2027sok')] = 'gaire2026sok'
setf('gaire2026sok', 'year', '2026'); setf('gaire2026sok', 'booktitle', 'Intelligent Systems and Applications (IntelliSys), Lecture Notes in Networks and Systems')
setf('gaire2026sok', 'note', 'Published online Aug. 2026; print volume dated 2027')
setf('rfc9207', 'author', '{Meyer zu Selhausen}, Karsten and Fett, Daniel')
setf('chen2024ioa', 'note', 'Published in Proc. Int. Conf. Learning Representations (ICLR), 2025')
setf('patil2023gorilla', 'note', 'Published in Advances in Neural Information Processing Systems 37 (NeurIPS), 2024')
setf('jeong2025mcpa2a', 'title', r'A Practical {MCP}$\times${A2A} Integration Framework for Interoperability in {LLM}-Based Autonomous Multi-Agent Systems')
setf('jeong2025mcpa2a', 'doi', '10.13088/jiis.2025.31.10.141')
delf('steiner2025mcp', 'doi'); delf('steiner2025mcp', 'note')
setf('lumer2025scalemcp', 'doi', '10.1007/978-3-032-15632-7_2')
setf('lumer2025scalemcp', 'note', 'Published in Computational Intelligence (IJCCI 2025), Communications in Computer and Information Science, Springer, 2026, pp. 23--42')
setf('vaziry2025x402', 'title', r'Enhancing the {A2A} Protocol with Blockchain-Based Identities and x402 Micropayments for Agentic {AI}')
setf('vaziry2025x402', 'year', '2026'); setf('vaziry2025x402', 'pages', '454--472')
setf('radosevich2025audit', 'author', 'John T. Halloran and Brandon Radosevich and Gavin Black')
setf('radosevich2025audit', 'note', 'Published in Assurance and Security for AI-enabled Systems 2026 (SPIE Defense + Security), 2026')
out = []
for k in order:
    e = ents[k]
    if not k.startswith('IEEEexample'): e = norm(e)
    out.append(e)
open(bibf, 'w').write('\n\n'.join(out) + '\n')
print('fixed', len(out), 'entries')
