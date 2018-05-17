import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Word:

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        inFile = open(WORDLIST_FILENAME, 'r', 0)
        line = inFile.readline()
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."
        return random.choice(wordlist)
