# Create a dictionary and set default value 'Developer' for all keys
D = dict.fromkeys(['Bob', 'Sam'], 'Developer')
print(D)
# Prints {'Bob': 'Developer', 'Sam': 'Developer'}

D = dict.fromkeys(['Bob', 'Sam'])
print(D)
# Prints {'Bob': None, 'Sam': None}

# As if default value is specified
L = ['Bob', 'Sam']
D = {key:'Developer' for key in L}
print(D)
# Prints {'Bob': 'Developer', 'Sam': 'Developer'}

# As if default value is not specified
L = ['Bob', 'Sam']
D = {key:None for key in L}
print(D)
# Prints {'Bob': None, 'Sam': None}

