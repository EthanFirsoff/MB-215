def demonstrate_boolean_operations():
    # Step 1: Declare two Boolean variables
    true_var = True
    false_var = False

    # Step 2: Demonstrate logical operations (AND, OR, NOT)
    
    # Logical AND
    print("Logical AND Operation:")
    print(f"True AND True: {true_var and true_var}")  # Expect True
    print(f"True AND False: {true_var and false_var}")  # Expect False
    print(f"False AND False: {false_var and false_var}")  # Expect False
    
    # Logical OR
    print("\nLogical OR Operation:")
    print(f"True OR True: {true_var or true_var}")  # Expect True
    print(f"True OR False: {true_var or false_var}")  # Expect True
    print(f"False OR False: {false_var or false_var}")  # Expect False
    
    # Logical NOT
    print("\nLogical NOT Operation:")
    print(f"NOT True: {not true_var}")  # Expect False
    print(f"NOT False: {not false_var}")  # Expect True

    # Step 3: Use a Boolean variable in a conditional statement
    print("\nConditional Statement with Boolean Variable:")
    if true_var:
        print("The condition is True.")
    else:
        print("The condition is False.")

# Call the function to demonstrate Boolean operations
demonstrate_boolean_operations()