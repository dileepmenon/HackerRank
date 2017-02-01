#!/bin/python3
import sys
import string
num_test = int(input())
for i in range(num_test):
    n = input()
    N,M,S = map(int,n.split(' '))
    Id_poison = (S+M-1)%N
    if Id_poison == 0:
        print(N)
    else:
        print(Id_poison)


