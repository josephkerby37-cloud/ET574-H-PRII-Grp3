# Name: Humaun Ahmed
# QCC ID: YOUR_QCC_ID

# Name: Kerby [Last Name]
# QCC ID: KERBY_QCC_ID

# Name: Kenn [Last Name]
# QCC ID: KENN_QCC_ID


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