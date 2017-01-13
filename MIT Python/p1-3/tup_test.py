# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:30:54 2016

@author: Dennis
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    oddtup = ()
    for t in range(len(aTup)):
        if t % 2 == 0:
            oddtup = oddtup + (aTup[t],)
    return oddtup

tup = ()
tup = oddTuples((1, 0, 9, 9, 11, 14, 11))
print(tup)