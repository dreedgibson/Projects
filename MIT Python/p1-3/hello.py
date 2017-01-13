# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 19:13:42 2016

@author: Dennis
"""

print("Please enter a string: ");

s = input()

count = 0

for i in range(0 , len(s)):
    if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        count = count + 1;

print ('Number of vowels: %i' % (count))
