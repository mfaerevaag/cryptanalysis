from binascii import hexlify
from numpy import binary_repr
import md5, random, time, csv

def a2bits(bytes):
    """Converts a sequence of bytes to to string of bits
    This function needs python >= 2.6"""
    return bin(int(b"1" + hexlify(bytes), 16))[3:23]

def bits2a(b):
    """Converts string of bits to its string representation"""
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

def md5_redux(s):
    """Reduction method to throw away all exceeding output bits from MD5 hashfunction. Outputs 20bit"""
    digest = md5.new(str(s)).digest()
    return int(a2bits(digest)[:20], 2)

def generate_list():
    """Generates a rainbow table"""
    dict = {}
    counter = 0
    for i in xrange(0, 2**16 - 1):
        red = random.getrandbits(20)
        red_start_point = binary_repr(red, width = 20)
        for x in xrange(0,255):
            red = md5_redux(red)
        red_end_point = binary_repr(red, width = 20)
        if red_start_point in dict:
            pass
        else:
            counter += 1
        if counter % 10000 == 0:
            print "Took i calls: %d and the counter is: %d" % (i, counter)
        dict[red_start_point] = red_end_point
    write_to_csv(dict)
    print counter

def write_to_csv(dict):
    """Writes the rainbow table to a .csv file"""
    w = csv.writer(open("table1.csv", "w"))
    for key, val in dict.items():
        w.writerow([key, val])

if __name__ == '__main__':
    start = time.clock()
    generate_list() 
    end = time.clock()
    print "Took: ", (end - start), " s"
            