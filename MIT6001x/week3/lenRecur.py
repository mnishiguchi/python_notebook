def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    
    write a recursive function
    Hint: String slicing may be useful in this problem...
    '''
    
    # if str is empty, length is 0
    if aStr == '':
        return 0
        
    # else, length is 1 + length of the rest of the string    
    return 1 + lenRecur(aStr[1:]) 
       
#test
aStr = 'christineNishiguchi'
print lenRecur(aStr), '---', len(aStr)