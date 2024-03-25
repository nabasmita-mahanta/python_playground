# 4 types of polymorphism

# different classes having same method name - duck typing

# child class overrides parent class method with same name - method overriding

# operators like '+' and '*' can behave differently based on what we use them for (eg 3*2=6 and python*3=pythonpythonpython)- operator overloading

# method overloading (NOT PRESENT IN PYTHON) - when in a same class we have same method names but with differnt parameters


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# car1.move()
# boat1.move()
# plane1.move()

list = [car1, boat1, plane1]

for x in list:
    x.move()
