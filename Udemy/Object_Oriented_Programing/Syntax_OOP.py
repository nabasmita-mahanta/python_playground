# Basic syntax of Object Oriented Programing

# class NameOfClass():
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#
#     def some_method(self):
#         # perform some action
#         print(self.param1)

class Dog():

    def __init__(self, breed,name,spots):
        # Attributes
        # We take in the argument
        # assign it using self. attribute name
        self.breed = breed
        self.name = name
        # Expects a boolean value here
        self.spots = spots


my_dog = Dog(breed='Lab',name='Kuku',spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)



