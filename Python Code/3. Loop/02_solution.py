n = int(input("Enter a number: "))

sum_even = 0

for i in range(1, input+1):
    if  i % 2 == 0:
        sum_even += 1

print("Sum of even number is: ", sum_even)
