#!/bin/python3

import sys

n = int(input().strip())
a = sorted([int(a_temp) for a_temp in input().strip().split(' ')])
coun = []
if [a[0]]*n == a:
    print(n)
else:
    for i in range(n-1):
        if a[i+1]-a[i] <=1:
            valid_element = [a[i], a[i+1]]
            t = i+2
            if t <= n-1:
                for i in range(t, n):
                    if all(abs(x-a[i]) <= 1 for x in valid_element):
                        valid_element.append(a[i])
                    else :
                        coun.append(len(valid_element))
                        i = t
    print(max(coun))
