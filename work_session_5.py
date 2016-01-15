# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?
#
#list1 = [1,2,3,4]
#list2 = [1,2,3,4]
#
#list1 = list1 + [5, 6]
#list2.append([5, 6])
#
# to check, you can print them out using the print statements below.
#
#print "showing list1 and list2:"
#print list1
#print list2

# What is the difference between these two pieces of code?
#list1 = [1,2,3,4,5]
#list2 = [1,2,3,4,5]
#
#def proc(mylist):
#    mylist = mylist + [6, 7]
#
#def proc2(mylist):
#    mylist.append(6)
#    mylist.append(7)
#
# Can you explain the results given by the print statements below?
#
#print "demonstrating proc"
#print list1
#proc(list1)
#print list1
#print
#print "demonstrating proc2"
#print list2
#proc2(list2)
#print list2
#
# Python has a special assignment syntax: +=.  Here is an example:
#
#list3 = [1,2,3,4,5]
#list3 += [6, 7]
#
# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=. 
#
#def proc3(mylist):
#	mylist += [6,7]

# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data
#
# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.
#
# To create a random integer from 0 to 10, we first import the 
# "random" module
#
#import random
#
# We then print a random integer using the random.randint(start, end) function
#print "Random number generated: " + str(random.randint(0,10))
#
# Remember that if we want to concatenate a string and a number, we need to convert the 
# integer into a string using the str() function
#
# We now want to create a list filled with random numbers. The list should be 
# of length 20
#
#random_list = []
#list_length = 20
#
# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.
#
#while len(random_list) < list_length:
#    random_list.append(random.randint(0,10))
#
# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
#print random_list

# Know we want to ask our self the question:
# How many occurrences of the number 9 appear in our randomly made list?
# For example if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to go loop through the list and count how many occurrences of the
# number 9. In this example, the number 9 occurs 3 times in the example
# list
#
#import random
#
# 1. Create random list of integers using while loop
#random_list = []
#list_length = 20
#
#while len(random_list) < list_length:
#  random_list.append(random.randint(0,10))
#    
# Write code here to loop through the list and count all occurrences
# of the number 9. If statements and While loops will help you solve
# this problem.
#
#count = 0
#for i in random_list:
#	if i == 9:
#		count +=1
#
###
#### Instructor Version
###while index < len(random_list):
###  if random_list[index] == 9:
###    count = count + 1
###  index = index + 1
###
#
# Test if our While loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
#print random_list
#print count

# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.
#
# Let's store our counts in a list of length 11 
# with zeros filled in.
#
# We can multiply a list construct to create a list with the same
# elements n number of times.
#count_list = [0] * 11
#
# Check that we have a list of length 11 with all 0 elements
#print count_list
#
# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# For example, assume count_list looks like this:
#
#count_list = [1,2,3,2,2,1,1,2,3,1,2]
#
# Let's print out the occurrences for the numbers 0, 4, 5, and 6
#print count_list[0]
#print count_list[4]
#print count_list[5]
#print count_list[6]
#
# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]
#
# Here's our code that we coded before
#
#import random
#
# Create random list of integers using while loop --------------------
#random_list = []
#list_length = 20
#
#while len(random_list) < list_length:
#  random_list.append(random.randint(0,10))
#
# --------------------------------------------------------------------
#
# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5
#
#count_list = [0] * 11
#index = 0
#
# Write code here to loop through every number in random_list and
# update count_list appropriately
#
#for i in random_list:
#	count_list[i] += 1
#
### Instructor Solution
### index =0
###
### while index < len(random_list):
###   number = random_list[index]
###   count_list[number] = count_list[number] + 1
###   index = index + 1
#
# Check the list we created
#print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
#print sum(count_list)

# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
#"""
#number | occurrence
#     0 | 1
#     1 | 2
#     2 | 3
#     3 | 2
#     4 | 2
#     5 | 1
#     6 | 1
#     7 | 2
#     8 | 3
#     9 | 1
#    10 | 2
#"""
# Here is our code we have written so far:
#
#import random
#
# Create random list of integers using while loop --------------------
#random_list = []
#list_length = 20
#
#while len(random_list) < list_length:
#    random_list.append(random.randint(0,10))
#
# Aggregate the data -------------------------------------------------
#count_list = [0] * 11
# index = 0
#
# My Code
#for i in random_list:
#	count_list[i] += 1
#
# Instructor Code
#while index < len(random_list):
#    number = random_list[index]
#    count_list[number] = count_list[number] + 1
#    index = index + 1
#    
# Write code here to summarize count_list and print a neatly formatted table that looks
# like this:
#
#index = 0
#print 'number | occurrence'
#while index < len(count_list):
#	for n in count_list:
#		if index == 10:
#			print ' ' * 4 + str(index) + ' | ' + str(n)
#		else:
#			print ' ' * 5 + str(index) + ' | ' + str(n)
#		index += 1
#"""
#number | occurrence
#     0 | 1
#     1 | 2
#     2 | 3
#     3 | 2
#     4 | 2
#     5 | 1
#     6 | 1
#     7 | 2
#     8 | 3
#     9 | 1
#    10 | 2
#"""
#
# Hint: To print 10 blank spaces in a row, we can multiply a string by a number "n"
# to print this string n number of times:
#print "Udacity! "*10
#
# BONUS!
# From your summarize code you just wrote, can you make the table even more visual by 
# replacing the count with a string of asterisks that represent the count of a number?
# The table should look like
#
#index = 0
#print 'number | occurrence'
#while index < len(count_list):
#	for n in count_list:
#		if index == 10:
#			print ' ' * 4 + str(index) + ' | ' + '*' * n
#		else:
#			print ' ' * 5 + str(index) + ' | ' + '*' * n
#		index += 1
#
#"""
#number | occurrence
#     0 | *
#     1 | **
#     2 | ***
#     3 | **
#     4 | **
#     5 | *
#     6 | *
#     7 | **
#     8 | ***
#     9 | *
#    10 | **
#"""
#
# Congratulations! You just created a distribution table of a list of numbers! 
# This is also known as a histogram
#
# Way to Dynamically Adjust Spacing
# num_len = len("number")
# while index < len(count_list):
#   num_spaces = num_len - len(str(index))

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.
#
#def product_list(list_of_numbers):
#    product = 1
#    for n in list_of_numbers:
#            product *= n
#    return product
#
#print product_list([9])
#>>> 9
#
#print product_list([1,2,3,4])
#>>> 24
#
#print product_list([])
#>>> 1

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
#
#def greatest(list_of_numbers):
#    great = 0
#    for n in list_of_numbers:
#        if n > great:
#            great = n
#    return great
#
#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0

# String.Split
# string_to_split.split(seperator)
# 	If <seperator> is blank it will split on single spaces
# test_string = "I am a NOUN"
# test_string.split()
# Result: ["I","am","a","NOUN"]

# Let's play around with one more string method: string.split(), which
# splits a string into a list of substrings, and returns it as a new list. 
# Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.
#
#string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
#string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
#list_of_words1 = string1.split()
#list_of_words2 = string2.split()
#print string1
#print string2

# Join
# " ".join()

# Here's another chance to practice your for loop skills. Write code for the 
# function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech, 
# else return None.
#
#def word_in_pos(word, parts_of_speech):
#    for part in parts_of_speech:
#        if part in word:
#            return part
#    return None
#
#test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
#parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]
#
#print word_in_pos(test_cases[0], parts_of_speech)
#print word_in_pos(test_cases[1], parts_of_speech)
#print word_in_pos(test_cases[2], parts_of_speech)
#print word_in_pos(test_cases[3], parts_of_speech)

# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 


parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
#from the gang called PLURALNOUN Wit Attitude"""

def word_in_pos(word, parts_of_speech):
	# Checks words in parts_of_speech list
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# This version parses out the punctuation!        
#def play_game(ml_string, parts_of_speech):    
#    replaced = []
#    # Breaks ml_string into a list of strings
#    libs = ml_string.split()
#    for i in libs:
#        if word_in_pos(i, parts_of_speech) == None:
#            replaced.append(i)
#        else:
#            replaced.append('corgi')
#    return " ".join(replaced)
    
# Instructor Version
def play_game(ml_string, parts_of_speech):
	replaced = []
	ml_string = ml_string.split()
	for word in ml_string:
		replacement = word_in_pos(word, parts_of_speech)
		if replacement != None:
			word = word.replace(replacement, "corgi")
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced

print play_game(test_string, parts_of_speech)

# raw_input
# user_input = raw_input("Type in a word")
# Displays a prompt for the user that says "Type in a word"
# Sets user_input to whatever the user types in
#
# So replace the 'corgi' part with
#        if replacement != None:
#            user_input = raw_input("Type in a: " + replacement + " ")
#            word = word.replace(replacement, user_input)
#            replaced.append(word)