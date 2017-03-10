#!bin/python3

n, k = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))
coun = 0
remainder_list = [x%k for x in l]
#Removing all elements exactly divisble by k
remainder_list1 = list(filter(lambda a : a != 0, remainder_list))
if len(remainder_list)-len(remainder_list1) > 0:
    coun += 1
if k%2 == 0:
    x = k/2
    remainder_list2 = list(filter(lambda a : a != x, remainder_list1))
    if len(remainder_list1)-len(remainder_list2) > 0:
        coun += 1
        remainder_list1 = remainder_list2[:]
divisible_pairs= []
x1 = 1
x2 = k-1
while x1<x2:
    divisible_pairs.append((x1, x2))
    x1 += 1
    x2 -= 1
for i in divisible_pairs:
    y = remainder_list1.count(i[0])
    z = remainder_list1.count(i[1])
    if y == z:
        coun += y
    else:
        coun += max(y, z)
    remainder_list1 = list(filter(lambda a : a != i[0] and a!= i[1], remainder_list1))
coun += len(remainder_list1)
print (coun)
