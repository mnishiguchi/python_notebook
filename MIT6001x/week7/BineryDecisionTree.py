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


## make a decision tree
## for efficiency should really generate on the fly, 
## but here will build and then search

## build a binery decision tree
def buildDTree(sofar, todo):
    '''build a tree of all the possible choices
    params arg0 empty list([]) , arg1 a list of elements to consider
    list element can be of any type
    return binaryTree object'''
    
    # if nothing to consider
    if len(todo) == 0:    # base case
        # just return a node with no child
        return binaryTree(sofar)
   
    #  else create a node two children (two options)
    else:
        withelt = buildDTree( sofar + [ todo[0] ],  todo[1:] )    # node ( sofar + 1elem vs remainder )
        withoutelt = buildDTree( sofar,  todo[1:] )    # node ( sofar + remainder )
        
        here = binaryTree(sofar)    # create a new node( sofar )
        here.setLeftBranch(withelt)    # set left child ( with elem added )
        here.setRightBranch(withoutelt)    # set right child (without )
        return here


def DFSDTree(root, valueFcn, constraintFcn):
    '''
    params valueFcn function to evaluate value,  function to ensure constraint is met
    return best node (best option)
    '''
    stack = [root]
    best = None
    visited = 0
    
     # repeat until stack is empty
    while len(stack) > 0:
        visited += 1    # update counter
        
        # ensure that this node pass the constraint
        if constraintFcn( stack[0].getValue() ):
            
            # if first time, this is node is the best one
            if best == None:
                best = stack[0]
                print best.getValue()
                
            # if this node has a greater total value than current best does, this node is the best one
            elif valueFcn( stack[0].getValue() ) > valueFcn( best.getValue() ):
                best = stack[0]
                print best.getValue()
                
            # pop the stack    
            temp = stack.pop(0)
            # if not None,  push Right child into stack
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            # if not None,  push Left child into stack
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
       
        # elemination
        else:
            stack.pop(0)
            
    print 'visited', visited
    return best


def BFSDTree(root, valueFcn, constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                print best.getValue()
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                print best.getValue()
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print 'visited', visited
    return best  

a = (6,3)
b = (7,2)
c = (8,4)
d = (9,5)

## build a decision tree
treeTest = buildDTree( [], [a,b,c,d] )

## value function
def sumValues(lst):
    '''return int that is a sum of values'''
    vals = [e[0] for e in lst]
    return sum(vals)
    
## constraint function
def sumWeights(lst):
    wts = [e[1] for e in lst]
    return sum(wts)
    
def WeightsBelow10(lst):
    '''return True if constraint is met'''
    return sumWeights(lst) <= 10

def WeightsBelow6(lst):
    '''return True if constraint is met'''
    return sumWeights(lst) <= 6


## search for a best decision
print ''
print 'DFS decision tree'
foobar = DFSDTree( treeTest, sumValues, WeightsBelow6 )
print foobar.getValue()

print ''
print 'BFS decision tree'
foobarnew = BFSDTree( treeTest, sumValues, WeightsBelow6 )
print foobarnew.getValue()

