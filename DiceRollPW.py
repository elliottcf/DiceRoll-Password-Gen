#!/usr/bin/env python
"""Creates a passphrase through PRNG dicerolls.

Needs the number of words and at least one word list.
"""
import random
import argparse
import csv
import os

__author__ = "Elliott Fawcett"
__copyright__ = "Copyright (c) 2014, elliottcf"

__license__ = "MIT"
__version__= "0.1"
__maintainer__ = "Elliott Fawcett"
__status__ = "Development"

parser = argparse.ArgumentParser(prog='DiceRollPW', description='Generates a passphrase from word lists.')
parser.add_argument('length', type=int, help='The number of words in the passphrase')
parser.add_argument('word_list_input', nargs='+', help='Word list files (csv or space-delimited')

args = parser.parse_args();
vars(args);

passphrase= [];
passphrase_length=args.length
word_list = [];
for filename in args.word_list_input:
    with open(os.path.normpath(filename),'r') as fo:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(fo.read(32))
        #Move the current position back to start of file
        position = fo.seek(0,0)
        #dialect.delimiter has the delimiter
        list_delimiter = dialect.delimiter
        filereader = csv.reader(fo, delimiter=list_delimiter, strict=True)
    
        try:
            for row in filereader:
                if (row != ' '):
                    word_list.extend(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, filereader.line_num, e))
        fo.close()
word_list = filter(None, word_list)
#print word_list
word_list_length = len(word_list)
number_gen = random.SystemRandom()
printing_pw=True
while (printing_pw):
    for ppword in xrange(passphrase_length):
        random_word = number_gen.randint(0,word_list_length-1)
        passphrase.append(word_list[random_word])
    print (' - ').join(passphrase);
    print "Your passphrase is: "+('').join(passphrase)
    print "Type \'r\' then \'Enter\' to generate another passphrase"
    print "Press \'Enter\' to quit"
    s = raw_input()
    if (s != 'r'):
        printing_pw=False
    else:
        passphrase[:]=[]
        print "Next:"


"""
The MIT License (MIT)

Copyright (c) 2014 elliottcf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
