# Abstract Method >> The method which only has the declaration not definition, called them as abstract method.
# Abstract Class >> The class which will have abstract method is called abstract classes.
# We have to import abc, ABC(abstract base classes), abstractmethod

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

