# Activity 6: Performing Calculations
# This program performs various calculations on two numbers entered by the user.

def main():
    # Prompt the user to enter two float numbers
    a = float(input("Please enter the first number (a): "))
    b = float(input("Please enter the second number (b): "))

    # Addition
    print(f"Addition (a + b): {a + b}")

    # Subtraction
    print(f"Subtraction (a - b): {a - b}")

    # Multiplication
    print(f"Multiplication (a * b): {a * b}")

    # Division
    if b != 0:
        print(f"Division (a / b): {a / b}")
    else:
        print("Cannot divide by zero.")

    # Integer Division
    if b != 0:
        print(f"Integer Division (a // b): {a // b}")
    else:
        print("Cannot perform integer division by zero.")

    # Remainder
    if b != 0:
        print(f"Remainder (a % b): {a % b}")
    else:
        print("Cannot find a remainder with division by zero.")

    # Exponent
    print(f"Exponent (a ** b): {a ** b}")

# Call the main function
if __name__ == "__main__":
    main()