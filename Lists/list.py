# The list() function creates a list from an iterable.

L = list()
print(L)
# Prints []

# string into list
T = list('abc')
print(T)
# Prints ['a', 'b', 'c']
# tuple into list
L = list((1, 2, 3))
print(L)
# Prints [1, 2, 3]
# sequence into list
L = list(range(0, 4))
print(L)
# Prints [0, 1, 2, 3]

# dictionary keys into list
L = list({'name': 'Bob', 'age': 25})
print(L)
# Prints ['age', 'name']
# set into list
L = list({1, 2, 3})
print(L)
# Prints [1, 2, 3]

