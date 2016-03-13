#
# use an iterative or recursive solution to this problem
# uses simple arithmatic operators and conditional testing.

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    return the largest power of b such that b to that power is still less than or equal to x.
    return an integer answer
    '''

    # initialize log equal to x
    ans = 0
    
    # repeat division x/b until x >= 1
    while True:
        x /= b
        if x >= 1:
            ans += 1
        else:
            break    
    return ans


##### test ######    
# Log_base(x) = exponent
import math
testSuite ={
    (27, 3):3,
    (26, 3):2,
    (28, 3):3,
    (4, 16):0,
    (2, 20):0,
    (44, 2):5,
    (139, 2):7,
    (8, 7):1
    }

for (x, base) in testSuite.keys():
    print
    print 'x:',x,'base:',base,
    myAnswer = myLog(x, base)
    correctAnswer = testSuite[(x, base)]
    if correctAnswer == myAnswer:
        print ''
    else:
        print '*******Fail*******'
        
    print '\tmyAnswer:  ', myAnswer,
    print '\tcorrectAnswer:  ', correctAnswer,
    print '\tPython: ', math.log(x, base)