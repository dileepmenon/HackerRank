#!/bin/python3
n = int(input())
b = input()
a = b.split(' ')
a = list(map(int,a))
if a[0]*len(a) == a:
    print(0)
else:
    arr = [(i,a.count(i)) for i in set(a)]
    sorted_by_second = sorted(arr, key=lambda tup:tup[1])
    x = sorted_by_second[-1]
    print(len(a)-x[1])
