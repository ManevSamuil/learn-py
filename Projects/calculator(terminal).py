# My first try for making a basic terminal made calculator

#
operation = input('''
What operation would you like to use:
+ for addition
- for substraction
* for multiplication
/ for devision
''')
    


# Input of the user for the numbers
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

# Addition
def addition1():
    print('{} + {} = '.format(number_1, number_2), end="") 
    
# Substraction
def substraction():
    print('{} - {} = '.format(number_1, number_2), end="", flush=True)
    

# Devide
def devide():
    print('{} ÷ {} = '.format(number_1, number_2), end="", flush=True)
    

# Multiplication
def multi():
    print('{} * {} = '.format(number_1, number_2), end="", flush=True)


if operation == "+":
    addition1()
    result_addition = number_1 + number_2
    print(result_addition)
elif operation == "-":
    substraction()
    result_sub = number_1 - number_2
    print(result_sub)
elif operation == "*":
    multi()
    result_multi = number_1 * number_2
    print(result_multi)
elif operation == "/":
    devide()
    result_dev = number_1 / number_2
    print(result_dev)
else:
    print("Sorry, you have chosen an invalid operation")
    
