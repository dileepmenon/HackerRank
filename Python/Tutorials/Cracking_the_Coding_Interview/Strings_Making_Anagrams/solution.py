#!bin/python3


def number_needed(a, b):
    uniq_a = set(a)
    uniq_b = set(b)
    al_coun_a = {}
    al_coun_b = {}
    for i in uniq_a:
        al_coun_a[i] = a.count(i)
    for i in uniq_b:
        al_coun_b[i] = b.count(i)
    num_del = 0
    for i in al_coun_a.keys():
        try:
            num_del += abs(al_coun_b[i] - al_coun_a[i])
        except:
            num_del += al_coun_a[i]
    for i in al_coun_b.keys():
        try:
            al_coun_a[i]
        except:
            num_del += al_coun_b[i]
    return num_del


a = input().strip()
b = input().strip()

print(number_needed(a, b))
