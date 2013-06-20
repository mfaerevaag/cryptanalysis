from sys import argv
import os

def decryption(cipher):

	found = False

	cip = list(cipher)

	plaintext = ['-'] * len(cip)

	remove_space(plaintext, cip)

	os.system('clear')

	while (not found):
		print "Cipher:    " + ''.join(cip)
		print "plaintext: " +''.join(plaintext)

		print """What would you like to do? \n1) Assign plaintext to cipher \n2) Unassign plaintext 
3) Letter frequencies in cipher/english \n4) Most frequent diagrams in cipher/text \n5) Finish decryption"""
		
		keyPressed = int(right_input(5))

		if (keyPressed == 1):
			assignPlainToCipher(cip, plaintext)
		elif(keyPressed == 2):
			unasignPlain(plaintext)
		elif(keyPressed == 3):
			display_letter(cip)
		elif(keyPressed == 4):
			display_diagrams(cip)
		elif(keyPressed == 5):
			print "This is the plaintext you found: " + ''.join(plaintext)
			found = True

		os.system('clear')

def assignPlainToCipher(cip, plaintext):
	
	keyToChange = str(raw_input("What cipher do you want to assign a plain character? ")).upper()
	keyChanged = str(raw_input("What letter do you want to input? ")).lower()
	for x in range(0, len(cip)):
		if(cip[x] == keyToChange):
			plaintext[x] = keyChanged

def unasignPlain(plaintext):
	
	keyToChange = str(raw_input("What plaintext character do you want to unassign? ")).lower()
	for x in range(0, len(plaintext)):
		if(plaintext[x] == keyToChange):
			plaintext[x] = '-'

def right_input(i):

	while True:
		x = raw_input("Please enter a value: ")
		try:
			keyPressed = int(x)
			if(keyPressed <= i):
				break
			else:
				print "Wrong input, try again"
		except:
			print "Wrong input, try again"
	return x

def remove_space(plaintext, cip):

	for x in xrange(0,len(cip)):
		if(cip[x] == ' '):
			plaintext[x] = ' '
	

def display_diagrams(cip):

	input_grams = open("output2.txt", "r")
	
	print "Ciphers frequency of dia/trigrams:"	
	
	print "Ciphers frequency of letters:"

	dict = {}

	count = 0

	for i in range(0, len(cip)):
		for j in range(2,4):
                        ch = str(''.join(cip[i:i+j]))
                if not ch.isalpha(): continue

                if ch in dict:
                        dict[ch] += 1
                else:
                        dict[ch] = 1
                count += 1

	for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
                if len(key) <= 1: continue
                print "{0}: {2:.3%}".format(key, value, 
                                            float(value)/float(count))                               
	
	print "English languge frequencies of tri/diagrams:"
	print ''.join(input_grams.readlines()[:20])

	raw_input("Press any key to continue: ")
	input_grams.close()

def display_letter(cip):

	input_frequency = open("output1.txt", "r")

	dict = {}
	
	print "Ciphers frequency of letters:"
	for i in range(0, len(cip)):
        	ch = str(''.join(cip[i:i+1]))
                
		if not ch.isalpha() or len(ch) > 1: continue

                if ch in dict:
                        dict[ch] += 1
                else:
                        dict[ch] = 1
                

	for key, value in sorted(dict.iteritems()):
  		print "{0}: {2:.3%}".format(key, value, float(value)/float(len(cipher))) 

	print "English languge frequencies of letters:"
	print ''.join(input_frequency.readlines())

	raw_input("Press any key to continue")
	input_frequency.close()

if __name__ == '__main__':
	
	os.system('clear')

	script, cipher = argv

	print "Hello! \nWelcome to our decryption assistance tool! How may I help you?"
	print "Press 1) for decryption"
	print "Press 0) for exit"

	keyPressed = int(right_input(1))

	if(keyPressed == 0):
		exit
	elif(keyPressed == 1):
		decryption(cipher.upper())
	else:
		print "Exiting"
