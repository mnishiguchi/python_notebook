# -*- coding: utf-8 -*-
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    
    if exp == 1 :
        return base
        
    else :    
        return base * recurPower(base, exp-1)


def test(base):        
    for i in range(10):
        print base, '**', i, ':', recurPower(base,i), '  ', base**i
       
test(2) 