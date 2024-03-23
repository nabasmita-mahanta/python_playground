class Person:
    def __init__(self, age, name):
        print("inside Init of Person")
        self.age = age
        self.name = name


class Student(Person):
    def __init__(self, roll, div, name, age):
        print("inside Init of Student")
        self.roll = roll
        self.div = div
        Person.__init__(self, age, name)


s1 = Student(31, 7, "Abhi", 27)
print(s1.name)
print(type(s1))
