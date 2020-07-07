# range operator

# for all numbers from 0 - 9 (not including 10)
for num in range(10):
    print(num)
print('\n')

# for range starting at 0, before 10, step size 2
for num in range(0,10,2):
    print(num)
print('\n')

# to save range:
print(list(range(0,10,2)))
print('\n')

# enumerate operator: index count in tuples
word = 'abcde'
for item in enumerate(word):
    print(item)
print('\n')

# zip operator zips together more than 1 list
mylist1 = ['a','b','c']
mylist2 = [1,2,3]
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)
zippee = list(zip(mylist1,mylist2))
print(zippee)
print('\n')

# "in" list, string, dictionary
print('x' in [1,2,3])
print('y' not in [1,2,3])
print('a' in 'a world')
print('mykey' in {'mykey': 1})
print(345 in {'mykey': 1}.keys())
print(345 in {'mykey': 1}.values())
print('\n')

# min
print(min([1,2,3]))
print('\n')

# max
print(max([1,2,3]))
print('\n')

# shuffle a list
from random import shuffle
mylist = [1,2,3,4]
shuffle(mylist)
print(mylist)
print('\n')

# grab a random integer
from random import randint
print(randint(0,100))
print('\n')

# allow user input, always as a string
result = input("Enter a number here:\n")
print(f'the number you entered is {int(result)}')
