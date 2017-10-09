#!/bin/python3

import sys


def candies(n, arr):
    opt_dist = [0]*len(arr)
    if len(arr) == 1:
        opt_dist[0] = 1
    if len(arr) > 1 and arr[0] <= arr[1]:
        opt_dist[0] = 1
    if len(arr) > 1 and arr[-1] <= arr[-2]:
        opt_dist[-1] = 1
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]: 
            opt_dist[i] = opt_dist[i-1] + 1
        else:
            opt_dist[i] = 1
    arr = arr[::-1]
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i] and opt_dist[n-1-i] <= opt_dist[n-i]:
            opt_dist[n-1-i] =  1 + opt_dist[n-i]
    return(sum(opt_dist))


if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = candies(n, arr)
    print(result)
