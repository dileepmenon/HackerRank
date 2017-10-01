#!/bin/python3

import sys

def solve(opr):
    op = opr[1]
    a, b = list(map(int, opr.split(op)))
    if op == '+':
        return a + b
    else:
        return a - b

if __name__ == "__main__":
    opr = input().strip()
    result = solve(opr)
    print(result)
