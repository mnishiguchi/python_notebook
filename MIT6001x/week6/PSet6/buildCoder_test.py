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
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    punc = string.punctuation
    digits = string.digits
    
    coder = dict()
    for i in range(26):
        #  The cipher is defined by the shift value.
        coder[ lower[i] ] = lower[ (i + shift) % 26 ]
        coder[ upper[i] ] = upper[ (i + shift) % 26 ]
  
    # Ignores non-letter characters  
    #for i in range( len (punc) ):
        #coder[ punc[i] ] = punc[i]
    #for i in range( len (digits) ):
        #coder[ digits[i] ] = digits[i]
    
    # Returns a dict that can apply a Caesar cipher to a letter.
    return coder
    
print buildCoder(9)
    