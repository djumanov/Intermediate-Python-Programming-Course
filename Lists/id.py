# The id() function returns a unique id for the specified object.

x = id('Hello!')
print(x)
# Prints 34936992
x = id(9999)
print(x)
# Prints 33739544
L = ['red', 'green', 'blue']
x = id(L)
print(x)
# Prints 33866256
class myfunc:
  pass
o = myfunc()
print(id(o))
# Prints 33666912

# Check if 'x' and 'y' have the same id (point to the same object)
x = 42
y = x
print(x is y)
# Prints True

print(30 is 20+10)
# Prints True
print('aa'*2 is 'a'*4)
# Prints True