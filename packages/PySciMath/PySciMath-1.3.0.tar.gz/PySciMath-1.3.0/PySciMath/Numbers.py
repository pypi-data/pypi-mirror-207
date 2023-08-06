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
def isPrime(number):
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

# Functions - Squares and Cubes
def square(number): return power(number, 2)
def cube(number): return power(number, 3)
def squareRoot(number): return number ** 0.5
def cubeRoot(number): return number ** (1/3)

# Functions - Odd and Even
def isOdd(number): return number % 2 == 1
def isEven(number): return number % 2 == 0