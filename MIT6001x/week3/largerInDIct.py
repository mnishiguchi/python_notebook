def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    # helper to sum len in the list
    def getSum(aList):
        #counter
        ctr = 0
        #iterate over each str count up length
        for x in aList :
            if type(x) == str:
                ctr += len(x)
            elif type(x) == int or type(x) == float :
                 ctr += 1
        return ctr
        
    # count total word lengths in each key's value
    # and swap value with result
    for key in aDict :
        aDict[key] = getSum( aDict[key] )
    
    # check the largest
    largest = 0
    winner = None
    for i in aDict :
        if largest <= aDict[i] :
            largest = aDict[i]
            winner = i
    return winner
       
# test
dict1 = { 'a': ['aardvark'],'b': ['baboon'], 'c': ['coati'],'d': ['donkey', 'dog', 'dingo'] }
dict2 ={'m': []}
print 'The winner is ' + str(biggest(dict2))