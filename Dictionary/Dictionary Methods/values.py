# Print all values from the dictionary
D = {'name': 'Bob', 'age': 25}
L = D.values()
print(L)
# Prints dict_values([25, 'Bob'])

# Iterate through all the values from a dictionary
D = {'name': 'Bob', 'age': 25}
for x in D.values():
    print(x)
# Prints 25 Bob

D = {'name': 'Bob', 'age': 25}

# Assign dict values to L
L = D.values()

# modify dict D
D['name'] = 'xx'

# L reflects changes done to dict D
print(L)
# Prints dict_values([25, 'xx'])