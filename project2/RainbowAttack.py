from sys import argv
from binascii import hexlify
import os, md5, random, csv

def a2bits(bytes):
    """Converts a sequence of bytes to to string of bits
    This function needs python >= 2.6"""
    return bin(int(b"1" + hexlify(bytes), 16))[3:]

def bits2a(b):
    """Converts string of bits to its string representation"""
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

def f(s):
    """Lowest 28 bits of MD5(s||u)"""
    digest = md5.new(str(s) + str(u)).digest()
    return int(a2bits(digest)[-28:], 2)

def generateRainbow(s):
    """Generate Rainbow Table for key s"""
    dict = {"test":s, "asdf":0xdaffeee}
    w = csv.writer(open("rainbow.csv", "w"))
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

    generateRainbow(s)
