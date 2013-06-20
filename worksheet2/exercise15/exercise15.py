#
# Exercise 15
# Worksheet 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

import time, csv, md5, random

BIT_SIZE   = 20
NUM_CHAINS = 2**16
CHAIN_LEN  = 2**8
TABLE_NAME = "table.csv"
LOG_FREQ   = 5000


def md5_redux(s):
    """MD5 reduction function.
    Throws away all exceeding output bits from MD5 digest"""
    return '0x' + md5.new(str(s)).hexdigest()[:BIT_SIZE/4]

def generate_list():
    """Generates a rainbow table"""
    dict = {}
    order, keys_checked = []
    counter = 0
    
    for i in xrange(0, NUM_CHAINS - 1):
        red = hex(random.getrandbits(BIT_SIZE))[:-1]
        red_start_point = red
        
        for x in xrange(0, CHAIN_LEN - 1):
            red = md5_redux(red)
            keys_checked.append(red)

        red_end_point = red
            
        if i % LOG_FREQ == 0:
           print "Took i calls: %d and the unique keys checked is: %d" % (i, len(set(keys_checked)))

        order.append(red_start_point)
        dict[red_start_point] = red_end_point
        counter += 1
        
    print len(set(keys_checked))
    print len(keys_checked)
    
    write_to_csv(dict, order)


def write_to_csv(dict, order):
    """Writes the rainbow table to a .csv file"""
    w = csv.writer(open(TABLE_NAME, 'w'))
    for key in order:
        value = dict[key]
        w.writerow([key, value])


def main():
    start = time.clock()
    
    generate_list()
    
    end = time.clock()
    print "Took: ", (end - start), " s"    


if __name__ == '__main__':
    main()
