# Assume that testList = [1, -4, 8, -9]
testList = [1, -4, 8, -9]

# helper function provided by mit600
# apply a function to each element of a list
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
# calculater        
def absSquare(a):
    return ( abs(a) )**2

applyToEach(testList, absSquare) 

#### Target result: [1, 16, 64, 81]

# print result
print testList     