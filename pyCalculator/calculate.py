import re


print("Welcome To Our Calculator")
AC = 0
running = True


def perform_arithmetic():

    # To access the global variables and change its value in a function
    global running, AC

    # if : to enter the equation or a number for evaluation
    # else : to output the answer of eval(equation) in a manner that is contained within input() method
    if AC == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(AC) + " ")

    # if equation == quit : exit the calculator program
    # elif equation == AC : reset the values and recur this method
    # else : validate the equation (without any letters and not used symbols) then store it in the variable equation
        # if AC global variable == 0 : evaluate the equation to print on the first if else block.
        # else : evaluate the content of the AC and the equation and stored it on AC to print on the 1st if else block
    if equation == 'quit':
        running = False
        print("Good Bye! Thank You")
    elif equation == 'AC':
        AC = 0
        perform_arithmetic()
    else:
        equation = re.sub('[a-zA-z(),." ]', '0+0', equation)
        if AC == 0:
            AC = eval(equation)
        else:
            AC = eval(int(AC) + equation)


while running:
    perform_arithmetic()
