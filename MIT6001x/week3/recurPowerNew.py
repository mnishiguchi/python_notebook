# -*- coding: utf-8 -*-
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    
    if exp > 0 and exp % 2 == 0 :
        return recurPowerNew( base * base, exp / 2 )
        
    elif exp > 0 and exp % 2 == 1 :
        return base * recurPowerNew(base, exp - 1)


def test(base):        
    for i in range(10):
        print base, '**', i, '=', recurPowerNew(base,i), '---', base**i
       
test(3) 