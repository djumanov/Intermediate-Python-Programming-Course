# .extend() - The extend() method extends the list by appending all the items from the iterable to the end of the list. This method does not return anything; it modifies the list in place.

# Add multiple items to a list
L = ['red', 'green', 'blue']
L.extend([1,2,3])
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

# Add tuple items to a list
L = ['red', 'green', 'blue']
L.extend((1,2,3))
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

# Add set items to a list
L = ['red', 'green', 'blue']
L.extend({1,2,3})
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

# Equivalent Methods
L = ['red', 'green', 'blue']
L[len(L):] = [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

# Concatenation operator
L = ['red', 'green', 'blue']
L = L + [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]
# Augmented assignment operator
L = ['red', 'green', 'blue']
L += [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]