# Lesson 2.3: Procedures (Input -> Function -> Output)

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# How do functions take input and produce output and what role do the keywords 
# def and return have to do with this process?

# What is a function?

# How do you make a function?
# Functions need a return line if they are going to produce anything

def sum(a, b):
	a = a + b
	return a

print sum(2, 123)
# Result 125

print sum("alpha", "beta")
# Result alphabeta

# How do you use a function?
# <function>(<input>, <input>, ...)
# Number of inputs/operands/arguments must match the number in the function

def rest_of_string(s):
	return s[1:]

print rest_of_string("audacity") # s = "audacity"
# Result: udacity

def inc(n):
	return n+1 # number + 1

print inc(10) # n = 10
# Result: 11

# When should you write a function?

# Why are functions so valuable?

# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).

# Mine
def square(a):
    b = a * a
    return b

# Instructor
def square(n):
	return n * n

print square(5)
# Result: 25

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.

def sum3(a,b,c):
    return a + b + c

print sum3(1,2,3)
# Result: 6

print sum3(93,53,70)
# Result: 216

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(string1,string2):
    return string1 + string2 + string2 + string1

print abbaize('a','b')
# Result: abba

print abbaize('dog','cat')
# Result: dogcatcatdog