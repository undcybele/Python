# Basic Data Types Challenge 1 : Letter Counter App

print("Welcome")

# Get user input
name = input("What is your name : ").title().strip()
print("Hello, {}.".format(name))

print("\nL E T T E R  C O U N T E R\n")

# Get input + standardize it
message = input("Enter a message : ").lower()
letter = input("Letter to be counted : ").lower()

# Count the number of occurances and display it
letter_count = message.count(letter)
print("{} -> {}".format(letter, letter_count))