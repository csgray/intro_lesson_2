# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.

def udacify(string):
	return 'U' + string

print udacify('dacians')
# Result: Udacians

print udacify('turn')
# Result: Uturn

print udacify('boat')
# Result: Uboat

# The return command ends the function so anything written after that won't
# actually do anything