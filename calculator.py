"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

# import all functions from arithmetic module
from arithmetic import *


def process_input(input_string):
    """ Process the string inputed by user and return operator and number list in a tuple

        Split the string inputed by user into a list. Define the first item in the list as operator. 
        Turn the rest of the items into integers and pack into a string with map function. 
        Return the operator and the number list as a touple
        """ 
    tokens = input_string.split()
    operator = tokens[0]
    numlist = map(int, tokens[1:])
    return operator, numlist


# make infinite loop
while True:
    # reads user input
    input_string = raw_input("> ")
    #unpack tuple from process_input function
    operator, numlist = process_input(input_string)

    # responses to different user inputs
    if operator == "q":
        break
    elif operator == "+":
        print add(numlist)
    elif operator == "-":
        print subtract(numlist)
    elif operator == "*":
        print multiply(numlist)
    elif operator == "/":
        print divide(numlist)
    elif operator == "square":
        print square(numlist) 
    elif operator == "cube":
        print cube(numlist)
    elif operator == "pow":
        print power(numlist)
    elif operator == "mod":
        print mod(numlist)
    else:
        print "I don't understand"
