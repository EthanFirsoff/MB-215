def convert_numeric_to_letter_grade():
    # Ask the user to input a numeric grade
    numeric_grade = float(input("Enter your numeric grade: "))

    # Determine the letter grade based on the numeric grade
    if numeric_grade >= 90:
        letter_grade = 'A+'
    elif numeric_grade >= 80:
        letter_grade = 'A'
    elif numeric_grade >= 70:
        letter_grade = 'B'
    elif numeric_grade >= 60:
        letter_grade = 'C'
    elif numeric_grade >= 50:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Output the letter grade to the user
    print(f"Your letter grade is {letter_grade}.")

# Call the function to perform the grade conversion
convert_numeric_to_letter_grade()