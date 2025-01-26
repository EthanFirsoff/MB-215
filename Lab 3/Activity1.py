def convert_km_to_miles():
    # Taking input from the user
    km = float(input("Enter distance in kilometers: "))

    # Conversion factor
    miles_per_km = 0.621371

    # Converting kilometers to miles
    miles = km * miles_per_km

    # Rounding the result to 2 decimal places
    rounded_miles = round(miles, 2)

    # Printing the result
    print(f"The distance in miles is {rounded_miles}.")

# Call the function to perform the conversion
convert_km_to_miles()