#!/bin/python3

import sys


n, t = input().strip().split(' ')
n, t = [int(n), int(t)]
c = list(map(int, input().strip().split(' ')))
num_cand = n
cand_added = []
for i in range(t):
    num_cand -= c[i]
    if num_cand < 5 and i != t-1:
        cand_added.append(n - num_cand)
        num_cand += n - num_cand
print(sum(cand_added))
