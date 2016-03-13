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
            encodedLetters.append( coder[letter] )
        else:
            encodedLetters.append( letter )
        
    # Returns the encoded text.
    return ''.join( encodedLetters )
    
print applyCoder("Hello, world!", buildCoder(3))
#'Khoor, zruog!'
print applyCoder("Khoor, zruog!", buildCoder(23))
#'Hello, world!'