def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0, 1)
list_vec = (1, 0, 1)

'''Long and not very beautiful approach'''

print('Giving the tuple/list elements as separate arguments')
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
print_vector(list_vec[0], list_vec[1], list_vec[2])

'''Using function arguments unpacking'''

print('Using * to unpack the tuple/list')
print_vector(*tuple_vec)
print_vector(*list_vec)

gen_expr = (x * x for x in range(3))
print_vector(*gen_expr)

dict_vec = { 'x': 1, 'y': 0, 'z': 1 }

print('Using ** to unpack the dict')
print_vector(**dict_vec)
print_vector(*dict_vec)