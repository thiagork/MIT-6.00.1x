# MIT 6.00.1x
# Problem Set 3
# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in
    lettersGuessed, False otherwise
    '''
    for n in secretWord:
        if n not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedCorrect = ''
    for n in secretWord:
        if n in lettersGuessed:
            guessedCorrect += n
        else:
            guessedCorrect += '_'
    # inserts space between letters
    guessedCorrect = " ".join(guessedCorrect)
    return guessedCorrect


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # from import string
    availableLetters = list(string.ascii_lowercase)
    for n in lettersGuessed:
        if n in availableLetters:
            availableLetters.remove(n)
    # Convers list into string
    availableLetters = ''.join(availableLetters)
    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    '''
    secretWord = str.lower(secretWord)
    guessesLeft = 8
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    while guessesLeft > 0:
        print("-----------")
        print("You have", guessesLeft, "guesses left")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        userInput = input("Please guess a letter: ")
        if userInput in lettersGuessed:
            # Line bellow broken to comply with pep8
            print("Oops! You've already guessed that letter:",
                  getGuessedWord(secretWord, lettersGuessed))
        else:
            if userInput in secretWord:
                lettersGuessed.append(userInput)
                # Line bellow broken to comply with pep8
                print("Good guess: ", getGuessedWord(secretWord,
                      lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print("-----------")
                    return print("Congratulations, you won!")
            else:
                # Line bellow broken to comply with pep8
                print("Oops! That letter is not in my word:",
                      getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(userInput)
                guessesLeft -= 1
    print("-----------")
    return print("Sorry, you ran out of guesses. The word was", secretWord)


secretWord = chooseWord(wordlist).lower()

# Change this and enjoy the game!
hangman('Testcase')
