#!/bin/python3

import sys

def patternCount(s):
    # Complete this function
	one_idx = []
	for i, s_i in enumerate(s):
		if s_i ==  '1':
			one_idx.append(i)
	coun = 0
	for j in range(len(one_idx)-1):
		a1 = one_idx[j]
		a2 = one_idx[j+1]
		diff_idx = a2 - a1
		if diff_idx > 1:
			if all([k == '0' for k in s[a1+1:a2]]):
				coun += 1
	return coun

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)


