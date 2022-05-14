# The globals() function returns the global symbol table as a dictionary. It contains information about all global variables.

# Each key in the dictionary holds the name of the variable. This dictionary is also accessible from within functions and can be used to update global variables directly.

# Declare some global variables
a = 10
b = 20
c = 30
d = 40
# Print the current global symbol table
print(globals())
# Prints {'__name__': '__main__',
#        '__doc__': None,
#        '__package__': None,
#        '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fed1a254358>,
#        '__spec__': None,
#        '__annotations__': {},
#        '__builtins__': <module 'builtins' (built-in)>,
#        '__file__': 'main.py',
#        '__cached__': None,
#        'a': 10,
#        'b': 20,
#        'c': 30,
#        'd': 40 }


x = 5       # global scope
def myfunc():
    x = 10  # local scope
    print('x inside function is', x)    
myfunc()
# Prints x inside function is 10
print('x outside function is', x)
# Prints x outside function is 5

# Get the value of global variable 'x'
x = 10
print(globals()['x'])
# Prints 10

# Get the filename of the current program
print(globals()['__file__'])
# Prints main.py

# Update global variable x inside a function
x = 5       # global scope
def myfunc():
    x = 10  # local scope
    globals()['x'] = 99    # update global x
    print('x inside function is', x)    
myfunc()
# Prints x inside function is 10
print('x outside function is', x)
# Prints x outside function is 99