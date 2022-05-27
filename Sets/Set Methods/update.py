# Update the set by adding items from other set
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
A.update(B)
print(A)
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
A |= B
print(A)
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

A = {'red', 'green', 'blue'}
B = {'yellow', 'orange', 'red'}
C = {'blue', 'red', 'black'}
# by method
A.update(B,C)
print(A)
# Prints {'blue', 'green', 'yellow', 'orange', 'black', 'red'}
# by operator
A |= B | C
print(A)
# Prints {'blue', 'green', 'yellow', 'orange', 'black', 'red'}