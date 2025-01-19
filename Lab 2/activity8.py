# Activity 8: Flowchart to Python Code
# This program calculates gross pay based on hours worked and hourly pay rate.

def main():
    # Include comments to explain the purpose of your code
    # Prompt the user to enter the number of hours worked
    hours = float(input("Enter the number of hours worked: "))
    
    # Prompt the user to enter their hourly pay rate
    pay_rate = float(input("Enter your hourly pay rate: "))
    
    # Calculate gross pay
    gross_pay = hours * pay_rate
    
    # Display the gross pay
    print(f"Your gross pay is: ${gross_pay:.2f}")

    # Test your program with various input values to ensure it behaves as expected
    # Use meaningful variable names

# Call the main function
if __name__ == "__main__":
    main()