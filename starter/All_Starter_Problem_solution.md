# Python Starter Problems

## Problem-1: Write a program to find the length of the variable name.

### Solution of Problem-1
**Code:**
```python
#Variable, name="Hello there"
name="Hello there"
print("Lenght of the variable 'name' is ", len(name))
```

**Output:**
```python
Lenght of the variable 'name' is  11
```

## Problem-2: Write a program to find the type of the variable name

### Solution of Problem-2
**Code:**
```python
#Variable, name="Hello there"
name="Hello there"
print("Type of variable 'name':", type(name))
```

**Output:**
```python
Type of variable 'name': <class 'str'>
```

## Problem-3: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder

### Solution of Problem-3
**Code:**
```python
#find who is elder
def find_elder(age1, age2):
    if age1 > age2:
        return "First brother is elder"
    elif age2 > age1:
        return "Second brother is elder"
    else:
        return "Both are of the same age"

# Example
print(find_elder(18, 21))
```

**Output:**
```python
Second brother is elder
```

## Problem-4: Write a program to find the index of 7
**Given Info:**\
numbers=[3, 5, 1, 9, 7, 2, 8 ]

### Solution of Problem-4
**Code:**
```python
numbers=[3, 5, 1, 9, 7, 2, 8 ] # list of numbers given
index_of_7 = numbers.index(7) 
print("The index of 7 is",index_of_7)
```

**Output:**
```python
The index of 7 is 4
```

## Problem-4.1: Write a program to find the index of bob 

**Given Info:**\
Where a list of student names is\
students = ['Alice', 'Bob', 'Charlie', 'David']

### Solution of Problem-4.1
**Code:**
```python
students = ['Alice', 'Bob', 'Charlie', 'David']
index_of_bob = students.index('Bob')
print("Bob is at index:", index_of_bob)
```

**Output:**
```python
Bob is at index: 1
```

## Problem-5: Write a program to sort the numbers in Ascending order
numbers=[3, 5, 1, 9, 7, 2, 8 ]

### Solution of Problem-5
**Code:**
```python
# Original list of numbers
numbers = [3, 5, 1, 9, 7, 2, 8]

# Sort the list in ascending order
numbers.sort()

# Print the sorted list
print("Numbers in ascending order:", numbers)
```

**Output:**
```python
Numbers in ascending order: [1, 2, 3, 5, 7, 8, 9]
```

## Problem-6: Write a function named "isLandscape" that takes 2 numbers (image width and height) as arguments and the function returns Landscape if the image width has a higher value than height. Returns Portrait otherwise
Hints: Use condition inside the function

### Solution of Problem-6
**Code:**
```python
# Define the function
def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

# Example usage
print("When width=1920 and height=1080 then the image is: ",isLandscape(1920, 1080))  # Output: Landscape
print("When width=800 and height=1200 then the image is: ",isLandscape(800, 1200))   # Output: Portrait
```

**Output:**
```python
When width=1920 and height=1080 then the image is:  Landscape
When width=800 and height=1200 then the image is:  Portrait
```

## Problem-7: Write a function that takes 1 number as argument. The function should return “Fizz” if the number is divisible by 3, the function should return “Buzz” if the number is divisible by 5, the function should return “FizzBuzz” if the number is divisible by both 5 and 3, otherwise return “Not a Fizz-buzz number”

Hints: Use condition inside the function

### Solution of Problem-7
**Code:**
```python
# Define the function
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

# Example usage
print("If number=15, the function output is:", fizz_buzz(15))  # Output: FizzBuzz
print("If number=9, the function output is:",fizz_buzz(9))   # Output: Fizz
print("If number=5, the function output is:", fizz_buzz(5))  # Output: Buzz
print("If number=7, the function output is:", fizz_buzz(7))   # Output: Not a Fizz-buzz number
```

**Output:**
```python
If number=15, the function output is: FizzBuzz
If number=9, the function output is: Fizz
If number=5, the function output is: Buzz
If number=7, the function output is: Not a Fizz-buzz number
```


## Problem-8: Guessing game
Write a function that takes a number 1 to 9 from the user input (use input function inside a function). Store a number in a variable (let’s assume 6). If the input value is less than the variable, print (your guess is almost there), if the input value is greater than the variable, print - your guess is higher, if the input value and variable are equals, print - Your Guess Is Correct!

### Solution of Problem-8
**Code:**
```python

```

**Example Interaction & Output:**
```python
Guess a number between 1 and 9: 5
Your guess is almost there.

Guess a number between 1 and 9: 7
Your guess is higher.

Guess a number between 1 and 9: 6
Your Guess Is Correct!
```

## 

### Solution of Problem-3
**Code:**
```python

```

**Output:**
```python

```

## 

### Solution of Problem-3
**Code:**
```python

```

**Output:**
```python

```


## 

### Solution of Problem-3
**Code:**
```python

```

**Output:**
```python

```