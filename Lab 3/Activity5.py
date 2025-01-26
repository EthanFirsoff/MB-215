def sum_numbers():
    # Initialize variables to store the total sum and count of numbers entered
    total_sum = 0
    count = 0
    
    # Implement a while loop that continues as long as the total sum is less than 100
    while total_sum < 100:
        # Prompt the user to either enter a number or a space (' ') to exit
        user_input = input("Enter a number or press space (' ') to exit: ")
        
        # Check if the user enters a space, break out of the loop immediately
        if user_input == ' ':
            break
        
        # If the user enters a number, add it to the total sum and increment the count
        try:
            number = float(user_input)
            total_sum += number
            count += 1
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Once the loop is exited, display the total sum and the count of numbers entered
    print(f"Total sum: {total_sum}")
    print(f"Count of numbers entered: {count}")

# Call the function to start the program
sum_numbers()