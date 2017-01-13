# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def payment(balance, annualInterestRate, monthlyPayment):
    monthlyInterest = annualInterestRate / 12
    loopBalance = balance
    for i in range(12):
        unpaid_balance = loopBalance - monthlyPayment
        newBalance = unpaid_balance * (1 + monthlyInterest)
        loopBalance = newBalance
    if newBalance < 0:
        print("Lowest payment: " + str(monthlyPayment))
    else:
        return payment(balance, annualInterestRate, monthlyPayment + 10)
   
monthlyPayment = 10

payment(4773, 0.2, monthlyPayment)