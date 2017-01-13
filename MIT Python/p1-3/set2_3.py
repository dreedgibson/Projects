# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def payment(balance, annualInterestRate, lowerbound, upperbound):
    """
    payment takes in a balance and an annual interest rate and calculates
    the minimum monthly payments to pay off the balance in full in 1 year
    """
    epsilon = 0.1
    monthlyInterest = annualInterestRate / 12
    monthlyPayment = (lowerbound + upperbound) / 2
    loopBalance = balance
    
    #change the value inside of range to set the number of months to payoff
    #ie 24 is 2 years 18 is 18 months etc.
    
    for i in range(60):
        unpaid_balance = loopBalance - monthlyPayment
        newBalance = unpaid_balance * (1 + monthlyInterest)
        loopBalance = newBalance
    if abs(balance - (balance - newBalance)) < epsilon:
        print("Lowest payment: " + str(round(monthlyPayment,2)))
        return 0
    elif newBalance < 0:
        return payment(balance, annualInterestRate, lowerbound, monthlyPayment)
    else:
        return payment(balance, annualInterestRate, monthlyPayment, upperbound)
  
#change only these two values, 
balance = 213000
annualInterestRate = 0.04375
 
#these are predefined in order to give a quicker solution 
lowerbound = balance / 60
upperbound = (balance * (1 + (annualInterestRate/12)) ** 60) / 60

payment(balance, annualInterestRate, lowerbound, upperbound)