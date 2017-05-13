#!bin/python3

s = input().strip()
a = []
for i in set(s):
    a.append((i, s.count(i)))
bool_list = [True if i[1] >= 2 and i[1] % 2 == 0 else False for i in a]
n1 = len(bool_list)-1
n2 = 1
if bool_list.count(True) == len(bool_list):
    print('YES')
elif bool_list.count(True) == n1 and bool_list.count(False) == n2:
    print('YES')
else:
    print('NO')

