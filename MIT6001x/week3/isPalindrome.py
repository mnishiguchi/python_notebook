# -*- coding: utf-8 -*-
# example of a “divide and conquer” algorithm

def isPalindrome(s):
    
    # First, convert the string	to just	characters,
    # by stripping out punctuation and converting upper	case to	lower case    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
 
               
    def isPal(s):
        #  Base case: a string of length 0 or 1 is a palindrome
        if len(s) <= 1:
            return True
        
        else:
            # If ﬁrst character matches last character,
            # then is a palindrome if middle section is a palindrome
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
    
#test
s = 'Madam im adam'
print s, isPalindrome(s)