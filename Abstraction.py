# Hiding the implementation details of a class from the user is called abstraction.
from abc import ABC,abstractmethod
class shape(ABC):   #abstract base class
    @abstractmethod #abstract method
    def area(self):
        pass
class circle(shape): #concrete class
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius