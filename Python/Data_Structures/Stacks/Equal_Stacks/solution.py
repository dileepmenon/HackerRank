#!bin/python3


def get_max_height(h1, h2, h3):
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)
    s = min(s1, s2, s3)
    while not all([s1 == s, s2 == s, s3 == s]):
        if s1 > s:
            s1 -= h1.pop()
        if s2 > s:
            s2 -= h2.pop()
        if s3 > s:
            s3 -= h3.pop()
        s = min(s1, s2, s3)
    return s


n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
print(get_max_height(h1[::-1], h2[::-1], h3[::-1]))
