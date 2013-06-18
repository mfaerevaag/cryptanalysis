from sys import argv
from binascii import hexlify
import os, md5, random

def a2bits(bytes):
    """Converts a sequence of bytes to to string of bits
    This function needs python >= 2.6"""
    return bin(int(b"1" + hexlify(bytes), 16))[3:]

def bits2a(b):
    """Converts string of bits to its string representation"""
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

def f(s):
    """Lowest 28 bits of MD5(s||u)"""
    digest = md5.new(str(s) + u).digest()
    return int(a2bits(digest)[-28:], 2)
    

if __name__ == '__main__': 
    os.system('clear')
    script = argv

    u = str(random.getrandbits(28))
    
    s = random.getrandbits(28)
    print "Key: \t0x%x" % s

    print "Low28: \t0x%x" % int(a2bits(str(s))[-28:], 2)

    print "f(s): \t0x%x" % f(s)

