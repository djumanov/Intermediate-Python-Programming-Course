# .count() - Use count() method to find the number of times the specified item appears in the list.

# Count number of occurrences of 'red'
L = ['red', 'green', 'blue']
print(L.count('red'))
# Prints 1

# Count number of occurrences of number '9'
L = [1, 9, 7, 3, 9, 1, 9, 2]
print(L.count(9))
# Prints 3

# Count Multiple Items
# If you want to count multiple items in a list, you can call count() in a loop.
# This approach, however, requires a separate pass over the list for every count() call; which can be catastrophic for performance. Use couter() method from class collections, instead.

# Count occurrences of all the unique items
L = ['a', 'b', 'c', 'b', 'a', 'a', 'a']
from collections import Counter
print(Counter(L))
# Prints Counter({'a': 4, 'b': 2, 'c': 1})