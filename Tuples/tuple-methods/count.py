# Count the number of occurrences of ‘red’
T = ('red', 'green', 'blue')
print(T.count('red'))
# Prints 1

# Count the number of occurrences of number ‘9’
T = (1, 9, 7, 3, 9, 1, 9, 2)
print(T.count(9))
# Prints 3

# Count occurrences of all the unique items
T = ('a', 'b', 'c', 'b', 'a', 'a', 'a')
from collections import Counter
print(Counter(T))
# Prints Counter({'a': 4, 'b': 2, 'c': 1})