# MIT 6.00.1x
# PRoblem Set 4
# Wordgame

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 3

# Line bellow broken to comply with pep8
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

wordList = loadWords()


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    returns: a dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    extraScore = 0
    if n == len(word):
        extraScore = 50
    # Line bellow broken to comply with pep8
    return sum([SCRABBLE_LETTER_VALUES[x] for x in word if x in
                SCRABBLE_LETTER_VALUES.keys()]) * len(word) + extraScore


def displayHand(hand):
    """
    Displays the letters currently in the hand.
    Doesn't return anything.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end="")
    print()


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3
    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    newHand = list(''.join([x*hand[x] for x in hand.keys()]))
    for i in word:
        if i in newHand:
            newHand.remove(i)
    return getFrequencyDict(newHand)


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if getFrequencyDict(word) == hand and word in wordList:
        return True
    else:
        if [x for x in word if x not in hand] == []:
            return sorted(list(word)) == sorted(
                [x for x in getFrequencyDict(word) if hand.get(x) >=
                 getFrequencyDict(word).get(x)]
            )
        else:
            return False


def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum([hand[x] for x in hand])


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    totalScore = 0
    while calculateHandlen(hand) > 0:
        displayHand(hand)
        # Line bellow broken to comply with pep8
        userInput = input(
            'Enter word, or a "." to indicate that you are finished: '
        )
        if userInput == ".":
            return print("Goodbye! Total score:", totalScore, "points.")
        else:
            if isValidWord(userInput, hand, wordList):
                totalScore += getWordScore(userInput, n)
                # Line bellow broken to comply with pep8
                print('" '+str(userInput)+' "', "earned",
                      getWordScore(userInput, n), " points. Total: ",
                      totalScore, " points")
                print('')
                hand = updateHand(hand, userInput)
            else:
                print("Invalid word, please try again.")
                print("")
    return print("Run out of letters. Total score:", totalScore, "points.")


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    userInput = ''
    while True:
        # Line bellow broken to comply with pep8
        userInput = input("Enter n to deal a new hand, r to replay the last" +
                          "hand, or e to end game: ")
        if userInput == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif userInput == 'r':
            try:
                playHand(hand, wordList, HAND_SIZE)
            except NameError:
                # Line bellow broken to comply with pep8
                print("You have not played a hand yet. " +
                      "Please play a new hand first!")
                print("")
        elif userInput == 'e':
            break
        else:
            print("Invalid command.")
    return None

if __name__ == '__main__':
    wordList = loadWords()
    HAND_SIZE = int(input("Enter hand size to play the game: "))
    playGame(wordList)
