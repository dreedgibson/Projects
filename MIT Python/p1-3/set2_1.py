# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def remain(balance, annualInterestRate, monthlyPaymentRate, numbercalls):
    monthlyInterest = annualInterestRate / 12
    printBalance = round(balance,2)
    if numbercalls == 12:
        print("Remaining balance: " + str(printBalance))
        return 0
    monthlyPayment = monthlyPaymentRate * balance
    unpaid_balance = balance - monthlyPayment
    newBalance = unpaid_balance * (1 + monthlyInterest)
    numbercalls += 1
    return remain(newBalance, annualInterestRate, monthlyPaymentRate, numbercalls)
   
numbercalls = 0

remain(balance, annualInterestRate, monthlyPaymentRate, numbercalls)