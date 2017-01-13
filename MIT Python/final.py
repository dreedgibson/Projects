# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:30:06 2016

@author: Dennis
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    
    if int(us_num) <= 10:
        return trans[str(int(us_num))]
    elif int(us_num) >= 20:
        if int(us_num) % 10 == 0:
            return trans[str(int(us_num) // 10)] + ' ' + trans['10']
        else:
            return trans[str(int(us_num) // 10)] + ' ' + trans['10'] + ' ' + trans[str(int(us_num) % 10)]
    else:
        return trans['10'] + ' ' + trans[str(int(us_num) % 10)]

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest_run = 0
    current_run = 1
    location = 0
    
    try:
        for i in range(len(L)):
            if L[i] >= L[i+1]:
                current_run += 1
            elif L[i] < L[i+1]:
                if current_run > longest_run:
                    longest_run = current_run
                    location = i - current_run
                current_run = 0
    except IndexError:
        if current_run > longest_run:
            longest_run = current_run
            location = len(L) - longest_run - 1
        current_run = 1
    
    try:
        for i in range(len(L)):
            if L[i] <= L[i+1]:
                current_run += 1
            elif L[i] > L[i+1]:
                if current_run > longest_run:
                    longest_run = current_run
                    location = i - current_run
                current_run = 0
    except IndexError:
        if current_run > longest_run:
            longest_run = current_run
            location = len(L) - longest_run - 1
    
    if location < 0:
        location = 0
    end = location + longest_run
    if end == len(L) - 1:
        end += 1
    
    return sum(L[location:end])


## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if not (status == 'citizen' or status == 'legal_resident' or status == 'illegal_resident'):
            raise ValueError('Status must be "citizen", "legal_resident", or "illegal_resident"')
        else:
            self.status = status
    def getStatus(self):
        """
        Returns the status
        """
        return self.status
        
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Lecturer.lecture(self, stuff)
    def lecture(self, stuff):         
        return 'It is obvious that ' + Lecturer.lecture(self, stuff) 
        

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def gpoly_func(x):
        k = len(L) - 1
        if len(L) == 1:
            return L[0]
        else:
            return L[0] * x ** k + general_poly(L[1:])
    return gpoly_func(x)

L = [1, 2, 3, 4, 5, 6, 7]
x = 100
print(general_poly(L))

