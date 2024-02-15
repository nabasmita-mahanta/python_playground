# If we define a variable inside _init_ then it is called as instance variable.
# If we define a variable outside _init_ and inside class is called class variable.

class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
