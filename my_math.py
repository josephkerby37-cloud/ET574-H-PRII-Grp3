import math

# Name: Humaun Ahmed
# QCC ID: YOUR_QCC_ID




def factorial(n):
    """
    Function Name: factorial
    Purpose: Calculates the factorial of a non-negative integer.
    Parameters: n - A non-negative integer.
    Return Value: The factorial of n.
    """

    if type(n) != int:
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


def volume_of_sphere(r):
    """
    Function Name: volume_of_sphere
    Purpose: Calculates the volume of a sphere.
    Parameters: r - The non-negative radius of the sphere.
    Return Value: The volume of the sphere.
    """

    if type(r) not in (int, float):
        raise TypeError("Radius must be a number")

    if r < 0:
        raise ValueError("Radius cannot be negative")

    pi = 3.141592653589793

    volume = (4 / 3) * pi * (r ** 3)

    return volume


# Name: Kerby [Last Name]
# QCC ID: KERBY_QCC_ID

# Name: Kenn [Last Name]
# QCC ID: KENN_QCC_ID


def sqrt(x):
    """
    Function Name: sqrt
    Purpose: Calculates the square root of a number.
    Parameters: x - A non-negative number.
    Return Value: The square root of x.
    """
    if type(x) not in (int, float):
        raise TypeError("Input must be a number")

    if x < 0:
        raise ValueError("Input must be non-negative")

    return math.sqrt(x)


def area_of_circle(r):
    """
    Function Name: area_of_circle
    Purpose: Calculates the area of a circle.
    Parameters: r - A non-negative radius.
    Return Value: The area of the circle.
    """
    if type(r) not in (int, float):
        raise TypeError("Radius must be a number")

    if r < 0:
        raise ValueError("Radius must be non-negative")

    return math.pi * (r ** 2)