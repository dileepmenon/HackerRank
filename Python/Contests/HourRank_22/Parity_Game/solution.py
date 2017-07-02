#!/bin/python3

import sys


def smallestSizeSubsequence(n, A):
    # Return the size of the smallest subsequence to remove
    odd = 0
    if n:
        if n == 1:
            return(-1)
        for i in A:
            if i % 2 != 0:
                odd += 1
        if odd == 2 and n == 2:
            return (-1)
        if odd % 2 == 0:
            return (0)
        else:
            return (1)
    else:
        return (-1)


n = int(input().strip())
A = list(map(int, input().strip().split(' ')))
result = smallestSizeSubsequence(n, A)
print(result)
