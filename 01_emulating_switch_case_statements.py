'''Normal way of handling with if/elif/else '''

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


print(dispatch_if('add', 5, 5))

'''Handling with dictionary'''

x = y = 0

dict_operators = {
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y
}

def dispatch_dict(operator, x, y):
    return dict_operators.get(operator, lambda: None)(x, y)


print(dispatch_dict('add', 5, 10))