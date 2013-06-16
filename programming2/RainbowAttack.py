from sys import argv
import os, md5, random


def f(s):
    s = str(s)
    m = md5.new()
    m.update(s)
    m.update(u)
    return m.digest()


if __name__ == '__main__': 
    os.system('clear')
    script, cipher = argv

    u = str(random.getrandbits(28))
    print f(cipher)
    
