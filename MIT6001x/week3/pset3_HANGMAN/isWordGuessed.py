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
    print result
    
    # if results are all True, return True, else False  
    return result.count(False) == 0   
    
# ----------test----------------
secretWord = 'apple' 
lettersGuessed = ['a', 'l', 'p', 'e']    #['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)
