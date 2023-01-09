#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: December 20 2022
# This program gets a string form the user and then displays
# each word in the string


# This function splits the original string into substrings
def string_parser(string):
    # Get a list of words by splitting wherever the delimiter is encountered
    # The default delimiter is a blank space
    list_of_words = string.split()

    # Returns the list of words
    return list_of_words


# This function gets the string and displays each word in it
def main():
    # Explain the programs purpose
    print(
        "This program will take in a sentence as input and display each word separately on a new line, without spaces."
    )

    # Get a string form the user
    user_string = input("Enter a string: ")

    # Call a function to split the string
    user_words_list = string_parser(user_string)

    # Display the words in the string separately by going through the list
    print("\nThe words in your sentence: ")
    for word in user_words_list:
        print(word)


if __name__ == "__main__":
    main()
