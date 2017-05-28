#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
a_srt = sorted(a)
min_diff  = abs(a_srt[1] - a_srt[0])
for i, a_i in enumerate(a_srt[1:]):
    diff = abs(a_i - a_srt[i])
    if diff < min_diff:
        min_diff = diff
print(min_diff)


