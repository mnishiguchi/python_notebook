# -*- coding: utf-8 -*-
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = min(a, b)

    while test > 1 :
        # if found, answer it
        if a % test == 0 and b % test == 0:
            return test
            
        # continue test 
        else:    
            test = test - 1  
            
    # if not found, answer is 1
    return 1

#test    
print gcdIter(9, 12)
    