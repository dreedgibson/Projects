# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 19:13:42 2016

@author: Dennis
"""

print("Please enter a string: ");

s = input()

#Variable Declaration
count_array = []
i_array = []
i = 0;

#Nested while loops to find all instances of letters in alphabetical order
while i < len(s):
    j = 0
    count = 0
    if i + j + 1 > len(s) - 1:
        break;
    while s[i + j + 1] > s[i + j]:
        count = count + 1;
        j += 1;
        if i + j + 2 > len(s):
            break;
    count_array.append(count)
    i_array.append(i) 
    i = i + j + 1;

countmem = 0;

#for loop to find the longest sequence of orders letters
for i in range(0, len(count_array)):
    if i + 1 > len(count_array) - 1:
        break;
    if count_array[i + 1] > count_array[countmem]:
        countmem = i + 1;

#defining the start and ending characters in the provided string
start = int(i_array[countmem])
end = int(i_array[countmem] + count_array[countmem] + 1)

#printing the longest sequence of characters in the given string
print("Longest substring in alphabetical order is: ", s[start: end])

