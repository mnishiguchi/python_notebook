# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

def findLongestAlphaString(s):
    longest = []
    letters = []
    
    for i in range( len(s) ) :
        #print i, '-----------------------------------------'
        # append this letter
        letters.append( s[i] )
        print letters
        
        # if next letter is NOT valid, that's it for this substring
        #print s[i], "vs", s[i + 1] , s[i] <= s[i + 1]
        if  i == len(s) -1 or s[i] > s[i + 1] : 
            # if this substring is the largest
            if len(letters) > len(longest) :
                #update largest
                longest = letters
            # empty the list
            letters = []
    print "Longest substring in alphabetical order is: ", "".join(longest)

# test 
s = 'uswvwqmezeawzpcxklov'
findLongestAlphaString(s)