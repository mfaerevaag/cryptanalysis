#
# Project 3
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#


TIMEINT_START = 1245646800
TIMEINT_END   = 1246251599

a = 69.069
c = 5
m = 2**32


def update(s):
    return (a * s + c) % m


def main():
    # Init s as s_0
    s = TIMEINT_START

    key = []
    for i in xrange(0, 15):
        s = update(s)
        key.append(float.hex(s)[-6:-4])

    print key


if __name__ == '__main__':
    main()
