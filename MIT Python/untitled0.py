# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:21:33 2016

@author: Dennis
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0 
    exponent1 = 1
    while True:
        if not (base ** exponent <= num and base ** exponent1 >= num):
            exponent += 1
            exponent1 += 1
        if base ** exponent <= num and base ** exponent1 >= num:
            break
    
    if abs(base ** exponent - num) > abs(base ** exponent1 - num):
        return exponent1
    else:
        return exponent

closest_power(4,62)