# scope

x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

# python follows LEGB rule the following order:

# L: local
# where num is local to the lambda function
lambda num:num**2

# alternative, local example
name = 'GLOBAL'
def greet():
    name = 'enclosed'
    def hello():
        name = 'local'
        print(f'Hello {name}')
    hello()
greet()

# E: enclosing
# when hello() is called, it looks inside hello() and name is not defined
# then it looks within greet() and finds name defined as 'enclosed'
name = 'GLOBAL'
def greet():
    name = 'enclosed'
    def hello():
        # name = 'local'
        print(f'Hello {name}')
    hello()
greet()


# G: global
# a global variable is defined as having no indentation, i.e. name = 'GLOBAL' above
name = 'GLOBAL'
def greet():
    # name = 'enclosed'
    def hello():
        # name = 'local'
        print(f'Hello {name}')
    hello()
greet()


# B: built-in
# an example would be a built-in function like len() to determine length

# change global variable within function scope

x = 25
def func():
    global x
    x = 'new value'
    print(f'changed x to {x}')
func()
print(x)
