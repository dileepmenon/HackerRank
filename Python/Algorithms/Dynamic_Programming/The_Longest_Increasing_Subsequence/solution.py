#!bin/python3


def get_length_LIS(arr, n):
    max_arr_idx = 0
    if not arr:
        return 0
    LIS = [0]*n
    LIS[0] = [arr[0]]
    for i in range(1, n):
        max_l_idx = 0
        max_l = 0
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i] and len(LIS[j]) > max_l:
            	max_l = len(LIS[j])
            	max_l_idx = j
        if not max_l:
            LIS[i] = [arr[i]]
        else:
            LIS[i] = LIS[max_l_idx] + [arr[i]]
        if len(LIS[i]) > len(LIS[max_arr_idx]):
            max_arr_idx = i
    return len(LIS[max_arr_idx])


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(get_length_LIS(arr, n))
