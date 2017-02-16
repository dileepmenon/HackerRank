#!/bin/python3

import sys
import string


h = list(map(int, input().strip().split(' ')))
word = input().strip()
s = []
for i in word:
    char_index = string.ascii_lowercase.index(i)
    s.append(h[char_index])
print(len(word)*1*max(s))
