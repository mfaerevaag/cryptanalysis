import os, md5, random, csv

u = "daffeda"
BIT_SIZE = 28
CHAIN_LEN  = 2**10
TABLE_NAME = "table.csv"
SERIAL_NO = "0123456"

def reduction(cipher, iteration = 0):
    """Lowest 28 bits of (MD5(s||u) % i)""" 
    return  hex((int(cipher, 16) + iteration) % 2**BIT_SIZE)[-BIT_SIZE/4 - 3: -1]

def md5_hash(s):
    """Hashes the original string and returns a hex string"""
    return '0x' + md5.new(str(s) + str(u)).hexdigest()[:-1]

def a(s, i=0):
    """Lowest 28 bits of (MD5(s||u) % i)"""    
    digest = md5.new(str(s) + str(u)).hexdigest()[-BIT_SIZE/4:]
    result = (int(digest, 16) + i) % 2**BIT_SIZE
    return result

s ="0x8e01844"
temp = s
lol = [reduction(md5_hash(s))] 
print lol[0]
for x in xrange(0, CHAIN_LEN):
    print x,
    hej = reduction(md5_hash(temp), x)
    temp = hej
    lol.append(hej)
    print hej
print len(lol)
