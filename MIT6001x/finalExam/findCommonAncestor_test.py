def findCommonAncestor(a, b):
    while True:
        # if last elems and 2nd last ones are identical
        if a[-1] == b[-1] and a[-2] == b[-2]:
            a.pop()
            b.pop()
        else:
            break 
    return(a, b)   
    
    
    
    
# test
d = [5,4,3,2,1]
g = [6,3,2,1]
print findCommonAncestor(d, g)