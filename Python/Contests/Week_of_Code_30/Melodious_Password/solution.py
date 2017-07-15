#!bin/python3

import sys
import string


n = int(input().strip())
char = string.ascii_lowercase
vow = 'aeiou'
const = ''.join(filter(lambda x: x not in vow+'y', char))
vow_con = []
con_vow = []
for i in vow:
    for j in const:
        vow_con.append(i+j)
for i in const:
    for j in vow:
        con_vow.append(i+j)


def vowel_const(s1, s2, coun):
    if coun == 1:
        return s1, s2
    a, b = [], []
    for s_i in (s1):
        for s_j in vow_con:
            a.append(s_i + s_j)
    for s_i in (s2):
        for s_j in con_vow:
            b.append(s_i + s_j)
    s1, s2 = a[:], b[:]
    coun -= 1
    return vowel_const(s1, s2, coun)


if n % 2 == 0:
    all_comb = vowel_const(vow_con, con_vow, n//2)
    for i in all_comb[0]:
        print(i)
    for i in all_comb[1]:
        print(i)
else:
    if n == 1:
        for i in vow+const:
            print(i)
    else:
        all_comb = vowel_const(vow_con, con_vow, (n-1)//2)
        print(all_comb[0])
        for i in all_comb[0]:
            for j in vow:
                print(i+j)
        for i in all_comb[1]:
            for j in const:
                print(i+j)



