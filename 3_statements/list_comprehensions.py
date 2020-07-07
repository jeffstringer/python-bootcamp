# list comprehension example

mystring = 'hello'
mylist = [letter for letter in mystring]
print(mylist)
print('\n')

# or list comprehension example with range of numbers
mylist2 = [num**2 for num in range(0,11)]
print(mylist2)
print('\n')

# operations in list comprehension
mylist3 = [x for x in range(0,11) if x%2==0]
print(mylist3)
print('\n')

# another calculation in list comprehension example
celcius = [-40,0,22,100]
farenheit = [(9/5)*temp + 32 for temp in celcius]
print(farenheit)

# if/else in list comprehension example, but not very readable
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

# an ugly nested loop example
mylist4 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist4)
