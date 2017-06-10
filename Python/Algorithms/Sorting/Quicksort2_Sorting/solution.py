#!bin/python3


def quicksort_recur(ar):
    if not ar:
        return []
    if len(ar) == 1:
        return ar
    else:
        part = {'l': [], 'e': [], 'r': []}
        p = ar[0]
        part['e'].append(p)
        for i in ar[1:]:
            if i < p:
                part['l'].append(i)
            elif i == p:
                part['e'].append(i)
            else:
                part['r'].append(i)
        s = (quicksort_recur(part['l']) + part['e']
             + quicksort_recur(part['r']))
        print (' '.join([str(i) for i in s]))
        return s


n = int(input())
ar = list(map(int, input().split(' ')))
l = quicksort_recur(ar)
