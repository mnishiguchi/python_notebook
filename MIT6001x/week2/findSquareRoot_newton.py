# Newton-Raphson

y = int(raw_input('Enter an integer: '))

# precision
epsilon = 0.01

# initial guess
guess = y / 2.0

# repeat until as accurate as epsilon
while abs(guess*guess - y) >= epsilon:
    
    # mathmatical formula to generate better guess for root
    guess = guess - ( ((guess**2) - y) / (2 * guess) )
    print guess
    
print('Square root of ' + str(y) + ' is about ' + str(guess))
