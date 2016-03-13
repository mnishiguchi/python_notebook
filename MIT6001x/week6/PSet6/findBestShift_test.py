import string
#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    # get all the alphabetical characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    # create a dict
    coder = dict()
    
    for i in range(26):
        #  The cipher is defined by the shift value.
        coder[ lower[i] ] = lower[ (i + shift) % 26 ]
        coder[ upper[i] ] = upper[ (i + shift) % 26 ]
    
    # Returns a dict that can apply a Caesar cipher to a letter.
    return coder

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encodedLetters = []
    
    for letter in text:
        if letter.isalpha():
            encodedLetters.append( coder[letter] )  # encode alphabetical characters
        else:
            encodedLetters.append( letter )  # ignore the other characters
        
    # Returns the encoded text.
    return ''.join( encodedLetters )

        
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    coder = buildCoder(shift)
    applyCoder(text, coder)
    
    # returns a new text Caesar shifted by the given shift
    return applyCoder(text, coder)

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    (bestShift, bestNum) = (0, 0)

    # apply all the shift to text (0 to 25 inclusive)
    for shift in range(26):
        ctr = 0
        # check how many words are exist in word list
        for w in text:
            if isWord( applyShift(w, shift) ):
                ctr += 1
        if ctr > bestNum:
            (bestShift, bestNum) = (shift, ctr)

    # return the shift that generates the largest number of English words
    return bestShift

findBestShift(wordList, text)
