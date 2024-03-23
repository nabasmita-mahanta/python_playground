from Telusko.oops.human import Human

# instantiation of object from a class

obj1 = Human("Nabasmita", "F", 25)
print(obj1.no_of_legs)
obj1.talk()
obj1.breathe()
print(obj1)

# lets create another human object
obj2 = Human(age=27, gender="M", name="Abhinov")
print(obj2.no_of_legs)
obj2.talk()
print(obj2)

print(type(obj1))