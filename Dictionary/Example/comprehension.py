#Suppose you want to create a dictionary of numbers & squares. You could build such dictionary by inserting one item at a time into an empty dictionary:
D = {}
D[0] = 0
D[1] = 1
D[2] = 4
D[3] = 9
D[4] = 16
print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Or, you could just use an iterator and the range() function:
D = {}
for x in range(5):
    D[x] = x**2

print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

D = {x: x**2 for x in range(5)}
print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

D = {c: c * 3 for c in 'RED'}
print(D)
# Prints {'R': 'RRR', 'E': 'EEE', 'D': 'DDD'}

L = ['ReD', 'GrEeN', 'BlUe']
D = {c.lower(): c.upper() for c in L}
print(D)
# Prints {'blue': 'BLUE', 'green': 'GREEN', 'red': 'RED'}

D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selectedKeys = [0, 2, 5]

X = {k: D[k] for k in selectedKeys}

print(X)
# Prints {0: 'A', 2: 'C', 5: 'F'}

D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
removeKeys = [0, 2, 5]

X = {k: D[k] for k in D.keys() - removeKeys}

print(X)
# Prints {1: 'B', 3: 'D', 4: 'E'}

D = {0: 'red', 1: 'green', 2: 'blue'}
R = {v: k for k,v in D.items()}
print(R)
# Prints {'red': 0, 'green': 1, 'blue': 2}L = ['red', 'green', 'blue']
D = {k:v for k,v in enumerate(L)}
print(D)
# Prints {0: 'red', 1: 'green', 2: 'blue'}


D = {ix: line for ix, line in enumerate(open('myFile.txt'))}
print(D)
# {0: 'First line\n',
#  1: 'Second line\n',
#  2: 'Third line\n'}

keys = ['red', 'green', 'blue']

# using dict comprehension
D = {k: 0 for k in keys}
print(D)
# Prints {'red': 0, 'green': 0, 'blue': 0}

# equivalent to using fromkeys() method
D = dict.fromkeys(keys, 0)
print(D)
# Prints {'red': 0, 'green': 0, 'blue': 0}




keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']

# using dict comprehension
D = {k: v for (k, v) in zip(keys, values)}
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# equivalent to using dict() on zipped keys/values
D = dict(zip(keys, values))
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}D = {x: x**2 for x in range(6) if x % 2 == 0}

print(D)
# Prints {0: 0, 2: 4, 4: 16}

D = {}
for x in range(5):
    if x % 2 == 0:
        D[x] = x**2

print(D)
# Prints {0: 0, 2: 4, 4: 16}

