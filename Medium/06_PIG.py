import random as rand

player1_score = 0
player2_score = 0
round_score = 0
current_player = 1

user1 = input("Enter your name: ").lower()
user2 = input("Enter your name: ").lower()

while True:
    print(f"{user1} score is {player1_score}")
    print(f"{user2} score is {player2_score}")

    whos_turn = input("Who's first: ").lower()

    if whos_turn == user1:
        while True:  # Player 1's turn
            ask_to_roll_or_hold = input("Do you want to roll or hold: ").lower()

            if ask_to_roll_or_hold == "roll":
                dice = rand.randint(1, 6)
                if dice == 1:
                    print("Oops! You rolled a 1! No points this turn.")
                    round_score = 0
                    break  # End player 1's turn
                else:
                    round_score += dice
                    print(f"Round Score: {round_score}")
            elif ask_to_roll_or_hold == "hold":
                player1_score += round_score
                round_score = 0
                break  # End player 1's turn
            else:
                print("Invalid Input")

        # Player 2's turn
        round_score = 0
        while True:
            ask_to_roll_or_hold = input(f"{user2} roll or hold: ").lower()

            if ask_to_roll_or_hold == "roll":
                dice = rand.randint(1, 6)
                if dice == 1:
                    print("Oops! You rolled a 1! No points this turn.")
                    round_score = 0
                    break
                else:
                    round_score += dice
                    print(f"Round Score: {round_score}")
            elif ask_to_roll_or_hold == "hold":
                player2_score += round_score
                round_score = 0
                break
            else:
                print("Invalid Input")

    elif whos_turn == user2:
        while True:  # Player 2's turn
            ask_to_roll_or_hold = input("Do you want to roll or hold: ").lower()

            if ask_to_roll_or_hold == "roll":
                dice = rand.randint(1, 6)
                if dice == 1:
                    print("Oops! You rolled a 1! No points this turn.")
                    round_score = 0
                    break
                else:
                    round_score += dice
                    print(f"Round Score: {round_score}")
            elif ask_to_roll_or_hold == "hold":
                player2_score += round_score
                round_score = 0
                break
            else:
                print("Invalid Input")

        # Player 1's turn
        round_score = 0
        while True:
            ask_to_roll_or_hold = input(f"{user1} roll or hold: ").lower()

            if ask_to_roll_or_hold == "roll":
                dice = rand.randint(1, 6)
                if dice == 1:
                    print("Oops! You rolled a 1! No points this turn.")
                    round_score = 0
                    break
                else:
                    round_score += dice
                    print(f"Round Score: {round_score}")
            elif ask_to_roll_or_hold == "hold":
                player1_score += round_score
                round_score = 0
                break
            else:
                print("Invalid Input")
    else:
        print("Invalid player name.")

    print(f"{user1} score is {player1_score}")
    print(f"{user2} score is {player2_score}")

    if player1_score >= 100:
        print(f"{user1} wins")
        break
    elif player2_score >= 100:
        print(f"{user2} wins")
        break