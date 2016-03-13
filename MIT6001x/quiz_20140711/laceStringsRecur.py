def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    print 'start'
    
    def helpLaceStrings(s1, s2, out):
        if s1 == '':         # base case
            print 'base case1'
            return out + s2
        if s2 == '':         # base case
            print 'base case2'
            return out + s1
        else:
            # if not base case, repeat stripping off s1[0] & s2[0]
            # and pass them in next recursive call as "out"
            print 'else'
            return out + helpLaceStrings( s1[1:], s2[1:], (s1[0] + s2[0]) ) 
            
    return helpLaceStrings(s1, s2, '')
    
    
# test
#example: ('abcd','efghi'), we would get the new string: 'aebfcgdhi'
(s1, s2) = ('abcd','efghi')
print laceStringsRecur(s1, s2)   