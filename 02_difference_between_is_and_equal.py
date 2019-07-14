a = [1, 2, 3]
b = a

print('a == b:', a == b)
print('a is b:', a is b)

c = list(a)

print('a == c:', a == c)
print('a is c:', a is c)

# The 'is' operator evaluates to True if two variables point to the same object
# The '==' operator evaluates to True if both objects are equal
