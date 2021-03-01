# Basic Data Types Challenge 5 : Multiplication/Exponentiation Table

# User input
name = input("Enter your name : ").title().strip()
num = float(input("Number : "))

# Multiplication Table
print("\nMultiplication Table :")
for i in range (1, 10):
    print("\t{} x {} = {}".format(i, num, round(i*num, 4)))

# Exponentiation Table 
print("\nExponent Table :")
for i in range (1, 10):
    print("\t{} ^ {} = {}".format(num, i, round(num**i, 4)))