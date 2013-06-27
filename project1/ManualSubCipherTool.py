#
# Manual Substitution Cipher Tool
# Project 1
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

from sys import argv
import os


def decryption(cipher):
        """Menu for assisting in decryption of ciphertext.
        Gives you possibilities for assigning plaintext letters to ciphertext letters,
        unassign letters in plaintext and display most frequent mono/dia/tri"""
	found = False

	cip = list(cipher)

	plaintext = ['-'] * len(cip)

	remove_space(plaintext, cip)

	os.system('clear')

	while not found:
		print "Cipher:    " + ''.join(cip)
		print "Plaintext: " +''.join(plaintext)

		print """What would you like to do?
1) Assign plaintext to cipher
2) Unassign plaintext 
3) Letter frequencies in cipher/english
4) Most frequent diagrams in cipher/text
5) Finish decryption"""
		
		keyPressed = int(right_input(5))

		if keyPressed == 1:
			assignPlainToCipher(cip, plaintext)
		elif keyPressed == 2:
			unasignPlain(plaintext)
		elif keyPressed == 3:
			display_letter(cip)
		elif keyPressed == 4:
			display_diagrams(cip)
		elif keyPressed == 5:
			print "This is the plaintext you found: " + ''.join(plaintext)
			found = True

		os.system('clear')

def assignPlainToCipher(cip, plaintext):
        """Assign plaintext character to corresponding ciphertext character.
        First input to console is the ciphertext letter you want to assign a new letter to.
        Second input is the plaintext letter you want to assign to a ciphertext letter.
        Then loops over entire cipher change every character."""	
	keyToChange = str(raw_input("What cipher do you want to assign a plain character? ")).upper()
	keyChanged = str(raw_input("What letter do you want to input? ")).lower()
	for x in range(0, len(cip)):
		if cip[x] == keyToChange:
			plaintext[x] = keyChanged

def unasignPlain(plaintext):
	"""Unassign previous assigned plaintext to ciphertext
    Input the plaintext character you want to unasign.
    Loops through entire plaintext to remove every character."""
	keyToChange = str(raw_input("What plaintext character do you want to unassign? ")).lower()
	for x in range(0, len(plaintext)):
		if plaintext[x] == keyToChange:
			plaintext[x] = '-'

def right_input(i):
        """Get input from user and validate.
        Function to make sure the right input is given.
        Right inputs is between 0 and the given i. Gives user another try if wrong key is pressed"""
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
        """Remove whitespaces from ciphertext. Loops over the ciphertext
        and sets corresponding plaintext position as whitespace."""
	for x in xrange(0,len(cip)):
		if cip[x] == ' ':
			plaintext[x] = ' '
	

def display_diagrams(cip):
        """Display dia and trigram frequencies in given ciphertext and compare to the given language's.
        Opens the output2.txt from created from the FreqAnalysis tool. Runs through the cipher text
        storing dia/trigrams in a dictonary. The ammount of appearances and the tri/diagram is then saved and printed.
        Then prints the most frequent dia/trigams from the english language"""
	input_grams = open("output2.txt", "r")
	
	print "Ciphers frequency of dia/trigrams:"	

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
        """Display letter frequencies in given ciphertext and compare to the given language's
        Opens the output1.txt generated from the FreqAnalysis tool. Runs through the cipher text and stores each letter and the ammount of times
        it's present in the text. Prints the character and corresponding ammount. Then outputs the frequencies of the english language
        from output2.txt"""
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
    """Tool for manual assitance in decryption of a substitution ciphertext.
    Possible to get analysis of both ciphertext and from the english language"""
    os.system('clear')

    script, cipher = argv

    print "Hello! \nWelcome to our decryption assistance tool! How may I help you?"
    print "1) Decrypt"
    print "0) Exit"

    keyPressed = int(right_input(1))

    if keyPressed == 0:
		exit
    elif keyPressed == 1:
		decryption(cipher.upper())
    else:
		print "Exiting"
