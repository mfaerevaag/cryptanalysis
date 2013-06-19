

A=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

B=[13,14,3,4,5,6,0,15,10,11,16,1,18,2,7,8,17,19,9,12]

C=[0]*20

x=1
curPos =0
temp = 0
modVal = 0
a=input ('Enter reduction size: ')
while x<len(A):
	temp=A[curPos]%a
	if B[temp] in C:
		temp=temp+1
		print ""
		if temp > len(A):
			temp = 0
	if A in C:
		break
	C[x]=B[temp]
	print "%d ->"%C[x],
	curPos=B[temp]
	x=x+1