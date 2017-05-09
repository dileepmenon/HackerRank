#!/bin/python3
import string


s = input()
l = []
for i in s:
    if i.isalpha():
        l.append(i.lower())
m = ''.join(sorted(set(l)))
if string.ascii_lowercase == m:
    print ('pangram')
else:
    print ('not pangram')
