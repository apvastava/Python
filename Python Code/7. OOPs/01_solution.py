class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# __init__ also known as Constructor
# my_car is object
# Car is Class
        
my_car = Car("Suzuki", "Wagoan-R")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
