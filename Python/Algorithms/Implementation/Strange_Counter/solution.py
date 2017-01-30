#!/bin/python3

import sys

t = int(input().strip())
num_min = 0
num_max = 3
while True:
	l= num_max-num_min
	if 	num_min+1<=t<=num_max:
		diff = abs(num_min+1-t)
		print(l-diff)
		break
	num_min = num_max
	num_max = num_min+2*l
