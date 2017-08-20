#!bin/python3


def PowerSum(arr, n, x):
    if len(arr) == 1:
        return arr
    p = PowerSum(arr[:-1], n, x)
    a = arr[-1]**n
    q = p + [(arr[-1])**n] + [i+a for i in p if i+a <= x]
    return q


x = int(input())
n = int(input())
arr = [i for i in range(1, int(x**(1.0/n))+1)]
m = PowerSum(arr, n, x)
print([i == x for i in m].count(True))
