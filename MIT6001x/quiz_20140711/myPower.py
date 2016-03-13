def myPower(n, x):
    if n==0 or x==0:
        return 0
        
    result = 1
    for i in range(x):
        result *= n
    return result

n = 4
x = 2    
print n,'**',x,'myPower', myPower(n, x)    
print n,'**',x, 'Python', n**x 