#!/bin/python3
import sys


def maximumSum(a):
    m1, m2 = a[0], a[0]
    for i in range(len(a)-1):
        m1 = max(m1, a[i+1], a[i+1]+m2)
        m2 = max(a[i+1], a[i+1]+m2)
    return m1


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input())
        a = list(map(int, input().strip().split(' ')))
        non_cont_sum = 0
        cont_sum = maximumSum(a)
        for i in a:
            if i > 0:
                non_cont_sum += i
        if not non_cont_sum:
            non_cont_sum = max(a)
        print('%d %d'%(cont_sum, non_cont_sum))
