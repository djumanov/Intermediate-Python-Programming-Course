# Perform union of two sets
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
print(A.union(B))
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
# by method
print(A.union(B))
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}
# by operator
print(A | B)
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

A = {'red', 'green', 'blue'}
B = {'yellow', 'orange', 'red'}
C = {'blue', 'red', 'black'}
# by method
print(A.union(B,C))
# Prints {'blue', 'green', 'yellow', 'orange', 'black', 'red'}
# by operator
print(A | B | C)
# Prints {'blue', 'green', 'yellow', 'orange', 'black', 'red'}