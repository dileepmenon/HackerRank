#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
	grade = int(input().strip())
	if grade >= 38:
		next_mult_5 = int(grade/5)*5+5
		modi_grade =  next_mult_5 if next_mult_5-grade < 3 else grade
	else:
		modi_grade = grade
	print(modi_grade)

