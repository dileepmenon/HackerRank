#!/bin/python3

import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
a_max = max(a)
b_min = min(b)
x=[]
num = a_max
while num<=b_min:
    x.append(num)
    num+=1
x_copy = x[:]
for i in x:
    arr1 = []
    arr2=  []
    for j in b:
        arr1.append(j%i)
    for k in a:
        arr2.append(i%k)
    if all(m == 0 for m in arr1) != True or all(n == 0 for n in arr2) != True:
        x_copy.remove(i)
x=x_copy
print(len(x))




