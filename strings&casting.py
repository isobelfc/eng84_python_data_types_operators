# Strings and Casting

# Let's have a look at some industry practices
# Single and double quotes examples

# single_quotes = 'single quotes \'Wow\''
# double_quotes = "double quotes 'Wow'"
# print(single_quotes)
# print(double_quotes)

# String slicing

greetings = "Hello world!"  # string
# indexing in Python starts from 0
# H e l l o   w o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

# How can we find out the length of this string
# We have a method called len() to find out
# print(len(greetings))

# We can get just part of the string

# Simple indexing
# print(greetings[0:5])  # outputs string from 0 to 4
# print(greetings[6:11])
#
# # Reverse indexing starts with -1
# print(greetings[-6:])

#   H   e   l  l  o     w  o  r  l  d  !
# -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# Let's have a look at some strings methods

# white_space = "lots of space at the end               "
# # strip() helps us remove all white spaces
# print(len(white_space))
# print(len(white_space.strip()))

# count() counts the number of times the word appears in the string
example_text = "here's some Text with lots of text"
# print(example_text.count("text"))

# upper() and lower() change text to all upper or lower case
print(example_text)
print(example_text.upper())
print(example_text.lower())
print(example_text.capitalize())  # Capitalises first letter of the string

# replace() to replace part of a string
print(example_text.replace("with", ","))
