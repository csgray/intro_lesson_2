# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3 # True
print 21 < 3 # False. 21 is greater than 3.
print 7 * 3 < 21 # False. They are equal.
print 7 * 3 != 21 # False. They are equal.
print 7 * 3 == 21 # True

# The equality comparison is done using == and not = because = means assignment

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1 # True
print 1 > 2 # False
print 5 < 20 # True
print 100 < 19 # False


print "Example 2: Equality and non-equality comparisons"
print 5 == 5  # True
print "hello" == "hello" # True
print 5 == 10 # False
print 5 == '5' # False (integer vs string)
print 7 != 10 #True
print 7 != 7 # False


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20: 
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"

# if <TestExpression>:
#	<Block>

def absolute(x):
	if x < 0:
		x = -x
	return x

print absolute(-1)
print absolute(2)

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(x,y):
	if x > y:
		return x
#	if x < y:
#		return y # This resulted in 'None' with equal values
	else: # Replacing last 'if' with this fixed it
		return y

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
	return name[0] == 'D'

print is_friend('Diane')
# Result: True

print is_friend('Fred')
# Result: False

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
	return name[0] == 'D' or name[0] == 'N'

# If the first expression evaluates to True, the value is True and the second
# expression is not evaluated.
# If the first expression evaluates to False, the value is the value of the
# second expression.

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# Mine
def biggest(x,y,z):
	if x > y and x > z:
		return x
	if x == y and x > z:
		return x
	if y > x and y > z:
		return y
	if y > x and y == z:
		return y
	else:
		return z

# It works, but here is the answer given:
def biggest(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

# Better answer
def bigger(a,b):
	if a > b:
		return a
	else:
		return b

def biggest(a,b,c):
	return bigger(bigger(a,b),c)

# Built-In Operator
# max(a,b,c)