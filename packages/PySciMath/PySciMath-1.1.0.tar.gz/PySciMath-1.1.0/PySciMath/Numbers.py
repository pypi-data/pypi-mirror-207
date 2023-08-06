# PySciMath - Numbers

''' This is the "Numbers" sub-module. '''

# Function 1 - HCF
def hcf(num1, num2):
    hcf = 1

    for i in range(1, min(num1, num2)):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf

# Function 2 - LCM
def lcm(num1, num2):
    if (num1 > num2):
        greater = num1
    else:
        greater = num2

    while True:
        if ((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

# Function 3 - Prime
def prime(number):
    isPrime = False

    if (number < 1):
        isPrime = False
    else:
        for i in range(2, int(number/2) + 1):
            if (number % i == 0):
                isPrime = False
                break
        else:
            isPrime = True

    return isPrime

# Function 4 - Power
def power(base, exponent):
    num = 1

    for i in range(exponent, 0, -1):
        num *= base

    return num

# Function 5 - Square
def square(number): return power(number, 2)

# Function 6 - Cube
def cube(number): return power(number, 3)

# Function 7 - Square Root
def squareRoot(number): return number ** 0.5