import time, csv, md5, random

def md5_redux(s):
    """Reduction method to throw away all exceeding output bits from MD5 hashfunction. Outputs 20bit"""
    return '0x' + md5.new(str(s)).hexdigest()[:5]

def generate_list():
    """Generates a rainbow table"""
    dict = {}
    order = []
    counter = 0
    keys_checked = []
    for i in xrange(0, 2**16 - 1):
        red = hex(random.getrandbits(20))[:-1]
        red_start_point = red
        
        for x in xrange(0, 255):
            red = md5_redux(red)
            keys_checked.append(red)

        red_end_point = red
            
        if i % 5000 == 0:
           print "Took i calls: %d and the unique keys checked is: %d" % (i, len(set(keys_checked)))

        order.append(red_start_point)
        dict[red_start_point] = red_end_point
        counter += 1
    print len(set(keys_checked))
    print len(keys_checked)
    write_to_csv(dict, order)

def write_to_csv(dict, order):
    """Writes the rainbow table to a .csv file"""
    w = csv.writer(open("table.csv", "w"))
    for key in order:
        value = dict[key]
        w.writerow([key, value])
#    for key, val in dict.items():
#        w.writerow([key, val])

if __name__ == '__main__':
    start = time.clock()
    generate_list() 
    end = time.clock()
    print "Took: ", (end - start), " s"    
