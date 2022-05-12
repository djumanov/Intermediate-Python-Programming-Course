# Nested lists

# positive indexes
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]
print(L[2][2])
# Prints ['eee', 'fff']
print(L[2][2][0])
# Prints eee

# negative indexes
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[-3])
# Prints ['cc', 'dd', ['eee', 'fff']]
print(L[-3][-1])
# Prints ['eee', 'fff']
print(L[-3][-1][-2])
# Prints eee


# Change Nested List Item Value

L = ['a', ['bb', 'cc'], 'd']
L[1][1] = 0
print(L)
# Prints ['a', ['bb', 0], 'd']