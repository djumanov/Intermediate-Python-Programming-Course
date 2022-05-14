# .copy() - The copy() method returns the Shallow copy of the specified list.
# Create a copy of list 'L'
L = ['red', 'green', 'blue']
X = L.copy()
print(X)
# Prints ['red', 'green', 'blue']

# Assignment statement does not copy objects. For example
# When you execute new_List = old_List, you don’t actually have two lists. The assignment just makes the two variables point to the one list in memory.
old_List = ['red', 'green', 'blue']
new_List = old_List
new_List[0] = 'xx'
print(old_List)
# Prints ['xx', 'green', 'blue']
print(new_List)
# Prints ['xx', 'green', 'blue']

# So, when you change new_List, old_List is also modified. If you want to change one copy without changing the other, use copy()method.
old_List = ['red', 'green', 'blue']
new_List = old_List.copy()
new_List[0] = 'xx'
print(old_List)
# Prints ['red', 'green', 'blue']
print(new_List)
# Prints ['xx', 'green', 'blue']


# Assigning a slice of the entire list to a variable is equivalent to copy() method.
L = ['red', 'green', 'blue']
X = L[:]
print(X)
# Prints ['red', 'green', 'blue']