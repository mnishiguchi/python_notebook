# -*- coding: utf-8 -*-
'''
Pset2
PROBLEM 1: PAYING THE MINIMUM  (10 points possible)

Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required by the credit card company each month.

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

# balance: the outstanding balance on the credit card
# annualInterestRate: annual interest rate as a decimal
# monthlyPaymentRate: minimum monthly payment rate as a decimal


###Test Case 1
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


totalPaid = 0.0

for i in range(1, 12+1) :
    # Compute the monthly payment, based on the previous month’s balance.
    monthlyPayment = balance * monthlyPaymentRate
    monthlyPayment = round(monthlyPayment, 2)
    
    # Update the outstanding balance by removing the payment, then charging interest on the result.
    balance = (balance - monthlyPayment) + (balance - monthlyPayment) * annualInterestRate / 12.0
    balance = round(balance, 2)
    
    # Output the month, the minimum monthly payment and the remaining balance.
    print 'Month:', i
    print 'Minimum monthly payment:', monthlyPayment                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    print 'Remaining balance:', balance
    
    # Keep track of the total amount of paid over all the past months so far.
    totalPaid += monthlyPayment
    
print 'Total paid:', round(totalPaid, 2)
print 'Remaining balance:', balance                                                                                                                                                                            
