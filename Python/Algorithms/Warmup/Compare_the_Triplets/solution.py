import sys

a0,a1,a2 = input().strip().split(' ')
list_1 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
list_2 = [int(b0),int(b1),int(b2)]
def compare(s1,s2):
    if s1>s2:
        return (1,0)
    elif s1<s2:
        return (0,1)
    else:
        return (0,0)
ali_score=0
bob_score=0
for s1,s2 in zip(list_1,list_2):
  t= compare(s1,s2)
  ali_score+=t[0]
  bob_score+=t[1]
print('%d %d'%(ali_score,bob_score))
