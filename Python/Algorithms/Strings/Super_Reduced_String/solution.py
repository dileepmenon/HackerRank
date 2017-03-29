#!/bin/python3
from itertools import groupby


s = input()
a = s
if len(a) < 2:
    print(a)
else:
    while any([a[i] == a[i+1] for i in range(len(a)-1)]):
        gr = ["".join(grp) for num, grp in groupby(a)]
        tmp = ''
        for i in gr:
            if len(i)%2 != 0:
                tmp += i[0]
        a = tmp

    if len(a) != 0:
        print (a)
    else:
        print ('Empty String')
