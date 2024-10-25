import random

# Randomly select a number between 1 and 10
number_to_guess = random.randint(1, 10)

# Number of attempts the user gets
attempts = 3

# Start the guessing game
for attempt in range(attempts):
    # Get the user's guess
    guess = int(input("Guess the number (between 1 and 10): "))
    
    # Check if the guess is correct
    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

# If they run out of attempts, reveal the correct number
if guess != number_to_guess:
    print(f"Sorry! The correct number was {number_to_guess}.")
