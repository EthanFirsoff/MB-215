def demonstrate_for_loops():
    # For loop with range to print even numbers from 2 to 20
    print("Even numbers from 2 to 20:")
    for number in range(2, 21, 2):
        print(number, end=' ')
    print("\n")

    # Nested for loop to create a multiplication table for numbers 1 to 3
    print("Multiplication table for numbers 1 to 3:")
    for i in range(1, 4):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}", end='    ')
        print("\n")

    # For loop to reverse a string. Note: Use 'Reserved' Keyword (Assuming 'Reserved' was meant to be 'reverse')
    input_string = "Hello"
    print(f"Reversing the string '{input_string}':")
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string
    print(reversed_string)

# Call the function to demonstrate different uses of for loops
demonstrate_for_loops()