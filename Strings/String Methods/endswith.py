# Check if the string ends with ‘ABC’
S = 'Bob is a CEO at ABC'
x = S.endswith('ABC')
print(x)
# Prints True

# Check if the string ends with a ‘ ? ‘
S = 'Is Bob a CEO?'
x = S.endswith('?')
print(x)
# Prints True

# Check if the substring (4th to 12th character) ends with 'CEO'
S = 'Bob is a CEO at ABC'
x = S.endswith('CEO',4,12)
print(x)
# Prints True

# Check if the string ends with one of the items in a tuple
S = 'Bob is a CEO'
suffixes = ('CEO','CFO','COO')
x = S.endswith(suffixes)
print(x)
# Prints True

# Check if the string ends with one of the items in a tuple
S = 'Sam is a CFO'
suffixes = ('CEO','CFO','COO')
x = S.endswith(suffixes)
print(x)
# Prints True

