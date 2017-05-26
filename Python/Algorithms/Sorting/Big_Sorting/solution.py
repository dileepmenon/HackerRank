#!/bin/python3

import sys


n = int(input().strip())
unsorted_i = 0
unsorted = []
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
sorted_arr = sorted(unsorted, key = int)
for i in sorted_arr:
    print(i)

