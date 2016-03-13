# x and epsilon int or float, power an int
# epsilon > 0 & power >=1
# returns a float y s.t. y**power is within epsilon of x.
# If such a float does not exist, it returns None

# can't find even powered root of negative number

def findRoot3(x, power, epsilon):

    if x < 0 and power % 2 == 0:
        return None
    
    # consider cases where x is a decimal fraction
    low = min(-1, x)
    high = max(1, x)
    
    # initial guess
    ans = (high+low)/2.0
 
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0 
            
    return ans

answer = findRoot3(25.0, 2, .001)
print answer 
