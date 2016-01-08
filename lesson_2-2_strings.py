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

# Method: procedure built into python

# Find second string within first string
# <string>.find(<string>)
# Result is the location of the first character where it appears
# Result will be -1 if the string does not appear at all

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1  

# Find second string within first string after <number> position
# <string>.find(<string>, <number>)

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string