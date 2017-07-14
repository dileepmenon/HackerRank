#!/bin/python3

import sys


n = int(input().strip())


def min_recur(s, coun):
    if coun == n-1:
        return s
    s = 'min(int, ' + s + ')'
    coun += 1
    return min_recur(s, coun)


print(min_recur('min(int, int)', 1))
