# Problem-1: Reverse a String Without Slicing

# Idefining a variable named input_string and assigning it the string "bongodev"
input_string = "bongodev"

# Initialize a new variable as an empty string to store the characters in reverse order.
reversed_string = ""

# Use a for loop to traverse the string in reverse order
# range(start, stop, step) function generates numbers from start to stop (exclusive), moving by step.
# start = len(input_string) - 1: gives the index of the last character and for "bongodev" (has 8 characters), this is 7.
# stop = -1: The loop will stop just before reaching index -1, so it includes index 0.
# step = -1: This means the loop goes backward, one step at a time.
# Access each character from the end using input_string[i].
# Then add (+=) that character to reversed_string.
# loop will run as: i = 7, 6, 5, 4, 3, 2, 1, 0

for i in range(len(input_string) - 1, -1, -1):
    reversed_string += input_string[i]

# Output the reversed string
print("Reversed String:", reversed_string)