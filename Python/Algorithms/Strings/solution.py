#!bin/python3

n = int(input().strip())
for i in range(n):
    s = input()
    if len(s) % 2 != 0:
        print(-1)
    else:
        t = int(len(s)/2)
        s1 = sorted(s[:t])
        s2 = sorted(s[t:])
        c = 0
        for i in set(s2):
            a = s2.count(i)
            b = s1.count(i)
            if a > b:
                c += a - b
        print(c)
