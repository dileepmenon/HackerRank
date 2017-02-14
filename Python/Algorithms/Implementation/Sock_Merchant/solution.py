#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

c.sort()
uniq_element = set(c)
s = 0
for i in uniq_element:
    coun = c.count(i)
    s += int(coun/2)
print(s)


