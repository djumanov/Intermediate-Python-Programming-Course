# .pop() - The pop() method removes a single list item at specified index and returns it. If no index is specified, pop() method removes and returns the last item in the list.

# Remove 2nd list item
L = ['red', 'green', 'blue']
L.pop(1)
print(L)
# Prints ['red', 'blue']

# Remove 2nd list item
L = ['red', 'green', 'blue']
L.pop(-2)
print(L)
# Prints ['red', 'blue']

L = ['red', 'green', 'blue']
x = L.pop(1)
# removed item
print(x)
# Prints green

L = ['red', 'green', 'blue']
L.pop()
print(L)
# Prints ['red', 'green']