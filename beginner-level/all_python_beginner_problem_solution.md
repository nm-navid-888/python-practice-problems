# Python Beginner-level Problems

## Problem-1: Reverse a String Without Slicing
You are building a simple text utility tool for your web app. 
    One of the requirements is to reverse a string input by a user.

-   **Input**: `"bongodev"`
    
-   **Output**: `"vedognob"`
    
-   **Hint**: Use a loop to read the string from end to start.

### Solution of Problem-1
**Code:**
```python
# Idefining a variable named input_string and assigning the string "bongodev"
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
```

**Output:**
```python
Reversed String: vedognob
```

## Problem-2: Count Vowels in a Sentence

As part of a data-cleaning pipeline, count how many vowels are in a string to later analyze readability.

-   **Input**: `"Data Science is awesome"`
    
-   **Output**: `9`
    
-   **Hint**: Convert string to lowercase and check each character.

### Solution of Problem-02
**Code:**
```python
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
    if char in vowels: # For each character, the code checks vowels
        vowel_count += 1

# Output the result
print("Number of vowels:", vowel_count)
```

**Output:**
```python
Number of vowels: 10
```

## Problem-3: Find Duplicates in a List

You’re given a user-uploaded list of tags. Identify duplicates for suggestion cleanup.

-   **Input**: `["ai", "ml", "python", "ml", "dl", "ai"]`
-   **Output**: `["ml", "ai"]`
-   **Hint**: Use a dictionary or set to track seen elements.

### Solution of Problem-03
**Code:**
```python
# Input list of tags
tags = ["ai", "ml", "python", "ml", "dl", "ai"]

# Dictionary to count occurrences
tag_count = {}

# Loop through each tag and count them
for tag in tags:
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1

# Extract duplicates (those with count > 1)
duplicates = [tag for tag, count in tag_count.items() if count > 1]

# Output the duplicates
print("Duplicate Tags:", duplicates)
```

**Output:**
```python
Duplicate Tags: ['ai', 'ml']
```

## 

### Solution of Problem-04
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-05
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-06
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-07
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-08
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-09
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-10
**Code:**
```python

```

**Output:**
```python

```