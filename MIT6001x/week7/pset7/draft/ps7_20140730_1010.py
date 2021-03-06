# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

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

#------------------------------------
# TRIGGER BASE CLASS
#------------------------------------
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

#------------------------------------
# WHOLE WORD TRIGGERS
#------------------------------------
class WordTrigger(Trigger):
    '''
    Subclass of Trigger.
    Inherits its evaluate method from Trigger.
    Cannot be instantiated due to being an abstract class.
    '''
    #  constructor
    def __init__(self, word):
        '''takes in a string word as an argument'''
        # inherit from Trigger super class
        Trigger.__init__(self)
        
        # set a trigger word
        self.word = word    
        
    def isWordIn(self, text):
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
            if w.upper() == self.word.upper():
                return True
        return False
    
class TitleTrigger(WordTrigger):
    '''fires alert when a news item's title contains a given word.'''
    # constructor
    def __init__(self, word):
        WordTrigger.__init__(self, word)    # inherit from superclass

    # override
    def evaluate(self, newsStory):
        """
        Params a news item (NewsStory object) 
        Returns True if an alert should be generated for the given word, or False otherwise.
        """ 
        return self.isWordIn( newsStory.getTitle() )
        
class SubjectTrigger(WordTrigger):
    '''fires alert when a news item's subject contains a given word.'''
    # constructor
    def __init__(self, word):
        WordTrigger.__init__(self, word)    # inherit from superclass
        
    # override
    def evaluate(self, newsStory):
        return self.isWordIn( newsStory.getSubject() )
             
class SummaryTrigger(WordTrigger):
    '''fires alert when a news item's Summary contains a given word.'''
    # constructor
    def __init__(self, word):
        WordTrigger.__init__(self, word)    # inherit from superclass
        
    # override
    def evaluate(self, newsStory):
        return self.isWordIn( newsStory.getSummary() )
        
#------------------------------------
# COMPOSITE TRIGGERS
#------------------------------------
class NotTrigger(Trigger):

    def __init__(self, tr):
        '''Param: an instance of a subclass of WordTrigger'''
        # inherit from superclass
        Trigger.__init__(self)
         # the inputted trigger object
        self.tr = tr
         
    def evaluate(self,  newsStory):
        '''Param: a NewsStory object
        Returns: True if the inputted triggers would NOT fire on a newsStory
        '''
        return not self.tr.evaluate(newsStory)

class AndTrigger(Trigger):
    def __init__(self, tr1, tr2):
        '''Param: two instances of subclass of WordTrigger'''
        # inherit from superclass
        Trigger.__init__(self)
        # the inputted trigger objects
        self.tr1 = tr1
        self.tr2 = tr2
         
    def evaluate(self,  newsStory):
        '''Param: a NewsStory object
        Returns: True if both of the inputted triggers would fire on passed newsStory
        '''
        return self.tr1.evaluate(newsStory) and self.tr2.evaluate(newsStory) 

class OrTrigger(Trigger):
    def __init__(self, tr1, tr2):
        '''Param: two instances of subclass of WordTrigger'''
        # inherit from superclass
        Trigger.__init__(self)
        # the inputted trigger objects
        self.tr1 = tr1
        self.tr2 = tr2
         
    def evaluate(self,  newsStory):
        '''Param: a NewsStory object
        Returns: True if either one (or both) of the inputted triggers would fire on passed newsStory
        '''
        return self.tr1.evaluate(newsStory) or self.tr2.evaluate(newsStory) 

#------------------------------------
# PHRASE TRIGGER
#------------------------------------

class PhraseTrigger(Trigger):
    '''This trigger fires when a given phrase is in any of the story's subject, title, or summary. '''   
    def __init__(self, phrase):
        Trigger.__init__(self)    # inherit
        self.phrase = phrase    # trigger phrase
        
    def evaluate(self,  newsStory):
        '''Param: a NewsStory object
        Returns: True if a trigger phrase is in any of the story's subject, title, or summary. '''
        # check if the trigger phrase is in the story's subject, title, or summary
        return self.phrase in newsStory.getSubject() or \
                        self.phrase in newsStory.getTitle() or \
                        self.phrase in newsStory.getSummary()

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    return stories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

