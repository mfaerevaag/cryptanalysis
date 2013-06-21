#
# Project 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

import os, md5, random, csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

BIT_SIZE = 28
NUM_CHAINS = 2**16
CHAIN_LEN  = 2**8
TABLE_NAME = "table.csv"
LOG_FREQ   = 5000

SERIAL_NO = 0123456
s = random.getrandbits(BIT_SIZE)
u = int("0xdaffeda", 16)


def f(s):
    """Lowest 28 bits of MD5(s||u)"""
    digest = md5.new(str(s) + str(u)).hexdigest()[:BIT_SIZE/4]
    return int(digest, 16)


def fi(s, i):
    """Lowest 28 bits of (MD5(s||u) % i)"""    
    digest = md5.new(str(s) + str(u)).hexdigest()[:BIT_SIZE/4]
    result = (int(digest, 16) + i) % BIT_SIZE
    return result


def read_table():
    """Read Rainbow Table from csv file"""
    dict = {}

    with open(TABLE_NAME, 'rb') as csvfile:
        table = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in table:
            dict[int(row.pop(), 16)] = int(row.pop(), 16)

    return dict


def find_key(table, r):
    for key, value in table.iteritems():
        if value is hex(r):
            print "> Eve > KEY FOUND: %s" % key
            return key

    print "> Eve > No key found"


def main():
    print "Fob > Hello, key fob no. %i is here!" % SERIAL_NO
    
    print "%sEve%s > Challenge:\t 0x%x" % (bcolors.WARNING, bcolors.ENDC, u)

    r = f(s)
    print "> Fob > Response:\t 0x%x" % r

    table = read_table()
    print "> Eve > Searching for key..."
    find_key(table, r)


if __name__ == '__main__':
    main()
