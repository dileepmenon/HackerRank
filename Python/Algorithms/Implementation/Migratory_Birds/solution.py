#!/bin/python3

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
num_type_arr = []
for i in range(1, 6):
	num_type_arr.append((i, types.count(i)))
num_type_max = max(x[1] for x in num_type_arr)
#Contain list of tuples in which second element has max occurences
max_num_type_arr = list(filter(lambda x : x[1] == num_type_max, num_type_arr))
print(max_num_type_arr[0][0])
