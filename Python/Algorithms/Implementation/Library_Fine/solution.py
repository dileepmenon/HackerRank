#!/bin/python3

import sys


d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if y1 < y2:
    fine = 0
elif y1 > y2:
    fine = 10000
else:
    if m1 > m2:
        fine = 500*(m1-m2)
    elif m1 < m2:
        fine = 0
    else :
        if d1 < d2:
            fine = 0
        elif d1 > d2:
            fine = 15*(d1-d2)
        else:
            fine = 0
print(fine)
