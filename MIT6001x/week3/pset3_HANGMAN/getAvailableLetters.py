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
    
          
# ----------test----------------
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
    
# ------------example---------------------   
#  >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#  >>> print getAvailableLetters(lettersGuessed)
#  abcdfghjlmnoqtuvwxyz