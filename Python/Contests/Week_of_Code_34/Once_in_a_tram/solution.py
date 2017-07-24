#!/bin/python3

import sys


def onceInATram(x):
    x += 1
    quo = x // 1000
    rem = x % 1000
    while (quo//100)+((quo//10)%10)+(quo%10) != (rem//100)+((rem//10)%10)+(rem%10):
        x += 1
        quo = x // 1000
        rem = x % 1000
    return x


if __name__ == "__main__":
    x = int(input().strip())
    result = onceInATram(x)
    print(result)
