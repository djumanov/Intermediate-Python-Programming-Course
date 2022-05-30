# Insert a key 'job' with default value 'Dev'
D = {'name': 'Bob', 'age': 25}
v = D.setdefault('job', 'Dev')
print(D)
# Prints {'job': 'Dev', 'age': 25, 'name': 'Bob'}
print(v)
# Prints Dev

# without default specified
D = {'name': 'Bob', 'age': 25}
v = D.setdefault('name')
print(v)
# Prints Bob

# with default specified
D = {'name': 'Bob', 'age': 25}
v = D.setdefault('name', 'Max')
print(v)
# Prints Bob


D = {'name': 'Bob', 'age': 25}
v = D.setdefault('job', 'Dev')
print(D)
# Prints {'job': 'Dev', 'age': 25, 'name': 'Bob'}
print(v)
# Prints Dev

D = {'name': 'Bob', 'age': 25}
v = D.setdefault('job')
print(D)
# Prints {'job': None, 'age': 25, 'name': 'Bob'}
print(v)
# Prints None

