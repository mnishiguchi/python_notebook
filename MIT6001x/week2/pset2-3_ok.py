# -*- coding: utf-8 -*-
'''
Pset2
PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

find the smallest monthly payment to the cent such that we can pay off the debt within a year.

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
'''

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

### Test Case 1:
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = round(annualInterestRate / 12.0, 2)

# set a range for search
low = balance / 12                                        # no interest
high = (balance * (1 + monthlyInterestRate)**12) / 12.0   # max interest

# initial guess
monthlyPayment = round((high + low) / 2, 2)
print 'initial guess', monthlyPayment
print ''

def balanceOneYearLater(balance, monthlyPayment) : 
    '''
    calculate balance of one year later based on passed monthly payment(fixed)
    return balance
    '''
  
    for i in range(1, 12+1) :
        # Update the outstanding balance by removing the payment, then charging interest on the result.
        balance = (balance - monthlyPayment) + (balance - monthlyPayment) * annualInterestRate / 12.0
        balance = round(balance, 2)
        
    return balance
    
# test  
while True :
    
    print 'low = ', low ,' high = ', high
    print 'monthlyPayment = ', monthlyPayment
    print ''
    
    # balance 1 year later
    remainingBalance = balanceOneYearLater(balance, monthlyPayment)
    print 'remainingBalance', remainingBalance
    
    # if paid too little, update low
    if remainingBalance > 0 :
        low = monthlyPayment
        monthlyPayment = (high + low) / 2.0
       
    # if paid too much, update high
    elif remainingBalance < 0 :
        high = monthlyPayment
        monthlyPayment = (high + low) / 2.0
        
    # if remainingBalance is 0.0, done!
    else :
        break   
                      
# the lowest monthly payment that will pay off all debt in under 1 year
print 'Lowest Payment:', round(monthlyPayment, 2)                                                                                                                                                                  
