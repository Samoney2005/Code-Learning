import random
from random import randint
life_points = 0
# choosing a random number between 1 an 100
rand_int = random.randint(1, 100)
print(f"Choose a number between (1-100): {rand_int}")

# Function to set difficulty
def diffi():
    game_mode = input("What game mode do you want (Easy or Hard)?:")
    if game_mode == "easy":
    # Life points needs to be set to 10
        life_points = 10
# elif if game_mode == hard
    elif game_mode == "hard":
    # Life points needs to be set to 5
        life_points = 5



# Let the user guess a number


# users_number = int(input("What number do you want between 1 and 100? "))

# Function to check user's guess and reduce by 1 if they get it wrong

# If the users guess is correct break out of the loop and say "you win"

# Repeat the guessing functionality if they get it wrong

# Once all wrong  say "you lose "  and break out of  the loop /reveal the number