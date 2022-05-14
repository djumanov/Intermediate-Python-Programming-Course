x = max(10, 20, 30)
print(x)
# Prints 30

x = max('red', 'green', 'blue')
print(x)
# Prints red

L = [300, 500, 100, 400, 200]
x = max(L)
print(x)
# Prints 500

L = []
x = max(L)
print(x)
# Triggers ValueError: max() arg is an empty sequence

# Specify default value '0'
L = []
x = max(L, default='0')
print(x)
# Prints 0

L = ['red', 'green', 'blue', 'black', 'orange']
x = max(L, key=len)
print(x)
# Prints orange

# Find out who is the oldest student
def myFunc(e):
  return e[1]	# return age
L = [('Sam', 35),
    ('Tom', 25),
    ('Bob', 30)]
x = max(L, key=myFunc)
print(x)
# Prints ('Sam', 35)

# Find out who is the oldest student
L = [('Sam', 35),
    ('Tom', 25),
    ('Bob', 30)]
x = max(L, key=lambda student: student[1])
print(x)
# Prints ('Sam', 35)

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

x = max(L, key=lambda student: student.age)
print(x)
# Prints ('Sam', 35)
