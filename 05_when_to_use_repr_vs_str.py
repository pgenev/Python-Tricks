class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'a {self.color} car'.format(self=self)


my_car = Car('red', 37281)

print(my_car)
print(str(my_car))
print('{}'.format(my_car))

# The print() function calls the str() method internally
# The format() function calls also the str() method internally

class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

my_car = Car2('red', 37281)

print(my_car)
print('{}'.format(my_car))
print(repr(my_car))

# __str__ vs __repr__

import datetime
today = datetime.date.today()
print(str(today))
print(repr(today))

# The __str__ method is used to give easy to ready representation of specific class
# __str__ ---> easy to read, for human consumption
# __repr__ ---> unambiguous
# The goal of the __repr__ method is to be explicit as possible about what this object is

class Car3:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)


my_car = Car3('red', 37281)
print(repr(my_car))
print(my_car)

# The default implementation of __str__ calls __repr__

# If we use __str__ on container with objects, the objects will be represented via the __repr__
print(str([today, today, today]))
# If we want to apply the __str__ over each single object, we have to iterate over the container
print([str(today) for today in [today, today, today]])