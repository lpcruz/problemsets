#!/usr/bin/env python
#-*- coding: utf-8 -*-


# TEST: Fibonacci Sequence in Python
# DESC: The Fibonnaci Sequence represents a series of numbers in which each number equals to the sum of the two preceding numbers.
#       The following script takes in a user input as an argument where which it will then output x amount of Fibonacci numbers.
# AUTHOR: Laurence Cruz

# intro
print "Hello there! Welcome to the Python Fibonacci Sequence."

# set the variable for user input
x = raw_input("To Start, how many Fibonnaci numbers do you want to see? Enter Number: ")

# with the user input in place, let's create a function
def fibonacci (n):
    '''Create two variables: a and b then give them values of 0 and 1. Let's make this the base-case.'''
    a = 0
    b = 1

    '''Recursive: Use a variable called 'Temp' to represent a Temporary Variable used to hold the previous value for later.'''
    for i in range(0,n):
        temp = a # temporary variable
        a = b
        b = temp + b

    '''return the object, which in this case is the temporary number that goes through the for loop range'''
    return a

#Output happens here:

for c in range(0,int(x)):
    print (fibonacci(c))

    # NOTE

    # Temporary variable will equal to 0 (which is also a, which will always change every iteration)
    # 0 will equal to 1
    # 1 = 0 + 1
    # Meaning, when we return "a" we are using that value as the "Temporary" variable. In this case, it would be 1.
