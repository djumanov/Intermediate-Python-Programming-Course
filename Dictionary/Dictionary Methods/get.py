D = {'name': 'Bob', 'age': 25}
print(D.get('name'))
# Prints Bob

D = {'name': 'Bob', 'age': 25}
print(D.get('job'))
# Prints None

D = {'name': 'Bob', 'age': 25, 'job': 'Manager'}
print(D.get('job', 'Developer'))
# Prints Manager

D = {'name': 'Bob', 'age': 25}
print(D.get('job','Developer'))
# Prints Developer

# key present
D = {'name': 'Bob', 'age': 25}
print(D['name'])
# Prints Bob
print(D.get('name'))
# Prints Bob

# key absent
D = {'name': 'Bob', 'age': 25}
print(D['job'])
# Triggers KeyError: 'job'
print(D.get('job'))
# Prints None

