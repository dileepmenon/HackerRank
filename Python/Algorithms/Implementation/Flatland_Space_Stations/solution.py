#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
srt_c = [-1]*(max(c)+1)
for i in c:
    srt_c[i] = i
srt_c = list(filter(lambda x: x != -1, srt_c))
dist = []
for i in range(n):
    if i < srt_c[0]:
        min_d = abs(srt_c[0] - i)
    elif i > srt_c[-1]:
        min_d = abs(srt_c[-1] - i)
    else:
        lo = 0
        hi = m - 1
        while lo <= hi:
            mid = (hi + lo)//2
            if i > srt_c[mid]:
                lo = mid
            elif i < srt_c[mid]:
                hi = mid
            else:
                min_d = abs(i - srt_c[mid])
                break
            if hi - lo == 1:
                min_d = min(abs(i - srt_c[lo]), abs(i - srt_c[hi]))
                break
    dist.append(min_d)
print(max(dist))
