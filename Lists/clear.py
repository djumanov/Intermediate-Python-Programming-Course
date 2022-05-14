# .clear() - Use clear() method to remove all items from the list.
L = ['red', 'green', 'blue']
L.clear()
print(L)
# Prints []


# equivalent methods
L = ['red', 'green', 'blue']
del L[:]
print(L)
# Prints []

L = ['red', 'green', 'blue']
L[:] = []
print(L)
# Prints []

L = ['red', 'green', 'blue']
L *= 0
print(L)
# Prints []