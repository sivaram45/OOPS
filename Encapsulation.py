#Binding data and methods into a single Entity is called Encapsulation

class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year
    def car_features(self):
        return f"{self.__year},{self.__make},{self.__model}"
car1 = Car("Toyota","Camry",2020)
print(car1.car_features())
