#!/bin/python3


num_items, index = list(map(int,input().split(' ')))
cost_items_list = list(map(int,input().split()))
anna_charge = int(input())
total_cost = sum(cost_items_list)
anna_share = int((total_cost-cost_items_list[index])/2)
if  anna_share == anna_charge:
    print ('Bon Appetit')
else:
    print(abs(anna_charge-anna_share))
