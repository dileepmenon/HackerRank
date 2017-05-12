#!/bin/python3

import string

import itertools


s = input().strip()
num_t = int(input().strip())
dict_alpha = {}
for n, i in enumerate(string.ascii_lowercase):
    dict_alpha[i] = n+1
alpha_rep = [''.join(value) for key, value in itertools.groupby(s)]
alpha_wei = [(dict_alpha[j[0]], j.count(j[0])) for j in alpha_rep]
t = [k for k in alpha_wei if k[1] >= 2]
for i in range(num_t):
    n_i = int(input().strip())
    if any([n_i == j[0] for j in alpha_wei]):
        print('Yes')
    else:
        bool_list = [True if (2 <= int(n_i/j[0]) <= j[1]) and (n_i % j[0]) == 0
                    else False for j in t]
        if any(bool_list):
            print('Yes')
        else:
            print('No')
