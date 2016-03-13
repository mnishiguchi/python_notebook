## Pset7  Problem 1
## class NewsStory

class NewsStory(object):
    '''Assume that parsing is already done
    contain  information for a news story'''
    # constructor
    def __init__(self, guid, title, subject, summary, link):     
        '''all params are of string type'''
        # instance variables
        self.guid  = guid  # globally unique id
        self.title  = title 
        self.subject = subject
        self.summary = summary
        self.link = link
        
    # instance methods
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