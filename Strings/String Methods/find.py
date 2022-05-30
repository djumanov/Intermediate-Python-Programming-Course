# Find if substring 'Developer' contains in a string
S = 'Bob is a Developer at ABC'
x = S.find('Developer')
print(x)
# Prints 9

# Find if substring 'Manager' contains in a string
S = 'Bob is a Developer at ABC'
x = S.find('Manager')
print(x)
# Prints -1

# Find 'Big' starting a position 7
S = 'Big, Bigger, Biggest'
x = S.find('Big',7)
print(x)
# Prints 13

# Find 'Big' in between 2 & 10
S = 'Big, Bigger, Biggest'
x = S.find('Big',2,10)
print(x)
# Prints 5

S = 'Bob is a Developer at ABC'
x = S.find('Manager')
print(x)
# Prints -1

