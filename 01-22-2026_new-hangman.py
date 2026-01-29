import random
import itertools

# Wordbank of Understanding
# words: This is the list of words we are using
# random_words: This is the random words that will be chosen there is no special order in hangman
# add_length: This is needed to know the amount of spaces needed for each random word
# word_length: This is the length of the word that is random
# letter_one: The letter in the random word
# storage:  This is where the word/letters will be stored when it is guessed
# guess_attempts: This is where the user is asked to guess a letter
# letter_two: The storage for the random words that is chosen
# found_letters: This is the storage for the found letter so they dont repeat again


# 1- list with words in variable
words = ["Kenya","Germany", "France", "China", "Mexico", "Senegal"]

# 2- pick a random word from the list
random_words = random.choice(words)

# 3- find the length of the random word
add_length = " "
word_length = len(random_words)
for underscore in range (word_length):
    add_length = add_length + "_"
print(add_length)

# 4- look at the letters in the word
for letter_one in random_words:
    print(letter_one)

# 4- Compare the players letter to the words letters
for letter_two in itertools.cycle(random_words):
    storage = " "
    found_letters = []

    # Ask the user to guess a letter
    guess_attempts = input("Guess a letter:")

    # Ask the user to guess a letter
    if guess_attempts == letter_two and found_letters:
        storage += letter_two
        print(f"You have already found letter {guess_attempts}!")


        print(storage)
    else:
        storage += "_"
        print(f"Incorrect guess, Try again!")

   # break # Break statement: immediately exit the loop
# print(f"value of storage is{storage}")

# still working on this












# 5 - 10 trys and the user gets game over!
# Note: add the ascii symbols as well for each life when incorrect guess
#   life_points = life_points - 1  #life_points -= 1
#         print(f"Remaining Lives:{life_points}")
#           if life_points == 0:
#               print("Game Over")
