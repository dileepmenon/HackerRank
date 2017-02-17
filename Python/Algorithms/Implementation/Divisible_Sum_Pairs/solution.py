#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
print(len([(i,j) for i in range(len(a)) for j in range(len(a)) if i<j and (a[i]+a[j])%k == 0]))
