class car:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_features(self):
        return f"{self.year},{self.make},{self.model}"
car1 = car("Toyota","Camry",2020)
print(car1.car_features())