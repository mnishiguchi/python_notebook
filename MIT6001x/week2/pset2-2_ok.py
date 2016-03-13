# -*- coding: utf-8 -*-
'''
Pset2
PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15 points possible)

calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

monthly payment:  must be a multiple of $10 and is the same for all months. 
'''

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

### Test Case 1:
balance = 819
annualInterestRate = 0.18

# initial guess (multiple of 10)
lowestMonthlyPayment = balance / 12
lowestMonthlyPayment = lowestMonthlyPayment - (lowestMonthlyPayment % 10)

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
    
    # balance 1 year later
    remainingBalance = balanceOneYearLater(balance, lowestMonthlyPayment)
    
    # if finish paying
    if remainingBalance <= 0 :
        break
        
    else :
        lowestMonthlyPayment += 10

# the lowest monthly payment that will pay off all debt in under 1 year
print 'Lowest Payment:', lowestMonthlyPayment                                                                                                                                                                    
