class Frob(object):
    """
    form a data structure called a doubly linked list
    
    """
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
# TODO      
# create a doubly linked collection of Frob instances with the property
# all Frobs with names that are alphabetically before a specific Frob's name appear ordered along the "before" link,
# all Frobs with names that are alphabetically after a specific Frob's name appear ordered along the "after" link
# (the exact ordering of the two identical Frobs does not matter)
def insert(atMe, newFrob):
    """
    appropriately inserts newFrob into the linked list that atMe is a part of. 
    
    parameters:
        atMe --  a Frob that is currently part of a doubly linked list
        newFrob  -- a new Frob with no "before" or "after" links to other Frobs
    """
    assert newFrob.getBefore() == None and newFrob.getAfter() == None
    
    def setNode(aFrob, before, after):
        aFrob.setBefore(before) 
        aFrob.setAfter(after)
        
    # ====if atMe and a new Frob are identical====     
    if atMe is newFrob:
        return    # do nothing
        
    # ====if atMe is a new Frob as well==== 
    if atMe.getBefore() == None and atMe.getAfter() == None:
        # compare and decide the order
        if atMe.myName() <= newFrob.myName():
            atMe.setAfter(newFrob)  
            newFrob.setBefore(atMe)  
            return
        else:
            atMe.setBefore(newFrob)  
            newFrob.setAfter(atMe)      
            return
        
    # ====if atMe <= newFrob, move UPWARDS====
    if atMe.myName() <= newFrob.myName():
        cursor = atMe.getAfter()
        
        # if it's end of the list
        if cursor == None:
            newFrob.setBefore(atMe) 
            atMe.setAfter(newFrob) 
            return
            
        # search for the insertion point up to the end of the list
        while True:
            # if insertion point is found
            if cursor.myName() >= newFrob.myName():
                # set newFrob before this cursor
                setNode(newFrob, cursor.getBefore(), cursor)
                # update the one before the cursor
                oneBefore = cursor.getBefore()
                oneBefore.setAfter(newFrob)                
                # update the one at the cursor
                cursor.setBefore(newFrob)
                return
            else:
                # if end of the list
                if cursor.getAfter() == None:
                    break
                else:  # else move up the cursor
                    cursor = cursor.getAfter()
                
        # if the end of the list is reached, set newFrob there
        newFrob.setBefore(cursor)
        # update this other one at the cursor
        cursor.setAfter(newFrob)
        return
              
    #==== if atMe is greater, move DOWNWARDS====
    elif atMe.myName() > newFrob.myName():
        cursor = atMe.getBefore()
        
        # if none before atMe, set newFrob there
        if cursor == None:
            newFrob.setAfter(atMe) 
            atMe.setBefore(newFrob)
            return

        # search until the beginning of the list
        while True:
            # if insertion point is found
            if cursor.myName() <= newFrob.myName():
                # set newFrob after this node
                setNode( newFrob, cursor, cursor.getAfter() )
                # update the one after cursor
                oneAfter = cursor.getAfter()
                oneAfter.setBefore(newFrob)                
                # update the one at cursor
                cursor.setAfter(newFrob)
                return
            else:
                if cursor.getBefore() == None:    # beginning of the list
                    break
                else:   # move down the cursor
                    cursor = cursor.getBefore()
                                              
        # if it's the beginning of the link, set newFrob there
        newFrob.setAfter(cursor)
        # update the one at cursor
        cursor.setBefore(newFrob)
        return
 
## ========test ===============  
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

#for frob in [eric, andrew, ruth, fred, martha]:
#    insert(eric, frob)

#for frob in [eric, andrew, ruth, fred, martha]:
#    print frob.myName(),
#    if frob.getBefore() != None:
#        print 'before:', frob.getBefore().myName(),
#    if frob.getAfter() != None:
#        print 'before:', frob.getBefore().myName()

    