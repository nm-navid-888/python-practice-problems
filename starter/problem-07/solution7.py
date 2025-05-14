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