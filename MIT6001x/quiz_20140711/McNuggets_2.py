def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 6*a + 9*b + 20*c == n:
                    return True              
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
       