from sys import argv
import os

def decryption(cipher):

	found = False

	cip = list(cipher)

	plaintext = ['-'] * len(cip)

	print len(plaintext)

	os.system('clear')

	while (not found):
		print ''.join(cip)
		print ''.join(plaintext)

		print """What would you like to do? \n1) Assign plaintext to cipher \n2) Unassign plaintext 
3) Letter frequencies in cipher/english \n4) Most frequent diagrams in cipher/text \n5) Finish decryption"""
		
		while True:
			x = raw_input("Please enter a value: ")
			try:
				keyPressed = int(x)
				if(keyPressed <= 5):
					break
				else:
					print "Wrong input, try again"
			except:
				print "Wrong input, try again"

		if (keyPressed == 1):
			assignPlainToCipher(cip, plaintext)
		elif(keyPressed == 2):
			unasignPlain(plaintext)	
		elif(keyPressed == 5):
			print "Found!"
			print ''.join(plaintext)
			found = True

		os.system('clear')

def assignPlainToCipher(cip, plaintext):
	
	keyToChange = str(raw_input("What letter do you want to change? "))
	keyChanged = str(raw_input("What letter do you want to input? "))
	for x in xrange(0, len(cip)):
		if(cip[x] == keyToChange):
			plaintext[x] = keyChanged

def unasignPlain(plaintext):
	
	keyToChange = str(raw_input("What letter do you want to change? "))
	for x in xrange(0, len(plaintext)):
		if(plaintext[x] == keyToChange):
			plaintext[x] = '-'

if __name__ == '__main__':
	
	os.system('clear')

	script, cipher = argv

	print "Hello! \nWelcome to our decryption assistance tool! How may I help you?"
	print "Press 1) for decryption"
	print "Press 0) for exit"

	while True:
		x = raw_input("Please enter a value: ")
		try:
			keyPressed = int(x)
			if(keyPressed <= 1):
				break
			else:
				print "Wrong input, try again"
		except:
			print "Wrong input, try again"
	

	if(keyPressed == 0):
		exit
	elif(keyPressed == 1):
		decryption(cipher.upper())
	else:
		print "You have entered a wrong key, please try again!"
