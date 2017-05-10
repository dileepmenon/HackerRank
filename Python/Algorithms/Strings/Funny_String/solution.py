#!/bin/python3


num_tc = int(input().strip())
for i in range(num_tc):
    s = input()
    ascii_s = [ord(c) for c in s]
    rev_s = s[-1::-1]
    ascii_rev_s = [ord(c) for c in rev_s]
    bool_list = []
    for n, (i, j) in enumerate(zip(ascii_s[:-1], ascii_rev_s[:-1])):
        if abs(ascii_s[n+1] - i) == abs(ascii_rev_s[n+1] - j):
           bool_list.append(True)
        else:
           bool_list.append(False)
    if all(bool_list):
        print ('Funny')
    else:
        print ('Not Funny')
