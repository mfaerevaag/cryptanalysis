#
# Project 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

from sys import argv
import os, md5, random, csv

BIT_SIZE = 28
TABLE_NAME = "table.csv"


def f(s, i):
    """Lowest 28 bits of MD5(s||u)"""
    digest = int(md5.new(str(s)).hexdigest()[-BIT_SIZE/4:], 16)
    result = (digest + i) % BIT_SIZE
    return '0x' + str(result)

def generate_table(s):
    """Generate Rainbow Table for key s"""
    dict = {"test":s, "asdf":0xdaffeee}
    w = csv.writer(open(TABLE_NAME, 'w'))
    for key, val in dict.items():
        w.writerow([key, val])


def getInput(i):
    while True:
        x = raw_input("Please enter a value: ")
        try:
            keyPressed = int(x)
            if(keyPressed <= i):
                break
            else:
                print "Wrong input, try again"
        except:
            print "Wrong input, try again"
    return x

if __name__ == '__main__': 
    os.system('clear')

    argcount = 0
    for arg in argv:
        argcount += 1
        
    if argcount < 2:
        print "Error: No key defined"
        exit()

    script, input = argv

    #random.getrandbits(28)
    s = int("0xabcdefe", 16)
    u = int("0xdaffeee", 16)

    print "Key: \t0x%x" % s
    print "f(s): \t0x%x" % f(s)

    generate_table(s)
