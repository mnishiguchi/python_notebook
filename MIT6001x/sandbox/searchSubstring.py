# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

def searchSubstring(s, sub):
    # get length of string
    sLen = len(s)
    # get length of substring
    subLen = len(sub)
    
    ctr = 0
    for i in range(0, sLen - subLen+1):
        # print s[i : i +subLen]
        if s[i : i +subLen] == sub:
            ctr += 1
    print "Number of times bob occurs is: ", ctr
    
# test
s = 'iuboboboboobobbobb'
sub ='bob'
searchSubstring(s, sub)