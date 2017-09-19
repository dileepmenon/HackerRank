#!bin/python3
m, n = list(map(int, input().strip().split(' ')))
arr_m = list(map(int, input().strip().split(' ')))
arr_n = list(map(int, input().strip().split(' ')))
tab = []
for i in range(n+1):
    tab.append([0]*(m+1))
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr_m[j-1] == arr_n[i-1]:
            tab[i][j] = tab[i-1][j-1] + 1
        else:
            tab[i][j] = max(tab[i-1][j], tab[i][j-1])
i = n
j = m
LCS = []
coun = 0
while i > 0 and j > 0:
    if arr_m[j-1] == arr_n[i-1]:
        LCS.append(arr_m[j-1])
        i = i - 1
        j = j - 1
    else:
        if tab[i-1][j] == tab[i][j-1]:
            i = i-1
        elif tab[i-1][j] > tab[i][j-1]:
            i = i-1
        else:
            j = j-1
for c in LCS[::-1]:
    print(c, end=' ')
