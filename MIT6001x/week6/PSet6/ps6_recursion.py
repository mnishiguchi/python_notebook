# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are
    indexing, slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 1:
        return aStr
    return aStr[-1] + reverseString( aStr[:-1] )


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    print 'x =', x
    
    # ensure params are not empty
    if word == '' or x == '':
        return False
    
    # base case
    if len(x) ==1:
        print 'base case'
        print x[0], 'in', word
        return x[0] in word
        
    # if first letter exists in word  
    if x[0] in word:
        print x[0], 'in', word
        # strip the substring ending with the letter away from word
        index = word.find( x[0] )
        chars = [ char for char in word ]
        word = ''.join( chars[index:] )
    else:
        return False
    return  x_ian(x[1:], word)
    

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
   
    

## -------test  reverseString(aStr) ----------
#import string
#aStr = string.ascii_uppercase
#print reverseString(aStr)
## -------test  x_ian(x, word) ----------
#(x, word) = 'eric', 'cerium'
#print x_ian(x, word)
