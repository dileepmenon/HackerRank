#!/bin/python3

import sys

from itertools import combinations


len_s = int(input().strip())
s = input().strip()
uniq_chars = set(s)
n = len(set(s)) - 2
if n < 0:
	print (0)
else:
	char_combinations = list(combinations(uniq_chars, n))
	t = []
	chars = list(s)
	for item in char_combinations:
		rm = chars[:]
		for item_to_delete in item:
			rm = list(filter(lambda a: a != item_to_delete, rm))
		distinct_alter_chars = all([rm[i] != rm[i+1] for i in range(len(rm)-1)])
		if distinct_alter_chars  and len(set(rm)) == 2:
			t.append(len(rm))
	if len(t) == 0:
		print(len(t))
	else:
		print(max(t))






