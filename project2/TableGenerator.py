#
# Project 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

import os, md5, random, csv, time

BIT_SIZE   = 28
NUM_CHAINS = 2**18
CHAIN_LEN  = 2**10
TABLE_NAME = "table.csv"
LOG_FREQ   = 5000

u = int("0xdaffeda", 16)


def md5_redux(s, i=0):
    """Lowest 28 bits of (MD5(s||u) % i)"""    
    digest = md5.new(str(s) + str(u)).hexdigest()[:BIT_SIZE/4]
    result = (int(digest, 16) + i) % 2**BIT_SIZE
    return result


def generate_table():
    """Generates a rainbow table"""
    dict = {}
    order = []
    counter = 0
    
    for i in xrange(0, NUM_CHAINS - 1):
        red = hex(random.getrandbits(20))[:-1]
        red_start_point = red

        for x in xrange(0, CHAIN_LEN - 1):
            red = md5_redux(red, x)

        red_end_point = red

        if counter % LOG_FREQ == 0:
            print "Took i calls: %d keys: %d" % (i, counter)

        order.append(red_start_point)
        dict[red_start_point] = red_end_point
        counter += 1

    write_to_csv(dict, order)

    
def write_to_csv(dict, order):
    """Writes the rainbow table to a .csv file"""
    w = csv.writer(open(TABLE_NAME, 'w'))
    for key in order:
        value = dict[key]
        w.writerow([key, hex(value)])


def main():
    start = time.clock()
    
    generate_table()
    
    end = time.clock()
    print "Took: ", (end - start), " s"
    

if __name__ == '__main__':
    main()
    
