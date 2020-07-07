# functions

def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(3, 4))

# default parameters
def say_name(name='Fudge'):
    print(f'Your name is {name}')

say_name()
say_name('Todd')

def even_check(num):
    return num % 2 == 0

print(f'10 is even? {even_check(10)}')
print(f'15 is even? {even_check(15)}')

# return true if any number in list is even
def even_in_list(list):
    for i in list:
        print(i)
        if i % 2 == 0:
            return True
    return False

print('Even in list?')
print(even_in_list([1,3,4,5,7]))

print('Even in list?')
print(even_in_list([1,3,5,7]))

# return all even numbers in the list
def list_of_evens(list):
    evens = []
    for num in list:
        if num % 2 == 0:
            evens.append(num)
    return evens

print('no evens in list')
print(list_of_evens([1,3,5]))

print('evens in list')
print(list_of_evens([1,2,4,5,7,9,10]))
