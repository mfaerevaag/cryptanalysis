#
# Project 3
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#


TIMEINT_START = 1245646800
TIMEINT_END   = 1246251599
CIPHERFILE    = "ciphertext_sheet3.txt"

a = 69.069
c = 5
m = 2**32


def update(s):
    return (a * s + c) % m


def init_key(s):
    key = []
    for i in xrange(0, 15):
        s = update(s)
        key.append(int(float.hex(s)[-6:-4], 16))

    return key


def load_cipher():
    f = open(CIPHERFILE, 'r')
    ciphertext = []
    for line in f:
        for c in line:
            ciphertext.append(c)
        
    return ciphertext


def encrypt(c, key, i):
#    return ord(c)
    return int(ord(c)) ^ key[i % 16]


def main():
    # Init s as s_0
    key = init_key(TIMEINT_START)
    
   # print key

    ciphertext = load_cipher()

#    print ciphertext

    for i in xrange(0, 10):
        print encrypt(ciphertext[i], key[i], i)


if __name__ == '__main__':
    main()
