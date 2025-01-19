# Activity 2: Area Calculator
# This program calculates the area of a rectangle based on user-provided length and width.

def main():
    # Prompt the user for the length of the rectangle
    length = float(input("Please enter the length of the rectangle: "))
    
    # Prompt the user for the width of the rectangle
    width = float(input("Please enter the width of the rectangle: "))
    
    # Calculate the area of the rectangle
    area = length * width
    
    # Display the area
    print(f"The area of the rectangle is {area} square units.")

# Call the main function
if __name__ == "__main__":
    main()