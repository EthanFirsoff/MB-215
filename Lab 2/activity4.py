# Activity 4: Data Table Formatter
# This program asks for several pieces of data from the user and displays them in a formatted table.

def main():
    # Ask the user for data to fill the table
    title = input("Enter the title of the table: ")
    column1 = input("Enter the first column title: ")
    column2 = input("Enter the second column title: ")
    column3 = input("Enter the third column title: ")

    # Ask for the data corresponding to each column
    data1 = input(f"Enter the data for {column1}: ")
    data2 = input(f"Enter the data for {column2}: ")
    data3 = input(f"Enter the data for {column3}: ")

    # Print the table header
    print("\n{:<20} {:<20} {:<20}".format(column1, column2, column3))
    print("-" * 60)  # This creates a simple line to separate headers from data

    # Print the data in formatted form
    print("{:<20} {:<20} {:<20}".format(data1, data2, data3))

    # Optionally, you can add more rows by repeating the data input and output sections

# Call the main function
if __name__ == "__main__":
    main()