# Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:   Number of vowels: 5

def countVowel():
    '''
    prompt user for a string and
    print number of vowels to the console
    '''
    #s = raw_input("Type a word: ")
    s = 'qzoaimthiuriqsundrtb'
    ctr = 0
    # iterate over word
    for letter in s :
        # if it is a vowel, update counter
        if letter in [ 'a', 'e', 'i', 'o', 'u' ] :
            ctr +=1
    print "Number of vowels: ", ctr
            
            
# call the function
countVowel()