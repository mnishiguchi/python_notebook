x = int(raw_input('Enter an integer: '))

# precision
epsilon = 0.01

# value by which ans increments each step
step = epsilon**2

# storages
numGuesses = 0
ans = 0.0

# repeat guess & check within range
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
    
print('numGuesses = ' + str(numGuesses))

# check if ans is accurate to expectation
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))
