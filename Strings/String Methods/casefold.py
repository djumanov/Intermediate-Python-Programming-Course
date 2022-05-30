# Make a string casefolded
S = 'Hello, World!'
x = S.casefold()
print(x)
# Prints hello, world!

S = 'Das straße'
x = S.casefold()
print(x)
# Prints das strasse

S = 'Das straße'
x = S.lower()
print(x)
# Prints das straße