# TIC TAC TOE GAME
# Steps:
# Step 1: initialize all the lists as empty
# Step 2: List will be needed with 9 numbers
# - Step 3: Ask the user if they want to play tic-tac-toe
# - If yes continue to the rest of code, if no exit the game
# - Step 4: randomize whoever starts either CPU or user
# - Step 5: pick a letter either x or o
# -There are 9 places, so user and CPU have to choose a space
# - Step 6: prompt where the user wants to place their choice between 1 and 9
# # - Step 7: Check If a spot is free (if not it should have been stored)
# # - Step 8:  Check if there is a winner (function)
#
# spaces = [" "," ", " ", " ", " ", " ", " ", " ", " " ]
# play = input("Would you like to play tic tac toe?")
# random_order= random.choice(player)
# print("This player will start first", random_order)
#  while True:
#     if play == "yes":
#         print("continue")
#     else:
#         break
#
#
'''
def check_empty(spot):
    if game_list[spot] == " ":
       game_list[spot] = "X"
    else:
        print("Sorry,this spot is taken already!")
        continue
'''

def check_winner():
    if game_list[1] == game_list[2] == game_list[3] == "X":
        print("You Win")


game_list = [" "," ", " ", " ", " ", " ", " ", " ", " "]
def board():
    # print(game_list[3])
    print(game_list[0],"|",game_list[1],"|",game_list[2])
    print("---+---+---")
    print(game_list[3],"|",game_list[4],"|",game_list[5])
    print("---+---+---")
    print(game_list[6],"|",game_list[7],"|",game_list[8])
   # print(game_list)

game = True
user_play = input("Would you like to play tic-tac-toe?")
while game:
    if user_play == "yes":
     #  print("continue")
        game = True
    else:
        game = False

    empty_spot = int(input("Choose a spot between the numbers (1-9):"))

    if game_list[empty_spot-1] == " ":
        game_list[empty_spot-1] = "X"
        board()
    else:
        print("Sorry,this spot is taken already!")
        continue

    # check_empty(empty_spot)
    check_winner()
