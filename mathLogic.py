import math  # Imports everything from the math module

def addition(num1, num2):
    """
    Perform addition operation.

    Parameters:
        num1 (float/int): First number.
        num2 (float/int): Second number.

    Returns:
        float/int: Result of addition operation.
    """
    return num1 + num2

def subtraction(num1, num2):
    """
    Perform subtraction operation.

    Parameters:
        num1 (float/int): First number.
        num2 (float/int): Second number.

    Returns:
        float/int: Result of subtraction operation.
    """
    return num1 - num2

def multiplication(num1, num2):
    """
    Perform multiplication operation.

    Parameters:
        num1 (float/int): First number.
        num2 (float/int): Second number.

    Returns:
        float/int: Result of multiplication operation.
    """
    return num1 * num2

def division(num1, num2):
    """
    Perform division operation.

    Parameters:
        num1 (float/int): Dividend.
        num2 (float/int): Divisor.

    Returns:
        float: Result of division operation.
        str: 'error' if division by zero occurs.
    """
    try:
        result = round((num1 / num2), 3)
    except ZeroDivisionError:
        return 'error'
    else:
        return result

def factorial(num):
    """
    Calculate factorial of a number.

    Parameters:
        num (int): Number to calculate factorial.

    Returns:
        int: Factorial of the given number.
        bool: False if ValueError occurs (e.g., negative number).
    """
    try:
        result = math.factorial(num)
    except ValueError:
        return False
    else:
        return result

def power(num):
    """
    Calculate the square of a number.

    Parameters:
        num (float/int): Number to calculate the square of.

    Returns:
        float/int: Square of the given number.
    """
    return pow(num, 2)

def log(num):
    """
    Calculate the base-10 logarithm of a number and round the result to 3 decimal places.

    Parameters:
        num (float or int): The number for which the logarithm will be calculated.

    Returns:
        float: The base-10 logarithm of the input number rounded to 3 decimal places.
    """
    return round(math.log10(num), 3)
def percentage(num):
    """
    Calculate the percentage of a number.

    Parameters:
        num (float/int): Number to calculate the percentage of.

    Returns:
        str: Percentage representation of the given number (formatted to two decimal places).
    """
    return f'{num/100:.2f}'

def perimeter_of_square(side):
    """
    Calculate the perimeter of a square.

    Parameters:
        side (float/int): Length of one side of the square.

    Returns:
        float/int: Perimeter of the square.
    """
    return side * 4

def area_of_square(side):
    """
    Calculate the area of a square.

    Parameters:
        side (float/int): Length of one side of the square.

    Returns:
        float: Area of the square.
    """
    return int(math.pow(side, 2))

def perimeter_of_rectangle(side1, side2):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
        side1 (float/int): Length of one side of the rectangle.
        side2 (float/int): Length of the adjacent side of the rectangle.

    Returns:
        float/int: Perimeter of the rectangle.
    """
    return (side1 * 2) + (side2 * 2)

def area_of_rectangle(side1, side2):
    """
    Calculate the area of a rectangle.

    Parameters:
        side1 (float/int): Length of one side of the rectangle.
        side2 (float/int): Length of the adjacent side of the rectangle.

    Returns:
        float/int: Area of the rectangle.
    """
    return side1 * side2

def perimeter_of_triangle(side1, side2, side3):
    """
    Calculate the perimeter of a triangle.

    Parameters:
        side1 (float/int): Length of one side of the triangle.
        side2 (float/int): Length of the second side of the triangle.
        side3 (float/int): Length of the third side of the triangle.

    Returns:
        float/int: Perimeter of the triangle.
    """
    return side1 + side2 + side3

def area_of_triangle(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
        base (float/int): Length of the base of the triangle.
        height (float/int): Height of the triangle.

    Returns:
        float: Area of the triangle.
    """
    return ((1/2) * base * height)

def circumference_of_circle(radius):
    """
    Calculate the circumference of a circle.

    Parameters:
        radius (float/int): Radius of the circle.

    Returns:
        float: Circumference of the circle.
    """
    return 2 * math.pi * radius

def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Parameters:
        radius (float/int): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    return math.pi * math.pow(radius, 2)