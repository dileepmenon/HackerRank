#!bin/python3

n = int(input())
m = list(map(int,(input().split(' '))))

for x in range(1,n+1):
    try:
        a = m.index(x)+1
        try:
            print(m.index(a)+1)
        except:
            pass
    except:
        pass
