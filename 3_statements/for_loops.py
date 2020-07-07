# iterables
my_list = [1,2,3]

# simple for loop
for item in my_list:
    print(item)


# for loop with some logic
for i in my_list:
    if (i % 2 == 0):
        print(f'number is even: {i}')
    else:
        print(f'number is odd: {i}')

# a list sum...
# demonstrate importance of white space:
list_sum = 0
for i in my_list:
    list_sum = list_sum + i
    print(list_sum)
# print(list_sum)

# can iterate over strings
for letter in 'hello world':
    print(letter)

# can iterate over tuples
tup = (1,2,3)
for t in tup:
    print(t)

# tuple unpacking:
mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist:
    print(a)
    print(b)

# iterater over dictionary
d = {'one': 1, 'two': 2, 'three': 3}
for k,v in d.items():
    print(f'key: {k}, value: {v}')
