# Encode the string to UTF-8
S = 'Das straße'
x = S.encode()
print(x)
# Prints b'Das stra\xc3\x9fe'

S = 'Das straße'

x = S.encode(encoding='ascii',errors='backslashreplace')
print(x)
# Prints b'Das stra\\xdfe'

x = S.encode(encoding='ascii',errors='ignore')
print(x)
# Prints b'Das strae'

x = S.encode(encoding='ascii',errors='namereplace')
print(x)
# Prints b'Das stra\\N{LATIN SMALL LETTER SHARP S}e'

x = S.encode(encoding='ascii',errors='replace')
print(x)
# Prints b'Das stra?e'

x = S.encode(encoding='ascii',errors='xmlcharrefreplace')
print(x)
# Prints b'Das straße'

x = S.encode(encoding='UTF-8',errors='strict')
print(x)
# Prints b'Das stra\xc3\x9fe'

