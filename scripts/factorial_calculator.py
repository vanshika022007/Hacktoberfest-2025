# factorial_calculator.py

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    print("Factorial Calculator Examples:")
    try:
        print(f"Factorial of 5: {factorial(5)}")  # Expected: 120
        print(f"Factorial of 0: {factorial(0)}")  # Expected: 1
        print(f"Factorial of 1: {factorial(1)}")  # Expected: 1
        print(f"Factorial of 10: {factorial(10)}") # Expected: 3628800
        # print(f"Factorial of -3: {factorial(-3)}") # This will raise a ValueError
        # print(f"Factorial of 3.5: {factorial(3.5)}") # This will raise a TypeError
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
