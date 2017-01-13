# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if not letter in lettersGuessed:
            return False
    return True
        
def isLetterGuessed(secretWord, letterGuessed):
    for letter in secretWord:
        if letter in letterGuessed:
            return True
    return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return_string = []

    for letter in secretWord:
        if not letter in lettersGuessed:
            return_string.append(' _ ')
        else:
            return_string.append(letter)
    s = ' '
    return_string = s.join(return_string)
    return return_string
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    lowercase = string.ascii_lowercase
    lowercase = list(lowercase)
    for letter in lettersGuessed:
        if letter in lowercase:
            lowercase.remove(letter)
    s = ''
    lowercase = s.join(lowercase)
    return lowercase

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("-----------")
    while guesses != 0:
        print("You have " + str(guesses) + " guesses left")
        letterstring = getAvailableLetters(lettersGuessed)
        print("Available letters: " + letterstring)
        choice = input("Please guess a letter: ")
        choice = str(choice.lower())
        while choice in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("You have " + str(guesses) + " guesses left")
            letterstring = getAvailableLetters(lettersGuessed)
            print("Available letters: " + letterstring)
            choice = input("Please guess a letter: ")
            choice = str(choice.lower())
        if isLetterGuessed(secretWord, choice):
            lettersGuessed.append(choice)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            guesses -= 1
            lettersGuessed.append(choice)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        print("-----------")

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was c. " + secretWord)
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
