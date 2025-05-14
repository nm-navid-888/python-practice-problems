def guessing_game():
    # Stored number
    secret_number = 6

    # Take input from the user and convert it to an integer
    guess = int(input("Guess a number between 1 and 9: "))

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Your guess is almost there.")
    elif guess > secret_number:
        print("Your guess is higher.")
    else:
        print("Your Guess Is Correct!")

# Run the function
guessing_game()
