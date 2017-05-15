#!bin/python3

a = str(input().strip())
b = str(input().strip())
if len(a) >= len(b):
    big = a
    small = b
else:
    big = b
    small = a
bool_list = []
for i in small:
    if i in big:
        bool_list.append(True)
        big = big.replace(i, '0', 1)
    else:
        bool_list.append(False)
coun = bool_list.count(True)
print(len(big)+len(small)-2*coun)
