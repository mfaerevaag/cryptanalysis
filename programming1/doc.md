Programming Project 1
=====================

**A tool for analyzing and decrypting a simple substitution cipher.**

## Overview

Consists of two Python scripts:

 * **FreqAnalysis.py**: Count the frequencies of letters, diagrams and
     trigrams in a given file.

 * **ManualSubCipherTool.py**: Helps to manually decrypt a given
     cypher by showing frequency analysis and comparing to the output
     for the previous mentioned script.
     
## Usage

### FreqAnalysis

Store the text you want analyzed in a file called `input.txt` in the
same directory as the `FreqAnalysis.py`, the run the script with:

    python FreqAnalysis.py
    
The output will then be stored in two files:

 1. `output1.txt`: Letter frequencies
 2. `output2.txt`: Dia- and trigram frequencies
 
*NOTE:* Out of the box contains `input.txt` a sample english text by
 [Project Gutenberg](www.gutenberg.org).
 
### ManualSubCipherTool

With a given cyphertext, `CyPhErTeXt`, run the script with:

    python ManualSubCipherTool.py "CyPhErTeXt"
    
You will now be prompted with an interactive command line interface
where you can select options with the number keys on the you keyboard.

*NOTE:* As noted under FreqAnalysis, it comes with a sample english
 word analysis. If your ciphertext is of a different language, you
 will have to run the FreqAnalysis tool of text in the wanted language.

## Further Help

For further help or explanation please contact one of us by mail and
we'll be happy to help:

 * Markus Faerevaag [s123692@student.dtu.dk](mailto:s123692@student.dtu.dk)
 * Christian Mathias Rohde Kiaer [s123812@student.dtu.dk](mailto:s123812@student.dtu.dk)
 * Jonathan Becktor [s123094@student.dtu.dk](mailto:s123094@student.dtu.dk)
