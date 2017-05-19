#!/bin/python3

import sys

def getMaxMonsters(n, hit, t, h):
    i = 0
    t_i = 0
    coun = 0
    s = sorted(h)
    while t_i < t and i < n:
        while s[i] > 0 and t_i < t:
            s[i] -= hit
            t_i += 1
        if s[i] <= 0:
            coun += 1
        i += 1
    return coun

n, hit, t = input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = list(map(int, input().strip().split(' ')))
result = getMaxMonsters(n, hit, t, h)
print(result)


