import random

choice = ["Rock", "Paper", "Scissors"]

def game():
    while True:
        p_score = 0
        c_score = 0
        for i in range(0, 5):
            c_choice = random.choice(choice)
            p_choice = input("Rock / Paper / Scissors ?\n")
            print(c_choice)
            if p_choice not in choice:
                print("Invalid choice.")
                break
            print("______________________\n")
            if(p_choice == c_choice):
                print("Tie.\n")
            elif p_choice == "Rock":
                if c_choice == "Paper":
                    print("You lost.\n")
                    c_score = c_score + 1
                else:
                    print("You won.\n")
                    p_score = p_score + 1
            elif p_choice == "Paper":
                if c_choice == "Scissors":
                    print("You lost.\n")
                    c_score = c_score + 1
                else:
                    print("You won.\n")
                    p_score = p_score + 1
            elif p_choice == "Scissors":
                if c_choice == "Rock":
                    print("You lost.\n")
                    c_score = c_score + 1
                else:
                    print("You won.\n")
                    p_score = p_score + 1
            i = i + 1

        print("The score is :")
        print(" Computer's score : " + str(c_score))
        print(" Your score : " + str(p_score))

        if(input("\nAgain? : y = yes, n = no : ") != "y"):
            print(" Computer's score : " + str(c_score))
            print(" Your score : " + str(p_score))
            break

game()