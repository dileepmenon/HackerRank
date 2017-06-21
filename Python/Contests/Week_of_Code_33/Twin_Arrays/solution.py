#!/bin/python3

import sys

def twinArrays(arr_A, arr_B):
    while True and arr_A and arr_B:
        min_A = min(arr_A); idx_A = arr_A.index(min_A)
        min_B = min(arr_B); idx_B = arr_B.index(min_B)
        if idx_A != idx_B:
            return(min_A+min_B)
        else:
            arr_A[idx_A] = 1000000
            min_A1 = min(arr_A)
            arr_B[idx_B] = 1000000
            min_B1 = min(arr_B)
            if min_A1 < min_B1:
                return(min_A1+min_B)
            else:
                return(min_A+min_B1)
    else:
        return(min_A+min_B)

n = int(input().strip())
arr_A = list(map(int, input().strip().split(' ')))
arr_B = list(map(int, input().strip().split(' ')))
result = twinArrays(arr_A, arr_B)
print(result)
