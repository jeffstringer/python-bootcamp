my_string = 'mystringisawesome'
print(my_string)

# Indexing

# example: first character
print(my_string[0])

# example: last character
print(my_string[-1])

# example: third from last character
print(my_string[-3])

# [start:stop:step]

# length of string
print('length of my_string:')
print(len(my_string))

# starting at index 2, go all the way to the end:
print(my_string[2:])

# first 3 letters:
print(my_string[:3])

# subsection in middle of string
print(my_string[2:-2])

# step size, or every n (3 here) letter in string
print(my_string[::3])

# reverse a string (step size is -1)
print(my_string[::-1])

# string concatentation
print('P' + 'am')

# letter 10 times
letter = 'z'
print(letter * 10)

# upper case
print(my_string.upper())

# split method
print('hello world'.split())

# string interpolation
print(f'My awesome string is {my_string}')

# more modern string interpolation?
name = Python
print('Hi, %s.' % name)
