#!bin/python3
num_queries = int(input())
st = []
for i in range(num_queries):
    query = list(map(int, (input().split(' '))))
    inst = query[0]
    if len(query) > 1:
        num = query[1]
        st.append(num)
    else:
        if inst == 2:
            st = st[1:]
        else:
            print(st[0])
