import random
life_points = 0
# 1. Function to set difficulty (Called once at the start)
def diffi():
    global life_points
    # .lower() added here to handle case-sensitivity
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_mode == "easy":
        life_points = 10
        print("You have 10 attempts remaining.")
    elif game_mode == "hard":
        life_points = 5
        print("You have 5 attempts remaining.")
    else:
        print("Invalid input. Defaulting to Easy mode (10 attempts).")
        life_points = 10

# 2. Function to check the guess (Called inside the loop)
def num_check(guess, target):
    global life_points
    if guess > target:
        print("Too high.")
        life_points -= 1
    elif guess < target:
        print("Too low.")
        life_points -= 1
    else:
        print(f"You got it! The answer was {target}.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate the secret number
rand_num = random.randint(1, 100)

# FUNCTION CALL 1: Set the difficulty before starting
diffi()

# Initialize users_number to something that won't match rand_num immediately
users_number = 0

# --- GAME LOOP ---
# Continue as long as they have lives and haven't guessed the right number
while users_number != rand_num and life_points > 0:
    print(f"You have {life_points} attempts remaining to guess the number.")

    # Get user input with error handling for invalid numbers
    try:
        users_number = int(input("Make a guess: "))

        # FUNCTION CALL 2: Check the number and update life_points
        num_check(users_number, rand_num)

        if users_number != rand_num and life_points > 0:
            print("Guess again.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

if life_points == 0 and users_number != rand_num:
    print("You've run out of guesses, you lose.")
    print(f"The correct number was: {rand_num}")