import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
index = len(a)-k
if index <0:
    num = len(a)
    while num<abs(index):
        num+=len(a)
    index = num+index
rot_a = a[index:]+a[:index]
for a0 in range(q):
    m = int(input().strip())
    print(rot_a[m])
