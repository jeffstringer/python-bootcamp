# *args is a tuple
def sum_nums(*args):
    print(args)
    return sum(args)
print(sum_nums(1,2,3,4,5))
print('\n')

# **kwargs is a dictionary
def legumes(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"your favorite fruit is: {kwargs['fruit']}")
    elif 'veggie' in kwargs:
        print(f"your favorite veggie is {kwargs['veggie']}")
    else:
        print('no legumes here!')


legumes(fruit='strawberry',veggie='cucumber')
legumes(veggie='cucumber')

# if using together, must have *args, **kwargs and no other arguments
