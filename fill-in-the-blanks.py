# IPND Stage 2 Final Project

easy1 = """
It's a dangerous business, Frodo, going out your ___1___. You step onto the
___2___, and if you don't keep your ___3___, there's no knowing where you might
be swept off to.
"""

def easy1_correct(blank):
    """Answer key for the 'easy1' paragraph."""
    if blank == 1:
        return "door"
    if blank == 2:
        return "road"
    if blank == 3:
        return "feet"

easy2 = """
It's the ___1___ that's never ___2___ as takes ___3___ to finish.
"""

def easy2_correct(blank):
    """Answer key for the 'easy2' paragraph."""
    if blank == 1:
        return "job"
    if blank == 2:
        return "started"
    if blank == 3:
        return "longest"

easy3 = """
Yet such is oft the course of ___1___ that move the wheels of the world: small
___2___ do them because they must, while the ___3___ of the great are elsewhere.
"""

def easy3_correct(blank):
    """Answer key for the 'easy3' paragraph."""
    if blank == 1:
        return "deeds"
    if blank == 2:
        return "hands"
    if blank == 3:
        return "eyes"

medium1 = """
War must be, while we defend our lives against a destroyer who would devour 
all; but I do not love the bright ___1___ for its sharpness, nor the ___2___ 
for its swiftness, nor the ___3___ for his glory. I love only that which they 
___4___.
"""

def medium1_correct(blank):
    """Answer key for the 'medium1' paragraph."""
    if blank == 1:
        return "sword"
    if blank == 2:
        return "arrow"
    if blank == 3:
        return "warrior"
    if blank == 4:
        return "defend"

medium2 = """
I have passed through ___1___ and deep ___2___, since we parted. I have 
___3___ much that I thought I knew, and ___4___ again much that I had ___3___.
"""

def medium2_correct(blank):
    """Answer key for the 'medium2' paragraph."""
    if blank == 1:
        return "fire"
    if blank == 2:
        return "water"
    if blank == 3:
        return "forgotten"
    if blank == 4:
        return "learned"

medium3 = """
And some things that should not have been forgotten were lost. ___1___ became 
___2___. ___2___ became ___3___. And for two and a half thousand years, the
___4___ passed out of all knowledge.
"""

def medium3_correct(blank):
    """Answer key for the 'medium3' paragraph."""
    if blank == 1:
        return "History"
    if blank == 2:
        return "legend"
    if blank == 3:
        return "myth"
    if blank == 4:
        return "ring"

hard1 = """
The ___1___? His sense of ___2___ was no less than yours, I deem. You wonder 
what his ___3___ is, where he came from. And if he was really ___4___ at heart.
What lies or threats led him on this long march from home. If he would not 
rather have stayed there in peace. ___5___ will make corpses of us all.
"""

def hard1_correct(blank):
    """Answer key for the 'hard1' paragraph."""
    if blank == 1:
        return "enemy"
    if blank == 2:
        return "duty"
    if blank == 3:
        return "name"
    if blank == 4:
        return "evil"
    if blank == 5:
        return "War"

hard2 = """
___1___ Rings for the Elven-kings under the sky,
___2___ for the Dwarf-lords in halls of stone,
___3___ for Mortal Men, doomed to die,
___4___ for the Dark Lord on his dark throne
In the Land of Mordor where the ___5___ lie.
___4___ Ring to rule them all, ___4___ Ring to find them,
___4___ Ring to bring them all and in the darkness bind them.
In the Land of Mordor where the ___5___ lie.
"""

def hard2_correct(blank):
    """Answer key for the 'hard2' paragraph."""
    if blank == 1:
        return "Three"
    if blank == 2:
        return "Seven"
    if blank == 3:
        return "Nine"
    if blank == 4:
        return "One"
    if blank == 5:
        return "Shadows"

hard3 = """
It's like in the great ___1___, Mr. Frodo. The ones that really mattered. Full
of ___2___ and ___3___ they were. And sometimes you didn't want to know the
___4___... because how could the ___4___ be happy? How could the world go back
to the way it was when so much bad had happened? But in the end, it's only a
___5___ing thing... this shadow. Even ___2___ must ___5___.
"""

def hard3_correct(blank):
    """Answer key for the 'hard3' paragraph."""
    if blank == 1:
        return "stories"
    if blank == 2:
        return "darkness"
    if blank == 3:
        return "danger"
    if blank == 4:
        return "end"
    if blank == 5:
        return "pass"

from random import randint

def correct_answer(blank, tries, answer, question):
    """Replaces the blank with the correct answer, advances to the next blank,
    and resets the number of tries the user has for the next question.
    """
    question = question.replace("___" + str(blank) + "___", answer)
    blank += 1
    tries = 0
    print "Correct!"
    print question
    return blank, tries, question

def wrong_answer(tries, question):
    """Increases tries by 1 each time the user gets it wrong until they have
    tried three times. Then it ends the program.
    """
    print "That's incorrect. You have " + str(2 - tries) + " tries remaining."
    while tries < 2:
        tries += 1
        print question
        return tries
    else:
        print "Better luck next time!"
        raise SystemExit

def easy_blank():
    """Starts at the first blank with zero tries then displays and retrieves
    the question paragraph. Keeps progressing through the blanks until all of
    the blanks are filled.
    """
    blank = 1
    tries = 0
    question = easy1
    print question
    # Easy questions have three blanks so once blank reaches four it stops
    while blank < 4: 
        answer = raw_input("What is the answer to blank #" + str(blank) + "?")
        if answer == easy1_correct(blank):
            blank, tries, question = correct_answer(blank, tries, answer, question)
        else:
            tries = wrong_answer(tries, question)
    print "Congratulations! You filled in all the blanks!"
    raise SystemExit

def medium_blank():
    """Starts at the first blank with zero tries then displays and retrieves
    the question paragraph. Keeps progressing through the blanks until all of
    the blanks are filled.
    """
    blank = 1
    tries = 0
    question = medium1
    print question
    # Medium questions have four blanks so once blank reaches five it stops
    while blank < 5: 
        answer = raw_input("What is the answer to blank #" + str(blank) + "?")
        if answer == medium1_correct(blank):
            blank, tries, question = correct_answer(blank, tries, answer, question)
        else:
            tries = wrong_answer(tries, question)
    print "Congratulations! You filled in all the blanks!"
    raise SystemExit

def hard_blank():
    """Starts at the first blank with zero tries then displays and retrieves
    the question paragraph. Keeps progressing through the blanks until all of
    the blanks are filled.
    """
    blank = 1
    tries = 0
    question = hard1
    print question
    # Hard questions have five blanks so once blank reaches six it stops
    while blank < 6: 
        answer = raw_input("What is the answer to blank #" + str(blank) + "?")
        if answer == hard1_correct(blank):
            blank, tries, question = correct_answer(blank, tries, answer, question)
        else:
            tries = wrong_answer(tries, question)
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
    print "Alright! Here is a easy paragraph:"
    easy_blank()

def medium():
    print "Alright! Here is a medium paragraph:"
    medium_blank()

def hard():
    print "Alright! Here is a hard paragraph:"
    hard_blank()

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