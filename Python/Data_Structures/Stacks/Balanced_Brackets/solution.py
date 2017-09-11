#!/bin/python3
import sys


def isBalanced(s):
    st = []
    l = ['{}', '[]', '()']
    for i in s:
        st.append(i)
        if len(st) > 1:
            if st[-2]+st[-1] in l:
                st.pop()
                st.pop()
    if not st:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
