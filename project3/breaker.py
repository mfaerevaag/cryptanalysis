#
# Project 3
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

from sys import argv
import os, time

# Given dates
DATE_FORMAT     = '%Y-%m-%d %H:%M:%S'
START_DATE      = '2009-06-22 00:00:00'
END_DATE        = '2009-06-28 23:59:59'  

# Given constants
a = 69069
c = 5
m = 2**32

PLAINFILE       = 'plaintext.txt'
KNOWN_PLAINTEXT = ['Snowden',
                   'Obama',
                   'Biden',
                   'Risen',
                   'Nelson',
                   'NSA', 'National Security Agency',
                   'China',
                   'Whistleblower',
                   'Hong Kong']


def calc_time(date, date_format):
    """Calculates seconds from UNIX epoch (1.1.1970) to given date"""
    return int(time.mktime(time.strptime(date, date_format))) - time.timezone


def update(s):
    """Update internal state"""
    return (a * s + c) % m


def init_key(s):
    """Init key with internal state"""
    key = []
    for i in xrange(0, 16):
        s = update(s)
        key.append(str(bin(s)[-8:]))

    return key


def load_cipher(inputfile):
    """Load ciphertext from file"""
    f = open(inputfile, 'r')
    ciphertext = []
    for line in f:
        for c in line:
            ciphertext.append(c)

    f.close()
    return ciphertext


def encrypt(c, key, i):
    """Encrypt character with i in key"""
    return ord(c) ^ int(key[i % 16], 2)


def check_plain(plain):
    """Check if text contains any of known plaintexts"""
    for word in KNOWN_PLAINTEXT:
        if word in plain:
            return True
        
    return False


def main():
    # Check if enough argument were given
    argcount = 0
    for arg in argv:
        argcount += 1    
    if argcount < 2:
        print "Error: No input file spesified"
        return 1

    script, inputfile = argv

    # Calculate times
    start = calc_time(START_DATE, DATE_FORMAT)
    end = calc_time(END_DATE, DATE_FORMAT)
    
    # Load ciphertext from inputfile
    ciphertext = load_cipher(inputfile)
    
    # Start bruteforce search
    for i in xrange(start, end):
        key = init_key(i)

        # Encrypt each character add append to string
        plain = ''
        for j in xrange(0, len(ciphertext)-1):
            c = chr(encrypt(ciphertext[j], key, j))
            plain += c

        ## See if string contains any of known plaintexts
        if check_plain(plain):
            print "Found plaintext after %i tries!" % (i - start)
            print "Key: ",
            for k in key:
                print chr(int(k, 2)),
            print "\n-----------------------------------------------------\n"
            
            print plain
            f = open(PLAINFILE, 'w')
            f.write(plain)
            f.close()
            
            break


if __name__ == '__main__':
    main()
