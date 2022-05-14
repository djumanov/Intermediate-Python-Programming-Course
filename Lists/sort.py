# .sort() - Use sort() method to sort the items of the list.

# Sort the list of strings
L = ['red', 'green', 'blue', 'orange']
L.sort()
print(L)
# Prints ['blue', 'green', 'orange', 'red']

# Sort the list of numbers
L = [42, 99, 1, 12]
L.sort()
print(L)
# Prints [1, 12, 42, 99]

L = ['red', 'blue', 1, 12, 'orange',42, 'green', 99]
L.sort()
# Triggers TypeError: '<' not supported between instances of 'int' and 'str'

L = ['red', 'green', 'blue', 'orange']
L.sort(reverse=True)
print(L)
# Prints ['red', 'orange', 'green', 'blue']

L = ['red', 'green', 'blue', 'orange']
L.sort(key=len)
print(L)
# Prints ['red', 'blue', 'green', 'orange']

# Sort a list of tuples based on the age of students
def myFunc(e):
  return e[1]	# return age
L = [('Bob', 30),
     ('Sam', 35),
     ('Max', 25)]
L.sort(key=myFunc)
print(L)
# Prints [('Max', 25), ('Bob', 30), ('Sam', 35)]

# Sort a list of dictionaries based on the age of students
def myFunc(e):
    return e['age']		# return age
L = [{'name': 'Bob', 'age': 30},
     {'name': 'Sam', 'age': 35},
     {'name': 'Max', 'age': 25}]
L.sort(key=myFunc)
print(L)
# [{'age': 25, 'name': 'Max'}, {'age': 30, 'name': 'Bob'}, {'age': 35, 'name': 'Sam'}]

# Case-sensitive sorting
L = ['Red', 'blue', 'Green', 'orange']
L.sort()
print(L)
# Prints ['Green', 'Red', 'blue', 'orange']

# Case-insensitive sorting
L = ['Red', 'blue', 'Green', 'orange']
L.sort(key=str.lower)
print(L)
# Prints ['blue', 'Green', 'orange', 'Red']

# sort() vs sorted()
# Get a sorted copy of the list with sorted()
L = ['red', 'green', 'blue', 'orange']
x = sorted(L)
print(x)
# Prints ['blue', 'green', 'orange', 'red']

# Iterate through a sorted list without changing the original
L = ['red', 'green', 'blue', 'orange']
for x in sorted(L):
    print(x)
# Prints blue green orange red
