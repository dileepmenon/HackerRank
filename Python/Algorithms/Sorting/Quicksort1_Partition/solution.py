#!bin/python3


n = int(input())
ar = list(map(int, input().split(' ')))
p = ar[0]
part = {'l': [], 'e': [], 'r': []}
part['e'].append(p)
for i in ar[1:]:
    if i < p:
        part['l'].append(i)
    elif i == p:
        part['e'].append(i)
    else:
        part['r'].append(i)
for i in ['l', 'e', 'r']:
    for j in part[i]:
        print(j, end=' ')
