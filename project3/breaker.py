#
# Project 3
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

import time

START_DATE    = '2009-06-22 00:00:00'
END_DATE      = '2009-06-28 23:59:59'

CIPHERFILE    = "ciphertext_sheet3.txt"
PLAINFILE     = 'plaintext.txt'
KNOWN_PLAINTEXT = ['Snowden',
                   'Obama',
                   'Biden',
                   'Risen',
                   'Nelson',
                   'NSA', 'National Security Agency',
                   'China',
                   'Whistleblower',
                   'Hong Kong']

# Given constants
a = 69069
c = 5
m = 2**32


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


def load_cipher():
    """Load ciphertext from file"""
    f = open(CIPHERFILE, 'r')
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
    # Calculcate time interval
    date_format = '%Y-%m-%d %H:%M:%S'
    start = int(time.mktime(time.strptime(START_DATE, date_format))) - time.timezone
    end = int(time.mktime(time.strptime(END_DATE, date_format))) - time.timezone

    # Start bruteforce search
    for i in xrange(start, end):
        key = init_key(i)

        ciphertext = load_cipher()

        plain = ''
        for j in xrange(0, len(ciphertext)-1):
            c = chr(encrypt(ciphertext[j], key, j))
            plain += c

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
