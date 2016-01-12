# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

# while <TextExpression>:
#	<Block>
# Keeps going so long as the test expression is true
# Moves to the next line once the test expression is false

# if <TextExpression>:
#	<Block>
# Goes down the block until it finds a true test expression

# This code demonstrates a while loop with a "counting variable"
i = 0
while i < 10:
    print i
    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(x):
	y = 1
	while y <= x:
		print y
		y = y + 1

print_numbers(3)

# 'n' usually stands for 'number'
# 'i' usually stands for iteration

# break
# while <TestExpression>:
#	<code>
#	if <breaktest>:
#		break
#	<MoreCode>

# break, if true, breaks out of the while loop and moves to the code after
# the while loop
