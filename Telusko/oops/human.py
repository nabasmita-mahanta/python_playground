from Telusko.oops.living import LivingThing


class Human(LivingThing):

    # (class variables or static variables)
    no_of_legs = 2

    # constructor method
    def __init__(self, name, gender, age):
        # properties
        self.name = name
        self.gender = gender
        self.age = age

    def talk(self):
        print("My name is " + self.name)

    def __str__(self):
        return f'HUMAN: name-{self.name}, gender-{self.gender}, age-{self.age}'



