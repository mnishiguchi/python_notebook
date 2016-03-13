
# 6a + 9b + 20c = n

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # test 0
    #----------------------
    if n == 0:
        return False
        
    # test 1 : modulo == 0
    #----------------------
    
    # initialize        
    a = 0  #  6pcs
    b = 0  #  9pcs
    c = 0  # 20pcs
    remainder = n
    print remainder
    if n % 6 == 0:
        a = int(remainder/6)
        return True
    if n % 9 ==0:
        b = int(remainder/9)
        return True
    if n % 20 == 0:
        c = int(remainder/20)
        return True
    
        
    # test 3
    #----------------------    
    # initially max num of 9pcs and then decrement num
    
    # initialize        
    a = 0  #  6pcs
    b = 0  #  9pcs
    c = 0  # 20pcs
    remainder = n
    print remainder    
    while c >= 0 :       
        if n >= 20:
            c = int(remainder/20 )
            remainder -= 20 * c
        if n >= 9:
            b = int(remainder/9 )
            remainder -= 9 * b
        if n >= 6:
            a = int( remainder/6 )
            remainder -= 6 * a
        print 'abc:', a, b, c
        
        if 6*a + 9*b + 20*c == n:
            return True
        else:
            c -= 1     
                
    # test 3
    #----------------------    
    # initially max num of 9pcs and then decrement num
    
    # initialize        
    a = 0  #  6pcs
    b = 0  #  9pcs
    c = 0  # 20pcs
    remainder = n
    print remainder    
    while b >= 0 :       
        if n >= 9:
            b = int(remainder/9 )
            remainder -= 9 * b
        if n >= 20:
            c = int(remainder/20 )
            remainder -= 20 * c
        if n >= 6:
            a = int( remainder/6 )
            remainder -= 6 * a
        print 'abc:', a, b, c
        
        if 6*a + 9*b + 20*c == n:
            return True
        else:
            b -= 1     
 
           
    # test 4
    #----------------------    
    # initially max num of 9pcs and then decrement num
    
    # initialize        
    a = 0  #  6pcs
    b = 0  #  9pcs
    c = 0  # 20pcs
    remainder = n
    print remainder    
    while c >= 0 :
        if n >= 20:
            c = int(remainder/20 )
            remainder -= 20 * c
        if n >= 6:
            a = int( remainder/6 )
            remainder -= 6 * a                   
        if n >= 9:
            b = int(remainder/9 )
            remainder -= 9 * b
        print 'abc:', a, b, c
        
        if 6*a + 9*b + 20*c == n:
            return True
        else:
            c -= 1 
            
    # test 5
    #----------------------    
    # initially max num of 9pcs and then decrement num
    
    # initialize        
    a = 0  #  6pcs
    b = 0  #  9pcs
    c = 0  # 20pcs
    remainder = n
    print remainder    
    while a >= 0 :
        if n >= 6:
            a = int( remainder/6 )
            remainder -= 6 * a 
        if n >= 20:
            c = int(remainder/20 )
            remainder -= 20 * c                 
        if n >= 9:
            b = int(remainder/9 )
            remainder -= 9 * b
        print 'abc:', a, b, c
        
        if 6*a + 9*b + 20*c == n:
            return True
        else:
            a -= 1                 

    # test 6
    #----------------------    
    # initially max num of 9pcs and then decrement num
    
    # initialize        
    a = 0  #  6pcs
    b = 0  #  9pcs
    c = 0  # 20pcs
    remainder = n
    print remainder    
    while a >= 0 :
        if n >= 6:
            a = int( remainder/6 )
            remainder -= 6 * a         
        
        if n >= 9:
            b = int(remainder/9 )
            remainder -= 9 * b
        if n >= 20:
            c = int(remainder/20 )
            remainder -= 20 * c
                  

        print 'abc:', a, b, c
        
        if 6*a + 9*b + 20*c == n:
            return True
        else:
            a -= 1                     
                        
                            
                                    
    return False          
        
        
        
        
        
    
###### test #####
testSuite = [
    (236, True),
    (146, True),
    (17, False),
    (45, True),
    (133, True),
    (28, False),
    (239, True),
    (16, False),
    (32, True),
    (62, True),
    (1, False)
    ]

for (k, v) in testSuite:
    print
    print '----------- n=',k, '-------------------------------'
    myAnswer = McNuggets(k)

    if v != myAnswer:
        print '*** FAIL ***'
    else:
        print 'OK'        
    print 'myAnswer:', myAnswer,'\tcorrectAnswer:'  ,v
       