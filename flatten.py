#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time

# TEST: Flatten in Python
# DESC: In Ruby, the 'Flatten' method allows you to convert a multi-dimensional array into a single-dimensional array.
# AUTHOR: Laurence Cruz

# intro
print "Hello there! Welcome to the Python version of Flatten"

def flatten():
    '''Create an array that has (3) arrays within it. We give it a variable called my_list'''
    my_list = [[1,2,3],[4,5,6],[7,8,9]]

    #Present user with list

    print "Here is your list: " + str(my_list)
    print "Now let's Flatten this"

    '''In Python, there's a sum method that essentially joins together values'''

    the_flattened_list = sum(my_list,[])

    #sleep for a bit - for the sake of suspense, I guess? 
    time.sleep(3)
    print "Here is your Flattened List: " + str(the_flattened_list)

flatten()
