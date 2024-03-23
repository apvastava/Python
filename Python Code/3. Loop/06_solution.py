number = int(input("Enter a number: "))
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1

   factorial *= number
   number -= 1

print("Factorial Value of number is: ", factorial)

