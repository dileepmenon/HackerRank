#!bin/python3
# Without Recursion


n = 10
s = []
for i in range(10):
    s.append(list(input()))
a = input().strip()
d = {}
for j in range(n):
        i = 0
        c = 0
        while i < n:
            if s[i][j] == '-':
                hd = (i, j, 'v')
            while i < n and s[i][j] == '-':
                c += 1
                i += 1
            if c > 2:
                d[hd] = c
            c = 0
            i += 1
for i in range(n):
        j = 0
        c = 0
        while j < n:
            if s[i][j] == '-':
                hd = (i, j, 'h')
            while j < n and s[i][j] == '-':
                c += 1
                j += 1
            if c > 2:
                d[hd] = c
            c = 0
            j += 1
k = list(d.keys())
h = [(i, list(filter(lambda x: len(x) == i[1], a.split(';'))))
     for i in d.items() if k.count(i[1]) < 2]
b = s[:]
h = sorted(h, key=lambda x: len(x[1]))
for i in h:
    t = i[0][0]
    if len(i[1]) == 1:
        if t[2] == 'h':
            b[t[0]][t[1]:t[1]+i[0][1]] = i[1][0]
        if t[2] == 'v':
            for l, m in enumerate(range(t[0], t[0]+i[0][1])):
                b[m][t[1]] = i[1][0][l]
while True:
    for i in h:
        t = i[0][0]
        if len(i[1]) > 1:
            if t[2] == 'h':
                idx1 = t[1]
                alpha = list(filter(lambda x: x != '-',
                             b[t[0]][t[1]:t[1]+i[0][1]]))
                if alpha:
                    idx2 = b[t[0]].index(alpha[0])
                    for n in i[1]:
                        if n[idx2-idx1] == alpha[0]:
                            b[t[0]][t[1]:t[1]+i[0][1]] = n
            if t[2] == 'v':
                idx1 = t[0]
                alpha = ''
                for l, m in enumerate(range(t[0], t[0]+i[0][1])):
                    if b[m][t[1]] != '-':
                        alpha = b[m][t[1]]
                        break
                if alpha:
                    idx2 = m
                    for n in i[1]:
                        if n[idx2-idx1] == alpha:
                            for l, m in enumerate(range(t[0], t[0]+i[0][1])):
                                b[m][t[1]] = n[l]
    if all([y != '-' for x in b for y in x]):
        break
for i in b:
    print(''.join(i))
