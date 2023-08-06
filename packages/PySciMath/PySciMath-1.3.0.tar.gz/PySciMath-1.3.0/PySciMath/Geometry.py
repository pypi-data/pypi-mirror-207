# PySciMath - Geometry

''' This is the "Geometry" sub-module. '''

# Imports
import math

# Constants
pi = 3.14159
goldenRatio = 1.61803

# Function 1 - Area
def area(**kwargs):
    shapeList = ["square", "rectangle", "triangle", "circle", "parallelogram", "trapezium", "rhombus"]
    keyList = []

    for key, value in kwargs.items():
        keyList.append(key)

    if ("shape" in keyList):
        if (kwargs["shape"] in shapeList):
            shape = kwargs["shape"]

            if (shape == "square"): # Square
                if ("side" in keyList):
                    if (isinstance(kwargs["side"], int)):
                        return kwargs["side"] * kwargs["side"]
                    else:
                        raise Exception("The 'side' argument should be an integer.")
                else:
                    raise Exception("To check the area of a square, the 'side' argument should be present.")
            elif (shape == "rectangle"): # Rectangle
                if ("length" in keyList and "width" in keyList):
                    if (isinstance(kwargs["length"], int) and isinstance(kwargs["width"], int)):
                        return kwargs["length"] * kwargs["width"]
                    else:
                        raise Exception("The 'length' and 'width' arguments should be an integer.")
                else:
                    raise Exception("To check the area of a rectangle, the 'length' and 'width' arguments should be present.")
            elif (shape == "triangle"): # Triangle
                if ("base" in keyList and "height" in keyList):
                    if (isinstance(kwargs["base"], int) and isinstance(kwargs["height"], int)):
                        return 0.5 * kwargs["base"] * kwargs["height"]
                    else:
                        raise Exception("The 'base' and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the area of a triangle, the 'base' and 'height' arguments should be present.")
            elif (shape == "circle"): # Circle
                if ("radius" in keyList):
                    if (isinstance(kwargs["radius"], int)):
                        return 3.14 * math.pow(kwargs["radius"], 2)
                    else:
                        raise Exception("The 'radius' argument should be an integer.")
                else:
                    raise Exception("To check the area of a circle, the 'radius' argument should be present.")
            elif (shape == "parallelogram"): # Parallelogram
                if ("base" in keyList and "height" in keyList):
                    if (isinstance(kwargs["base"], int) and isinstance(kwargs["height"], int)):
                        return kwargs["base"] * kwargs["height"]
                    else:
                        raise Exception("The 'base' and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the area of a parallelogram, the 'base' and 'height' arguments should be present.")
            elif (shape == "trapezium"): # Trapezium
                if ("base1" in keyList and "base2" in keyList and "height" in keyList):
                    if (isinstance(kwargs["base1"], int) and isinstance(kwargs["base2"], int) and isinstance(kwargs["height"], int)):
                        return 0.5 * kwargs["height"] * (kwargs["base1"] + kwargs["base2"])
                    else:
                        raise Exception("The 'base1', 'base2', and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the area of a trapezium, the 'base1', 'base2', and 'height' arguments should be present.")
            elif (shape == "rhombus"): # Rhombus
                if ("diagonal1" in keyList and "diagonal2" in keyList):
                    if (isinstance(kwargs["diagonal1"], int) and isinstance(kwargs["diagonal2"], int)):
                        return (kwargs["diagonal1"] * kwargs["diagonal2"]) / 2
                    else:
                        raise Exception("The 'diagonal' and 'diagonal2' arguments should be an integer.")
                else:
                    raise Exception("To check the area of a rhombus, the 'diagonal1' and 'diagonal2' arguments should be present.")
        else:
            raise Exception("The 'shape' argument should be a square, rectangle, triangle, circle, parallelogram, trapezium, or rhombus.")
    else:
        raise Exception("The 'shape' argument should be present in this function.")

# Function 2 - Volume
def volume(**kwargs):
    shapeList = ["cube", "cuboid", "cone", "cylinder", "sphere", "hemisphere", "pyramid"]
    keyList = []

    for key, value in kwargs.items():
        keyList.append(key)

    if ("shape" in keyList):
        if (kwargs["shape"] in shapeList):
            shape = kwargs["shape"]

            if (shape == "cube"): # Cube
                if ("side" in keyList):
                    if (isinstance(kwargs["side"], int)):
                        return math.pow(kwargs["side"], 3)
                    else:
                        raise Exception("The 'side' argument should be an integer.")
                else:
                    raise Exception("To check the volume of a cube, the 'side' argument should be present.")
            elif (shape == "cuboid"): # Cuboid
                if ("length" in keyList and "width" in keyList and "height" in keyList):
                    if (isinstance(kwargs["length"], int) and isinstance(kwargs["width"], int) and isinstance(kwargs["height"], int)):
                        return kwargs["length"] * kwargs["width"] * kwargs["height"]
                    else:
                        raise Exception("The 'length', 'width', and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the volume of a cuboid, the 'length', 'width', and 'height' arguments should be present.")
            elif (shape == "cone"): # Cone
                if ("raidus" in keyList and "height" in keyList):
                    if (isinstance(kwargs["radius"], int) and isinstance(kwargs["height"], int)):
                        return (1/3) * 3.14 * math.pow(kwargs["radius"], 2) * kwargs["height"]
                    else:
                        raise Exception("The 'radius' and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the volume of a cone, the 'radius' and 'height' arguments should be present.")
            elif (shape == "cylinder"): # Cylinder
                if ("radius" in keyList and "height" in keyList):
                    if (isinstance(kwargs["radius"], int) and isinstance(kwargs["height"], int)):
                        return 3.14 * math.pow(kwargs["radius"], 2) * kwargs["height"]
                    else:
                        raise Exception("The 'radius' and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the volume of a cylinder, the 'radius' and 'height' arguments should be present.")
            elif (shape == "sphere"): # Sphere
                if ("radius" in keyList):
                    if (isinstance(kwargs["radius"], int)):
                        return (4/3) * 3.14 * math.pow(kwargs["radius"], 3)
                    else:
                        raise Exception("The 'radius' argument should be an integer.")
                else:
                    raise Exception("To check the volume of a sphere, the 'radius' argument should be present.")
            elif (shape == "hemisphere"): # Hemisphere
                if ("radius" in keyList):
                    if (isinstance(kwargs["radius"], int)):
                        return (2/3) * 3.14 * math.pow(kwargs["radius"], 3)
                    else:
                        raise Exception("The 'radius' argument should be an integer.")
                else:
                    raise Exception("To check the volume of a hemisphere, the 'radius' argument should be present.")
            elif (shape == "pyramid"): # Pyramid
                if ("length" in keyList and "width" in keyList and "height" in keyList):
                    if (isinstance(kwargs["length"], int) and isinstance(kwargs["width"], int) and isinstance(kwargs["height"], int)):
                        return (length * width * height) / 3
                    else:
                        raise Exception("The 'length', 'width', and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the volume of a pyramid, the 'length', 'width', and 'height' arguments should be present.")
        else:
            raise Exception("The 'shape' argument should be a cube, cuboid, cone, cylinder, sphere, hemisphere, or pyramid.")
    else:
        raise Exception("The 'shape' argument should be present in this function.")

# Function 3 - Surface Area
def surfaceArea(**kwargs):
    shapeList = ["cube", "cuboid", "cone", "cylinder", "sphere", "hemisphere"]
    keyList = []

    for key, value in kwargs.items():
        keyList.append(key)

    if ("shape" in keyList):
        if (kwargs["shape"] in shapeList):
            shape = kwargs["shape"]

            if (shape == "cube"): # Cube
                if ("side" in keyList):
                    if (isinstance(kwargs["side"], int)):
                        if ("lateral" in keyList):
                            if (isinstance(kwargs["lateral"], bool)):
                                if (kwargs["lateral"] == True):
                                    return 4 * math.pow(side, 2)
                                else:
                                    return 6 * math.pow(side, 2)
                            else:
                                raise Exception("The 'lateral' argument should be either True or False.")
                        else:
                            return 6 * math.pow(kwargs["side"], 2)
                    else:
                        raise Exception("The 'side' argument should be an integer.")
                else:
                    raise Exception("To check the surface area of a cube, the 'side' argument should be present.")
            elif (shape == "cuboid"): # Cuboid
                if ("length" in keyList and "width" in keyList and "height" in keyList):
                    if (isinstance(kwargs["length"], int) and isinstance(kwargs["width"], int) and isinstance(kwargs["height"], int)):
                        if ("lateral" in keyList):
                            if (isinstance(kwargs["lateral"], bool)):
                                if (kwargs["lateral"] == True):
                                    return 2 * kwargs["height"] * (kwargs["length"] + kwargs["width"])
                                else:
                                    return 2 * ((kwargs["length"] * kwargs["width"]) + (kwargs["width"] * kwargs["height"]) + (kwargs["length"] * kwargs["height"]))
                            else:
                                raise Exception("The 'lateral' argument should be either True or False.")
                        else:
                            return 2 * ((kwargs["length"] * kwargs["width"]) + (kwargs["width"] * kwargs["height"]) + (kwargs["length"] * kwargs["height"]))
                    else:
                        raise Exception("The 'length', 'width', and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the surface area of a cuboid, the 'length', 'width', and 'height' arguments should be present.")
            elif (shape == "cone"): # Cone
                if ("raidus" in keyList and "height" in keyList):
                    if (isinstance(kwargs["radius"], int) and isinstance(kwargs["height"], int)):
                        slantHeight = math.sqrt(math.pow(kwargs["radius"], 2) + math.pow(kwargs["height"], 2))

                        if ("lateral" in keyList):
                            if (isinstance(kwargs["lateral"], bool)):
                                if (kwargs["lateral"] == True):
                                    return 3.14 * kwargs["radius"] * slantHeight
                                else:
                                    return 3.14 * kwargs["radius"] * (slantHeight + kwargs["radius"])
                            else:
                                raise Exception("The 'lateral' argument should be either True or False.")
                        else:
                            return 3.14 * kwargs["radius"] * (slantHeight + kwargs["radius"])
                    else:
                        raise Exception("The 'radius' and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the surface area of a cone, the 'radius' and 'height' arguments should be present.")
            elif (shape == "cylinder"): # Cylinder
                if ("radius" in keyList and "height" in keyList):
                    if (isinstance(kwargs["radius"], int) and isinstance(kwargs["height"], int)):
                        if ("lateral" in keyList):
                            if (isinstance(kwargs["lateral"], bool)):
                                if (kwargs["lateral"] == True):
                                    return 2 * 3.14 * kwargs["radius"] * kwargs["height"]
                                else:
                                    return 2 * 3.14 * kwargs["radius"] * (kwargs["radius"] + kwargs["height"])
                            else:
                                raise Exception("The 'lateral' argument should be either True or False.")
                        else:
                            return 2 * 3.14 * kwargs["radius"] * (kwargs["radius"] + kwargs["height"])
                    else:
                        raise Exception("The 'radius' and 'height' arguments should be an integer.")
                else:
                    raise Exception("To check the surface area of a cylinder, the 'radius' and 'height' arguments should be present.")
            elif (shape == "sphere"): # Sphere
                if ("radius" in keyList):
                    if (isinstance(kwargs["radius"], int)):
                        if ("lateral" in keyList):
                            if (isinstance(kwargs["lateral"], bool)):
                                if (kwargs["lateral"] == True):
                                    return 4 * 3.14 * math.pow(kwargs["radius"], 2)
                                else:
                                    return 4 * 3.14 * math.pow(kwargs["radius"], 2)
                            else:
                                raise Exception("The 'lateral' argument should be either True or False.")
                        else:
                            return 4 * 3.14 * math.pow(kwargs["radius"], 2)
                    else:
                        raise Exception("The 'radius' argument should be an integer.")
                else:
                    raise Exception("To check the surface area of a sphere, the 'radius' argument should be present.")
            elif (shape == "hemisphere"): # Hemisphere
                if ("radius" in keyList):
                    if (isinstance(kwargs["radius"], int)):
                        if ("lateral" in keyList):
                            if (isinstance(kwargs["lateral"], bool)):
                                if (kwargs["lateral"] == True):
                                    return 2 * 3.14 * math.pow(kwargs["radius"], 2)
                                else:
                                    return 3 * 3.14 * math.pow(kwargs["radius"], 2)
                            else:
                                raise Exception("The 'lateral' argument should be either True or False.")
                        else:
                            return 3 * 3.14 * math.pow(kwargs["radius"], 2)
                    else:
                        raise Exception("The 'radius' argument should be an integer.")
                else:
                    raise Exception("To check the surface area of a hemisphere, the 'radius' argument should be present.")
        else:
            raise Exception("The 'shape' argument should be a cube, cuboid, cone, cylinder, sphere, or hemisphere.")
    else:
        raise Exception("The 'shape' argument should be present in this function.")

# Function 4 - Circumference
def circumference(radius): return 2 * 3.14 * radius

# Function 5 - Hypotenuse
def hypotenuse(side1, side2): return math.sqrt(math.pow(side1, 2) + math.pow(side2, 2))

# Function 6 - Arc Length
def arcLength(angle, radius): return radius * angle

# Function 7 - Herons Formula
def heronsFormula(side1, side2, side3):
    semiPerimeter = (side1 + side2 + side3) / 2

    return math.sqrt(semiPerimeter * (semiPerimeter - side1) * (semiPerimeter - side2) * (semiPerimeter - side3))