#!/bin/python3


def get_path(n, d, x, y):
    grid_00= []
    grid_01= []
    grid_10= []
    grid_11= []
    for i in range(n):
        grid_00.append([0]*n)
        grid_01.append([0]*n)
        grid_10.append([0]*n)
        grid_11.append([0]*n)
    for i in range(n):
        if i % 2 == 0:
            a = list(range(n*(i+1), n*(i+1) - n, -1))[::-1]
            b = list(range(n*(i+1), n*(i+1) - n, -1))
            grid_00[i] = a
            grid_01[i] = b
        else:
            a = list(range(n*(i+1), n*(i+1) - n, -1))[::-1]
            b = list(range(n*(i+1), n*(i+1) - n, -1))
            grid_00[i] = b
            grid_01[i] = a
    grid_10[0] = list(range(n, n+n))
    for i in range(1, n):
        grid_10[i] = [n-i] + list(range(grid_10[i-1][n-1] + 1, grid_10[i-1][n-1] + n))
    for i in range(1, n):
        if i % 2 != 0:
            grid_10[i][1:] = grid_10[i][1:][::-1]
    for i in range(n):
        grid_11[i] = grid_10[i][::-1]
    if (x, y) == (0,0):
        if d =='n':
            for i in grid_00:
                print(*i)
        elif d == 's':
            for i in grid_11[::-1]:
                print(*i[::-1])
        elif d == 'e':
             for i in zip(*grid_10):
                print(*i[::-1])
        else:
            for i in zip(*grid_00):
                print(*i)
    if (x, y) == (0, n-1):
        if d =='n':
            for i in grid_01:
                print(*i)
        elif d == 's':
            for i in grid_11[::-1]:
                print(*i)
        elif d == 'e':
             for i in zip(*grid_00):
                print(*i[::-1])
        else:
            for i in zip(*grid_10):
                print(*i)
    if (x, y) == (n-1,0):
        if d =='n':
            for i in grid_10:
                print(*i)
        elif d == 's':
            for i in grid_00[::-1]:
                print(*i)
        elif d == 'e':
             for i in zip(*grid_11):
                print(*i[::-1])
        else:
            for i in list(zip(*grid_00))[::-1]:
                print(*i)
    if (x, y) == (n-1,n-1):
        if d =='n':
            for i in grid_11:
                print(*i)
        elif d == 's':
            for i in grid_00[::-1]:
                print(*i[::-1])
        elif d == 'e':
             for i in zip(*grid_01):
                print(*i[::-1])
        else:
            for i in zip(*grid_11):
                print(*i)


if __name__ == "__main__":
    n = int(input().strip())
    d = input().strip()
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]
    get_path(n, d, x, y)
