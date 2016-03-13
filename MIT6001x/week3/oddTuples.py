def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
    # then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple')
    newTuple = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            newTuple += (aTup[i],)
    return newTuple
    
#test
aTup = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(aTup)
