#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())
s_len = len(s)
if s_len == 0:
    print (0)
else:
    num_a_initial =  int(n/s_len)*s.count('a')
    if len(s)!=1:
        num_a_final = s[:(n%s_len)].count('a')
    else:
        num_a_final = 0
    num_a = num_a_initial+num_a_final
    print(num_a)
























