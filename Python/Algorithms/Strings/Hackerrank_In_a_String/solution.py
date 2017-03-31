#!/bin/python3

import sys


q = int(input().strip())
check_str = 'hackerrank'
for a0 in range(q):
    s = input().strip()
    indices = []
    try:
        s1 = s
        indices.append(s.index(check_str[0]))
        s1 = s1[indices[-1]+1:]
        for i in check_str[1:-1]:
            index = s1.index(i)
            indices.append(index+indices[-1]+1)
            s1 = s1[index+1:]
        indices.append(s1.index(check_str[-1])+indices[-1]+1)
        if all([indices[i]<indices[i+1] for i in range(len(indices)-1)]):
            print('YES')
        else:
            print('NO')
    except:
        print('NO')
