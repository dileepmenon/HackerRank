#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
coun = 0
while i < n-1:
    try:
        len_jump = 2 if c[i+2] != 1 else 1
        i += len_jump
        coun += 1
    except:
        len_jump = 1
        i += len_jump
        coun += 1
print(coun)
