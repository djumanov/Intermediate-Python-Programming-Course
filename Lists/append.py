# .append()
L = ['red', 'green', 'blue']
L.append('yellow')
print(L)
# Prints ['red', 'green', 'blue', 'yellow']

# Append list to a list
L = ['red', 'green', 'blue']
L.append([1,2,3])
print(L)
# Prints ['red', 'green', 'blue', [1, 2, 3]]

# Append tuple to a list
L = ['red', 'green', 'blue']
L.append((1,2,3))
print(L)
# Prints ['red', 'green', 'blue', (1, 2, 3)]

# append() vs extend()
L = ['red', 'green']
L.append('blue')
print(L)
# Prints ['red', 'green', 'blue']

L = ['red', 'green']
L.extend('blue')
print(L)
# Prints ['red', 'green', 'b', 'l', 'u', 'e']