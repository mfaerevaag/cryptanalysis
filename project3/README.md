Project 3
=========

A simple Python script for cracking a known ciphertext with known
encryption algorithm.


## Content

 * `Breaker.py` - The script used for breaking the ciphertext
 * `ciphertext.txt` - The file containing the ciphertext
 * `plaintext.txt` - The produced plaintext from the ciphertext
 

## Usage

To decipher the ciphertext, run the `Breaker.py` script with an input
file, containing the ciphertext:

    $ python Breaker.py ciphertext_sheet3.txt
    
This will produce a file called plaintext.txt, if it is successful.


## Logic

The script essentially runs a smart brute-force attack. 

As we know the time period the file was decrypted, we take all the
possible times and iterates over them. For each relevant time encrypt
each letter with the given algorithm, and see if the result contains
any of the words in our array of known plaintext words.
