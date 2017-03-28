#!/bin/python3

p = int(input())
q = int(input())

kaprekar_numbers = []

if p < 10:
    kaprekar_numbers.append(1)
    p = 9

for n in range(p, q+1):
    square = n**2
    d = len(str(n))
    d_square = len(str(n**2))

    i = d_square-d if d_square%2 ==0 else d_square-d+1

    first_split = int(square / (10**(i)))
    next_split  = square % (10**(d))

    if first_split+next_split == n and next_split != 0:
        kaprekar_numbers.append(n)

if len(kaprekar_numbers) != 0:
    for i in kaprekar_numbers:
        print(i, end = ' ')
else:
    print('INVALID RANGE')

