# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4152219158/m-48204891

def print_all_elements(p):
    for e in p:
        print e

myList = [1, 2, [3, 4]]
# print_all_elements(myList)

# For Loop Structure
# for <name> in <list>:
#     <block>

# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing
    

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country

# For loops automatically assume that <name> refers to the lements in <list>

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(numbers):
    base = 0 
    for n in numbers:
    	answer = base + n 
        base = answer
    return base

#print sum_list([1, 7, 4])
#>>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134

#Instructor version
# def sum_list(p) # p for 'paramater'
#     result = 0
#     for e in p: # e for 'elements'
#     result = result + e
# return result

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.
 
def measure_udacity(p):
    result = 0
    for e in p:
        if e[0] == 'U':
            result += 1
    return result

#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2

# Instructor Version
# def measure_udacity(U):
#     count = 0
#     if e[0] == 'U'
#         count = count + 1
#     return count

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p,value):
    index = -1
    for e in p:
        if e == value:
            index = p.index(value)
    return index
    
#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1

# Instructor Method
# def find_element(p,t):
#     i = 0
#     while i < len(p):
#         if p[i] == t:
#             return i
#         i = i +1
#     return -1
#
# OR
#
# def find_element(p,t):
#     i = 0
#     for e in p:
#         if e == t:
#              return i
#         i = i + 1
#     return -1
#
# 'e' automatically increases as it moves through the parameter

# Index
# <list>.index(<value>)
# if <value> is in the <list>, returns the first position where <value> is
# found in <list>. Otherwise produces an error.

# In
# <value> in <list>
# if <value> is in the <list>, output is True. Otherwise, output is False.
#
# Not In
# <value> not in <list>
# === not <value> in <list>

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(p,t):
	if t in p:
		return p.index(t)
	return -1

#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1

# Instructor Version
# def find_element(p,t):
#     if t in p:
#         return p.indext(t)
#     else:
#         return -1
#
# OR
#
# def find_element(p,t):
#     if t not in p:
#         return -1
#     return p.index(t)