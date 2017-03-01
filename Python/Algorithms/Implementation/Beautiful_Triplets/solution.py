#!bin/python3

def func(s,arr):
    n, d = list(map(int,s.split(' ')))
    arr = list(map(int,arr.split(' ')))
    triplets = []
    tup = ()
    del_elements = []
    while len(arr) != 0:
        i = 0
        tup = (arr[i],)
        del_elements.append(arr[i])
        t = arr[i]+d
        while t in arr and arr.index(t)<len(arr):
            tup+=(t,)
            del_elements.append(t)
            i = arr.index(t)
            if len(tup) == 3:
                triplets.append(tup)
                t = arr[i] - d
                i = arr.index(t)
                tup= (t,)
            t+=d
        else:
            for j in set(del_elements):
                arr.remove(j)
            del_elements = []
    print (len(set(triplets)))


s = input()
arr = input()
func(s,arr)
