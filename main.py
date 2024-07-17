import random

print("Welcome to Rock Paper Scissors!")
name = input("What is your name?\n")


def gameplay():
    choices = ["rock", "paper", "scissors"]
    type_game = int(input(f"Hello, {name}!\nWould you like to play single-player or against a friend?\n(1/2)"))
    count_player = 0
    count_computer = 0
    count_player2 = 0
    if type_game == 1:
        print("You will play against the computer.")
        games = int(input("How many games would you like to play?\nChoose 3(2 out of 3)/5(3 out of 5)\n"))
        while True:
            computer = random.choice(choices)
            player = input("Choose rock, paper or scissors.\n").lower()

            if player not in choices:
                print("Invalid choice.")
                continue
            print(f'Computer chose {computer}')
            if player == computer:
                print("It's a tie!")
            elif (player == "rock" and computer == "scissors") or \
                    (player == "paper" and computer == "rock") or \
                    (player == "scissors" and computer == "paper"):
                print("You win!")
                count_player += 1

            else:
                print("You lost!")
                count_computer += 1
            if count_player == games - count_player + 1:
                print(f"Game over!\nThe score was:\n{count_player}-{count_computer}\n{name} won!")
                print("Thanks for playing!")
                break
            elif count_computer == games - count_computer + 1:
                print(f"Game over!\nThe score was:\n{count_player}-{count_computer}\nComputer won!")
                print("Thanks for playing!")
                break
    elif type_game == 2:
        name2 = input("You will play against your friend. What is his name?\n")
        games = int(input("How many games would you like to play?\nChoose 3(2 out of 3)/5(3 out of 5)\n"))
        while True:
            player = input(f"{name}, choose rock, paper or scissors.\n").lower()
            player2 = input(f"{name2}, choose rock, paper or scissors.\n").lower()

            if player not in choices or player2 not in choices:
                print("Invalid choice.")
                continue
            if player == player2:
                print("It's a tie!")
            elif (player == "rock" and player2 == "scissors") or \
                    (player == "paper" and player2 == "rock") or \
                    (player == "scissors" and player2 == "paper"):
                print(f"{name} won!")
                count_player += 1
            else:
                print(f"{name2} won!")
                count_player2 += 1
            if count_player == games - count_player + 1:
                print(f"Game over!\nThe score was:\n{count_player}-{count_player2}\n{name} won!")
                print("Thanks for playing!")
                break
            elif count_player2 == games - count_player2 + 1:
                print(f"Game over!\nThe score was:\n{count_player}-{count_player2}\n{name2} won!")
                print("Thanks for playing!")
                break


gameplay()
