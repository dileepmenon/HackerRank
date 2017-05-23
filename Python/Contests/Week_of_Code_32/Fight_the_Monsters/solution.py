#!/bin/python3

import sys
import math


def getMaxMonsters(n, hit, t, h):
    i = 0
    t_i = 0
    coun = 0
    s = sorted(h)
    while t_i < t and i < n:
        a = int(math.ceil(s[i]/hit))
        b = t - t_i
        if t_i+a > t:
            s[i] -= hit*b
            t_i += b
        else:
            s[i] -= hit*a
            t_i += a
        if s[i] <= 0:
            coun += 1
        i += 1
    return coun


n, hit, t = input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = list(map(int, input().strip().split(' ')))
result = getMaxMonsters(n, hit, t, h)
print(result)
