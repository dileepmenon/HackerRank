#!/bin/python3

import sys


def howManyGames(p, d, m, s):
    if s < p:
        return 0
    x = int((p-m)/float(d)) + 1
    if p - (x*d) < m:
        x -= 1
    if (p*(x+1)) - (0.5*x*(x+1)*d) > s:
        a = p
        i = 1
        while s - a >= 0:
            a += p - (i*d)
            i += 1
        return i-1
    else:
        l = int((s-((x+1)*p-(0.5*x*(x+1))*d))/float(m)) + 1
        return (x+l)


if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
