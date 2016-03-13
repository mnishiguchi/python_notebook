# use the idea of bisection search to determine if a character is in a string,
# so long as the string is sorted in alphabetical order.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    # Base case : if length is 0 or 1, just compare char with str[0]
    if len(aStr) == 1:
        return char == aStr[0]
    elif aStr == '':
        return False
        
    # check if midpoint of str
    mid = len(aStr) / 2
    if char == aStr[mid] :
        return True
        
    elif char > aStr[mid] :
        # check above midpoint
        return isIn( char, aStr[mid+1:] )
        
    elif char < aStr[len(aStr) / 2] :
        # check below midpoint
        return isIn( char, aStr[:mid] )    
        
        
#test
char = 'c'
aStr = 'abcdefgtyz'
print 'Is there', char, 'in', aStr, '? ---', isIn(char, aStr)  