# map
my_nums = [1,2,3,4]

def square(num):
    return num**2

for item in map(square, my_nums):
    print(item)

# want list back?
print(list(map(square, my_nums)))

# filter
def check_even(num):
    return num % 2 == 0

for item in filter(check_even,my_nums):
    print(item)

# lambda is an anonymous function
def square(num):
    return num ** 2

# square as lambda
lambda num: num ** 2

# we can pass in a lambda function instead of a square function for example
print(list(map(lambda num: num ** 2, my_nums)))

# another lambda example
names = ['Ricky', 'Bobby', 'Sally']
print(list(map(lambda name:name[::-1], names)))
