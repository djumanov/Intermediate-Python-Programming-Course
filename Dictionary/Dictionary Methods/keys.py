# Print all keys from the dictionary
D = {'name': 'Bob', 'age': 25}
L = D.keys()
print(L)
# Prints dict_keys(['age', 'name'])

# Iterate through all the keys from a dictionary
D = {'name': 'Bob', 'age': 25}
for x in D.keys():
    print(x)
# Prints age name

D = {'name': 'Bob', 'age': 25}

# Assign dict keys to L
L = D.keys()

# modify dict D
D['job'] = 'Developer'

# L reflects changes done to dict D
print(L)
# Prints dict_keys(['job', 'age', 'name'])
