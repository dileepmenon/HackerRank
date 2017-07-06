#!/bin/python3
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    a_srt = sorted(a)
    len_a = len(a_srt)
    coun = 0
    if len_a > 1:
        j = 1
    else:
        j = 0
    for i, a_i in enumerate(a_srt[:-1]):
        while j != len_a  and abs(a_i - a_srt[j]) <= k:
            if abs(a_i - a_srt[j]) == k:
                coun += 1
                j = j + 1
                break
            j += 1
    return coun
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
