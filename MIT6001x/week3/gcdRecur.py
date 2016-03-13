def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    #------------Euclid's algorithm---------------------
    # If b = 0, then the answer is a
    # Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    #---------------------------------------------------

    # If b = 0, then the answer is a
    if min(a, b) == 0:
        return max(a, b)
        
    # Otherwise, gcd(a, b) is the same as gcd(b, a % b)    
    else:
        return gcdRecur(b, a % b)

#test    
print gcdRecur(345, 444)    