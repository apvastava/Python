def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")



print_kwargs(name = "Iron Man", power = "Sniper")
print_kwargs(name = "Hulk")
print_kwargs(name = "Thor", power = "Stone")
print_kwargs(enemy = "Dr. Jhatka")