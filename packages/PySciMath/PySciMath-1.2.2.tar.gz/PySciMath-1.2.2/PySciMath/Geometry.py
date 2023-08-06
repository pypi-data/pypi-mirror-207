# PySciMath - Geometry

''' This is the "Geometry" sub-module. '''

# Imports
import math

# Constants
pi = 3.14159
goldenRatio = 1.61803

# Functions - Area
def squareArea(side): return side * side
def rectangleArea(length, width): return length * width
def triangleArea(base, height): return 0.5 * base * height
def circleArea(radius): return 3.14 * math.pow(radius, 2)
def parallelogramArea(base, height): return base * height
def trapeziumArea(base1, base2, height): return 0.5 * height * (base1 + base2)
def rhombusArea(diagonal1, diagonal2): return (diagonal1 * diagonal2) / 2

# Functions - Volume
def cubeVolume(side): return math.pow(side, 3)
def cuboidVolume(length, width, height): return length * width * height
def coneVolume(radius, height): return (1/3) * 3.14 * math.pow(radius, 2) * height
def cylinderVolume(radius, height): return 3.14 * math.pow(radius, 2) * height
def sphereVolume(radius): return (4/3) * 3.14 * math.pow(radius, 3)
def hemisphereVolume(radius): return (2/3) * 3.14 * math.pow(radius, 3)
def pyramidVolume(length, width, height): return (length * width * height) / 3

# Functins - Surface Area
def cubeSA(side, lateral=False):
    if (lateral == False):
        area = 6 * math.pow(side, 2)
    else:
        area = 4 * math.pow(side, 2)

    return area

def cuboidSA(length, width, height, lateral=False):
    if (lateral == False):
        area = 2 * ((length * width) + (width * height) + (length * height))
    else:
        area = 2 * height * (length + width)

    return area

def coneSA(radius, height, lateral=False):
    slantHeight = math.sqrt(math.pow(radius, 2) + math.pow(height, 2))

    if (lateral == False):
        area = 3.14 * radius * (slantHeight + radius)
    else:
        area = 3.14 * radius * slantHeight

    return area

def cylinderSA(radius, height, lateral=False):
    if (lateral == False):
        area = 2 * 3.14 * radius * (radius + height)
    else:
        area = 2 * 3.14 * radius * height

    return area

def sphereSA(radius, lateral=False):
    if (lateral == False):
        area = 4 * 3.14 * math.pow(radius, 2)
    else:
        area = 4 * 3.14 * math.pow(radius, 2)

    return area

def hemisphereSA(radius, lateral=False):
    if (lateral == False):
        area = 3 * 3.14 * math.pow(radius, 2)
    else:
        area = 2 * 3.14 * math.pow(radius, 2)

    return area

# Functions - Miscellaneous
def circumference(radius): return 2 * 3.14 * radius
def hypotenuse(side1, side2): return math.sqrt(math.pow(side1, 2) + math.pow(side2, 2))
def arcLength(angle, radius): return radius * angle

def heronsFormula(side1, side2, side3):
    semiPerimeter = (side1 + side2 + side3) / 2

    return math.sqrt(semiPerimeter * (semiPerimeter - side1) * (semiPerimeter - side2) * (semiPerimeter - side3))