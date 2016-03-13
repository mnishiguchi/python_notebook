# MIT600 week2
# findCubicRoot_forloop.py

x = int(raw_input('Enter an integer: '))

for ans in range(0, abs(x)+1):  # generate step
    print ans
    if ans**3 == abs(x):        # test&check
        break
    
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
    
else:
    if x < 0:
        ans = -ans
        
    print('Cube root of ' + str(x) + ' is ' + str(ans))      
    print('    ' + str(ans) + '**3' + ' = ' + str(x))