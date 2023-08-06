# PySciMath - Arithmetic

''' This is the "Arithmetic" sub-module. '''

# Functions - Simple Arithmetic Operations
def add(num1, num2): return num1 + num2
def subtract(num1, num2): return num1 - num2
def multiply(num1, num2): return num1 * num2
def divide(num1, num2): return num1 / num2

# Function 1 - Factorial
def factorial(number):
    f = 1

    for i in range(1, number + 1):
        f = f * i

    return f