#!/bin/python3
import sys


store = {}


def getWays(n, c):
    if n == 0:
        return 1
    if not c or n < 0:
        return 0
    if len(c) == 1 :
        if c[0] == n:
            return 1
    n_new = n - c[0]
    c_new = [i for i in c if i<= n_new]
    try:
        d = store[(c[0], len(c), n)]
        return d
    except:
        s = getWays(n_new, c_new[:]) + getWays(n, c[1:])
        store[(c[0], len(c), n)] = s
        return s


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
c = sorted(c)
ways = getWays(n, c)
print(ways)
