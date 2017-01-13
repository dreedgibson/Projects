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

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    dotprod = 0
    for i in range(len(listA)):
        dotprod += listA[i] * listB[i]
    return dotprod

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    for i in range(len(L)):
        L[i].reverse()
    L.reverse()
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    d3 = {}
    d4 = {}
    for key in d1:
        if key in d2:
            d3[key] = f(d1[key], d2[key])
        else:
            d4[key] = d1[key]
    for key in d2:
        if not key in d1:
            d4[key] = d2[key]

    return(d3, d4)
    
def f(i):
    return i + 2
def g(i):
    return i > 5
    
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    i = 0
    while i < len(L):
        if g(f(L[i])) is False:
            L.remove(L[i])
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
    
    try:
        return max(L)
    except ValueError:
        return -1

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
        return aList
    elif type(aList[0]) == list:
        return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])
            
L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
L1 = flatten(L)
print(L1)
