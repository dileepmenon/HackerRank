#!/bin/python3
import math


def advert(count, num_advert, c, s):
    if count == c:
        return s
    else:
        num_like_advert = int(math.floor(num_advert/2))
        num_advert = num_like_advert*3
        c += 1
        s += num_like_advert
        return advert(count, num_advert, c, s)


count = int(input())
print(advert(count, 5, 0 ,0))
