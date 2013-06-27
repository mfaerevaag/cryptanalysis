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
import md5, random, csv, os

BIT_SIZE = 28
CHAIN_LEN  = 2**10
TABLE_NAME = "table.csv"
SERIAL_NO = "0123456"

#s ='0x46d2260'
s ='0x8b392c4'
#s ='0x31e6ee3'
#s ='0x56259ab'
#s = hex(random.randint(16777216, 268435455))

u = "daffeda"

def reduction(cipher, iteration = 0):
    """Lowest 28 bits of (MD5(s||u) % i).
    Reduction function from the rainbow tables.
    Returns the hex value""" 
    return  hex((int(cipher, 16) + iteration) % 2**BIT_SIZE)[-BIT_SIZE/4 - 3: -1]

def md5_hash(s):
    """Hashes the original string and returns a hex string"""
    return '0x' + md5.new(str(s) + str(u)).hexdigest()[:-1]

#def f(s, i=0):
 #   """Lowest 28 bits of (MD5(s||u) % i)"""    
 #   digest = '0x' + md5.new(str(s) + str(u)).hexdigest()
  #  result = hex((int(digest, 16) + i) % 2**BIT_SIZE)[:BIT_SIZE/4+2]
   # return result


def read_table():
    """Read Rainbow Table from csv file"""
    dict = {}
    with open(TABLE_NAME, 'rb') as csvfile:
        table = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in table:
            dict[str(row[0])] = str(row[1])
    return dict


def find_key(table, r):
    """Search for matching respons in Rainbow-table
    First generates the successors of r.
    Then checks through the loaded rainbowtable if any matching values between the successors and the rainbowtable are found.
    If a match is found, the starting point of the given match is used to compute the predecessor of r.
    The predecessor of r, should be the key we are looking for."""
    #Initialize the list of successors of r.
    succ = [r]
    #Fills the list of successors of r.
    for i in xrange(1, CHAIN_LEN):
        succ.append(reduction(md5_hash(succ[i - 1]), i))

    #Looks through the dictonary given in the input.
    for key, value in table.iteritems():
        #If a value is in the successor list, ss = key.
        if value in succ:
            print "\tCollition: %s -> %s" % (key, value)
            ss = key
            #Starts with ss and computes the predecessor of r.
            for i in xrange(0, CHAIN_LEN):
                rs = reduction(md5_hash(ss), i)
                #if rs is equal to r, then the key should've been found.
                if rs==r:
                    #returns the predecessor.
                    return ss
                ss = rs
    return -1


def main():
    """main method for Rainbow attack on a car."""
    os.system('clear')
    #Printouts for console.
    print " Fob > Hello, key fob no. %s is here!" % SERIAL_NO
        
    print " Eve > Challenge: 0x%s" % u
    #Generates r
    r = reduction(md5_hash(s))
    print " Fob > Response:  %s" % r
    #loads the table from the csv file.
    table = read_table()
    print " Eve > Cracking..."
    
    #Tries to find the key
    key = find_key(table, r)

    if key is -1:
        print " Eve > %s" % colored('No key found!', 'red')
    else:
        print " Eve > %s: %s" % (colored('Key found', 'green'), key)

    print "\tActual key: %s" % s



if __name__ == '__main__':
    main()
