#!bin/python3

n = int(input())
l1 = list(map(int, input().split(' ')))
m = int(input())
l2 = list(map(int, input().split(' ')))
uniq_ele_l1 = set(l1)
a = []
for i in uniq_ele_l1:
    coun1 = l1.count(i)
    coun2 = l2.count(i)
    if coun1 != coun2:
        a.append(i)
for j in a:
    print(j, end=' ')
