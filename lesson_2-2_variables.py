# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# What is a variable?
#  Variables make it easy to refer to expressions
# What does it mean to assign a value to a variable?
#  States the expression or number that the variable represents
# What is the difference between what the equals = means in math versus in
#   programming?
#   The = does not mean equal in programming. It is an arrow indicating that
#   the value to the right should be assigned to the variable on the left.
# What's the difference between this: 2 + 3 = 5 and this: my_variable = 5?
#   2 + 3 = 5 is an arithmetic expression and its result
#   my_variable = 5 assigns the vlaue 5 to my_variable

# Assignment Statement: Name = Expression

# Variables Quiz
speed_of_light = 299792458.0 #meters per second
cycles_per_second = 2700000000.0 #2.7 GHz
distance_per_cycle = speed_of_light / cycles_per_second
print distance_per_cycle

# You can update the values of a variable as Python moves down the code

cycles_per_second = 2800000000.0 #2.8 GHz
distance_per_cycle = speed_of_light / cycles_per_second
print distance_per_cycle

# Python will keep calculating and updating the value of a variable
days = 7 * 7 # 49
days = 48 # 48
days = days - 1 # 47
days = days - 1 # 46
print days # 46

# Varying Variables Quiz 1
hours = 9 # 9
hours = hours + 1 # 10
hours = hours * 2 # 20
print hours # 20 

# Varying Variables Quiz 2
# minutes = minutes + 1 # No initial value assigned to minutes
# seconds = minutes * 60
# NameError: name 'minutes' is not defined

# Python evaluates the right side first

# Spirit Age Quiz
year = 365 #days
age = year * 29
print age
