def ind_search(p, c_mod):
    l = [i[0] for i in c_mod]
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (hi+lo)//2
        if p < l[mid]:
            hi = mid-1
        elif p > l[mid]:
            lo = mid+1
        else:
            a = True
            break
    else:
        a = False
    return a, c_mod[mid][1]


t = int(input())
for i in range(t):
    m = int(input())
    n = int(input())
    c = list(map(int, input().split(' ')))
    c_mod = [(c_i, i) for i, c_i in enumerate(c)]
    srt_c_mod = sorted(c_mod, key=lambda x: x[0])
    k = int(m/2.0)
    for i in range(1, k+1):
        p = i; q = m - i
        if p != q:
            bool_1, indx_p = ind_search(p, srt_c_mod)
            bool_2, indx_q = ind_search(q, srt_c_mod)
            if bool_1 and bool_2:
                break
        else:
            bool_1, indx_p = ind_search(p, srt_c_mod)
            srt_c_mod.remove((p, indx_p))
            bool_2, indx_q = ind_search(q, srt_c_mod)
            if bool_1 and bool_2:
                break
    indx_list = [indx_p+1, indx_q+1]
    print(min(indx_list), max(indx_list))
