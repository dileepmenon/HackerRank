n = int(input())
st = [0]
for i in range(n):
    q = [int(i) for i in input().split()]
    if len(q) > 1:
        st.append(max(q[1], st[-1]))
    elif q[0] == 2:
        st.pop()
    else:
        print(st[-1])
