# IPND Stage 2 Final Project

# This is the start of the data structures
# The questions are quotes from The Lord of the Rings by J. R. R. Tolkien

# Modes is a dictionary of three empty lists keyed to the difficulty levels
modes = {"easy": [],
         "medium": [],
         "hard": [],
         }

# Appends the first easy question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["easy"].append({"question": """
It's a dangerous business, Frodo, going out your ___1___. You step onto the
___2___, and if you don't keep your ___3___, there's no knowing where you might
be swept off to.
""", "answers": ["door", "road", "feet"],
    })

# Appends the second easy question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["easy"].append({"question": """
It's the ___1___ that's never ___2___ as takes ___3___ to finish.
""", "answers": ["job", "started", "longest"],
    })

# Appends the third easy question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["easy"].append({"question": """
Yet such is oft the course of ___1___ that move the wheels of the world: small
___2___ do them because they must, while the ___3___ of the great are elsewhere.
""", "answers": ["deeds", "hands", "eyes"],
    })

# Appends the first medium question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["medium"].append({"question": """
War must be, while we defend our lives against a destroyer who would devour 
all; but I do not love the bright ___1___ for its sharpness, nor the ___2___ 
for its swiftness, nor the ___3___ for his glory. I love only that which they 
___4___.
""", "answers": ["sword", "arrow", "warrior", "defend"]
    })

# Appends the second medium question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["medium"].append({"question": """
I have passed through ___1___ and deep ___2___, since we parted. I have 
___3___ much that I thought I knew, and ___4___ again much that I had ___3___.
""", "answers": ["fire", "water", "forgotten", "learned"]
    })

# Appends the third medium question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["medium"].append({"question": """
And some things that should not have been forgotten were lost. ___1___ became 
___2___. ___2___ became ___3___. And for two and a half thousand years, the
___4___ passed out of all knowledge.
""", "answers": ["History", "legend", "myth", "ring",]
    })

# Appends the first hard question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["hard"].append({"question": """
The ___1___? His sense of ___2___ was no less than yours, I deem. You wonder 
what his ___3___ is, where he came from. And if he was really ___4___ at heart.
What lies or threats led him on this long march from home. If he would not 
rather have stayed there in peace. ___5___ will make corpses of us all.
""", "answers": ["enemy", "duty", "name", "evil", "War",]
    })

# Appends the second hard question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["hard"].append({"question": """
___1___ Rings for the Elven-kings under the sky,
___2___ for the Dwarf-lords in halls of stone,
___3___ for Mortal Men, doomed to die,
___4___ for the Dark Lord on his dark throne
In the Land of Mordor where the ___5___ lie.
___4___ Ring to rule them all, ___4___ Ring to find them,
___4___ Ring to bring them all and in the darkness bind them.
In the Land of Mordor where the ___5___ lie.
""", "answers": ["Three", "Seven", "Nine", "One", "Shadows",]
    })

# Appends the third hard question keyed to "question"
# and the the answers as a list keyed to "answers"
modes["hard"].append({"question": """
It's like in the great ___1___, Mr. Frodo. The ones that really mattered. Full
of ___2___ and ___3___ they were. And sometimes you didn't want to know the
___4___... because how could the ___4___ be happy? How could the world go back
to the way it was when so much bad had happened? But in the end, it's only a
___5___ing thing... this shadow. Even ___2___ must ___5___.
""", "answers": ["stories", "darkness", "danger", "end", "pass"],
    })

# Four quotes from the Adeptus Mechanicus in a list
wisdom = ["""
A powerful man is not a man who dissects the universe like a puzzle-box,
examining it piece by piece and measuring each piece with scientific precision.
A powerful man has only to look upon the universe to change it.
    - Techno-Magos Gaelos
        """,
        """
Our enemies may rest but rust never sleeps.
    - Tech-Priest Jung
        """,
        """
You may say, "It is impossible for a man to become like the Machine."
And I would reply that only the smallest mind strives to comprehend its limits.
    - Fabricator-General Kane
        """,
        """
A man may die yet still endure if his work enters the greater work, for time is
carried upon a current of forgotten deeds, and events of great moment are but
the culmination of a single carefully placed thought.
    - Techno-Magos Mojaro
        """
    ]


# This is the start of the actual code
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


def quiz(question_dict):
    """Asks the user to fill in the blanks and determines whether or not the
    answer is correct after stripping out any capitalization. Congratulates the
    user and quits the program once all the blanks are filled in.
    """
    blank = 1
    tries = 0
    question = question_dict["question"]
    answers = question_dict["answers"]
    print question
    while blank <= len(answers):
        answer = raw_input("What is the answer to blank #" + str(blank) + "? ")
        # Converts the user's answer to all lower case
        answer = answer.lower()
        # Compares the user's answer to a lower case version of the dictionary answer
        # blank - 1 because blank is in human terms but the list starts at 0
        if answer == answers[blank - 1].lower():
            # Plugs the dictionary answer back in so that it has the correct capitalization
            blank, tries, question = correct_answer(blank, tries, answers[blank - 1], question)
        else:
            tries = wrong_answer(tries, question)
    print "Congratulations! You filled in all the blanks!"
    raise SystemExit


def main_screen():
    """Starts the game by allowing the user to select their difficulty level
    or the wisdom generator.
    """
    choice = raw_input("Make your choice: ")
    # 
    if choice == "easy" or choice == "medium" or choice == "hard":
        print "Alright! Here is a " + choice + " paragraph:"
        return quiz(modes[choice][randint(0, 2)])
    # Prints a random quote from the wisdom collection
    if choice == "wisdom":
        print wisdom[randint(0,3)]
    # Terminates the program if the user types "quit" or "exit"
    if choice == "quit" or choice == "exit":
        raise SystemExit
    # Invalid input shows the valid inputs and loops back to the prompt
    else:
        print "That is not a valid input. Try 'easy', 'medium', 'hard', or 'wisdom'."
        print "You may also 'quit' or 'exit'."
        main_screen()


# This is the main menu that shows up when the program launches
# Had to escape out the last backslash
print """
 ______ _ _ _    _____        _______ _               ____  _             _    
|  ____(_) | |  |_   _|      |__   __| |             |  _ \| |           | |   
| |__   _| | |____| |  _ __ ____| |  | |__   ___ ____| |_) | | __ _ _ __ | | __
|  __| | | | |____| | | '_ \____| |  | '_ \ / _ \____|  _ <| |/ _` | '_ \| |/ /
| |    | | | |   _| |_| | | |   | |  | | | |  __/    | |_) | | (_| | | | |   < 
|_|    |_|_|_|  |_____|_| |_|   |_|  |_| |_|\___|    |____/|_|\__,_|_| |_|_|\_\\

There are three difficulties: easy, medium, hard
Or maybe you want some words of _wisdom_?
"""
main_screen()
