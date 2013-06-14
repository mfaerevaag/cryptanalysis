
input = open("input.txt", "r")
output1 = open("output1.txt", "w")
output2 = open("output2.txt", "w")

dict = {}
total = [0,0]

for line in input:
    line = line.upper()

    for i in range(0, len(line)):
        for j in range(1, 4):
            ch = line[i:i+j]

            if not ch.isalpha(): continue

            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
                
            total[0 if len(ch) < 2 else 1] += 1

for key in sorted(dict.keys()):
    file = output2 if len(key) > 1 else output1
    idx = 0 if len(key) < 1 else 1
    file.write("{0}: {1} ({2:.3%})\n".format(key, dict[key], 
                                         float(dict[key])/float(total[idx])))

