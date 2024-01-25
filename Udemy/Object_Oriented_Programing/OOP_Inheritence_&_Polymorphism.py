# Inheritence

class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("WOOF!!")


mydog = Dog()
myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()
mydog.who_am_i()
mydog.bark()


# POLYMORPHISM

class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class Animal():

    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof"
class Cat(Animal):
    def speak(self):
        return self.name + " says meow"

fido = Dog("Fido")
iris = Cat("Iris")

print(fido.speak())
print(iris.speak())
