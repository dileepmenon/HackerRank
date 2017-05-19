def duplication(x):
    s = '0'
    while len(s) <= x:
        s_comp = ''.join(['1' if i == '0' else '0' for i in s])
        s = s + s_comp
    print s
    return s[x]

