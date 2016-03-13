# helper function provided by mit600
# apply each function in the list to a passed number
# arg[0] : list of function name; arg[1] int or float
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append( L[i] (x) )
    return result
        
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

# test
print applyEachTo([inc, square, halve, abs], -3)


 