def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    
    guess = 1.0  
    print
    print 'start guess', guess  ################
      
    for i in range(100):       
        if abs( guess - f(guess) ) < epsilon:
            return guess
        else:
            guess = f(guess)
        print 'i =', i, 'guess, f(guess) =', guess, f(guess)  ################  
          
    return guess


def babylon(a):
    def test(x):
        return 0.5 * ( (a / x) + x )  
    return test 
             
def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)    

                              
#test
print sqrt(9)