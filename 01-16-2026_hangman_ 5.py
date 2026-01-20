import random

# 1- list with words in variable
words = ["Kenya","Germany", "France", "China", "Mexico", "Senegal"]

# 2- pick a random word from the list
# Note: You need to know the length of the word
random_words = random.choice(words)
# print(random_words)
add_length = " "

word_length = len(random_words)
for underscore in range (word_length):
    add_length = add_length + "_"
print(add_length)

# 3- look at the letters in the word | letter_one is the letter in the random word
for letter_one in random_words:
    print(letter_one)


# 4- Compare the players letter to the words letters | letter_two is the storage for the random word chosen
# Note:  when its right the letter must hold its place in the word
while True:
    storage = " "

    under_storage = "_"
    guess_attempts = input("Guess a letter:")
    for letter_two in random_words:
        if letter_two == guess_attempts:
            storage = letter_two + storage

        else:
            storage = storage + under_storage

    print(storage)


# create an empty list here and then link it to the storage



# 9- when not right the life counts will have a limit of 10

# 10- when limit exceeded print games over!

