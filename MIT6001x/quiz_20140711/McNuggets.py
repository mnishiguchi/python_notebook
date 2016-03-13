def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n == 0:
        return False
        
    packages = { '20pcs': 0, '9pcs': 0, '6pcs': 0 }
    totalPcs = 0
    remainder = n
    
    if remainder%20 == 0:
        packages['20pcs'] = int(remainder/20)
        remainder -= (20 * packages['20pcs'])
        #print ' remainder',remainder    # debug
    if remainder%9 ==0:
        packages['9pcs'] = int(remainder/9)
        remainder -= (9 * packages['9pcs'])
        #print ' remainder',remainder    # debug
    if remainder%6 == 0:
        packages['6pcs'] = int(remainder/6)
        remainder -= (6 * packages['6pcs'])
        #print ' remainder',remainder    # debug
        
    if remainder >= 20:
        packages['20pcs'] = int(remainder/20)
        remainder -= (20 * packages['20pcs'])
        #print ' remainder',remainder    # debug
    if remainder >= 9:
        packages['9pcs'] = int(remainder/9)
        remainder -= (9 * packages['9pcs'])
        #print ' remainder',remainder    # debug
    if remainder >= 6:
        packages['6pcs'] = int(remainder/6)
        remainder -= (6 * packages['6pcs'])
        #print ' remainder',remainder    # debug
    print packages    # debug
    print ' remainder',remainder
    print 'sum', 20*packages['20pcs']+9*packages['9pcs']+6*packages['6pcs'] 
    return remainder == 0
    
# test
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
       