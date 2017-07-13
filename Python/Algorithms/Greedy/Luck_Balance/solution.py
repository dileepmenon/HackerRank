#!bin/python3


num_con, k = list(map(int, input().split(' ')))
a = []
for i in range(num_con):
    s = list(map(int, input().split(' ')))
    a.append((s[0], s[1]))
imp = list(filter(lambda x: x[1] == 1, a))
len_imp = len(imp)
un_imp_luck = [x[0] for x in list(filter(lambda x: x[1] == 0, a))]
imp_srt = sorted(imp, key=lambda x: x[0])
m = len_imp - k
if m < 0:
    m = 0
imp_luck_less_than_k = [x[0] for x in imp_srt[m:]]
rem_imp_luck = [x[0] for x in imp_srt[:m]]
tot_luck = sum(imp_luck_less_than_k) + sum(un_imp_luck) - sum(rem_imp_luck)
print(tot_luck)
