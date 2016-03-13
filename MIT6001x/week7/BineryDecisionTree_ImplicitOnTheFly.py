class binaryTree(object):
    def __init__(self, value):
        self.value = value    # can be any type
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None 
    def setLeftBranch(self, node):
        self.leftBranch = node
    def setRightBranch(self, node):
        self.rightBranch = node
    def setParent(self, parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return self.value

## only to generate the nodes of the tree as needed.
## more efficient than explicit decision trees
## implicit search of a tree, built on the fly

def decisionTreeImplicit( toConsider, avail ):
    '''params arg0 list of lists  [ value, spaceConstraint ]
    return best solution ( totalValue, ( (val, space), (val, space), ... ) )
    '''
    
    # if there's nothing left to consider, or if there's no more room left in here,
    # the result to return is just a value zero. And there's no solution.
    if toConsider == [] or avail == 0:
        result = ( 0, () )
     
    # if available space is NOT enough, this node should be ignored
    elif toConsider[0][1] > avail:
        # examine rest of the stuff toConsider, recursively
        result = decisionTreeImplicit( toConsider[1:],  avail )

    else:
         # if available space is enough, this node is the nextItem to be considered
         # then split it into two branches, call the function recursively for the rest of toConsider
        nextItem = toConsider[0]
        
        # branch 1:  with nextItem
        ( withVal, withItems ) = decisionTreeImplicit( toConsider[1:],  avail - nextItem[1] )    # subtract space
        # add value
        withVal += nextItem[0]
        
        # branch 2: without nextItem
        ( withoutVal, withoutItems )  = decisionTreeImplicit( toConsider[1:],  avail )    # same availability because any space is used
        
        # check which branch has higher totalValue, and take the higher one
        if withVal > withoutVal:
            result = ( withVal,  withItems + ( nextItem, ) )  #  add nextItem to result
        else:
            result =  withoutVal, withoutItems 
            
    return result


## stuff to consider
a = [6, 3]
b = [7, 2]
c = [8, 4]
d = [9, 5]

stuff = [ a , b , c , d ]

(val, taken) = decisionTreeImplicit( stuff, 10 )

print ''
print 'implicit decision search'
print 'value of stuff'
print val
print 'actual stuff'
print taken

