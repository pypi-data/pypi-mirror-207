# PySciMath - Quadratic

''' This is the "Quadratic" sub-module. '''

# Imports
import math

# Function 1 - Find Roots
def findRoots(a, b, c):
    newA = float(a)
    newB = float(b)
    newC = float(c)

    discriminant = math.sqrt((b**2) - (4*a*c))

    alpha = (-b + discriminant) / (2*a)
    beta = (-b - discriminant) / (2*a)

    return (alpha, beta)