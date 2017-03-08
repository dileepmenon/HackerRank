#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
max_height = max(height)
if max_height <= k :
	print(0)
else:
	print(max_height-k)
