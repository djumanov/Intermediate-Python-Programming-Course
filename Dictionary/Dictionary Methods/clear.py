D = {'name': 'Bob', 'age': 25}
D.clear()
print(D)
# Prints {}


# Assigning an empty dictionary D = {} is  not same as D.clear().
old_Dict = {'name': 'Bob', 'age': 25}
new_Dict = old_Dict
old_Dict = {}
print(old_Dict)
# Prints {}
print(new_Dict)
# Prints {'age': 25, 'name': 'xx'}

old_Dict = {'name': 'Bob', 'age': 25}
new_Dict = old_Dict
old_Dict.clear()
print(old_Dict)
# Prints {}
print(new_Dict)
# Prints {}