#!/bin/python3

import sys

import itertools

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
for topic_i in range(n):
   topic_t = list(map(int, list(input().strip())))
   topic.append(topic_t)
tup_list = list(itertools.combinations(range(1, n+1), 2))
tup_dict = {}
max_num_one = 0
coun_list = []
for i in tup_list:
    coun = [x or y for x,y in zip(topic[i[0]-1], topic[i[1]-1])].count(1)
    coun_list.append(coun)
    if max_num_one < coun:
        max_num_one = coun
num_teams_max_coun = len(list(filter(lambda x : x == max_num_one, coun_list)))
print(max_num_one)
print(num_teams_max_coun)
