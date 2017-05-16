#!bin/python3

import itertools

n = int(input())
for i in range(n):
    s = input().strip()
    coun = 0
    for i in itertools.groupby(s):
        coun += len(list(i[1]))-1
    print(coun)

