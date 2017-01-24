import sys
h = int(raw_input().strip())
m = int(raw_input().strip())
d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
          19 : 'ninteen', 20 : 'twenty', 21 : 'twenty one', 22 : 'twenty two', \
          23 : 'twenty three', 24 : 'twenty four', 25 : 'twenty five', \
          26 : 'twenty six', 27 : 'twenty seven', 28 : 'twenty eight', \
          29 : 'twenty nine', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', \
          60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninty'}
if m == 0:
	print ("%s o' clock"%d[h])
elif m == 1:
	print ('%s minute past %s'%(d[m],d[h]))
elif m == 15:
    print ('quarter past %s'%d[h])
elif m>1 and m<30:
	print ('%s minutes past %s'%(d[m],d[h]))
elif m == 30:
	print ('half past %s'%d[h])
elif m == 45:
	print ('quarter to %s'%d[h+1])
elif m>30 and m<60:
	print ('%s minutes to %s'%(d[60-m],d[h+1]))
else:
	pass
