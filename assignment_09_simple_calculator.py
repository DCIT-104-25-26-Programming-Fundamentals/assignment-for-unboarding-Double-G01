# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
# =============================================================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Returns the result of a / b, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Returns the remainder of a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def get_two_numbers():
    """Reads and returns the two operands from the user."""
    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))
    return first, second


def run_operation(symbol, func, zero_division_check=False):
    """Reads two numbers, applies func, and prints the result.

    If zero_division_check is True, func returning None means division
    or modulus by zero, so a clear error message is printed instead.
    """
    first, second = get_two_numbers()
    result = func(first, second)

    if zero_division_check and result is None:
        print("Error: Cannot divide by zero.")
        return

    # print whole numbers without a trailing .0, like the example output
    def clean(value):
        return int(value) if value == int(value) else value

    first_display = clean(first)
    second_display = clean(second)
    result_display = clean(result)

    print(f"Result: {first_display} {symbol} {second_display} = {result_display}")


def print_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "1":
            run_operation("+", add)
        elif choice == "2":
            run_operation("-", subtract)
        elif choice == "3":
            run_operation("*", multiply)
        elif choice == "4":
            run_operation("/", divide, zero_division_check=True)
        elif choice == "5":
            run_operation("%", modulus, zero_division_check=True)
        elif choice == "6":
            run_operation("**", exponentiate)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
