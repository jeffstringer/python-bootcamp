num = 4
while num > 0:
    num -= 1
    print(num)
else:
    print('done')
print('\n')

mystring = 'sammy'
# break
# breaks out of the closest enclosing loop

for letter in mystring:
    if letter == 'a':
        break
    print(letter)
print('\n')

# continue
# goes to the top of the closest enclosing loop
# if letter is 'a', continue
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
print('\n')

# pass
# does nothing at all
x = [1,2,3]
for item in x:
    # pass prevent error when no logic present in for loop
    pass
print('end of my script')
