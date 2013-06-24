#
# Project 2
#
# 01435 Practiacal Cryptanalysis
# Technical University of Denmark

# Markus Faerevaag              (s123692@student.dtu.dk)
# Christian Mathias Rohde Kiaer (s123812@student.dtu.dk)
# Jonathan Becktor              (s123094@student.dtu.dk)
#

import math

LETTERS = ['A','B','C','D','E',
           'F','G','H','I','J',
           'K','L','M','N','O',
           'P','Q','R','S','T',
           'U','V','W','X','Y','Z']
PERC    = [0.082, 0.015, 0.028, 0.043, 0.127,
           0.022, 0.02, 0.061, 0.07, 0.002,
           0.008, 0.04, 0.024, 0.067, 0.075,
           0.019, 0.001, 0.060, 0.063, 0.091,
           0.028, 0.01, 0.023, 0.001, 0.02, 0.001]


def calc_entropy(letter):
        """Calculates entropy for given letter"""
        P = PERC[LETTERS.index(letter.upper())]
	return P * math.log(1/P)/math.log(2)


def main():
        # Sum entropy for each letter
        sum = 0
        for letter in LETTERS:
                entropy = calc_entropy(letter)
                sum += entropy
                print "%s: %.3f" % (letter, entropy)

        print "The average number of bits: %f" % sum


if __name__ == '__main__':
        main()
