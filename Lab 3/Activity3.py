import math

def calculate_cylinder_volume():
    # Import the math module for mathematical functions
    
    # Ask the user to input the diameter of the cylinder's circular end
    diameter = float(input("Enter the diameter of the cylinder in cm: "))
    
    # Ask the user to input the height of the cylinder
    height = float(input("Enter the height of the cylinder in cm: "))
    
    # Calculate the radius from the diameter
    radius = diameter / 2
    
    # Consider the initial value of pi and then round it to 2 decimal places
    pi = round(math.pi, 2)
    
    # Calculate the volume using the formula: volume = pi * radius² * height
    volume = pi * (radius ** 2) * height
    
    # Output the calculated volume
    print(f"The volume of the cylinder is {volume:.2f} cubic centimeters.")

# Call the function to perform the calculation
calculate_cylinder_volume()