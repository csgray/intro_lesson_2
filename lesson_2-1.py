# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

print 3
print 1 + 1

# "What is Programming?" vocabulary
# computer: a universal machine that can be programmed to do any computation
# program: what tells the computer what steps to take
# precise sequence of steps: series of instructions to accomplish a task
# computation: 
# high-level language: input that works through an interpreter and not on the
#   computer directly
# input: programs that we write
# interpreter: executes our programs on the computer

print 52 * 3 + 12 * 9
print (52 * 3) + (12 * 9)
print 52 * (3 + 12) * 9
print 365 * 24 * 60 * 60 # seconds in a year

# First Programming Quiz
print 7 * 7 * 24 * 60

# Reasons We Don't Use Natural Languages
# ambiguity: different people can interpret the same sentence to mean different
#   things, but we want computers to interpret things the same way every time
# verbosity: takes too many words to detail every step

# print 2 + 2 +
# We can figure out what that means, but Python produces a syntax error

# Backus-Naur Form
# <non-terminal> -> replacement
# keep going until everything is a terminal

# Python Grammar for Arithmetic Expressions
# Expression -> Expression Operator Expression
# Expression -> Number
# Expression -> ( Expression )
# Operator -> +
# Operator -> *
# Number -> 0,1,...

# Speed of Light
print 299792458 * 100 * 1.0/1000000000

# Integer Division
# Python ignores the decimal (remainder) when you divide an integer by another
# integer