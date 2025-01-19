# Activity 5: Using Constants Variables
# This program calculates the area of a circle using a constant variable for PI and a user-provided radius.

def main():
    # Define the constant PI
    PI = 3.14159

    # Prompt the user to enter the radius of the circle
    radius = float(input("Please enter the radius of the circle: "))

    # Calculate the area of the circle
    area = PI * (radius ** 2)

    # Display the area
    print(f"The area of the circle with radius {radius} is {area:.2f} square units.")

# Call the main function
if __name__ == "__main__":
    main()