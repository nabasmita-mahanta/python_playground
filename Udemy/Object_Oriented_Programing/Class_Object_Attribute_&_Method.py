class Dog():
    # class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name):
        # Attributes
        # We take in the argument
        # assign it using self. attribute name
        self.breed = breed
        self.name = name

    # Attributes and methods are two important concepts in
    # Object-Oriented Programming (OOP).
    # Attributes are characteristics of an object,
    # while methods are functions that act on an object.
    # Operations/Actions ----> Methods
    def bark(self, number):
        print("Woof! My name is {} and my number is {}".format(self.name, number))


my_dog = Dog('lab', 'Franky')
print(type(my_dog))
print(my_dog.species)
print(my_dog.name)
my_dog.bark(10)


class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * self.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())
