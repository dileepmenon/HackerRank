#!/bin/python3
import sys
import re

q = int(input().strip())
for a0 in range(q):
	s = input().strip()
	t = int(len(s)/2)
	for i in range(t):
		l = ''
		k1 = 0
		a = s[:i+1]
		l += a
		b = str(int(a)+1)
		if b in s:
			k2 = s.index(b)
		else:
			k2 = 0
		while b in s and k2 == k1+len(a):
			l += b
			a = b
			k1 = [m.start() for m in re.finditer(b, s) if m.start() >= k1][0]
			b = str(int(a)+1)
			indices = [m.start() for m in re.finditer(b, s) if m.start() >= k1]
			if indices != []:
				k2 = indices[0]
		if l == s:
			print ('YES ' + s[:i+1])
			break
	else:
		print ('NO')
