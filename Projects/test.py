# Input of the user for the numbers
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Addition
def addition1():
    print('{} + {} = '.format(number_1, number_2), end="")

# Check the operation and perform the corresponding action
if operation == "+":
    addition1()  # Call the addition1 function to display the expression
    result_addition = number_1 + number_2  # Calculate the result
    print(result_addition)  # Print the result
else:
    print("Invalid operation. Please enter a valid operation.")
