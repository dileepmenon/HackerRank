t1, t2, n = list(map(int, input().split(' ')))
t = [0]*2
t[0] = t1
t[1] = t2
for i in range(2, n):
    t_old = t[1]
    t_next = t[0] + t[1]**2
    t[0] = t_old
    t[1] = t_next
print(t[1])
