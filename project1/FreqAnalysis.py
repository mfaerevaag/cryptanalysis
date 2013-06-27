from sys import argv
import os

if __name__ == '__main__':
    """Tool for analysing an input text, and outputting a frequency
    analysis of mono/dia/trigrams in a given input text. Takes the input file and runs through it, saving the
    ammount of times a character and dia/trigrams is present. Then outputs the given values to 2 .txt files.
    If a british english text is given as a input file, a representation close to the frequency of letters of the english alphabet should be outputtet."""
    os.system('clear')

    # Check if enough argument were given
    argcount = 0
    for arg in argv:
        argcount += 1    
    if argcount < 2:
        print "Error: No input file spesified"

    script, inputfile = argv

    # Open files for reading and writing
    input = open(inputfile, 'r')
    output1 = open("output1.txt", 'w')
    output2 = open("output2.txt", 'w')

    # Declare variables to scope
    dict = {}
    count = [0, 0]

    # Itereate lines in input file
    for line in input:
        line = line.upper() # Clean line

        # For every leagal permutation
        for i in xrange(0, len(line)):
            # Mono-, dia- and trigrams
            for j in xrange(1, 4):
                ch = line[i:i+j] # Substring w/ *gram

                # Continue if not all letters
                if not ch.isalpha(): continue 

                # Lazy create and inc counter
                if ch in dict:
                    dict[ch] += 1
                else:
                    dict[ch] = 1

                # Increment total number of *grams
                count[0 if len(ch) < 2 else 1] += 1

    # Print all monograms to file
    for key, value in sorted(dict.iteritems()):
        if len(key) > 1: continue
        output1.write("{0}: {2:.3%}\n".format(
                key, value, float(value)/float(count[0])))

    # Print all di- and trigrams to file
    for key, value in sorted(dict.iteritems(), 
                             key=lambda (k, v): (v, k), reverse=True):
        if len(key) <= 1: continue
        output2.write("{0}: {2:.3%}\n".format(
                key, value, float(value)/float(count[0])))

    print "Successfully analyzed %s" % inputfile
    
    # Close files before finish
    input.close()
    output1.close()
    output2.close()

