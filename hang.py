import random
import string
from word import *

WORDLIST_FILENAME = "palavras.txt"

def isWordGuessed(secretWord, lettersGuessed):

    secretLetters = []
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():
     guessed = ''

     return guessed

def getAvailableLetters():

    import string
    available = string.ascii_lowercase

    return available


class Hangman:

    guesses = 8
    lettersGuessed = []
    secretWord = ''

    #funcao para pegar Palavra Secreta
    def secretWord(self, secretWord):
        self.secretWord = secretWord

    def gameHangam(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secretWord), ' letters long.'
        print '-------------'

        while  isWordGuessed(self.secretWord, self.lettersGuessed) == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            available = getAvailableLetters()
            auxAvailable = getAvailableLetters()
            for letter in available:
                if letter in self.lettersGuessed:
                    available = available.replace(letter, '')

            print 'Available letters', available
            letter = raw_input('Please guess a letter: ')
            while letter.__len__() > 1 or letter not in auxAvailable:
                print '\nAttention!\n'
                print 'You only need one letter at a time!'
                print 'Available letters', available
                letter = raw_input('Please guess a letter: ')

            if letter in self.lettersGuessed:

                guessed = getGuessedWord()
                for letter in self.secretWord:
                    if letter in self.lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Oops! You have already guessed that letter: ', guessed
            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)

                guessed = getGuessedWord()
                for letter in self.secretWord:
                    if letter in self.lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Good Guess: ', guessed
            else:
                self.guesses -=1
                self.lettersGuessed.append(letter)

                guessed = getGuessedWord()
                for letter in self.secretWord:
                    if letter in self.lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Oops! That letter is not in my word: ',  guessed
            print '------------'

        else:
            if isWordGuessed(self.secretWord, self.lettersGuessed) == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


word = Word()
secretWord = word.loadWords().lower()
hangman = Hangman()
hangman.secretWord(secretWord)
hangman.gameHangam()
