from itertools import izip, cycle
import time
time1 = time.clock()
cntr = 0;
myKey="AAAAAAAAAAAADDAz"
plaintext="Secretfoemotherd"
def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
encrypted = xor(plaintext, key=myKey)
lostKey=[65]*16
while True:
	original = xor(encrypted, key=''.join(chr(i) for i in lostKey))
	if original == plaintext:
		print "Wohoo we found the key again"
		print "Plaintext is: "+plaintext+" the bruteforce text is: "+original
		print "I ran: %d Times"%cntr
		runspeed = time.clock()-time1
		print "Time in seconds: %f"%runspeed
		break
 	index = 15;  	  
	lostKey[index]=lostKey[index]+1
	while index >= 0 and lostKey[index] >= 123:
		    lostKey[index] = 65
		    index=index-1
		    if index < 0: 
		      break
		    lostKey[index]=lostKey[index]+1
	cntr = cntr +1