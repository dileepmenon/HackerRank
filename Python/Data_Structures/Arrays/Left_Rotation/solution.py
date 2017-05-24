#!bin/python3

n, d = map(int, input().strip().split(' '))
s = map(int, input().strip().split(' '))
j = d % n
rot = s[j:] + s[:j]
for i in rot:
    print (i, end=" ")
