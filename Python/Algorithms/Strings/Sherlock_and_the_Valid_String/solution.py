#!/bin/python3

import sys


def isValid(s):
    alpha_coun = []
    for i in set(s):
        alpha_coun.append(s.count(i))
    a = list(set(alpha_coun))
    if len(a) > 2:
        return 'NO'
    else:
        if len(a) == 2:
            a1_coun = alpha_coun.count(a[0])
            a2_coun = alpha_coun.count(a[1])
            if a1_coun == 1 or a2_coun == 1:
                if abs(a[1] - a[0]) == 1:
                    return 'YES'
                elif a[0] == 1 or a[1] == 1:
                    return 'YES'
                else:
                    return 'NO'
            else:
                return 'NO'
        else:
            return 'YES'


s = input().strip()
result = isValid(s)
print(result)
