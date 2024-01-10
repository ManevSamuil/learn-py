# Select operator

def sel_opt():
    global oper
    oper = input("Select operation(+,-,*,/): ")

sel_opt()
   
# List of numbers
def num_sel():
    global num_1, num_2
    num_1 = int(input("Please select your first number: "))
    num_2 = int(input("Please select your second number: "))
num_sel()

def oper_do():
    if oper == "+":
        print("{} + {} = ".format(num_1, num_2), end="")
        print(num_1 + num_2)
    elif oper == "-":
        print("{} - {} = ".format(num_1, num_2), end="")
        print(num_1 - num_2)
    elif oper == "*":
        print("{} * {} = ".format(num_1, num_2), end="")
        print(num_1 * num_2)
    elif oper == "/":
        print("{} + {} = ".format(num_1, num_2), end="")
    else:
        print("Invalid operation")
oper_do()
        
def again():
    global sel_again        
    sel_again = input(''' Do you wish to countinue.
Y for yes
N for no
: ''')

again()
while sel_again == ("Y").lower():
    sel_opt()
    num_sel()
    oper_do()
    again()
if sel_again == ("N").lower():
    print("See you later")
else:
    again()
    


