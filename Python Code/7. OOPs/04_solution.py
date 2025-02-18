class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def chai_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car): 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model X", "85kWh")
print(my_tesla.chai_brand())

