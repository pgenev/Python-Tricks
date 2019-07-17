import math

class MyClass:

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# Can modify object instance state
    # Instance method - yes
    # Class method - no
    # Static method - no
# Can modify class state
    # Instance method - yes
    # Class method - yes
    # Static method - no

obj = MyClass()

print('instance method', obj.method())
print('class method', obj.classmethod())
print('static method', obj.staticmethod())
print('class method', MyClass.classmethod())
print('static method', MyClass.staticmethod())

class Pizza:
    def __init__(self, ingredients, radius=None):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return 'Pizza({self.ingredients})'.format(self=self)

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi

print(Pizza.margherita())
print(Pizza.prosciutto())

# When to use staticmethods
print(Pizza(['cheese'], radius=4.5).area())
print(Pizza._circle_area(12))
