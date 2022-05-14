# The locals() function returns the local symbol table as a dictionary. It contains information about all local variables.

# global variables
a = 10
b = 20
def myfunc():
    # local variables
    c = 30
    d = 40
    print(locals())
myfunc()
# Prints {'c': 30, 'd': 40}

x = 5       # global scope
def myfunc():
    x = 10  # local scope
    print('x inside function is', x)    
myfunc()
# Prints x inside function is 10
print('x outside function is', x)
# Prints x outside function is 5

# Get the value of local variable 'x'
x = 10
print(locals()['x'])
# Prints 10