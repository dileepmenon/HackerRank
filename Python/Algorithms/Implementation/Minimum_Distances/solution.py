#!/bin/python3

import sys

import collections
from collections import Counter


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
if abs(len(set(A))-len(A)) == 0:
    print (-1)
else:
    dup_A = Counter(A)
    dup_ele_A = []
    for i in dup_A:
        if dup_A[i] > 1:
            dup_ele_A.append(i)
    dups_index = collections.defaultdict(list)
    for dup in dup_ele_A:
        for index, item in enumerate(A):
            if item == dup:
                dups_index[item].append(index)
    index_diff_min = 2e5
    for index_list in dups_index.values():
        if len(index_list) == 2:
            index_diff  = abs(index_list[1] - index_list[0])
        else:
            l = []
            for i,j in enumerate(index_list[:-1]):
                l.append(abs(index_list[i+1] - index_list[i]))
            index_diff = min(l)
        if index_diff_min > index_diff:
            index_diff_min = index_diff
    print(index_diff_min)
