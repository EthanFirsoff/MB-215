# Activity 1: Simple Greeting Program
# This program asks for the user's name and age, calculates the year they were born, and greets them.

def main():
    # Ask the user for their name
    name = input("Please enter your name: ")
    
    # Ask the user for their age
    age = int(input("Please enter your age: "))
    
    # Calculate the year they were born
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year - age
    
    # Print a greeting message
    print(f"Hello, {name}! You were born in the year {birth_year}.")

# Call the main function
if __name__ == "__main__":
    main()