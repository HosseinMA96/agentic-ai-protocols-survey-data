#!/usr/bin/env python3
"""Cohen's kappa between dp_coding.tsv (coder 1) and a filled second_coder_sample.tsv (coder 2).
usage: kappa.py [second_coder_sample.tsv]"""
import csv, sys, collections
c1 = {r['item']: r for r in csv.DictReader(open('dp_coding.tsv'), delimiter='\t')}
s = [r for r in csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else 'second_coder_sample.tsv'), delimiter='\t') if r['primary_dp_coder2'].strip()]
if not s: sys.exit('second coder column is empty')
for col1, col2 in (('primary_dp', 'primary_dp_coder2'), ('plane', 'plane_coder2')):
    pairs = [(c1[r['item']][col1], r[col2].strip().upper()) for r in s if r[col2].strip()]
    n = len(pairs); po = sum(a == b for a, b in pairs) / n
    A = collections.Counter(a for a, _ in pairs); B = collections.Counter(b for _, b in pairs)
    pe = sum(A[k] * B[k] for k in set(A) | set(B)) / n ** 2
    print(f'{col1}: n={n} agreement={po:.3f} kappa={(po - pe) / (1 - pe):.3f}')
