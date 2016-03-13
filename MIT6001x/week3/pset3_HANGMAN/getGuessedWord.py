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

# ----------test----------------
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print type( getGuessedWord(secretWord, lettersGuessed) )

#------example---------------------------
#  >>> secretWord = 'apple' 
#  >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#  >>> print getGuessedWord(secretWord, lettersGuessed)
#  '_ pp_ e'