#!/bin/python3

import sys


n = int(input().strip())
p = int(input().strip())

if p%2 == 0:
	beg = 0
	end = n if n%2 == 0 else n-1
else:
	beg  = 1
	end  = n+1 if n%2 == 0 else n

#number of pages to turn from start
num_page_start = int((p-beg)/2)
#number of pages to turn from end
num_page_end = int((end-p)/2)

min_num_page = min(num_page_start,num_page_end)
print(min_num_page)
