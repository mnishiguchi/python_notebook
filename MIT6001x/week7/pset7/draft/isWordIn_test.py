import string

#  one new method
def isWordIn(self, text):
        '''Takes in one string argument text; not case-sensitive.
        Returns True if the whole word word is present in text.
        '''
        assert type(text) == str
        
        # create a list of punctuation signs
        puncList = [ string.punctuation[i] for i in range( len(string.punctuation) ) ]
        
        # replaces every punctuation mark in a string with a space.
        for punc in puncList:
            text = text.replace( punc, ' ' )    
        words = text.split(' ')    
        # check if trigger word exists in the list
        for w in words:
            if w.upper() == word.upper():
                return True
        return False
        
def isWordIn1(self, text):
        '''Takes in one string argument text; not case-sensitive.
        Returns True if the whole word word is present in text.
        '''
        assert type(text) == str
        
        # replaces every punctuation mark in a string with a space.
        for punc in  [ string.punctuation[i] for i in range( len(string.punctuation) ) ]:
            t = text.replace( punc, ' ' )    
        words = t.split(' ')    
        
        # check if trigger word exists in the list
        for w in words:
            if w.upper() == word.upper():
                return True
        return False
                
## test         
(word, text) =  'OFT', 'Koala bears!are s!oft and cud!dly'        
print isWordIn(word, text)
print isWordIn1(word, text)