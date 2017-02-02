#!/bin/python3
import sys
n = int(input().strip())
def factorial(N):
    if N==1:
        return 1
    else:
        return N*factorial(N-1)
print(factorial(n))
