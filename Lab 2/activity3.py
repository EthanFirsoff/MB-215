# Activity 3: String Assembly
# This program takes three different strings from the user, concatenates them into a full sentence, and prints the result.

def main():
    # Ask the user for three separate strings
    string1 = input("Enter the first part of the sentence: ")
    string2 = input("Enter the second part of the sentence: ")
    string3 = input("Enter the third part of the sentence: ")
    
    # Concatenate the strings into a full sentence
    full_sentence = string1 + " " + string2 + " " + string3
    
    # Print the concatenated sentence
    print("The full sentence is:", full_sentence)

# Call the main function
if __name__ == "__main__":
    main()