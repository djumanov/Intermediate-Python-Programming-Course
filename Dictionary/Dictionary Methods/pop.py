D = {'name': 'Bob', 'age': 25}
D.pop('age')
print(D)
# Prints {'name': 'Bob'}

D = {'name': 'Bob', 'age': 25}
v = D.pop('age')
print(v)
# Prints 25

D = {'name': 'Bob', 'age': 25}
D.pop('job')
# Triggers KeyError: 'job'

D = {'name': 'Bob', 'age': 25}
v = D.pop('age', 0)
print(D)
# Prints {'name': 'Bob'}
print(v)
# Prints 25

D = {'name': 'Bob', 'age': 25}
v = D.pop('job', 'Developer')
print(v)
# Prints Developer