#!bin/python3

n = int(input())
list_str = []
for i in range(n):
    s = input()
    list_str.append(s)
list_uniq_alpha = set(''.join(s))
coun = 0
for i in list_uniq_alpha:
    if all([i in j for j in list_str]):
        coun += 1
print(coun)

