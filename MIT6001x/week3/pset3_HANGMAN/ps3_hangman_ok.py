# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

# ensure path is correct
WORDLIST_FILENAME = "C:\\Users\\Masatoshi_2\\Canopy\\6.00.1x Files\\week3\\pset3_HANGMAN\\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # list of results with indexes matched with secretWords
    result = [False] * len(secretWord)
    
    # check if each letter of secretWord exists in lettersGuessed
    for i in range( len(secretWord) ):     
        if lettersGuessed.count( secretWord[i] ) > 0:
            # remember result for each index
            result[i] = True 
    
    # if results are all True, return True, else False  
    return result.count(False) == 0 


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # list of results with indexes matched with secretWords
    result = [False] * len(secretWord)
    
    # check if each letter of secretWord exists in lettersGuessed
    for i in range( len(secretWord) ):     
        if lettersGuessed.count( secretWord[i] ) > 0:
            # retain the letter if already guessed
            result[i] = secretWord[i]
        else:
            # replace a letter with '_' if not guessed yet 
            result[i] = '_'
            
    # convert to str by joining all list element     
    return ''.join(result)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    availableLetters = []
    
    # iterate from a thru z; if available, append to list
    for char in string.ascii_lowercase:
        if lettersGuessed.count(char) == 0:
            availableLetters.append(char)
            
    # convert to str by joining all list element 
    return ''.join(availableLetters)
    

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
    # Welcome message
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %d letters long.' % len(secretWord)
    
    # counter for lives
    LIVES_MAX = 8
    lives = LIVES_MAX
    
    # list to remember used letters
    lettersUsed = []
    
    # list to remember correctly guessed letters
    lettersGuessed = []
    
    while 0 < lives:
        # print current status
        print '-------------'
        print 'You have %d guesses left.' % lives
        print 'Available Letters: %s' % getAvailableLetters(lettersUsed)
        
        # prompt for a guess
        guess = raw_input('Please guess a letter: ')
            
        # convert user input to lower case.
        guess = guess.lower()
        
        # check if user inputted letter is already used
        if guess in lettersUsed:
            print 'Oops! You\'ve already guessed that letter: %s' % getGuessedWord(secretWord, lettersGuessed)
            continue
        else:   
            # update used letter
            lettersUsed.append(guess)
           
        # got it right
        if guess in secretWord:
            # remember guessed letter
            lettersGuessed.append(guess)  
            print 'Good guess: %s' % getGuessedWord(secretWord, lettersGuessed)
                
            # check if entire secretWord is guessed
            if isWordGuessed(secretWord, lettersGuessed):
                print '-------------'
                print 'Congratulations, you won!'
                return
        
        # got it wrong        
        else:
            # decrement lives
            lives = lives - 1   
            print 'Oops! That letter is not in my word: %s' % getGuessedWord(secretWord, lettersGuessed)
            
    # if lives are used up, gameover 
    print '-------------'  
    print 'Sorry, you ran out of guesses. The word was %s' % secretWord


#-----------------------------------
# test

# random pick
secretWord = chooseWord(wordlist).lower()
# call hangman
hangman(secretWord)
