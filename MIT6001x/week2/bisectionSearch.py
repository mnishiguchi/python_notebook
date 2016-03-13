x = int(raw_input('Enter an integer: '))

# accuracy(+/-)
epsilon = 0.00001

# record how many times the program guessed
numGuesses = 0

# current range for search
low = 0.0
high = x    # initial value: user's input

# hit the mid point
ans = (high + low) / 2.0

# repeat same sequence until as accurate as epsilon
while abs(ans**2 - x) >= epsilon:
    
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    
    # if ans is too low, update low
    if ans**2 < x:
        low = ans
        ans = (high + low) / 2.0
        
    # if ans is too high, update high
    else:
        high = ans
        ans = (high + low) / 2.0
    
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))