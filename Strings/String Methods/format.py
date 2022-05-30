# Access arguments by default order (implicit)
S = '{} is {} years old.'.format('Bob', 25)
print(S)

# Prints Bob is 25 years old.

# Access arguments by positional index (explicit)
S = '{1} is {0} years old.'.format(25, 'Bob')
print(S)

# Prints Bob is 25 years old.

# Access arguments by name
S = '{name} is {age} years old.'.format(name='Bob', age=25)
print(S)

# Prints Bob is 25 years old.

# Align text left
S = '{:<12}'.format('Left')
print(S)

# Prints Left        

# Align text right
S = '{:>12}'.format('Right')
print(S)

# Prints        Right

# Align text center
S = '{:^12}'.format('Center')
print(S)

# Prints    Center   

# Choose custom fill character
S = '{:*^12}'.format('Center')
print(S)

# Prints ***Center***

# Truncate string to two characters
S = '{:.2}'.format('Python')
print(S)

# Prints Py

# Add padding to a truncated string and align it center
S = '{:^10.2}'.format('Python')
print(S)

# Prints     Py    

# Convert 42 to hex, octal, binary and unicode character
S = 'int:{0:d}, hex:{0:x}, oct:{0:o}, bin:{0:b}, char:{0:c}'.format(42)
print(S)

# Prints int:42, hex:2a, oct:52, bin:101010, char:*

# Add a prefix to Hex, Octal and Binary
S = 'hex:{0:#x}; oct:{0:#o}; bin:{0:#b}'.format(42)
print(S)

# Prints hex:0x2a; oct:0o52; bin:0b101010

# Show floating point number
S = '{:f}'.format(3.141592653)
print(S)

# Prints 3.141593

# Specify digits after the decimal point (Precision)
S = '{:.2f}'.format(3.141592653)
print(S)

# Prints 3.14

# Display numbers with exponent notation
S = '{:.2e}'.format(3141592653)
print(S)

# Prints 3.14e+09

# Format number as percentage
S = '{:.2%}'.format(19.5/22)
print(S)

# Prints 88.64%

# Display sign for both positive and negative numbers
S = '{:+.2f}, {:+.2f}'.format(3.14, -3.14)
print(S)

# Prints +3.14, -3.14

# Display sign only for negative numbers
S = '{:-.2f}, {:-.2f}'.format(3.14, -3.14)
print(S)

# Prints 3.14, -3.14

# Display a space for positive numbers
S = '{: .2f}, {: .2f}'.format(3.14, -3.14)
print(S)

# Prints  3.14, -3.14

# Add padding to a number
S = '{:5d}'.format(42)
print(S)

# Prints    42

# Padding zeros to a number
S = '{:0>3d}'.format(7)
print(S)

# Prints 007

# Padding zeros to a floating point
S = '{:06.2f}'.format(3.141592653589793)
print(S)

# Prints 003.14

# Padding zeros to a negative number
S = '{:0=8d}'.format(-120)
print(S)

# Prints -0000120

# Using the comma as a thousands separator
S = '{:,}'.format(1234567890)
print(S)

# Prints 1,234,567,890

# Using underscore as a nibble separator
S = '{:_b}'.format(0b01010101010)
print(S)

# Prints 10_1010_1010

# Using datetime formatting
import datetime
D = datetime.datetime(2010, 7, 4, 12, 15, 58)
S = '{:%Y-%m-%d %H:%M:%S}'.format(D)
print(S)

# Prints 2010-07-04 12:15:58

# Parametrized fill, alignment and width
S = '{:{fill}{align}{width}}'.format('center', fill='*', align='^', width='12')
print(S)

# Prints ***center***

