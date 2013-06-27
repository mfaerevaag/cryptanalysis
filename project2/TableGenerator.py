#
# Project 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

import md5, random, csv, time

#Constants used to create the table.
BIT_SIZE   = 28
NUM_CHAINS = 2**18
CHAIN_LEN  = 2**10
TABLE_NAME = "tabletest.csv"
LOG_FREQ   = 5000
#Challenge key u
u = "daffeda"

def reduction(cipher, iteration):
    """Lowest 28 bits of (MD5(s||u) % i)""" 
    return  hex((int(cipher, 16) + iteration) % 2**BIT_SIZE)[-BIT_SIZE/4 - 3: -1]

def md5_hash(s):
    """Hashes the original string and returns a hex string"""
    return '0x' + md5.new(str(s) + str(u)).hexdigest()[:-1]

def generate_table():
    """Generates a rainbow table.
    Fills a hashtable with random generated start points and their corresponding endpoints.
    Runs through the given number of chains and length of each chain. Ends of with writing the dictonary to a .csv file."""
    dict = {}

    #Runs the loop through the number of chains
    for i in xrange(0, NUM_CHAINS):
        red = hex(random.randint(16777216, 268435455))

        #Random generated startpoint.
        red_start_point = red

        #Computes the end point, by hashing the start point through the number of chains.
        for x in xrange(0, CHAIN_LEN):
            cipher = md5_hash(red)
            red = reduction(cipher, x) 

        #Endpoint for storage in table.
        red_end_point = red

        #Prints ammount of times loop has run.
        if i % LOG_FREQ == 0:
            print "Took i calls: %d" % (i)
        dict[red_start_point] = red_end_point

    write_to_csv(dict)

    
def write_to_csv(dict):
    """Writes the rainbow table to a .csv file"""
    w = csv.writer(open(TABLE_NAME, 'w'))
    for key, value in dict.items():
        w.writerow([key, value])


def main():
    """Tool for generating a rainbowtable from given constants."""
    start = time.clock()
    generate_table()    
    end = time.clock()
    print "Took: ", (end - start), " s"
    
if __name__ == '__main__':
    main()
    
