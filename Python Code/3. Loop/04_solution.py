input_str = str(input("Enter a Word: "))

reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str 

print(reversed_str)