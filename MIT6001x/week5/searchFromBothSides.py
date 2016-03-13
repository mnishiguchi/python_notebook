
def linearSearch(L, e):
    '''
    arg0 list of positive int, sorted by ascending order
    arg1 int to search for
    return True if e is in L
    '''
    # probe the list from left to right
    # if e is greater than value at current cursor, return False
    
    for i in range(len(L)):
        print i,  ## debug
        if L[i] == e:
            return True
        if L[i] > e:  ## consider not found
            return False
    return False

def searchFromBothSides(L, e):
    '''
    arg0 list of positive int, sorted by ascending order
    arg1 int to search for
    return True if e is in L
    '''
    # probe the list from both sides 
    # if e is greater than value at current cursor, return False
    
    size = len(L)
    for i in range(size):
        print i,  ## debug
        if L[size-i-1] == e or L[i] == e:  ## probe the list from both sides 
            return True
        if L[size-i-1] < e or L[i] > e:    ## consider not found
            break
    return False
    
##-----------------------------------------------------------------------------    
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

e = 39

print L
print linearSearch(L,e)
print searchFromBothSides(L, e)