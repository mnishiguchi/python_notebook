def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    
    guess = 1.0  
    print
    print 'start', guess  ################  
      
    for i in range(100):

        print i, 'before', guess, f(guess)  ################        
        if abs( guess - f(guess) ) < epsilon:
            return guess
        else:
            guess = f(guess)
        print i, 'after', guess, f(guess)  ################  
          
    return guess

            
#test
def f(n):
    '''make hale then plus 0.25'''
    return n * 0.5 + .25


print fixedPoint(f, 0.000000000005)