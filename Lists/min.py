x = min(10, 20, 30)
print(x)
# Prints 10

x = min('red', 'green', 'blue')
print(x)
# Prints blue

L = [300, 500, 100, 400, 200]
x = min(L)
print(x)
# Prints 100

L = []
x = min(L)
print(x)
# Triggers ValueError: min() arg is an empty sequence

# Specify default value '0'
L = []
x = min(L, default='0')
print(x)
# Prints 0

L = ['red', 'green', 'blue', 'black', 'orange']
x = min(L, key=len)
print(x)
# Prints red

# Find out who is the youngest student
def myFunc(e):
  return e[1]	# return age
L = [('Sam', 35),
    ('Tom', 25),
    ('Bob', 30)]
x = min(L, key=myFunc)
print(x)
# Prints ('Tom', 25)

# Find out who is the youngest student
L = [('Sam', 35),
    ('Tom', 25),
    ('Bob', 30)]
x = min(L, key=lambda student: student[1])
print(x)
# Prints ('Tom', 25)


# Custom class
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __repr__(self):
		return repr((self.name, self.age))
# a list of custom objects
L = [Student('Sam', 35),
	Student('Tom', 25),
	Student('Bob', 30)]

x = min(L, key=lambda student: student.age)
print(x)
# Prints ('Tom', 25)
