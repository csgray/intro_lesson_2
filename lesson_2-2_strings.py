# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Hello!!! Quiz
name = "Corey"
print name

# Concatenation is the value of a string plus another string
print "Hello " + name
print "Hello " + name + "!"

# Cannot concatenate string and integers
# Can multiply strings

print "Hello " + name + 10 * "!"

# This code shows some basic variable assignment and string printing. 
name = "Andy"
print "Hello " + name
print name * 4

# This code shows the difference between the string "4" and the number 4.
print 4
print "4"
print 4 + 4
print "4" + "4"

# This code shows some of the different mistakes that are easy to make while 
# working with strings. Remove one comment at a time and press Test Run to 
# see what happens. Be sure to re-comment before moving on or the program
# will keep showing you an error.
#print 'hello"
#print hello
#print "hello

# This code will give you a peek at what you are about to learn! Uncomment 
# all of the lines below to get a glimpse of "string indexing"
name = "Andy"
print name[0]
print name[1]
print name[2]
print name[3]

# Indexing Strings
# Square brackets will select the n-character of a string
print name[1+1]
#print name[4] #IndexError: string index out of range
print name[-1]

#Selecting Sub-Sequences
# <string>[<expression>] => one-character string
# <string>[<start-expression> : <stop-expression>] => character from start
#   through stop-1
word = 'assume'
print word[3]
print word[3:4]
print word[3:3]
print word[4:6]
print word[4:]
print word[:2]
print word[:]

#Capital Udacity Quiz
s = 'audacity'
# print s[1].upper() + s[2:]
print 'U' + s[2:]