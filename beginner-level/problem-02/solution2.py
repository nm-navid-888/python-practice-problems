# Input string
input_string = "Data Science is awesome"

# Convert to lowercase to handle both upper and lower cases
input_string = input_string.lower()

# Define the vowels
vowels = "aeiou"

# Initialize a counter
vowel_count = 0

# Loop through each character in the string
for char in input_string:
    if char in vowels:
        vowel_count += 1

# Output the result
print("Number of vowels:", vowel_count)