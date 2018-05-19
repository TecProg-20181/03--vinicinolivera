import random
import string
import os.path
import sys

WORDLIST_FILENAME = "palavras.txt"

class Word:

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        if os.path.isfile(WORDLIST_FILENAME):
            print "Loading word list from file..."
            inFile = open(WORDLIST_FILENAME, 'r', 0)
            line = inFile.readline()
            wordlist = string.split(line)
            print "  ", len(wordlist), "words loaded."
            return random.choice(wordlist)
        else:
            print "File ", WORDLIST_FILENAME, "not found!"
            sys.exit()
