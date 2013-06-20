import md5, random, time, csv

def md5_redux(s):
    """Reduction method to throw away all exceeding output bits from MD5 hashfunction. Outputs 20bit"""
    return '0x' + md5.new(str(s)).hexdigest()[:5]

def generate_list():
    """Generates a rainbow table"""
    dict = {}
    order = []
    counter = 0
    for i in xrange(0, 2**16 - 1):
        red = hex(random.getrandbits(20))[:-1]
        red_start_point = red
        
        for x in xrange(0, 255):
            red = md5_redux(red)
            
        red_end_point = red

        # Skip if already in dict
        if red_start_point in dict:
            continue
        else:
            counter += 1
            
        if counter % 5000 == 0:
            print "Took i calls: %d and the counter is: %d" % (i, counter)

        order.append(red_start_point)
        dict[red_start_point] = red_end_point
        
    write_to_csv(dict, order)

def write_to_csv(dict, order):
    """Writes the rainbow table to a .csv file"""
    w = csv.writer(open("table1.csv", "w"))
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
