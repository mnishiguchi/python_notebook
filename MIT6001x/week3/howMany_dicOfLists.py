def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # extract values(lists) from aDict
    values = aDict.values()
    
    #counter
    ctr = 0
    
    for list in values :
        ctr += len(list)
        
    return ctr
        
# test
aDict = { 'a': ['aardvark'],
          'b': ['baboon'],
          'c': ['coati'],
          'd': ['donkey', 'dog', 'dingo'] }
          
print howMany(aDict)