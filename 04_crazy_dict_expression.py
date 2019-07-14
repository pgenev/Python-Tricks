crazy_dict = {True: 'yes', 1: 'no', 1.0: 'maybe'}

print(crazy_dict)
print('True == 1 == 1.0', True == 1 == 1.0)

# bool is a subtype of the Integer

ys = dict()
ys[True] = 'yes'
print('key with value "yes": ', ys)
print('Overwriting the value with "no"')
ys[1] = 'no'
print('key with value "no": ', ys)
print('Overwriting the value with "maybe"')
ys[1.0] = 'maybe'
print('key with value "maybe": ', ys)

