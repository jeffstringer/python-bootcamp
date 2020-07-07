# unordered collections of unique values

my_set = set()
print(my_set)

# add item
my_set.add(1)
print(my_set)

# add another unique value
my_set.add(2)
print(my_set)

# won't add as values must be unique
my_set.add(2)
print(my_set)

# tuple will only store unique values
my_list = [1,1,2,2,2,3,3,3]
print(set(my_list))
