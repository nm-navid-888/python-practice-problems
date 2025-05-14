# Given paragraph
rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

# Create a dictionary to count character frequency
char_count = {}

# Loop through each character in the string
for char in rhyme:
    # Ignore spaces and punctuation, make lowercase for uniformity
    if char.isalpha():
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1

# Find the character with the maximum frequency
most_frequent = max(char_count, key=char_count.get)

# Print the result
print("The most frequent character is:", most_frequent)
print("It appears", char_count[most_frequent], "times.")