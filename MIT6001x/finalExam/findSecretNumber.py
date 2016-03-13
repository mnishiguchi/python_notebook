def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    # initial guess
    guess = 1
    
    # if the initial guess is correct
    if isMyNumber(guess) == 0:                       # 1 => 0
        return guess
    
    # keep on guessing
    while True:
        sign = isMyNumber(guess)
        # if guess is correct
        if sign == 0:
            break
        # if guess is too small
        if sign == -1:
            # double it
            guess *= 2
        # if guess is too large
        else:
            # decrement by one
            guess -= 1
            
    return guess