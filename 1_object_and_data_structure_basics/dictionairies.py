# simple dictionary
my_dictionary = {'one': 1, 'two': 2}
print(my_dictionary)

#
d = {
    'k1': [1,2,3],
    'k2': {
        'insideKey': 100
    }
}
print(d['k2']['insideKey'])

# re-assign value to dictionary
d['k2']['insideKey'] = 200
print(d['k2']['insideKey'])

# dictionary keys
print(d.keys())

# dictionary values
print(d.values())

# dictionary pairings -> returned as tuples
print(d.items())
