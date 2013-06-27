Programming Project 1
=====================

**A tool for analyzing and decrypting a simple substitution cipher.**

## Overview

Consists of two Python scripts:

 * **FreqAnalysis.py**: Count the frequencies of letters, diagrams and
     trigrams in a given file.

 * **ManualSubCipherTool.py**: Helps to manually decrypt a given
     cipher by showing frequency analysis and comparing to the output
     for the previous mentioned script.

*NOTE:* Written in markdown. Open in browser to have good support. 
## Usage

### FreqAnalysis

Store the text you want analyzed in a file in the
same directory as the `FreqAnalysis.py`, the run the script with:

    python FreqAnalysis.py input.txt
    
Where `input.txt` is your input file.
    
The output will then be stored in two files:

 1. `output1.txt`: Letter frequencies
 2. `output2.txt`: Dia- and trigram frequencies

Docstrings is inserted for offical Python documentation.
 
*NOTE:* Out of the box contains `input.txt` a sample English text by
 [Project Gutenberg](www.gutenberg.org). Given another input text, the
 output frequencies will be different.
 
### ManualSubCipherTool

Uses a ciphertext as input. Run with:

    python ManualSubCipherTool.py "CyPhErTeXt"

Where "CyPhErTeXt" is the substituted cipher text.
    
You will now be prompted with an interactive command line interface.
It will be possible to navigate through with keyboard commands as input.

The tool uses the output from the FreqAnalysis tool for showing
frequencies of mono/dia/trigrams.

Docstrings is inserted for offical Python documentation.

*NOTE:* As noted under FreqAnalysis, it comes with a sample English
 word analysis. If your ciphertext is of a different language, you
 will have to run the FreqAnalysis tool of text in the wanted language.


## Logic behind.

The FreqAnalysis tool is based on an input .txt file. It the uses the following:

1. Input text is loaded
2. The tool runs through the input text, saving all characters/dia/trigrams and the ammount of times they have been spotted.
3. Outputs two .txt files containing, one containing the frequencies of letters and one containing frequencies of dia/trigrams in the text.

The ManualSubCipherTool is based around assistance in decryption of a cipher text. It follows this order:

1. The tool is started with a input cipher.
2. 5 Possibilities are given:
    1. Assign a plaintext letter to a ciphertext letter.
    2. Unassign a plaintext letter.
    3. Display frequencies of letters in cipher/english language.
    4. Display frequencies of dia/trigrams in cipher/english language.
    5. Finish your decryption
3. This is repeated untill you find the desired plaintext.

The following snippet of code is the corner stone of the two tools, wich gives us the frequencies of mono/dia/trigrams in our cipher and the english language:

    #Itereate lines in input file
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

It lets us assign mono/dia/trigrams in a HashTable and assign the value as the ammount of times they have been checked.

## Further Help

For further help or explanation please contact one of us by mail and
we'll be happy to help:

 * Markus Faerevaag [s123692@student.dtu.dk](mailto:s123692@student.dtu.dk)
 * Christian Mathias Rohde Kiaer [s123812@student.dtu.dk](mailto:s123812@student.dtu.dk)
 * Jonathan Becktor [s123094@student.dtu.dk](mailto:s123094@student.dtu.dk)
