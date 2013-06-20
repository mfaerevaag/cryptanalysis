

A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

B=[13,14,3,4,5,6,15,10,11,16,1,2,7,8,9,12]

curPos=0
x=0
while x<len(A):
	A[curPos]=B[A[curPos]]
	curPos=B[A[curPos]]
	x=x+1
for x in xrange(0,len(A)):
		print A[x]+"->"	