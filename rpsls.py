# Rock Paper Scissors Lizard Spock
# Bolea Andreea

import random

# un array cu optiuni
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


def game(option):
    player_choice = option
    computer_choice = random.randrange(0, 5)
    winner = (computer_choice - player_choice) % 5

    player_win = False if (winner < 3) else True

    print("You chose " + choices[option])
    print("Computer chooses " + choices[computer_choice])
    if player_win:
        print("You win!\n")
    elif computer_choice == player_choice:
        print("Its a tie!\n")
    else:
        print("Computer wins!\n")


# main
player_option = int(input(
    "Choose your option:\n Rock - 0, Paper - 1, Scissors - 2,  Lizard - 3, Spock - 4 : "))

if player_option > 4:
    print("Illegal move! Go to jail\n")
    exit()

game(player_option)
