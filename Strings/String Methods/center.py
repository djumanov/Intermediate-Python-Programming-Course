# Align text center
S = 'Centered'
x = S.center(14)
print(x)

# Prints    Centered   

# center() with '*' as a fill character
S = 'Centered'
x = S.center(14, '*')
print(x)

# Prints ***Centered***

# Align text center with format()
S = 'Centered'
x = '{:*^14}'.format(S)
print(x)

# Prints ***Centered***

