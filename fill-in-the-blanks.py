# IPND Stage 2 Final Project

# Paragraph provided by the sample code for testing
sample = """
A ___1___ is created with the def keyword. You specify the inputs a ___1___
takes by adding ___2___ separated by commas between the parentheses. ___1___s
by default return ___3___ if you don't specify the value to return. ___2___ can
be standard data types such as string, number, dictionary, tuple, and ___4___
or can be more complicated such as objects and lambda functions.
"""

from random import randint

def sample_correct(blank):
    """Answer key for the 'sample' paragraph."""
    if blank == 1:
        return "function"
    if blank == 2:
        return "inputs"
    if blank == 3:
        return "None"
    if blank == 4:
        return "list"

def correct_answer(blank, tries, answer, sample):
    """Replaces the blank with the correct answer, advances to the next blank,
    and resets the number of tries the user has for the next question.
    """
    sample = sample.replace("___" + str(blank) + "___", answer)
    blank += 1
    tries = 0
    print "Correct!"
    print sample
    return blank, tries, sample

def wrong_answer(tries, sample):
    """Increases tries by 1 each time the user gets it wrong until they have
    tried three times. Then it ends the program.
    """
    print "That's incorrect. You have " + str(2 - tries) + " tries remaining."
    while tries < 2:
        tries += 1
        print sample
        return tries
    else:
        print "Better luck next time!"
        raise SystemExit

def medium_blank():
    """Starts at the first blank with zero tries then displays and retrieves
    the question paragraph. Keeps progressing through the blanks until all of
    the blanks are filled.
    """
    blank = 1
    tries = 0
    global sample
    print sample
    # Medium questions have four blanks so once blank reaches five it stops
    while blank < 5: 
        answer = raw_input("What is the answer to blank #" + str(blank) + "?")
        if answer == sample_correct(blank):
            blank, tries, sample = correct_answer(blank, tries, answer, sample)
        else:
            tries = wrong_answer(tries, sample)
    print "Congratulations! You filled in all the blanks!"
    raise SystemExit

def main_screen():
    """Starts the game by allowing the user to select their difficulty level
    or the wisdom generator.
    """
    choice = raw_input("Make your choice: ")
    if choice == 'easy':
        return easy()
    if choice == 'medium':
        return medium()
    if choice == 'hard':
        return hard()
    if choice == 'wisdom':
        return wisdom_generator()
    # Terminates the program if the user types 'quit' or 'exit'
    if choice == 'quit' or 'exit':
        raise SystemExit
    # Invalid input shows the valid inputs and loops back to the prompt
    else:
        print "That is not a valid input. Try 'easy', 'medium', 'hard', or 'wisdom'."
        main_screen()

def easy():
    print "Easy Paragraph"

def medium():
    paragraph = randint
    print "Alright! Here is a medium paragraph:"
    medium_blank()

def hard():
    print "Hard Paragraph"

def wisdom_generator():
    """Randomly selects and prints a quote from the Adeptus Mechanicus."""
    wisdom = randint(0,3)
    if wisdom == 0:
        print """
A powerful man is not a man who dissects the universe like a puzzle-box,
examining it piece by piece and measuring each piece with scientific precision.
A powerful man has only to look upon the universe to change it.
    - Techno-Magos Gaelos
        """
    if wisdom == 1:
        print """
Our enemies may rest but rust never sleeps.
    - Tech-Priest Jung
        """
    if wisdom == 2:
        print """
You may say, "It is impossible for a man to become like the Machine."
And I would reply that only the smallest mind strives to comprehend its limits.
    - Fabricator-General Kane
        """
    if wisdom == 3:
        print """
A man may die yet still endure if his work enters the greater work, for time is
carried upon a current of forgotten deeds, and events of great moment are but
the culmination of a single carefully placed thought.
    - Techno-Magos Mojaro
        """

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