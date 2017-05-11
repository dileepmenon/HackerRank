#!bin/python3

n = int(input().strip())
for i in range(n):
    a = input()
    b = input()
    for i in a:
        if i in b:
            print('YES')
            break
    else:
        print('NO')

