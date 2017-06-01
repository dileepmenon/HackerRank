#!bin/python3


n_str = int(input())
list_str = []
for i in range(n_str):
    list_str.append(input())
n_q = int(input())
list_q_coun = []
for i in range(n_q):
    q = input()
    list_q_coun.append([q == j for j in list_str].count(True))
for i in list_q_coun:
    print(i)
