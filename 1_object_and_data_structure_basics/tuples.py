# tuples are similar to lists, but they are immutable

t = (1,2,3,2)
my_list = [4,5,6]

# count tuple
print(t.count(2))

# index where item appears first
print(t.index(2))

# error thrown:
# TypeError: 'tuple' object does not support item assignment
t[0] = 2
print(t)
