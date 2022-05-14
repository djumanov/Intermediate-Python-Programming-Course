# Check if any item in a list is True
L = [0, 0, 0]
print(any(L))   # Prints False
L = [0, 1, 0]
print(any(L))   # Prints True

L = [False, 0, 1]
print(any(L))   # Prints True
T = ('', [], 'green')
print(any(T))   # Prints True
S = {0j, 3+4j, 0.0}
print(any(S))   # Prints True

D1 = {0: 'Zero', 0: 'Nil'}
print(any(D1))   # Prints False
D2 = {'Zero': 0, 'Nil': 0}
print(any(D2))   # Prints True

L = []
print(any(L))   # Prints False