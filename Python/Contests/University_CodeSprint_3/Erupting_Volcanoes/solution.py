#!/bin/python3

import sys


def update_grid(grid, x, y, w):
    d1 = [x-1, y-1]
    d2 = [x+1, y+1]
    s = 2
    t = w-1
    grid[x][y] +=  w
    while t >= 0 and (d1[0] >= 0 or d1[1] >= 0):
        try:
            if d1[0] >= 0 and d1[1] >= 0:
                grid[d1[0]][d1[1]] +=  t
        except:
            pass
        i = d1[0]
        j = d1[1] + 1
        while j <= d1[1] + s and j <= n - 1:
            try:
                if j >= 0 and d1[0] >= 0:
                    grid[d1[0]][j] +=  t
            except:
                pass
            j += 1
        i = d1[0] + 1
        j = d1[1] 
        while i <= d1[0] + s and i <= n - 1:
            try:
                if i >= 0 and d1[1] >= 0:
                    grid[i][d1[1]] +=  t
            except:
                pass
            i += 1
        d1[0] -= 1
        d1[1] -= 1
        s += 2
        t -= 1
    s = 2
    t = w-1
    while t>= 0 and (d2[0] <= n-1 or d2[1] <= n-1):
        try:
            if d2[0] <= n-1 and d2[1] <= n-1:
                grid[d2[0]][d2[1]] +=  t
        except:
            pass
        i = d2[0]
        j = d2[1] - 1
        while j >= d2[1] - (s-1) and j >= 0:
            try:
                if j <= n-1 and d2[0] <= n-1:
                    grid[d2[0]][j] +=  t
            except:
                pass
            j -= 1
        i = d2[0] - 1
        j = d2[1]
        while i >= d2[0] - (s-1) and i >= 0:
            try:
                if i <= n-1 and d2[1] <= n-1:
                    grid[i][d2[1]] +=  t
            except:
                pass
            i -= 1
        d2[0] += 1
        d2[1] += 1
        s += 2
        t -= 1
    return grid[:]


if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for i in range(n):
        grid.append([0]*n)
    for a0 in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        new_grid = update_grid(grid[:], x, y, w)
        grid = new_grid[:]
    max_ele = 0
    for i in grid:
        for j in i:
            if j > max_ele:
                max_ele = j
    print(max_ele)
