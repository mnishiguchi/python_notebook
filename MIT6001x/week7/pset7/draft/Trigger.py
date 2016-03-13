## Pset7  Problem 2
## Implement a word trigger abstract class, WordTrigger

import string

#======================
# Part 1
# Data structure design
#======================

class NewsStory(object):
    '''
    Assume that parsing is already done
    contains  information for a news story
    '''
    # constructor
    def __init__(self, guid, title, subject, summary, link):     
        '''all params are of string type'''
        # instance variables
        self.guid  = guid  # globally unique id
        self.title  = title 
        self.subject = subject
        self.summary = summary
        self.link = link
        
    # instance getter methods
    def getGuid(self):
        return self.guid        
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link



#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Baseclass
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    '''
    Subclass of Trigger.
    Inherits its evaluate method from Trigger.
    Cannot be instantiated due to being an abstract class.
    '''
    #  constructor
    def __init__(self, word):
        '''takes in a string word as an argument'''
        Trigger.__init__(self)    # inherit from Trigger super class
        
        # set a trigger word
        self.word = word    
        
    #  one new method
    def isWordIn(self, text):
        '''Takes in one string argument text; not case-sensitive.
        Returns True if the whole word word is present in text.
        '''
        assert type(text) == str
        # To deal with punctuation
        # replaces every punctuation mark in a string with a space.
        for punc in string.punctuation:
            text.replace( punc, ' ' )
            
        words = text.split(' ')    # list of words
        
        # check if trigger word exists in the list
        for w in words:
            if w.upper() == self.word.upper():
                return True
        return False
    
    # override superclass
    def evaluate(self, text):
        """
        Param text a string
        Returns True if an alert should be generated for the given word, or False otherwise.
        """ 
        return self.isWordIn(text)
        
        
# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    '''fires alert when a news item's title contains a given word.'''
    # constructor
    def __init__(self, word):
        WordTrigger.__init__(self, word)    # inherit from superclass
    
    def evaluate(self, article):
        
        return self.evaluate(article.getTitle())


        
## test
test = NewsStory('my ID', 'my Title', 'my Subject', 'some long summary', 'www.mnishiguchi.com')
print type(test.getTitle())
trig = TitleTrigger('title' )
trig.evaluate(test)