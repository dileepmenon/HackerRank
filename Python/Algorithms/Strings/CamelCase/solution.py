#!/bin/python3

import sys


s = input().strip()
coun = 1
for i in s:
	if i.isupper():
		coun += 1
print (coun)
