# binaryConverter.py

n = int(raw_input('Enter an integer: '))

# remember positive or negative
if n < 0:
    isNeg = True
    n = abs(n)
else:
    isNeg = False

# storage of result, initialize as empty str
result = ''

# if 0, binary is 0 also
if n == 0:
    result = '0'

# calculate binary from 2**0 to left       
while n > 0:
    result = str(n % 2) + result  # each bit's value : modulo 2
    n = n / 2                     # shift left
    
if isNeg:
    result = '-' + result
    
print result
