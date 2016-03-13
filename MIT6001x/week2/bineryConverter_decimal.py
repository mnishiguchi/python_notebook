# binaryConverter_decimal.py

x = float(raw_input('Enter a decimal number between 0 and 1: '))

# power
p = 0

# get the value of the power where there is no reminder in the next decimal place right
while ((2**p) * x) % 1 != 0:
    print('Remainder = ' + '(2**'+ str(p) + ' * ' + str(x) + ') - int(' + '2**' + str(p) + ' * ' + str(x) + ')')
    print('          = ' + str( (2**p) * x - int( (2**p) * x) ) )
    
    p += 1

# number to be converted to binary without decimal point    
num = int(x * (2**p))
print ('x * (2**p) = ' + str(x) + ' * ' + '2**' + str(p) + ' = ' + str(num))

# if 0, binary is 0 also
result = ''
if num == 0:
    result = '0'

# conver to binary   
while num > 0:
    result = str(num%2) + result  # next bit
    num = num / 2                 # shift left

# determine correct decimal place   
for i in range(p - len(result)):
    result = '0' + result

# add decimal point
print ''   
print('0.' + result)
