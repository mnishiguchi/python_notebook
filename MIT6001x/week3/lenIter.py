def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    
    Write an iterative function, lenIter,
    which computes the length of an input argument (a string),
    by counting up the number of characters in the string.
    '''
    ctr = 0
    temp = ''
    
    # compare passed str with temp
    while temp != aStr:
        
        # append a letter one by one
        temp = temp + aStr[ctr]
        
        # count up
        ctr = ctr + 1
    
    return ctr
    
#test
aStr = 'christineNishiguchi'
print lenIter(aStr), '---', len(aStr)