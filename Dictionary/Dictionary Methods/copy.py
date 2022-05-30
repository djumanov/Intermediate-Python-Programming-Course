D = {'name': 'Bob', 'age': 25}
X = D.copy()
print(X)
# Prints {'age': 25, 'name': 'Bob'}

# Assignment statements does not copy object
old_Dict = {'name': 'Bob', 'age': 25}
new_Dict = old_Dict
new_Dict['name'] = 'xx'
print(old_Dict)
# Prints {'age': 25, 'name': 'xx'}
print(new_Dict)
# Prints {'age': 25, 'name': 'xx'}

old_Dict = {'name': 'Bob', 'age': 25}
new_Dict = old_Dict.copy()
new_Dict['name'] = 'xx'
print(old_Dict)
# Prints {'age': 25, 'name': 'Bob'}
print(new_Dict)
# Prints {'age': 25, 'name': 'xx'}

D = {'name': 'Bob', 'age': 25}
X = {k:v for k,v in D.items()}
print(X)
# Prints {'age': 25, 'name': 'Bob'}