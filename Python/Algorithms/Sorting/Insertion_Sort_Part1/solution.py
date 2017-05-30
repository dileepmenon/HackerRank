#!bin/python3


n = int(input())
a = list(map(int, input().split(' ')))
i = n-1
temp = a[i]
while i != 0 and a[i] < a[i-1]:
    a[i] = a[i-1]
    print(' '.join(map(str, a)))
    a[i-1] = temp
    i -= 1
else:
    a[i] = temp
    print(' '.join(map(str, a)))
