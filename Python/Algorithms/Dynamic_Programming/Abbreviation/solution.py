#!/bin/python


def abbreviation(a, b):
    return get_abbrev(a, b, 0, 0)


def get_abbrev(a, b, i1, i2):
    while i1 < len(a) and i2 < len(b):
        try:
            return d[(a[i1:], b[i2:])]
        except:
            if a[i1] == b[i2]:
                i1 += 1
                i2 += 1
            elif a[i1] == b[i2].lower():
                s = get_abbrev(a, b, i1+1, i2+1) or get_abbrev(a, b, i1+1, i2)
                d[(a[i1:], b[i2:])] = s
                return s
            else:
                if a[i1] == a[i1].upper():
                    return False
                else:
                    i1 += 1
    if i1 >= len(a) and i2 >= len(b):
        return True
    if i1 >= len(a) and i2 < len(b):
        return False
    if i1 < len(a) and i2 >= len(b):
        if a[i1:] == a[i1:].lower():
            return True
        else:
            return False


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
