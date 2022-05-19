# Find index of 'green' in a tuple
T = ('red', 'green', 'blue', 'yellow')
print(T.index('green'))
# Prints 1

# Find first occurrence of character ‘c’
T = ('a','b','c','d','e','f','a','b','c','d','e','f')
print(T.index('c'))
# Prints 2

# Find 'c' starting a position 5
T = ('a','b','c','d','e','f','a','b','c','d','e','f')
print(T.index('c',5))
# Prints 8

# Find 'c' in between 5 & 10
T = ('a','b','c','d','e','f','a','b','c','d','e','f')
print(T.index('c',5,10))
# Prints 8

T = ('a','b','c','d','e','f','a','b','c','d','e','f')
print(T.index('x'))
# Triggers ValueError: tuple.index(x): x not in tuple
# also within search bound
T = ('a','b','c','d','e','f','a','b','c','d','e','f')
print(T.index('c',4,7))
# Triggers ValueError: tuple.index(x): x not in tuple

T = ('a','b','c','d','e','f','a','b','c','d','e','f')
if 'x' in T:
    print(T.index('x'))