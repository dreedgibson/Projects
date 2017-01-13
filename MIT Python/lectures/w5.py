# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:03:53 2016

@author: Dennis
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
    
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
    
    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals
    
    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """returns length of the set"""
        count = 0
        for elt in self.vals:
            count += 1
        return count
    
    def intersect(self, other):
        s1 = intSet()
        for i in self.vals:
            if i in other.vals:
                s1.insert(i)
        return s1

def genPrimes():
    p =[] #prime list
    x = 2
    while True:
        count = 0
        for elt in p:
            if (x % elt) != 0:
                count += 1
        if count == len(p):
            p.append(x)
            yield x
            x += 1
        else:
            x += 1

y = genPrimes()
y.__next__()
