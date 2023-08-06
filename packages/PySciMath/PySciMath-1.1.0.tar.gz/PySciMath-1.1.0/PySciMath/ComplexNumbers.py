# PySciMath - Complex Numbers

''' This is the "Complex Numbers" sub-module. '''

# Imports
import math
import cmath

# Functions - Algebra
def addition(z1, z2): return z1 + z2
def subtraction(z1, z2): return z1 - z2
def multiplication(z1, z2): return z1 * z2
def divide(z1, z2): return z1 / z2

# Functions - Modulus, Conjugate, and Multiplicative Invers
def modulus(z): return abs(z)
def conjugate(z): return z.conjugate()
def multiplicativeInverse(z): return conjugate(z) / (math.pow(modulus(z), 2))

# Function - Polar Representation
def polar(z): return cmath.polar(z)