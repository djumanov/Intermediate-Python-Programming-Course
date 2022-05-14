# Check if all items in a list are True
L = [1, 1, 1]
print(all(L))   # Prints True
L = [0, 1, 1]
print(all(L))   # Prints False

L = [True, 0, 1]
print(all(L))   # Prints False
T = ('', 'red', 'green')
print(all(T))   # Prints False
S = {0j, 3+4j}
print(all(S))   # Prints False

D1 = {0: 'Zero', 1: 'One', 2: 'Two'}
print(all(D1))   # Prints False
D2 = {'Zero': 0, 'One': 1, 'Two': 2}
print(all(D2))   # Prints True

# empty iterable
L = []
print(all(L))   # Prints True
# iterable with empty items
L = [[], []]
print(all(L))   # Prints False

