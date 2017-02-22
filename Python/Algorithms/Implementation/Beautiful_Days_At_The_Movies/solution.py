#!bin/python3

i,j,k = map(int,input().split(' '))
s = 0
for m in range(i,j+1):
    l = abs((m - int(str(m)[::-1]))/k)
    if (l).is_integer():
        s += 1
    else:
        pass
print(s)
