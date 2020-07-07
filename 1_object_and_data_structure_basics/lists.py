my_list = [1,2,3]
print(my_list)

# length of list
print(len(my_list))

# first item in list
print(my_list[0])

# last 2 items in list (from index 1 forward)
print(my_list[1:])

# concatenate lists
another_list = [4,5]
print(my_list + another_list)

# alter list
my_list[0] = 6
print(my_list)
my_list = [1,2,3]

# append: add item to end of list
my_list.append(4)
print(my_list)
my_list = [1,2,3]

# pop: remove item from end of list
my_list.pop()
print(my_list)
my_list = [1,2,3]

# sorted lists
num_list = [10,11,1,2]
num_list.sort() # can't print this as it will return "NoneType"
print(num_list)

# reverse list
my_list.reverse()
print(my_list)
