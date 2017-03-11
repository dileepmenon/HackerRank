#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E = 100
for i in range(0, n, k):
    if i+k <= n-1:
        if  c[i+k] == 1:
            E -= 3
        else:
            E -= 1
    else:
        if c[0] == 1:
            E -= 3
        else:
            E -= 1
print(E)
