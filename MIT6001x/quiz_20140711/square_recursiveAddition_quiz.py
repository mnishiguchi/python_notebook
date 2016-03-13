def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    '''add up x n times recursively'''
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

# test
for i in range(0,10):    
    print i,':',Square(i)