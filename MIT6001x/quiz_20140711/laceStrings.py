#example: 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # variables
    len1 = len(s1)
    len2 = len(s2)
    commonLen = 0
    difference = 0    
    tailSrting = ''
    lacedString = ''
    
    if len1 > len2:
        difference = len1 - len2
        commonLen = len2
        tailSrting = s1[-(difference):]
    elif len1 < len2:
        difference = len2 - len1
        commonLen = len1
        tailSrting = s2[-(difference):]
    else:
        difference = 0
        commonLen = len1
        tailSrting = ''     
        
    for i in range(commonLen): 
        lacedString += s1[i]
        lacedString += s2[i]

    return lacedString + tailSrting
        
# test

(s1, s2) = ('ioxwcfbpg', 'yriqtwfpu')
print laceStrings(s1, s2)   
    