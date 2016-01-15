# IPND Stage 2 Final Project

# Paragraph provided by the sample code for testing
sample = '''
A ___1___ is created with the def keyword. You specify the inputs a ___1___
takes by adding ___2___ separated by commas between the parentheses. ___1___s
by default return ___3___ if you don't specify the value to return. ___2___ can
be standard data types such as string, number, dictionary, tuple, and ___4___
or can be more complicated such as objects and lambda functions.
'''

def sample_correct(blank):
    if blank == 1:
        return "function"
    if blank == 2:
        return "inputs"
    if blank == 3:
        return "None"
    if blank == 4:
        return "list"

#def correct_answer():

#def wrong_answer():

def medium_blank():
    blank = 1
    global sample
    print sample
    # Medium questions have four blanks so once blank reaches five it stops
    while blank < 5: 
        tries = 0
        answer = raw_input("What is the answer to blank #" + str(blank) + "?")
        if answer == sample_correct(blank):
                global sample
                sample = sample.replace("___" + str(blank) + "___", answer)
                blank += 1
                tries = 0
                print sample
        else:
                while tries < 3:
                    tries += 1
                    print "That's incorrect. You have " + str(3 - tries) + " tries remaining."
                else:
                    print "Better luck next time!"
    print "Congratulations! You filled in all the blanks!"


from random import randint

# Prompts users to choose their difficulty level or the wisdom generator
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
    # Invalid input shows the valid inputs and loops back to the prompt
    else:
        print "That is not a valid input. Try 'easy', 'medium', 'hard', or 'wisdom'."
        main_screen()

def easy():
    print ""
    print "Easy Paragraph"

def medium():
    print ""
    print "Alright! Here is a medium paragraph:"
    medium_blank()

def hard():
    print ""
    print "Hard Paragraph"

# Randomly selects and prints a quote from the Adeptus Mechanicus
# Uses ''' to print quotes as blocks of text
def wisdom_generator():
    wisdom = randint(0,3)
    if wisdom == 0:
        print '''
A powerful man is not a man who dissects the universe like a puzzle-box,
examining it piece by piece and measuring each piece with scientific precision.
A powerful man has only to look upon the universe to change it.
    - Techno-Magos Gaelos
        '''
    if wisdom == 1:
        print '''
Our enemies may rest but rust never sleeps.
    - Tech-Priest Jung
        '''
    if wisdom == 2:
        print '''
You may say, "It is impossible for a man to become like the Machine."
And I would reply that only the smallest mind strives to comprehend its limits.
    - Fabricator-General Kane
        '''
    if wisdom == 3:
        print '''
A man may die yet still endure if his work enters the greater work, for time is
carried upon a current of forgotten deeds, and events of great moment are but
the culmination of a single carefully placed thought.
    - Techno-Magos Mojaro
        '''

# This is the main menu that shows up when the program launches
# Had to escape out the last backslash
print '''
 ______ _ _ _    _____        _______ _               ____  _             _    
|  ____(_) | |  |_   _|      |__   __| |             |  _ \| |           | |   
| |__   _| | |____| |  _ __ ____| |  | |__   ___ ____| |_) | | __ _ _ __ | | __
|  __| | | | |____| | | '_ \____| |  | '_ \ / _ \____|  _ <| |/ _` | '_ \| |/ /
| |    | | | |   _| |_| | | |   | |  | | | |  __/    | |_) | | (_| | | | |   < 
|_|    |_|_|_|  |_____|_| |_|   |_|  |_| |_|\___|    |____/|_|\__,_|_| |_|_|\_\\

There are three difficulties: easy, medium, hard
Or maybe you want some words of _wisdom_?'''
main_screen()

#def play_game(paragraph):
#	print paragraph
#	fill_blanks(paragraph, blank)

# Prompts the user for input then fills in the blank
#def fill_blanks(paragraph, blank):
#	paragraph = paragraph.replace('___' + str(blank) + '___', input1)
#	return paragraph
