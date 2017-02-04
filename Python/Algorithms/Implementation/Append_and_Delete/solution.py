#!/bin/python3

import sys

def substr(s1,s2):
	s=''
	if len(s1)>len(s2):
	    b=len(s2)
	else:
	    b=len(s1)
	for i in range(b):
	    if s1[i] == s2[i]:
	        s+=s1[i]
	        if i+1!=b and s1[i+1]!=s2[i+1]:
	            break
	return(s)

s = input().strip()
t = input().strip()
k = int(input().strip())
if s == t:
	a = len(s)
	if k==2*a:
		print('Yes')
	elif k%2==0:
		print('Yes')
	else:
		if k>2*a:
			print('Yes')
		else:
			print('No')
else:
    n = substr(s,t)
    if n!='':
        x = s.split(substr(s,t))[1]
        y = t.split(substr(s,t))[1]
        num1 = len(x)
        num2 = len(y)
    else:
        num1 = len(s)
        num2 = len(t)
    if n== '':
        if num1==num2:
            if k>=2*num1:
                print('Yes')
            else:
                print('No')
        else:
            if k>=num1+num2:
                print('Yes')
            else:
                print('No')
    else:
        if s==len(s)*s[0] and t==len(t)*t[0]:
            l=len(substr(s,t))
            num=abs(k-l)
            if len(s)>len(t):
                p=len(s)
            else:
                p=len(t)
            if k>=abs(l-p):
                    print('Yes')
            else:
                    print('No')
        elif x=='' or y=='':
            if num2==k:
                print ('Yes')
            else:
                print ('No')
        elif k-num1>0 and k-num1 == num2:
            print('Yes')
        else:
            print('No')




