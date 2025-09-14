# Import necessary library
import random

# Get user's name
user_name = input("Welcome to the higher/lower game! Enter your name: ")

# Initialize game loop
while True:
    # Get lower bound from user with input validation
    while True:
        lower_bound = int(input(f"Hello, {user_name}! Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        if lower_bound < upper_bound:
            break
        else:
            print("Error: The lower bound must be less than the upper bound.")

    # Generate a random number between lower and upper bounds
    target_number = random.randint(lower_bound, upper_bound)

    # Initialize guess loop
    while True:
        # Get user's guess with input validation
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

        # Check the guess and provide feedback
        if guess < target_number:
            print("Nope, too low.")
        elif guess > target_number:
            print("Nope, too high.")
        else:
            print(f"You got it, {user_name}! The correct number was {target_number}.")
            break  # Exit the guess loop since the user guessed correctly

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break  # Exit the game loop if the user doesn't want to play again

print("Thanks for playing the higher/lower game, goodbye!")