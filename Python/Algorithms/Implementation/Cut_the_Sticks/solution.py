#!/bin/python3
import sys
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
temp=arr[:]
while(len(arr)!=0):
 count=0
 print(len(temp))
 for i in range(len(temp)):
   if temp[i]==min(arr):
       count+=1
   temp[i]-=min(arr)
 for i in range(count):
    temp.remove(0)
 arr=temp[:]
