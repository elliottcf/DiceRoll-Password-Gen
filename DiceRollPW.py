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

