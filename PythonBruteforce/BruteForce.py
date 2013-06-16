from itertools import izip, cycle
cntr = 0;
myKey="AAAAAAAAAAAAAAAd"
plaintext="Secretfoemotherd"
def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
encrypted = xor_crypt_string(plaintext, key=myKey)
lostKey=[65]*16
newKey=['A']*16
while True:
	for x in xrange(0,16):
		newKey[x]=chr(lostKey[x])
	original = xor_crypt_string(encrypted, key=newKey)
	if original == plaintext:
		print "Wohoo we found the key again"
		print "Plaintext is: "+plaintext+" the bruteforce text is: "+original
		print "I ran: %d Times"%cntr
		break
 	index = 15;  	  
	lostKey[index]=lostKey[index]+1
	while index >= 0 and lostKey[index] >= 122:
		    lostKey[index] = 65
		    index=index-1
		    if index < 0: 
		      break
		    lostKey[index]=lostKey[index]+1
	cntr = cntr +1