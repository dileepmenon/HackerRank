#!/bin/python3

import sys


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
highest_score = [score[0]]
lowest_score = [score[0]]
for i, j in enumerate(score[1:]):
	prev_high = highest_score[i]
	prev_low = lowest_score[i]
	if j >= max(prev_high, prev_low):
		highest_score.append(j)
		lowest_score.append(prev_low)
	elif j<= min(prev_high, prev_low):
		highest_score.append(prev_high)
		lowest_score.append(j)
	else:
		highest_score.append(prev_high)
		lowest_score.append(prev_low)
high_num = len([a for a in list(set(highest_score)) if a != score[0]])
low_num = len([b for b in list(set(lowest_score)) if b != score[0]])
print('%d %d'%(high_num, low_num))


