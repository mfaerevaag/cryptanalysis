import math
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sum =0

def find_perc(s):

	perc=[0.082,0.015,0.028,0.043,0.127,0.022,0.02,0.061,0.07,0.002,0.008,0.04,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,0.028,0.01,0.023,0.001,0.02,0.001]

	letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	pos = 0
	temp = s.upper()
	if temp in letter:
		for x in xrange(1,len(letter)):
			if temp==letter[x]:
				pos = x
	return perc[pos]


def calc_ent(s):
	P=find_perc(s)
	sum=0
	temp = math.log(1/P)/math.log(2)
	#temp = (-P*(math.log(P)/math.log(2)))-((1-P)*(math.log(1-P)/math.log(2)))
	sum=P*temp
	print sum
	return sum


for x in xrange(0,25):
	sum=sum+calc_ent(letters[x])
	print x

print "The min bit is : %f"%sum