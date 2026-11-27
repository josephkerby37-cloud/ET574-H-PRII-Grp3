# Name: Kerby Joseph | QCC ID: # 24767298

import math

def sqrt(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)


def area_of_circle(r):
    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (r ** 2)

def factorial(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input cannot be negative")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def volume_of_sphere(r):
    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")

    return (4 / 3) * math.pi * (r ** 3)