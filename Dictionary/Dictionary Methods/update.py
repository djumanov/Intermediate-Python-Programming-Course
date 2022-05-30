from pyrsistent import v


D1 = {'name': 'Bob'}
D2 = {'job': 'Dev', 'age': 25}
D1.update(D2)
print(D1)
# Prints {'job': 'Dev', 'age': 25, 'name': 'Bob'}

D1 = {'name': 'Bob', 'age': 25}
D2 = {'job': 'Dev', 'age': 30}
D1.update(D2)
print(D1)
# Prints {'job': 'Dev', 'age': 30, 'name': 'Bob'}

# Passing a dictionary object
D = {'name': 'Bob'}
D.update({'job': 'Dev', 'age': 25})
print(D)
# Prints {'job': 'Dev', 'age': 25, 'name': 'Bob'}

# Passing a list of tuples
D = {'name': 'Bob'}
D.update([('job', 'Dev'), ('age', 25)])
print(D)
# Prints {'age': 25, 'job': 'Dev', 'name': 'Bob'}

# Passing an iterable of length two (nested list)
D = {'name': 'Bob'}
D.update([['job', 'Dev'], ['age', 25]])
print(D)
# Prints {'age': 25, 'job': 'Dev', 'name': 'Bob'}

# Specifying key:value pairs as keyword arguments
D = {'name': 'Bob'}
D.update(job = 'Dev', age = 25)
print(D)
# Prints {'job': 'Dev', 'age': 25, 'name': 'Bob'}

