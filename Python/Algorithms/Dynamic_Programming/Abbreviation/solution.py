#!/bin/python

# For larger test cases, due to many recursive calls will get RunTime Error.
# Better to write a Bottom Up approach (Iterative Solution) for below code



def abbreviation(a, b):
    if not a and not b:
        return True
    if not a and b:
        return False
    if a and not b:
        if a == a.lower():
            return True
        else:
            return False
    try:
        return d[(a, b)]
    except:
        if a[-1] == b[-1]:
            s = abbreviation(a[:-1], b[:-1])
        elif a[-1] == b[-1].lower():
            s = (abbreviation(a[:-1], b[:-1]) or abbreviation(a[:-1], b[:]))
        else:
            if a[-1] == a[-1].upper():
                return False
            else:
                s = abbreviation(a[:-1], b[:])
        d[(a, b)] = s
        return s


if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        a = raw_input().strip()
        b = raw_input().strip()
        d = {}
        result = abbreviation(a, b)
        if result:
            print ('YES')
        else:
            print ('NO')
