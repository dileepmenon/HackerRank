#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
num_apple = [1 for i in apple if i+a>=s and i+a<=t].count(1)
num_orange = [1 for i in orange if i+b>=s and i+b<=t].count(1)
print (num_apple)
print(num_orange)
