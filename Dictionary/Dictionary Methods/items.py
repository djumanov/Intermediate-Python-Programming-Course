# Print all items from the dictionary
D = {'name': 'Bob', 'age': 25}
L = D.items()
print(L)
# Prints dict_items([('age', 25), ('name', 'Bob')])

# Iterate through both keys and values of a dictionary
D = {'name': 'Bob', 'age': 25}
for x in D.items():
    print(x)
# Prints ('age', 25)
# Prints ('name', 'Bob')

D = {'name': 'Bob', 'age': 25}

# Assign dict items to L
L = D.items()

# modify dict D
D['name'] = 'xx'

# L reflects changes done to dict D
print(L)
# Prints dict_items([('age', 25), ('name', 'xx')])

