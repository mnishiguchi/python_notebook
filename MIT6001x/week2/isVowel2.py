def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    
    list = ['a', 'e', 'i', 'o', 'u'];
    return char.lower() in list

print isVowel2('a')