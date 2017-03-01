#!bin/python3

def func(s,arr):
    n, d = list(map(int,s.split(' ')))
    arr = list(map(int,arr.split(' ')))
    triplets = []
    tup = ()
    for i in range(n):
        tup = (arr[i],)
        t = arr[i]+d
        while t in arr and arr.index(t)<n:
            tup+=(t,)
            i = arr.index(t)
            if len(tup) == 3:
                triplets.append(tup)
                t = arr[i] - d
                i = arr.index(t)
                tup= (t,)
            t+=d
    print (len(set(triplets)))


s = input()
arr = input()
func(s,arr)
