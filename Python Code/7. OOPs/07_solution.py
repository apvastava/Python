class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    @staticmethod
    def general_description():
        return "Cars are amazing."
    

my_car = Car("Mercedes", "G-Wagon")
print(my_car.general_description())
