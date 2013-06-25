import os, md5, random, csv

u = "daffeda"
BIT_SIZE = 28
CHAIN_LEN  = 2**10
TABLE_NAME = "table.csv"
SERIAL_NO = "0123456"

def f(s, i=0):
    """Lowest 28 bits of (MD5(s||u) % i)"""    
    digest = '0x' + md5.new(str(s) + str(u)).hexdigest()[-BIT_SIZE/4:]
    result = hex((int(digest, 16) + i) % 2**BIT_SIZE)
    return result


def a(s, i=0):
    """Lowest 28 bits of (MD5(s||u) % i)"""    
    digest = md5.new(str(s) + str(u)).hexdigest()[-BIT_SIZE/4:]
    result = (int(digest, 16) + i) % 2**BIT_SIZE
    return result

s = "0x33cad1d"
temp = s
lol = [s]
for x in xrange(0, CHAIN_LEN):
    print x,
    hej = f(temp, x)
    temp = hej
    lol.append(hej)
    print hej
print len(lol)
