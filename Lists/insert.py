# .insert() - Use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right.

# Insert 'yellow' at 2nd position
L = ['red', 'green', 'blue']
L.insert(1,'yellow')
print(L)
# Prints ['red', 'yellow', 'green', 'blue']

# Insert 'yellow' at 2nd position
L = ['red', 'green', 'blue']
L.insert(-2,'yellow')
print(L)
# Prints ['red', 'yellow', 'green', 'blue']

L = ['red', 'green', 'blue']
L.insert(10,'yellow')
print(L)
# Prints ['red', 'green', 'blue', 'yellow']

# insert() vs append()
L = ['red', 'green', 'blue']
L.insert(len(L),'yellow')
print(L)
# Prints ['red', 'green', 'blue', 'yellow']
# is equivalent to
L = ['red', 'green', 'blue']
L.append('yellow')
print(L)
# Prints ['red', 'green', 'blue', 'yellow']

# insert() vs extend()
L = ['red', 'green']
L.insert(2,'blue')
print(L)
# Prints ['red', 'green', 'blue']

L = ['red', 'green']
L.extend('blue')
print(L)
# Prints ['red', 'green', 'b', 'l', 'u', 'e']