# -*- coding: utf-8 -*-

# calculates the exponential baseexp by simply using successive multiplication.
# should compute base**exp by multiplying base times itself exp times
# Your code must be iterative - use of the ** operator is not allowed.

#    take in two values - base can be a float or an integer; 
#    exp will be an integer ≥ 0. return one numerical value.

def iterPower(base, exp) :
    if exp == 0:
        return 1
        
    result = base
    while exp > 1 :
        result = result * base
        exp = exp - 1
    return result
    
def test():        
    for i in range(10):
        print '2**', i, ':', iterPower(3,i)
        
test()       
        