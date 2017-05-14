#!/bin/python3

import sys


S = input().strip()
S_act = 'SOS'*int(len(S)/3)
coun = [True if i == j else False for i,j in zip(S, S_act)].count(False)
print(coun)
