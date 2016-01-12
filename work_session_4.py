# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    while n > 0:
        print n
        n = n - 1
#   if n == 0: 
# This wasn't needed. The code automatically moves on when the while ends.
    print 'Blastoff!'

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    if biggest(a,b,c) == a:
        return bigger(b,c)
    if biggest(a,b,c) == b:
        return bigger(a,c)
    if biggest(a,b,c) == c:
        return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

# Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

from random import randint

def random_noun():
    if randint(0,1) == 0:
        return 'sofa'
    else:
        return 'llama'

print(random_noun())
# Make sure you include the paranthesis!

# Write code for the function random_verb, which takes in no inputs but outputs 
# one of two verbs randomly. Use the randint function to generate a number from 0-1 
# and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

from random import randint

def random_verb():
    if randint(0,1) == 0:
        return 'run'
    else:
        return 'kayak'

print(random_verb())
     
# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == 'NOUN':
        return random_noun()
    if word == 'VERB':
        return random_verb()
    else:
        return word[0]

print word_transformer('NOUN')
print word_transformer('VERB')
print word_transformer('test')

# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

print 'Mad Lib Generator'

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    if word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    while len(mad_lib) > 3:
        processed = processed + word_transformer(mad_lib[:4])
        if mad_lib[:4] == 'NOUN' or mad_lib[:4] == 'VERB':
            mad_lib = mad_lib[3:]
        mad_lib = mad_lib[1:]
    return processed + mad_lib

# Instructor Version
# def process_madlib(mad_lib):
#     processed = ""
#     index = 0
#     box_length = 4
#     while index < len(mad_lib):
#         frame = mad_lib[index:index + box_length]
#         to_add = word_transformer(frame)
#         processed += to_add
#         if len(to_add) == 1:
#             index += 1
#         else:
#             index += 4
#     return processed

    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
test_string_3 = "NOUN VERB NOUN VERBNOUNNOUN VERB NOUN VERB"
print process_madlib(test_string_1)
print process_madlib(test_string_2)
print process_madlib(test_string_3)

