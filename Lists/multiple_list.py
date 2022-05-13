# Modify multiple list items
L = ['a', 'b', 'c', 'd', 'e']
L[1:4] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'e']

# Replace multiple elements in place of a single element
L = ['a', 'b', 'c', 'd', 'e']
L[1:2] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'c', 'd', 'e']

# Insert at the start
L = ['a', 'b', 'c']
L[:0] = [1, 2, 3]
print(L)
# Prints [1, 2, 3, 'a', 'b', 'c']
# Insert at the end
L = ['a', 'b', 'c']
L[len(L):] = [1, 2, 3]
print(L)
# Prints ['a', 'b', 'c', 1, 2, 3]

# Insert in the middle
L = ['a', 'b', 'c']
L[1:1] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'b', 'c']

# Delete Multiple List Items
L = ['a', 'b', 'c', 'd', 'e']
L[1:5] = []
print(L)
# Prints ['a']

L = ['a', 'b', 'c', 'd', 'e']
del L[1:5]
print(L)
# Prints ['a']

# Clone or Copy a List
L1 = ['a', 'b', 'c', 'd', 'e']
L2 = L1[:]
print(L2)
# Prints ['a', 'b', 'c', 'd', 'e']
print(L2 is L1)
# Prints False

