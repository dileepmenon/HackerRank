#!bin/python3
n = int(input())
k = int(input())
s = []
for i in range(n):
    s.append(int(input().strip()))
s = sorted(s)
mini = 1e10
for n, i in enumerate(s[:-(k-1)]):
    m = s[n+k-1] - s[n]
    if m < mini:
        mini = m
print(mini)
