#!/bin/python3
import sys
import math
import string

s = input().strip()
row = int(math.floor(math.sqrt(len(s))))
column = int(math.ceil(math.sqrt(len(s))))
if row*column < len(s):
    row+=1
temp =  ''
for i in range(row):
    x = i*column
    y = s[x:x+column]
    if len(y)!=column:
        y+='\n'*(column-len(y))
    temp+= y+' '
encrypt_str = ''
for j in range(column):
    str_temp = ''
    for  l  in temp[:-1].split(' '):
        str_temp+= l[j]
    encrypt_str+= str_temp.strip()+' '
print (encrypt_str.strip(' '))
