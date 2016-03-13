
print 'Please think of a number between 0 and 100!'

# initial range for search
high = 100
low = 0

# hit the midpoint
guess = (high + low) / 2

while(True):
    print('Is your secret number ' + str(guess) + '?'),
    confirm = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    
    if confirm.lower() == 'h':
        high = guess
        guess = (high + low) / 2
    elif confirm.lower() == 'l':
        low = guess
        guess = (high + low) / 2
    elif confirm.lower() == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.'
        
print('Game over. Your secret number was: ' + str(guess))   