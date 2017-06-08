#!bin/python3

t = int(input())
for i in range(t):
    n = int(input())
    alpha_list = []
    for j in range(n):
        alpha_list.append(input())
    l = [sorted(i) for i in alpha_list]
    m = []
    for k in range(n):
        s = ''
        for j in l:
            s += j[k]
        m.append(s)
    if all([sorted(k) == list(k) for k in m]):
        print('YES')
    else:
        print('NO')
