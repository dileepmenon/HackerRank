#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
dist = []
for i in range(n):
	min_d = 1e6
	for j in range(m):
		d = min(abs(i-j))
		if d < min_d:
			 min_d = d
	dist.append(d)
print(max(dist))
