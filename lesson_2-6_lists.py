# Lesson 2.6: Structured Data - Lists

# Similar to how strings are sequences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

# <list> = [<expression>,<expression>,...]

# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, "Goodbye!"]
print mixed_list

print "Example 5: Lists can even contain other lists"
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print list_with_lists

# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month):
	return days_in_month[month-1]

#print how_many_days(1)
#>>> 31

#print how_many_days(9)
#>>> 30

# Every entry in the following list is itself a list
nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[0]

print "What do you think this will print?"
print first_concept 

print "Since first_concept was itself a list, we can access its elements"
first_title = first_concept[0]
first_description = first_concept[1]


print "What will this print?"
print first_title
print first_description

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

india = countries[1]
print india[1]
# print countries[1][1]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

print countries[0][2] / countries[2][2]

# Mutation
# You can change the value of a list after you create it.

p = ['H','e','l','l','o']
print p
p[0] = 'Y'
print p 
q = p
q[4] = '!'
print p

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'
print stooges

# Aliasing
# Two different ways to refer to the same object
# If two variables have the same assignment and you change the values of part
# of that assignment, both variables reflect the change.
# If you reassign one of the variables, they break the alias.
# variables instead of just 

spy = [0,0,7]
agent = spy
print spy, agent
spy [2] = agent[2] +1
print spy, agent

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

def replace_spy(p):
	p[2] +=1


# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print spy

# No return statement is necessary because we are not returning a new value but
# changing the old value

# List Operations
# <list>.append(<element>)
#	Adds a new element to a list

# <list1> + <list2>
#	Creates a new list that combines the two lists

# len(<list>)
#	Number of (outer) elements in the input

