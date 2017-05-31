#!bin/python3


n = int(input())
a = list(map(int, input().split(' ')))
for i in range(1, n):
    j = i
    temp = a[j]
    while j != 0 and a[j] < a[j-1]:
        a[j] = a[j-1]
        a[j-1] = temp
        j -= 1
    print(' '.join(map(str,a)))
