# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 19:13:42 2016

@author: Dennis
"""

print("Please enter a string: ");

s = input()

count = 0

for i in range(0 , len(s)):
    if i + 2 > len(s):
        break;
    if (s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b'):
        count += 1;

print ('Number of times bob occurs is: %i' % (count))
