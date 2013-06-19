from sys import argv
import os

if __name__ == '__main__':
    os.system('clear')

    argcount = 0
    for arg in argv:
        argcount += 1
        
    if argcount < 2:
        print "Error: No input file spesified"
        exit()

    script, inputfile = argv

    input = open(inputfile, "r")
    output1 = open("output1.txt", "w")
    output2 = open("output2.txt", "w")

    dict = {}
    total = [0, 0]

    for line in input:
        line = line.upper()
        
        for i in range(0, len(line)):
            for j in range(1, 4):
                ch = line[i:i+j]
                
                if not ch.isalpha():
                    continue
                
                if ch in dict:
                    dict[ch] += 1
                else:
                    dict[ch] = 1
                    
                total[0 if len(ch) < 2 else 1] += 1

    # Monograms
    for key, value in sorted(dict.iteritems()):
        if len(key) > 1:
            continue
        output1.write("{0}: {2:.3%}\n".format(
                key, value, float(value)/float(total[0])))

    # Di- and trigrams
        for key, value in sorted(dict.iteritems(), 
                                 key=lambda (k, v): (v, k), reverse=True):
            if len(key) <= 1:
                continue
            output2.write("{0}: {2:.3%}\n".format(
                    key, value, float(value)/float(total[0])))
  
    input.close()
    output1.close()
    output2.close()

