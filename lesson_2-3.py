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