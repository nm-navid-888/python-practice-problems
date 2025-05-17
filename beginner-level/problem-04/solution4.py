# Import Necessary Module
import string

# Defines a function named is_palindrome that takes the word as argument
def is_palindrome(word):
    # Convert to lowercase (Normalize Input)
    word = word.lower()

    # Remove punctuation and spaces
    # If the character is not punctuation and not a space, it adds the character to clean_word
    clean_word = '' # Initializes an empty string
    for char in word:
        if char not in string.punctuation and char != ' ':
            clean_word += char

    # Check if the cleaned word is the same as its reverse
    return clean_word == clean_word[::-1]

# Example usage
print("Madam is a palindrome word: ", is_palindrome("Madam"))          # True
print("Hello World is a palindrome: ", is_palindrome("Hello World"))    # False
print("A man, a plan, a canal, Panama is a palindrome: ", is_palindrome("A man, a plan, a canal, Panama")) # True