#
# Project 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

from termcolor import colored
import os, md5, random, csv

BIT_SIZE = 28
CHAIN_LEN  = 2**10
TABLE_NAME = "table.csv"
LOG_FREQ   = 5000

SERIAL_NO = 0123456
#s = hex(random.getrandbits(BIT_SIZE))[:-1]
s = random.getrandbits(BIT_SIZE)
#s = "0x57c09f4"
u = int("0xdaffeda", 16)
#u = "0xdaffeda"


def cstring(msg, color):
    c = ''
    if color.lower() is 'red':
        c = '033[91m'
    elif color.lower() is 'yellow':
        c = '033[93m'
    elif color.lower() is 'green':
        c = '033[92m'

    return "%s %s %s" % (c, msg, c)


#def f(s):
#    """Lowest 28 bits of MD5(s||u)"""
#    digest = md5.new(str(s) + str(u)).hexdigest()[:BIT_SIZE/4]
#    return int(digest, 16)


def f(s, i=0):
    """Lowest 28 bits of (MD5(s||u) % i)"""    
    digest = md5.new(str(s) + str(u)).hexdigest()[:BIT_SIZE/4]
    result = (int(digest, 16) + i) % 2**BIT_SIZE
#    return hex(result)
    return result


def read_table():
    """Read Rainbow Table from csv file"""
    dict = {}

    with open(TABLE_NAME, 'rb') as csvfile:
        table = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in table:
#            dict[str(row[0])] = str(row[1])
            dict[int(str(row[0]), 16)] = int(str(row[1]), 16)

    return dict


def find_key(table, r):
    succ = [f(r)]
    for i in xrange(0, CHAIN_LEN - 1):
        succ.append(f(succ[i-1], i))

    for key, value in table.iteritems():
        if value in succ:
            print "Key: 0x%x Value: 0x%x" % (key, value)
            

    return -1


def main():
    print " Fob > Hello, key fob no. %i is here!" % SERIAL_NO
    
    print " Eve > Challenge: 0x%x" % u

    r = f(s)
    print " Fob > Response:  0x%x" % r

    table = read_table()
    print " Eve > Searching for key..."
    
    key = find_key(table, r)

    if key is -1:
        print " Eve > %s" % colored('No key found!', 'red')
    else:
        print " Eve > %s: 0x%x" % (colored('Key found', 'green'), key)

    print " Fob > Actual key was: 0x%x" % s

    exit(1 if key is -1 else 0)


if __name__ == '__main__':
    main()
