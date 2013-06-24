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

The script essentially runs a **smart brute-force** attack:

 1. We first calculate the relevant time interval the cipher was
 created.
 2. Load ciphertext from file
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
