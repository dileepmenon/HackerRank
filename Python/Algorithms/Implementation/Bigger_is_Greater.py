#!bin/python3
from itertools import permutations

t = int(input())
for i in range(t):
    s = input()
    if s[0]*len(s)  == s:
        print ('no answer')
    else:
        p = list(s)
        ind1 = -1
        for i in range(1, len(p)):
            if p[i] > p[i-1]:
                ind1 = i
        if ind1 != -1:
            for j in range(ind1, len(p)):
                if p[j] > p[ind1-1]:
                    ind2 = j
            p[ind1-1], p[ind2] =  p[ind2], p[ind1-1]
            p[ind1:] = p[ind1:][-1::-1]
            print (''.join(p))
        else:
            print ('no answer')
