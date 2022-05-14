# .index() - The index() method searches for the first occurrence of the given item and returns its index. If specified item is not found, it raises ‘ValueError’ exception.

# Find the index of 'green' in a list
L = ['red', 'green', 'blue', 'yellow']
print(L.index('green'))
# Prints 1

# Find first occurrence of character ‘c’
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c'))
# Prints 2

# Find 'c' starting a position 5
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c',5))
# Prints 8

# Find 'c' in between 5 & 10
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c',5,10))
# Prints 8

# index() on Item that Doesn’t Exist
# index() method raises a ‘ValueError’ if specified item is not found in the list.

L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('x'))
# Triggers ValueError: 'x' is not in list
# also within search bound
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c',4,7))
# Triggers ValueError: 'c' is not in list

L = ['a','b','c','d','e','f','a','b','c','d','e','f']
if 'x' in L:
    print(L.index('x'))