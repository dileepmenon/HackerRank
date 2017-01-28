#!/bin/python3
import sys
import math

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v2>=v1:
    print ('NO')
else:
    t_max = int(math.ceil((x2-x1)/(v1-v2)))
    for i in range(1,t_max+1):
        if x1+v1*i == x2+v2*i:
            print ('YES')
            break
    else:
        print ('NO')
