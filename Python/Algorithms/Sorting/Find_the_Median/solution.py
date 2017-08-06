#!bin/python3


n = int(input())
arr = list(map(int, input().split()))
s = [0] * (max(arr)+1)
for i in arr:
    if s[i] == 0:
        s[i] = [i, 1]
    else:
        s[i][1] += 1
srt_arr = []
for i in s[1:]:
    if i != 0:
        srt_arr += [i[0]] * i[1]
num_zero = arr.count(0)
if num_zero:
    srt_arr = ([0]*num_zero) + srt_arr
print(srt_arr[(len(srt_arr)-1)//2])
