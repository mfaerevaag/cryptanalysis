Project 3
=========

A Python script for cracking known ciphertexts with a known
encryption algorithm.


## Content

 * `Breaker.py` - The script used for the "breaking" of the ciphertext
 * `ciphertext.txt` - The file containing the ciphertext
 * `plaintext.txt` - The produced plaintext from the ciphertext
 

## Usage

To decipher the ciphertext, run the `Breaker.py` script with an input
file, containing the ciphertext:

    $ python Breaker.py ciphertext_sheet3.txt
This requiers the ciphertext file to be in the same directory as the script. 
This will produce a file called plaintext.txt, if it is successful.

## Functionality

The script has a couple of functions that will be described:

 1. `calc_time(date, date_format)` This simply finds the seconds from 1.1.1970 to the given date.
 2. `update(s)` This function is the update function given in the assignment for each new key initialization
 3. `load_cipher(inputfile)` takes an inputfile and puts every character in a list and returns it
 4. `encrypt(c, key, i)` takes 3 variables a caracter form the caracter list the a key and i which is from the start point to end point of time when the file could have been encrypted.
 5. `check_plain(plain)` this function checks if our decrypted text is equal to any of our plaintexts.


## Logic

The script essentially runs a **smart brute-force** attack:

 1. We first calculate the relevant time interval within the cipher was
 created.
 2. Ciphertext loaded from file
 3. Start brute-force search for every possible time
     1. Initialize key with current time / internal state
     2. Encrypt every character in ciphertext with current state
     3. Check if result contains any of the words in the array of
     possible known plaintext elements.
     4. If found, print key and write to file


## Further Help

For further help or explanation please contact one of us by mail and
we'll be happy to help:

 * Markus Faerevaag [s123692@student.dtu.dk](mailto:s123692@student.dtu.dk)
 * Christian Mathias Rohde Kiaer [s123812@student.dtu.dk](mailto:s123812@student.dtu.dk)
 * Jonathan Becktor [s123094@student.dtu.dk](mailto:s123094@student.dtu.dk)
