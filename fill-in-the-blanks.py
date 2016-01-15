# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

def main_screen():
    choice = raw_input("Make your choice: ")
    if choice == 'easy':
        return easy()
    if choice == 'medium':
        return medium()
    if choice == 'hard':
        return hard()
    if choice == 'wisdom':
        return wisdom_generator()
    else:
        print "That is not a valid input. Try 'easy', 'medium', 'hard', or 'wisdom'."
        return choice

def easy():
    print ""
    print "Easy Paragraph"

def medium():
    print ""
    print "Medium Paragraph"

def hard():
    print ""
    print "Hard Paragraph"

def wisdom_generator():
    from random import randint
    wisdom = randint(0,3)
    if wisdom == 0:
        print ""
        print "A powerful man is not a man who dissects the universe like a puzzle-box,"
        print "examining it piece by piece and measuring each piece with scientific precision."
        print "A powerful man has only to look upon the universe to change it."
        print "    - Techno-Magos Gaelos"
    if wisdom == 1:
        print ""
        print "Our enemies may rest but rust never sleeps."
        print "    - Tech-Priest Jung"
    if wisdom == 2:
        print ""
        print 'You may say, "It is impossible for a man to become like the Machine."'
        print "And I would reply that only the smallest mind strives to comprehend its limits."
        print "    - Fabricator-General Kane"
    if wisdom == 3:
        print ""
        print "A man may die yet still endure if his work enters the greater work, for time is"
        print "carried upon a current of forgotten deeds, and events of great moment are but"
        print "the culmination of a single carefully placed thought."
        print "    - Techno-Magos Mojaro"


print " ______ _ _ _    _____        _______ _               ____  _             _    "
print "|  ____(_) | |  |_   _|      |__   __| |             |  _ \| |           | |   "
print "| |__   _| | |____| |  _ __ ____| |  | |__   ___ ____| |_) | | __ _ _ __ | | __"
print "|  __| | | | |____| | | '_ \____| |  | '_ \ / _ \____|  _ <| |/ _` | '_ \| |/ /"
print "| |    | | | |   _| |_| | | |   | |  | | | |  __/    | |_) | | (_| | | | |   < "
print "|_|    |_|_|_|  |_____|_| |_|   |_|  |_| |_|\___|    |____/|_|\__,_|_| |_|_|\_\\"
print ""
print 'There are three difficulties: easy, medium, hard'
print 'Or maybe you want some words of _wisdom_?'
main_screen()




#def play_game(paragraph):
#	print paragraph
#	fill_blanks(paragraph, blank)

# Prompts the user for input then fills in the blank
#def fill_blanks(paragraph, blank):
#	paragraph = paragraph.replace('___' + str(blank) + '___', input1)
#	return paragraph
