#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
l = [int(a),int(b),int(c),int(d),int(e)]
l.sort()
min_l = sum(l[:-1])
max_l = sum(l[:0:-1])
print('%d %d'%(min_l,max_l))
