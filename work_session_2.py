# Write Python code that prints out the number of hours in 7 weeks.
# 7 weeks * 7 days * 24 hours
print 7  * 7 * 24

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[0] + t[2:]

# Insert the proper slicing indices for the substring variable 
# so that the slice is a string that contains everything after "A NOUN". 
# For example, if we wanted to store everything after "went", the returned 
# string would be equal to sentence[11:].

sentence = "A NOUN went on a walk."
substring = sentence[6:]

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after
# "VERB" in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:-17]
substring3 = sentence[-13:]

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "pineapple" # your noun here
verb_replacement = "shimmy" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + \
	verb_replacement + substring3
print new_sentence

# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

mary = "Mary"
randa = mary
katie = randa
salwa = katie
kathleen = salwa
gabriel = kathleen

# Are you wondering why there's two ways to make strings 
# (single quotes AND double quotes)?? 
#
# Look at the code on line 11. It uses the single quote ' to 
# create a string. But it also has a double quote " inside of the
# string.

# Would we be able to create a string like the one below if we 
# could only use the double quote " to create strings?

div_with_class = '<div class="concept-description">'
just_the_class = div_with_class[5:-1]
print just_the_class

# In addition to using single quotes (') or double quotes (")
# to create a string, you can also use TRIPLE quotes to create
# a multi-line string. 

print """I am a string 
that takes up 
multiple lines."""

print '''I am also a string
that makes up multiple lines!'''

print '''
<div class="concept">
    <div class="concept-title">
        Multi-line strings
    </div>
    <div class="concept-description">
        Multi-line strings can be made with triple single 
        quotes or triple double quotes. But I'm not sure
        why they are useful yet.
    </div>
</div>
'''

# Use string sequencing to take the single HTML <div> element
# below (written on one line) and then prints it up as three
# lines. 
# The first line should just be the opening tag: <div>
# The second line should be the text within the div (don't forget to indent)
# The third line should just be the closing tag.

div_element = "<div>I am learning to code!</div>"

opening_tag = div_element[0:5] # add the appropriate numbers to each side of the colon
indent      = '  ' # modify this string so that it indents the inner text.
inner_text  = div_element[5:-6] # add the appropriate numbers to each side of the colon
closing_tag = div_element[-6:] # add the appropriate numbers to each side of the colon

print opening_tag
print indent + inner_text
print closing_tag

# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find at https://goo.gl/Pde1nZ or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find("NOUN")
verb_position = text.find("VERB")

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

first = text.find("zip")
print text.find("zip", first + 1)

text = "all zip files are compressed"
print text.find("zip", first + 1)

# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace("NOUN", "duck")
sentence = sentence.replace("VERB", "waddle")
print sentence
